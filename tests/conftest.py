from datetime import datetime, timezone

import numpy as np
import pandas as pd
import pytest

import n1_meta_signal as runner
import n1_meta_signal_core as core
from n1_data_quality import sessions_between


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Network is forbidden in unit tests")
    monkeypatch.setattr(core.requests, "get", forbidden)
    monkeypatch.setattr(core.yf, "download", forbidden)
    monkeypatch.setattr(core.yf, "Ticker", forbidden)


@pytest.fixture
def inputs():
    dates = sessions_between(pd.Timestamp("2023-01-03"), pd.Timestamp("2026-09-17"))
    close = 100.0 + np.arange(len(dates)) * 0.05 + np.sin(np.arange(len(dates)) / 3)
    frame = pd.DataFrame({"Open": close, "High": close + 1, "Low": close - 1, "Close": close}, index=dates)
    price_data = {symbol: (frame.copy(), "test_fixture", []) for symbol in ("QQQ", "GLD", "XLV", "^VIX")}
    weeks = pd.date_range("2026-07-24", "2026-09-18", freq="W-FRI", name="applied_row_week")
    lineage = pd.DataFrame({"p_applied": 80.0, "p_raw": 80.0,
                            "p_raw_source_week": (weeks - pd.Timedelta(days=7)).strftime("%Y-%m-%d")}, index=weeks)
    return price_data, lineage


@pytest.fixture
def workspace(tmp_path, monkeypatch, inputs):
    for variable, filename in [("STATE_PATH", "state.json"), ("SIGNAL_PATH", "signal.json"),
                               ("MD_PATH", "signal.md"), ("LINEAGE_PATH", "lineage.csv")]:
        monkeypatch.setattr(core, variable, tmp_path / filename)
    monkeypatch.setattr(runner, "STATUS_PATH", tmp_path / "status.json")
    monkeypatch.setattr(runner, "AUDIT_DIR", tmp_path / "audit")
    prices, lineage = inputs
    state = dict(core.ANCHOR, signal_date="2026-09-15", comparison1_last_raw_state="YELLOW")
    signal, state = core.calculate_signal(state, prices, lineage, pd.Timestamp("2026-09-16"))
    runner.publish_checkpoint(signal, state, lineage, datetime(2026, 9, 17, 1, tzinfo=timezone.utc))
    return signal, state, prices, lineage
