import copy
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import pytest

import n1_meta_signal as runner
import n1_meta_signal_core as core
from n1_data_quality import DataQualityError, strict_loads
from n1_validate_outputs import validate_outputs

NOW = datetime(2026, 9, 18, 1, tzinfo=timezone.utc)


def protected_bytes():
    return {path: path.read_bytes() for path in (core.SIGNAL_PATH, core.STATE_PATH, core.LINEAGE_PATH, core.MD_PATH)}


def wire_prices(monkeypatch, prices, lineage):
    monkeypatch.setattr(core, "fetch_prices", lambda symbol, **kwargs: prices[symbol])
    monkeypatch.setattr(core, "liquidity_panel", lambda: lineage.copy())


def test_missing_close_cannot_become_yellow_or_advance_state(workspace, monkeypatch):
    _, _, prices, lineage = workspace
    prices["QQQ"][0].loc[pd.Timestamp("2026-09-17"), "Close"] = np.nan
    wire_prices(monkeypatch, prices, lineage)
    before = protected_bytes()
    with pytest.raises(DataQualityError, match="INVALID_OHLC") as failed:
        runner.execute(now=NOW)
    status = runner.record_failure(failed.value, NOW)
    assert status["status"] == "BLOCKED"
    assert status["execution_target"] is None
    assert status["previous_signal_date"] == "2026-09-16"
    assert protected_bytes() == before


@pytest.mark.parametrize("bad_p", [np.nan, np.inf, -1.0, 101.0])
def test_invalid_p_cannot_advance_state(workspace, monkeypatch, bad_p):
    _, _, prices, lineage = workspace
    lineage.loc[pd.Timestamp("2026-09-11"), "p_applied"] = bad_p
    wire_prices(monkeypatch, prices, lineage)
    before = protected_bytes()
    with pytest.raises(DataQualityError):
        runner.execute(now=NOW)
    assert protected_bytes() == before


def test_new_session_then_same_session_is_idempotent(workspace, monkeypatch):
    _, _, prices, lineage = workspace
    wire_prices(monkeypatch, prices, lineage)
    first = runner.execute(now=NOW)
    state_before = core.STATE_PATH.read_bytes()
    assert first["signal_date"] == "2026-09-17"
    assert first["data_missing"] is False
    validate_outputs()
    def unavailable(*args, **kwargs):
        raise AssertionError("Same-session run must not fetch prices")
    monkeypatch.setattr(core, "fetch_prices", unavailable)
    repeat = runner.execute(now=NOW)
    assert repeat["action"] == "HOLD_PREVIOUS_VALIDATED_TARGET"
    assert core.STATE_PATH.read_bytes() == state_before
    assert repeat["comparison1_raw_streak"] == first["comparison1_raw_streak"]
    validate_outputs()


def test_same_session_refuses_legacy_nan_json(workspace):
    text = core.SIGNAL_PATH.read_text(encoding="utf-8")
    signal = strict_loads(text)
    text = text.replace(str(signal["qqq_adjusted_close"]), "NaN")
    core.SIGNAL_PATH.write_text(text, encoding="utf-8")
    before = protected_bytes()
    with pytest.raises(DataQualityError, match="NONFINITE_JSON"):
        runner.execute(now=datetime(2026, 9, 17, 1, tzinfo=timezone.utc))
    assert protected_bytes() == before


def test_multiple_missing_sessions_require_explicit_recovery(workspace):
    with pytest.raises(DataQualityError, match="EXPLICIT_RECOVERY"):
        runner.execute(now=datetime(2026, 9, 19, 1, tzinfo=timezone.utc))


def prepare_recovery(workspace, monkeypatch):
    _, _, prices, lineage = workspace
    anchor = dict(core.ANCHOR, signal_date="2026-08-31", comparison1_last_raw_state="YELLOW")
    signal, state = core.calculate_signal(anchor, prices, lineage, pd.Timestamp("2026-09-01"))
    monkeypatch.setattr(runner, "load_checkpoint", lambda repair_from=None: (copy.deepcopy(signal), copy.deepcopy(state)))
    wire_prices(monkeypatch, prices, lineage)
    monkeypatch.setattr(runner, "archived_lineages", lambda days: {
        day.strftime("%Y-%m-%d"): (lineage.copy(), "a" * 40) for day in days
    })
    return prices, lineage


def test_ordered_recovery_replays_all_eleven_sessions(workspace, monkeypatch):
    prepare_recovery(workspace, monkeypatch)
    output = runner.execute(repair_from="a" * 40, now=NOW)
    assert output["recovery"]["sessions"] == 11
    assert output["signal_date"] == "2026-09-17"
    assert "RECOVERY_CURRENT_PRICE_VINTAGE" in output["warnings"]
    audit = strict_loads((runner.AUDIT_DIR / "calculation.json").read_text())
    dates = [record["signal"]["signal_date"] for record in audit["sessions"]]
    assert dates == sorted(dates) and len(set(dates)) == 11


def test_recovery_failure_midway_publishes_nothing(workspace, monkeypatch):
    prices, _ = prepare_recovery(workspace, monkeypatch)
    prices["QQQ"][0].loc[pd.Timestamp("2026-09-08"), "Close"] = np.nan
    before = protected_bytes()
    with pytest.raises(DataQualityError):
        runner.execute(repair_from="a" * 40, now=NOW)
    assert protected_bytes() == before


def test_recovery_missing_vintage_does_not_use_today_fred(workspace, monkeypatch):
    prepare_recovery(workspace, monkeypatch)
    monkeypatch.setattr(runner, "archived_lineages", lambda days: {})
    before = protected_bytes()
    with pytest.raises(DataQualityError, match="VINTAGE_MISSING"):
        runner.execute(repair_from="a" * 40, now=NOW)
    assert protected_bytes() == before


def test_dry_run_does_not_publish(workspace, monkeypatch):
    prepare_recovery(workspace, monkeypatch)
    before = protected_bytes()
    runner.execute(repair_from="a" * 40, now=NOW, dry_run=True)
    assert protected_bytes() == before


def test_recovery_ref_must_be_immutable_sha(workspace):
    with pytest.raises(DataQualityError, match="FULL_COMMIT_SHA"):
        runner.load_checkpoint("tqg651")


def test_provider_fallback_validates_before_accepting(inputs, monkeypatch):
    prices, _ = inputs
    good = prices["QQQ"][0]
    bad = good.copy()
    bad.iloc[-1, bad.columns.get_loc("Close")] = np.nan
    monkeypatch.setattr(core, "fetch_tiingo", lambda *args: bad)
    monkeypatch.setattr(core.yf, "download", lambda *args, **kwargs: good)
    frame, provider, notes = core.fetch_prices("QQQ", asof=pd.Timestamp("2026-09-17"))
    assert provider == "yfinance_shadow_fallback"
    assert "INVALID_OHLC" in notes[0]
    assert np.isfinite(frame.iloc[-1]["Close"])


def test_retry_single_symbol_history_without_filling_nan(inputs, monkeypatch):
    prices, _ = inputs
    good = prices["QQQ"][0]
    bad = good.copy()
    bad.iloc[-1, bad.columns.get_loc("Close")] = np.nan
    monkeypatch.setattr(core, "fetch_tiingo", lambda *args: bad)
    monkeypatch.setattr(core.yf, "download", lambda *args, **kwargs: bad)
    class Ticker:
        def history(self, **kwargs):
            assert kwargs["repair"] is False
            return good
    monkeypatch.setattr(core.yf, "Ticker", lambda *args: Ticker())
    frame, _, notes = core.fetch_prices("QQQ", asof=pd.Timestamp("2026-09-17"))
    assert len(notes) == 2 and frame.iloc[-1]["Close"] == good.iloc[-1]["Close"]


def test_provider_diagnostics_do_not_expose_exception_url(monkeypatch):
    def failed(*args, **kwargs):
        raise RuntimeError("https://provider.example/?token=SUPER_SECRET")
    monkeypatch.setattr(core, "fetch_tiingo", failed)
    monkeypatch.setattr(core.yf, "download", failed)
    monkeypatch.setattr(core.yf, "Ticker", failed)
    with pytest.raises(DataQualityError) as error:
        core.fetch_prices("QQQ", asof=pd.Timestamp("2026-09-17"))
    assert "SUPER_SECRET" not in str(error.value)
    assert "RuntimeError" in str(error.value)


def test_valid_calculation_matches_pre_fix_golden(inputs):
    # Recorded from the audited pre-fix core at 963565a with the same finite fixture.
    prices, lineage = inputs
    state = dict(core.ANCHOR, signal_date="2026-09-16", comparison1_last_raw_state="YELLOW")
    result, _ = core.calculate_signal(state, prices, lineage, pd.Timestamp("2026-09-17"))
    expected = {
        "qqq_adjusted_close": 147.42594319322572,
        "sma20": 146.03135053754778, "sma50": 145.2150773498946,
        "sma200": 141.47612922705758, "wilder_rsi14": 76.54624091142011,
    }
    for field, value in expected.items():
        assert result[field] == pytest.approx(value, rel=1e-10)
    assert result["final_regime"] == "BULL"
    assert result["comparison1_raw_state"] == "GREEN"
    assert result["comparison1_confirmed_target"] == "QLD"
    assert result["comparison3_target"] == "QLD"
    assert result["execution_target"] == "QQQ"


def declining_prices(inputs):
    prices, lineage = inputs
    frame = prices["QQQ"][0]
    values = np.linspace(300, 100, len(frame)) + np.sin(np.arange(len(frame)))
    for column in frame:
        frame[column] = values + ({"High": 1, "Low": -1}.get(column, 0))
    state = dict(core.ANCHOR, signal_date="2026-09-16", trend200_state="DOWN",
                 comparison1_confirmed_state="RED", comparison1_last_raw_state="RED")
    return state, prices, lineage


def test_recovery_cannot_guess_unarchived_router_macro(inputs):
    state, prices, lineage = declining_prices(inputs)
    with pytest.raises(DataQualityError, match="RECOVERY_ROUTER_MACRO"):
        core.calculate_signal(state, prices, lineage, pd.Timestamp("2026-09-17"), allow_router_fetch=False)


def test_nan_router_input_cannot_fall_back_to_xlv(inputs, monkeypatch):
    state, prices, lineage = declining_prices(inputs)
    index = prices["QQQ"][0].index
    monkeypatch.setattr(core, "fred_asof", lambda *args: pd.Series(np.nan, index=index))
    with pytest.raises(DataQualityError, match="ROUTER_INPUT_UNAVAILABLE"):
        core.calculate_signal(state, prices, lineage, pd.Timestamp("2026-09-17"))


def test_tiingo_valid_data_does_not_call_fallback(inputs, monkeypatch):
    prices, _ = inputs
    monkeypatch.setattr(core, "fetch_tiingo", lambda *args: prices["QQQ"][0])
    _, provider, notes = core.fetch_prices("QQQ", asof=pd.Timestamp("2026-09-17"))
    assert provider == "tiingo" and notes == []


def test_cli_failure_returns_error_and_keeps_checkpoint(workspace, monkeypatch):
    import sys
    monkeypatch.setattr(sys, "argv", ["n1_meta_signal.py"])
    def fail(**kwargs):
        raise DataQualityError("TEST_MISSING_DATA")
    monkeypatch.setattr(runner, "execute", fail)
    before = protected_bytes()
    assert runner.main() == 1
    assert protected_bytes() == before
    assert strict_loads(runner.STATUS_PATH.read_text())["status"] == "BLOCKED"
