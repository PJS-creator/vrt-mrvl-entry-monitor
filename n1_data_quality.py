"""Fail-closed input/output contracts for the N1 shadow runner only."""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
import tempfile
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any

import exchange_calendars as xcals
import numpy as np
import pandas as pd


class DataQualityError(ValueError):
    """Safe diagnostic codes only; never include provider URLs or credentials."""


def reject_constant(value: str) -> None:
    raise DataQualityError(f"NONFINITE_JSON:{value}")


def strict_loads(text: str) -> dict:
    result = json.loads(text, parse_constant=reject_constant)
    if not isinstance(result, dict):
        raise DataQualityError("JSON_OBJECT_REQUIRED")
    check_finite_tree(result)
    return result


def check_finite_tree(value: Any, path: str = "root") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            check_finite_tree(child, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            check_finite_tree(child, f"{path}[{index}]")
    elif isinstance(value, float) and not math.isfinite(value):
        raise DataQualityError(f"NONFINITE:{path}")


def json_bytes(value: Any) -> bytes:
    check_finite_tree(value)
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")


def stable_hash(value: Any) -> str:
    check_finite_tree(value)
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def number(value: Any, name: str, *, positive: bool = False, bounded: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float, np.number)):
        raise DataQualityError(f"NUMERIC_REQUIRED:{name}")
    if not math.isfinite(value):
        raise DataQualityError(f"NONFINITE:{name}")
    if positive and value <= 0:
        raise DataQualityError(f"POSITIVE_REQUIRED:{name}")
    if bounded and not 0 <= value <= 100:
        raise DataQualityError(f"OUT_OF_RANGE:{name}")
    return float(value)


@lru_cache(maxsize=4)
def calendar(year: int):
    # QQQ and the US-listed Router ETFs share these regular-session holidays.
    return xcals.get_calendar("XNYS", start=f"{year - 25}-01-01", end=f"{year + 2}-12-31")


def completed_session(now: datetime | None = None) -> pd.Timestamp:
    current = pd.Timestamp(now or datetime.now(timezone.utc))
    if current.tzinfo is None:
        raise DataQualityError("UTC_CLOCK_REQUIRED")
    current = current.tz_convert("UTC")
    cal = calendar(current.year)
    day = current.tz_localize(None).normalize()
    sessions = cal.sessions_in_range(day - pd.Timedelta(days=14), day)
    done = [s for s in sessions if cal.session_close(s) + pd.Timedelta(minutes=15) <= current]
    if not done:
        raise DataQualityError("NO_COMPLETED_US_SESSION")
    return pd.Timestamp(done[-1]).tz_localize(None).normalize()


def next_session(day: pd.Timestamp) -> str:
    return calendar(day.year).next_session(day).strftime("%Y-%m-%d")


def sessions_between(start: pd.Timestamp, end: pd.Timestamp) -> pd.DatetimeIndex:
    return calendar(end.year).sessions_in_range(start, end).tz_localize(None)


def validate_prices(frame: pd.DataFrame, symbol: str, asof: pd.Timestamp, count: int = 260) -> pd.DataFrame:
    columns = ["Open", "High", "Low", "Close"]
    if frame is None or frame.empty or not set(columns).issubset(frame.columns):
        raise DataQualityError(f"PRICE_COLUMNS_MISSING:{symbol}")
    result = frame[columns].copy()
    result.index = pd.to_datetime(result.index).tz_localize(None).normalize()
    result = result.loc[result.index <= asof].sort_index()
    if result.index.has_duplicates:
        raise DataQualityError(f"DUPLICATE_PRICE_DATE:{symbol}")
    expected = sessions_between(asof - pd.Timedelta(days=count * 2), asof)[-count:]
    if len(expected) != count or asof not in result.index:
        raise DataQualityError(f"STALE_OR_SHORT_PRICES:{symbol}:{asof.date()}")
    if not expected.isin(result.index).all():
        raise DataQualityError(f"MISSING_PRICE_SESSION:{symbol}")
    try:
        result = result.astype(float)
    except (TypeError, ValueError) as exc:
        raise DataQualityError(f"NONNUMERIC_PRICE:{symbol}") from exc
    values = result.loc[expected].to_numpy()
    if not np.isfinite(values).all() or (values <= 0).any():
        raise DataQualityError(f"INVALID_OHLC:{symbol}")
    if not np.isfinite(result["Close"].to_numpy()).all() or (result["Close"] <= 0).any():
        raise DataQualityError(f"INVALID_CLOSE_HISTORY:{symbol}")
    recent = result.loc[expected]
    if ((recent["High"] < recent[["Open", "Close", "Low"]].max(axis=1))
            | (recent["Low"] > recent[["Open", "Close", "High"]].min(axis=1))).any():
        raise DataQualityError(f"INCONSISTENT_OHLC:{symbol}")
    # Never drop a missing completed session or fill a missing Close with yesterday's price.
    return result


REQUIRED_SIGNAL = {
    "validation_class", "signal_date", "execution_date", "qqq_adjusted_close",
    "sma20", "sma50", "sma200", "wilder_rsi14", "trend200_state", "recovery_state",
    "liquidity_p_raw_source_week", "liquidity_p_applied_row_week", "liquidity_p_applied",
    "liquidity_state", "comparison1_raw_state", "comparison1_raw_streak",
    "comparison1_confirmed_state", "comparison1_confirmed_target", "comparison3_target",
    "red_router_active", "router_asset", "final_regime", "active_engine",
    "base_execution_target", "n1_overlay_active", "n1_overlay_reason_code",
    "execution_target", "entry_filter", "reason_codes", "warnings", "data_missing",
    "rules_sha256", "input_sha256", "state_sha256", "price_source_id",
}
REQUIRED_STATE = {
    "signal_date", "trend200_state", "recovery_state", "liquidity_state",
    "comparison1_confirmed_state", "comparison1_candidate_state", "comparison1_candidate_count",
    "comparison1_last_raw_state", "comparison1_raw_streak", "comparison3_target",
    "router_latch_active", "router_asset", "router_entry_date", "execution_target",
}


def validate_checkpoint(signal: dict, state: dict, rules_hash: str) -> None:
    check_finite_tree(signal)
    check_finite_tree(state)
    if REQUIRED_SIGNAL - signal.keys() or REQUIRED_STATE - state.keys():
        raise DataQualityError("CHECKPOINT_FIELDS_MISSING")
    for field in ("qqq_adjusted_close", "sma20", "sma50", "sma200"):
        number(signal[field], field, positive=True)
    for field in ("wilder_rsi14", "liquidity_p_applied"):
        number(signal[field], field, bounded=True)
    if signal["data_missing"] is not False:
        raise DataQualityError("CHECKPOINT_NOT_VALIDATED")
    if signal["validation_class"] not in {
        "A_NORMAL", "B_WARN", "NO_NEW_COMPLETED_US_SESSION", "B_WARN_NO_NEW_SESSION"
    }:
        raise DataQualityError("CHECKPOINT_NOT_VALIDATED")
    if signal["rules_sha256"] != rules_hash or signal["state_sha256"] != stable_hash(state):
        raise DataQualityError("CHECKPOINT_HASH_MISMATCH")
    if signal["signal_date"] != state["signal_date"] or signal["execution_target"] != state["execution_target"]:
        raise DataQualityError("CHECKPOINT_STATE_MISMATCH")
    for signal_field, state_field in (
        ("trend200_state", "trend200_state"), ("recovery_state", "recovery_state"),
        ("liquidity_state", "liquidity_state"), ("comparison1_confirmed_state", "comparison1_confirmed_state"),
        ("comparison1_raw_state", "comparison1_last_raw_state"), ("comparison1_raw_streak", "comparison1_raw_streak"),
        ("comparison3_target", "comparison3_target"), ("red_router_active", "router_latch_active"),
        ("router_asset", "router_asset"),
    ):
        if signal[signal_field] != state[state_field]:
            raise DataQualityError(f"CHECKPOINT_STATE_MISMATCH:{signal_field}")
    for obj, fields in ((signal, ("recovery_state", "red_router_active", "n1_overlay_active")),
                        (state, ("recovery_state", "router_latch_active"))):
        if any(type(obj[field]) is not bool for field in fields):
            raise DataQualityError("BOOLEAN_STATE_REQUIRED")
    if signal["trend200_state"] not in {"UP", "DOWN"}:
        raise DataQualityError("INVALID_TREND_STATE")
    for field in ("input_sha256", "rules_sha256", "state_sha256"):
        if not isinstance(signal[field], str) or not re.fullmatch(r"[0-9a-f]{64}", signal[field]):
            raise DataQualityError(f"INVALID_HASH:{field}")
    expected_input = stable_hash({"signal_date": signal["signal_date"], "close": signal["qqq_adjusted_close"],
                                  "p": signal["liquidity_p_applied"], "provider": signal["price_source_id"]})
    if signal["input_sha256"] != expected_input:
        raise DataQualityError("INPUT_HASH_MISMATCH")
    try:
        date = pd.Timestamp(signal["signal_date"])
        if signal["signal_date"] != date.strftime("%Y-%m-%d") or not calendar(date.year).is_session(date):
            raise ValueError
        if pd.Timestamp(signal["execution_date"]) <= date:
            raise ValueError
    except (TypeError, ValueError) as exc:
        raise DataQualityError("INVALID_CHECKPOINT_DATE") from exc
    targets = {"QQQ", "QLD", "TQQQ", "GLD", "XLV"}
    for field in ("execution_target", "base_execution_target", "comparison1_confirmed_target", "comparison3_target"):
        if signal[field] not in targets:
            raise DataQualityError(f"INVALID_TARGET:{field}")
    for field in ("liquidity_state", "final_regime"):
        if signal[field] not in {"BULL", "MIXED", "BEAR"}:
            raise DataQualityError(f"INVALID_STATE:{field}")
    if state["comparison1_confirmed_state"] not in {"GREEN", "YELLOW", "RED"}:
        raise DataQualityError("INVALID_CONFIRMED_STATE")
    if state["comparison1_candidate_state"] not in {None, "GREEN", "YELLOW", "RED"}:
        raise DataQualityError("INVALID_CANDIDATE_STATE")
    for field in ("comparison1_raw_streak", "comparison1_candidate_count"):
        if type(state[field]) is not int or state[field] < 0:
            raise DataQualityError(f"INVALID_COUNTER:{field}")
    if state["router_latch_active"]:
        if state["router_asset"] not in {"QQQ", "GLD", "XLV"} or not state["router_entry_date"]:
            raise DataQualityError("INVALID_ROUTER_STATE")
    elif state["router_asset"] is not None or state["router_entry_date"] is not None:
        raise DataQualityError("INACTIVE_ROUTER_HAS_ASSET")


def publish_files(payloads: dict[Path, bytes]) -> None:
    """Stage all bytes before replacement; roll back ordinary write failures.

    The signal/state hash detects a process/power loss between replacements.
    Callers validate the entire checkpoint before calling this function.
    """
    staged: dict[Path, Path] = {}
    previous = {path: path.read_bytes() if path.exists() else None for path in payloads}
    replaced = []
    try:
        for path, content in payloads.items():
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".n1-", delete=False) as file:
                staged[path] = Path(file.name)
                file.write(content)
                file.flush()
                os.fsync(file.fileno())
        for path, temp in staged.items():
            os.replace(temp, path)
            replaced.append(path)
    except BaseException:
        for path in reversed(replaced):
            if previous[path] is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(previous[path])
        raise
    finally:
        for temp in staged.values():
            temp.unlink(missing_ok=True)
