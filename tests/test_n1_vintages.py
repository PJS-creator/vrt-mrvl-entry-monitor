from types import SimpleNamespace

import pandas as pd
import pytest

import n1_meta_signal_core as core
import n1_vintages as vintages
from n1_data_quality import DataQualityError

DAY = pd.Timestamp("2026-09-23")


def test_vintage_rejects_current_series_or_wrong_vintage():
    for header in ("WALCL", "WALCL_20260924"):
        with pytest.raises(DataQualityError, match="HEADER_MISMATCH"):
            vintages.parse_vintage(f"observation_date,{header}\n2026-09-16,100\n", "WALCL", DAY)


@pytest.mark.parametrize("rows,code", [
    ("2026-09-24,100", "DATES_INVALID"),
    ("2026-09-16,100\n2026-09-16,101", "DATES_INVALID"),
    ("2026-09-16,NaN", "VALUES_INVALID"),
    ("2026-09-16,Infinity", "VALUES_INVALID"),
    ("2026-09-16,abc", "VALUES_INVALID"),
    ("2026-09-16,0", "VALUES_INVALID"),
    ("2026-09-01,100", "VINTAGE_STALE"),
])
def test_bad_vintage_data_is_rejected(rows, code):
    with pytest.raises(DataQualityError, match=code):
        vintages.parse_vintage(f"observation_date,WALCL_20260923\n{rows}\n", "WALCL", DAY)


def test_vintage_allows_reported_missing_days_and_zero_reverse_repos():
    result = vintages.parse_vintage(
        "observation_date,RRPONTSYD_20260923\n2026-09-21,0\n2026-09-22,.\n2026-09-23,1\n",
        "RRPONTSYD", DAY,
    )
    assert result.tolist() == [0.0, 1.0]
    assert pd.Timestamp("2026-09-22") not in result.index


def test_vintage_fetch_saves_exact_source_bytes_and_date(tmp_path, monkeypatch):
    calls = []
    def get(url, params, timeout):
        calls.append(dict(params))
        text = f"observation_date,{params['id']}_20260923\n2026-09-22,100\n"
        return SimpleNamespace(text=text, content=text.encode(), url=url,
                               raise_for_status=lambda: None)
    monkeypatch.setattr(vintages.requests, "get", get)
    monkeypatch.setattr(vintages, "build_liquidity_panel", lambda data: pd.DataFrame(data))
    _, metadata = vintages.fetch_liquidity_vintage(DAY, tmp_path)
    assert all(call["vintage_date"] == "2026-09-23" for call in calls)
    assert {call["id"] for call in calls} == set(vintages.SERIES)
    assert len(metadata["sources"]) == 3
    assert (tmp_path / "manifest-2026-09-23.json").exists()
    for source in metadata["sources"]:
        import hashlib
        assert hashlib.sha256((tmp_path / source["file"]).read_bytes()).hexdigest() == source["sha256"]


def test_cboe_parser_preserves_official_ohlc(monkeypatch):
    text = "DATE,OPEN,HIGH,LOW,CLOSE\n09/22/2026,15.1,16.2,14.3,15.4\n"
    monkeypatch.setattr(core.requests, "get", lambda *args, **kwargs:
                        SimpleNamespace(text=text, raise_for_status=lambda: None))
    frame = core.fetch_cboe_vix()
    assert frame.index[0] == pd.Timestamp("2026-09-22")
    assert frame.iloc[0].tolist() == [15.1, 16.2, 14.3, 15.4]
