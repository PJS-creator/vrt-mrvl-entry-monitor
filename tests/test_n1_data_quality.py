from datetime import datetime, timezone

import numpy as np
import pandas as pd
import pytest

import n1_data_quality as quality
import n1_meta_signal as runner
import n1_meta_signal_core as core
from n1_validate_outputs import validate_outputs


@pytest.mark.parametrize("value", ["NaN", "Infinity", "-Infinity", "1e999"])
def test_strict_json_rejects_nonfinite(value):
    with pytest.raises(quality.DataQualityError):
        quality.strict_loads('{"value":' + value + '}')


@pytest.mark.parametrize("field", ["qqq_adjusted_close", "sma20", "sma50", "sma200", "wilder_rsi14", "liquidity_p_applied"])
@pytest.mark.parametrize("value", [None, float("nan"), float("inf"), "NaN", True])
def test_required_numeric_fields_fail_closed(workspace, field, value):
    signal, state, *_ = workspace
    signal[field] = value
    with pytest.raises(quality.DataQualityError):
        quality.validate_checkpoint(signal, state, runner.rules_hash())


def test_optional_inactive_router_nulls_are_valid(workspace):
    signal, state, *_ = workspace
    assert state["router_asset"] is None
    quality.validate_checkpoint(signal, state, runner.rules_hash())


@pytest.mark.parametrize("field", ["signal_date", "execution_target", "state_sha256", "rules_sha256"])
def test_mismatched_checkpoint_rejected(workspace, field):
    signal, state, *_ = workspace
    signal[field] = "wrong"
    with pytest.raises(quality.DataQualityError):
        quality.validate_checkpoint(signal, state, runner.rules_hash())


def test_hash_is_strict_and_rules_hash_ignores_checkout_line_endings(tmp_path, monkeypatch):
    with pytest.raises(quality.DataQualityError):
        quality.stable_hash({"x": float("nan")})
    rules = tmp_path / "rules.yaml"
    monkeypatch.setattr(core, "YAML_PATH", rules)
    rules.write_bytes(b"a: 1\nb: 2\n")
    unix = core.rules_hash()
    rules.write_bytes(b"a: 1\r\nb: 2\r\n")
    assert core.rules_hash() == unix


@pytest.mark.parametrize("kind", ["nan_close", "inf_high", "missing_day", "duplicate", "stale", "zero"])
def test_bad_price_frames_rejected(inputs, kind):
    prices, _ = inputs
    frame = prices["QQQ"][0].copy()
    if kind == "nan_close":
        frame.iloc[-1, frame.columns.get_loc("Close")] = np.nan
    elif kind == "inf_high":
        frame.iloc[-1, frame.columns.get_loc("High")] = np.inf
    elif kind == "missing_day":
        frame = frame.drop(frame.index[-5])
    elif kind == "duplicate":
        frame = pd.concat([frame, frame.tail(1)])
    elif kind == "stale":
        frame = frame.iloc[:-1]
    else:
        frame.iloc[-1, frame.columns.get_loc("Close")] = 0
    with pytest.raises(quality.DataQualityError):
        quality.validate_prices(frame, "QQQ", pd.Timestamp("2026-09-17"))


def test_intraday_row_does_not_poison_completed_session(inputs):
    prices, _ = inputs
    frame = prices["QQQ"][0].copy()
    frame.loc[pd.Timestamp("2026-09-18")] = np.nan
    trimmed = quality.validate_prices(frame, "QQQ", pd.Timestamp("2026-09-17"))
    assert trimmed.index.max() == pd.Timestamp("2026-09-17")


def test_calendar_holiday_early_close_and_settlement_buffer():
    assert quality.completed_session(datetime(2026, 9, 7, 23, tzinfo=timezone.utc)) == pd.Timestamp("2026-09-04")
    assert quality.next_session(pd.Timestamp("2026-09-04")) == "2026-09-08"
    assert quality.completed_session(datetime(2026, 11, 27, 18, 14, tzinfo=timezone.utc)) == pd.Timestamp("2026-11-25")
    assert quality.completed_session(datetime(2026, 11, 27, 18, 15, tzinfo=timezone.utc)) == pd.Timestamp("2026-11-27")


def test_save_json_never_overwrites_with_nan(tmp_path):
    path = tmp_path / "saved.json"
    path.write_bytes(b"original")
    with pytest.raises(quality.DataQualityError):
        core.save_json(path, {"x": np.nan})
    assert path.read_bytes() == b"original"


def test_staged_write_rolls_back_ordinary_failure(tmp_path, monkeypatch):
    first, second = tmp_path / "first", tmp_path / "second"
    first.write_bytes(b"first-old")
    second.write_bytes(b"second-old")
    replace = quality.os.replace
    count = 0
    def fail_second(src, dst):
        nonlocal count
        count += 1
        if count == 2:
            raise OSError("simulated write failure")
        replace(src, dst)
    monkeypatch.setattr(quality.os, "replace", fail_second)
    with pytest.raises(OSError):
        quality.publish_files({first: b"first-new", second: b"second-new"})
    assert first.read_bytes() == b"first-old"
    assert second.read_bytes() == b"second-old"
    assert not list(tmp_path.glob(".n1-*"))


def test_ci_contract_checks_status_hash_and_lineage(workspace):
    validate_outputs()
    status = quality.strict_loads(runner.STATUS_PATH.read_text())
    status["signal_sha256"] = "wrong"
    core.save_json(runner.STATUS_PATH, status)
    with pytest.raises(quality.DataQualityError, match="RUN_STATUS"):
        validate_outputs()


def test_finite_but_different_lineage_fails(workspace):
    signal, _, _, lineage = workspace
    changed = lineage.copy()
    changed.loc[pd.Timestamp("2026-09-11"), "p_applied"] = 81.0
    with pytest.raises(quality.DataQualityError, match="LINEAGE_MISMATCH"):
        runner.validate_lineage(changed, signal)


def test_old_missing_close_is_not_silently_skipped_by_rsi(inputs):
    prices, _ = inputs
    frame = prices["QQQ"][0].copy()
    frame.iloc[10, frame.columns.get_loc("Close")] = np.nan
    with pytest.raises(quality.DataQualityError, match="CLOSE_HISTORY"):
        quality.validate_prices(frame, "QQQ", pd.Timestamp("2026-09-17"))


def test_finite_but_inconsistent_ohlc_rejected(inputs):
    prices, _ = inputs
    frame = prices["QQQ"][0].copy()
    frame.iloc[-1, frame.columns.get_loc("High")] = 1.0
    with pytest.raises(quality.DataQualityError, match="INCONSISTENT_OHLC"):
        quality.validate_prices(frame, "QQQ", pd.Timestamp("2026-09-17"))


def test_recomputed_state_hash_cannot_hide_signal_state_mismatch(workspace):
    signal, state, *_ = workspace
    state["trend200_state"] = "DOWN"
    signal["state_sha256"] = quality.stable_hash(state)
    with pytest.raises(quality.DataQualityError, match="STATE_MISMATCH"):
        quality.validate_checkpoint(signal, state, runner.rules_hash())


def test_modified_price_rejected_by_input_hash(workspace):
    signal, state, *_ = workspace
    signal["qqq_adjusted_close"] += 1
    with pytest.raises(quality.DataQualityError, match="INPUT_HASH_MISMATCH"):
        quality.validate_checkpoint(signal, state, runner.rules_hash())
