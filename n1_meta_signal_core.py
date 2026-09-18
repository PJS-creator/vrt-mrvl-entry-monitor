#!/usr/bin/env python3
"""Daily shadow runner for Meta-v1.0 + RED Router-S1 + N1 + V4.

This runner never submits broker orders. It writes a deterministic signal JSON,
Markdown summary, persistent state snapshot, and liquidity-P lineage CSV.
"""
from __future__ import annotations

import hashlib
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests
import yfinance as yf

from n1_data_quality import (
    DataQualityError, completed_session, json_bytes, next_session, number,
    publish_files, stable_hash, strict_loads, validate_checkpoint, validate_prices,
)

ROOT = Path(__file__).resolve().parent
YAML_PATH = ROOT / "strategies" / "qqq_meta_v1_red_router_s1_n1_v4_shadow_v2_3.kis.yaml"
STATE_PATH = ROOT / "n1_latest_state_snapshot.json"
SIGNAL_PATH = ROOT / "n1_latest_signal.json"
MD_PATH = ROOT / "n1_latest_signal.md"
LINEAGE_PATH = ROOT / "n1_liquidity_p_lineage.csv"

ANCHOR_DATE = pd.Timestamp("2026-07-31")
ANCHOR = {
    "signal_date": "2026-07-31",
    "trend200_state": "UP",
    "recovery_state": False,
    "liquidity_state": "BULL",
    "comparison1_confirmed_state": "YELLOW",
    "comparison1_candidate_state": None,
    "comparison1_candidate_count": 0,
    "comparison1_raw_streak": 12,
    "comparison3_target": "QLD",
    "router_latch_active": False,
    "router_asset": None,
    "router_entry_date": None,
    "execution_target": "QQQ",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rules_hash() -> str:
    # Git may check out CRLF on Windows; hash the canonical repository LF text.
    return sha256_bytes(YAML_PATH.read_bytes().replace(b"\r\n", b"\n"))


def read_state() -> dict[str, Any]:
    if STATE_PATH.exists():
        return strict_loads(STATE_PATH.read_text(encoding="utf-8"))
    return dict(ANCHOR)


def save_json(path: Path, obj: Any) -> None:
    publish_files({path: json_bytes(obj)})


def fetch_tiingo(symbol: str, start: str) -> pd.DataFrame:
    token = os.getenv("TIINGO_API_TOKEN", "").strip()
    if not token:
        raise DataQualityError("TIINGO_TOKEN_NOT_CONFIGURED")
    url = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices"
    response = requests.get(
        url,
        params={"startDate": start, "resampleFreq": "daily", "token": token},
        timeout=45,
    )
    response.raise_for_status()
    rows = response.json()
    if not rows:
        raise DataQualityError(f"TIINGO_EMPTY_RESPONSE:{symbol}")
    df = pd.DataFrame(rows)
    df["Date"] = pd.to_datetime(df["date"], utc=True).dt.tz_convert(None).dt.normalize()
    return df.set_index("Date").rename(
        columns={"adjOpen": "Open", "adjHigh": "High", "adjLow": "Low", "adjClose": "Close"}
    )[["Open", "High", "Low", "Close"]].astype(float)


def fetch_prices(
    symbol: str, start: str = "2005-01-01", *, asof: pd.Timestamp | None = None,
) -> tuple[pd.DataFrame, str, list[str]]:
    asof = asof if asof is not None else completed_session()
    warnings: list[str] = []
    try:
        df = validate_prices(fetch_tiingo(symbol, start), symbol, asof)
        return df, "tiingo", warnings
    except Exception as exc:
        code = str(exc) if isinstance(exc, DataQualityError) else type(exc).__name__
        warnings.append(f"TIINGO_FALLBACK:{symbol}:{code}")
    # Retry via single-symbol history if a bulk download is incomplete. Do not
    # merge providers, synthesize a Close, or enable Yahoo's price repair mode.
    for attempt in range(2):
        try:
            if attempt == 0:
                df = yf.download(symbol, start=start, auto_adjust=True, progress=False,
                                 actions=False, threads=False, timeout=30)
                if isinstance(df.columns, pd.MultiIndex):
                    df.columns = df.columns.get_level_values(0)
            else:
                df = yf.Ticker(symbol).history(start=start, auto_adjust=True, actions=False,
                                               repair=False, timeout=30)
            return validate_prices(df, symbol, asof), "yfinance_shadow_fallback", warnings
        except Exception as exc:
            code = str(exc) if isinstance(exc, DataQualityError) else type(exc).__name__
            warnings.append(f"YFINANCE_ATTEMPT_{attempt + 1}:{symbol}:{code}")
    raise DataQualityError("PRICE_PROVIDERS_EXHAUSTED:" + "|".join(warnings))


def wilder_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0.0)
    loss = -delta.clip(upper=0.0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    rs = avg_gain / avg_loss.replace(0.0, np.nan)
    out = 100.0 - 100.0 / (1.0 + rs)
    return out.where(avg_loss != 0.0, 100.0)


def fred_series(series_id: str) -> pd.Series:
    from io import StringIO
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv"
    r = requests.get(url, params={"id": series_id}, timeout=45)
    r.raise_for_status()
    df = pd.read_csv(StringIO(r.text))
    df.columns = ["Date", series_id]
    df["Date"] = pd.to_datetime(df["Date"])
    values = pd.to_numeric(df[series_id], errors="coerce")
    return pd.Series(values.to_numpy(), index=df["Date"], name=series_id).dropna().sort_index()


def percentile_prior(window: pd.Series, value: float) -> float:
    arr = window.dropna().to_numpy(dtype=float)
    if len(arr) == 0:
        return float("nan")
    less = np.sum(arr < value)
    equal = np.sum(arr == value)
    return 100.0 * (less + 0.5 * equal) / len(arr)


def liquidity_panel() -> pd.DataFrame:
    walcl = fred_series("WALCL") / 1000.0
    tga = fred_series("WDTGAL") / 1000.0
    rrp = fred_series("RRPONTSYD")
    start = min(walcl.index.min(), tga.index.min(), rrp.index.min())
    end = max(walcl.index.max(), tga.index.max(), rrp.index.max())
    daily = pd.DataFrame(index=pd.date_range(start, end, freq="D"))
    daily["WALCL"] = walcl.reindex(daily.index).ffill()
    daily["WDTGAL"] = tga.reindex(daily.index).ffill()
    daily["RRPONTSYD"] = rrp.reindex(daily.index).ffill()
    wed = daily.resample("W-WED").last().dropna()
    wed["net_liquidity"] = wed["WALCL"] - wed["WDTGAL"] - wed["RRPONTSYD"]
    wed["growth_26w_log"] = np.log(wed["net_liquidity"] / wed["net_liquidity"].shift(26))
    wed["growth_13w_smooth"] = wed["growth_26w_log"].rolling(13, min_periods=13).mean()
    p_raw = []
    for i, val in enumerate(wed["growth_13w_smooth"]):
        if i < 260 or pd.isna(val):
            p_raw.append(float("nan"))
        else:
            p_raw.append(percentile_prior(wed["growth_13w_smooth"].iloc[i - 260:i], float(val)))
    wed["p_raw"] = p_raw
    panel = wed.copy()
    panel.index = panel.index + pd.Timedelta(days=2)
    panel.index.name = "applied_row_week"
    panel["p_applied"] = panel["p_raw"].shift(1)
    panel["p_raw_source_week"] = panel.index.to_series().shift(1).dt.strftime("%Y-%m-%d")
    return panel


def hysteresis(prev: str, p: float) -> str:
    if not math.isfinite(p):
        return prev if prev in {"BULL", "MIXED", "BEAR"} else "MIXED"
    if prev == "BULL":
        return "BULL" if p >= 65 else ("BEAR" if p <= 25 else "MIXED")
    if prev == "BEAR":
        return "BEAR" if p <= 35 else ("BULL" if p >= 75 else "MIXED")
    if p >= 75:
        return "BULL"
    if p <= 25:
        return "BEAR"
    return "MIXED"


def confirmed_state_update(prev: dict[str, Any], raw: str) -> tuple[str, str | None, int]:
    current = prev.get("comparison1_confirmed_state", "YELLOW")
    candidate = prev.get("comparison1_candidate_state")
    count = int(prev.get("comparison1_candidate_count", 0))
    if raw == current:
        return current, None, 0
    if raw == candidate:
        count += 1
    else:
        candidate, count = raw, 1
    if count >= 2:
        return raw, None, 0
    return current, candidate, count


def target_for_comp1(state: str) -> str:
    return {"GREEN": "TQQQ", "YELLOW": "QLD", "RED": "QQQ"}[state]


def fred_asof(series_id: str, signal_date: pd.Timestamp, lag_sessions: int = 1) -> pd.Series:
    s = fred_series(series_id)
    s = s.reindex(pd.date_range(s.index.min(), signal_date, freq="D")).ffill()
    business = pd.bdate_range(s.index.min(), signal_date)
    return s.reindex(business).ffill().shift(lag_sessions)


def calculate_signal(
    state: dict[str, Any],
    price_data: dict[str, tuple[pd.DataFrame, str, list[str]]],
    lineage: pd.DataFrame,
    signal_date: pd.Timestamp,
    *, allow_router_fetch: bool = True,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Calculate a single session without publishing any checkpoint files."""
    prior_signal_date = pd.Timestamp(state.get("signal_date", ANCHOR_DATE))
    warnings: list[str] = []
    frames = {}
    for symbol, (frame, _, notes) in price_data.items():
        frames[symbol] = validate_prices(frame, symbol, signal_date)
        warnings.extend(notes)
    qqq, gld, vix = frames["QQQ"], frames["GLD"], frames["^VIX"]
    provider = price_data["QQQ"][1]
    qqq["SMA20"] = qqq["Close"].rolling(20).mean()
    qqq["SMA50"] = qqq["Close"].rolling(50).mean()
    qqq["SMA200"] = qqq["Close"].rolling(200).mean()
    qqq["RSI14"] = wilder_rsi(qqq["Close"], 14)

    applicable = lineage.loc[lineage.index <= signal_date]
    if applicable.empty:
        raise DataQualityError("P_APPLIED_MISSING")
    p_row = applicable.iloc[-1]
    p_applied = number(p_row["p_applied"], "p_applied", bounded=True)
    if pd.isna(p_row["p_raw_source_week"]) or signal_date - applicable.index[-1] > pd.Timedelta(days=7):
        raise DataQualityError("P_LINEAGE_STALE_OR_MISSING")
    liquidity_state = hysteresis(str(state.get("liquidity_state", "MIXED")), p_applied)

    row = qqq.loc[signal_date]
    close = number(row["Close"], "qqq_adjusted_close", positive=True)
    sma20, sma50, sma200 = [number(row[key], key, positive=True) for key in ("SMA20", "SMA50", "SMA200")]
    rsi = number(row["RSI14"], "RSI14", bounded=True)
    prev_rsi = number(qqq["RSI14"].iloc[-2], "previous_RSI14", bounded=True)
    weekly = qqq.resample("W-FRI").last().dropna(subset=["Close", "SMA200"])
    last2 = weekly.tail(2)
    trend = str(state.get("trend200_state", "UP"))
    if len(last2) == 2:
        if bool((last2["Close"] > last2["SMA200"]).all()):
            trend = "UP"
        elif bool((last2["Close"] < last2["SMA200"]).all()):
            trend = "DOWN"

    recovery = bool(state.get("recovery_state", False))
    if trend == "UP":
        recovery = False
    else:
        last5 = qqq.tail(5)
        if len(last5) == 5 and bool((last5["Close"] > last5["SMA20"]).all()) and row["SMA20"] > qqq["SMA20"].iloc[-6]:
            recovery = True
        if len(qqq) >= 2 and bool((qqq["Close"].tail(2) <= qqq["SMA20"].tail(2)).all()):
            recovery = False

    final_regime = "BEAR" if trend == "DOWN" and not recovery else ("BULL" if trend == "UP" and liquidity_state == "BULL" else "MIXED")

    raw1 = "GREEN" if close > sma50 and close > sma200 else ("RED" if close < sma50 and close < sma200 else "YELLOW")
    raw_streak = int(state.get("comparison1_raw_streak", 0)) + 1 if raw1 == state.get("comparison1_last_raw_state", raw1) else 1
    confirmed1, candidate1, candidate_count1 = confirmed_state_update(state, raw1)
    comp1_target = target_for_comp1(confirmed1)

    comp3 = str(state.get("comparison3_target", "QLD"))
    if comp3 == "TQQQ" and prev_rsi <= 80 < rsi:
        comp3 = "QLD"
    elif comp3 == "QLD" and close < sma200 and prev_rsi <= 40 < rsi:
        comp3 = "TQQQ"

    latch_active = bool(state.get("router_latch_active", False))
    router_asset = state.get("router_asset")
    router_entry_date = state.get("router_entry_date")
    if latch_active and not (final_regime == "BEAR" and confirmed1 == "RED"):
        latch_active, router_asset, router_entry_date = False, None, None

    if final_regime == "BEAR" and confirmed1 == "RED" and not latch_active:
        if not allow_router_fetch:
            raise DataQualityError("RECOVERY_ROUTER_MACRO_VINTAGE_UNAVAILABLE")
        try:
            vix_s = vix["Close"].reindex(qqq.index).ffill()
            hy = fred_asof("BAMLH0A0HYM2", signal_date)
            real = fred_asof("DFII10", signal_date)
            dollar = fred_asof("DTWEXBGS", signal_date)
            # Missing Router inputs must not silently select the defensive asset.
            for label, series, lag in (("VIX", vix_s, 11), ("HY", hy, 21),
                                       ("REAL", real, 21), ("DOLLAR", dollar, 21)):
                number(series.loc[signal_date], label)
                number(series.iloc[-lag], f"{label}_LAG")
            qqq_gate = (
                float(vix_s.loc[signal_date]) < float(vix_s.iloc[-11])
                and float(hy.loc[signal_date]) <= float(hy.iloc[-21])
                and close > float(qqq["Close"].iloc[-6])
            )
            gld_close = float(gld["Close"].reindex(qqq.index).ffill().loc[signal_date])
            gld_sma20 = float(gld["Close"].rolling(20).mean().reindex(qqq.index).ffill().loc[signal_date])
            gld_gate = gld_close > gld_sma20 and (
                float(real.loc[signal_date]) < float(real.iloc[-21])
                or float(dollar.loc[signal_date]) < float(dollar.iloc[-21])
            )
            router_asset = "QQQ" if qqq_gate else ("GLD" if gld_gate else "XLV")
        except Exception as exc:
            raise DataQualityError(f"ROUTER_INPUT_UNAVAILABLE:{type(exc).__name__}") from exc
        latch_active = True
        router_entry_date = signal_date.strftime("%Y-%m-%d")

    active_engine = "COMPARISON1" if final_regime == "BEAR" else "COMPARISON3"
    base_target = router_asset if latch_active else (comp1_target if final_regime == "BEAR" else comp3)
    n1_active = final_regime == "BULL" and active_engine == "COMPARISON3" and comp3 == "QLD" and base_target == "QLD" and not latch_active
    post_n1_target = "QQQ" if n1_active else base_target

    new_session = signal_date > prior_signal_date
    next_execution_date = next_session(signal_date)
    rules_digest = rules_hash()
    validation_class = "A_NORMAL" if not warnings else "B_WARN"
    if not new_session:
        validation_class = "NO_NEW_COMPLETED_US_SESSION" if not warnings else "B_WARN_NO_NEW_SESSION"

    state_out = {
        "signal_date": signal_date.strftime("%Y-%m-%d"),
        "trend200_state": trend,
        "recovery_state": recovery,
        "liquidity_state": liquidity_state,
        "comparison1_confirmed_state": confirmed1,
        "comparison1_candidate_state": candidate1,
        "comparison1_candidate_count": candidate_count1,
        "comparison1_last_raw_state": raw1,
        "comparison1_raw_streak": raw_streak,
        "comparison3_target": comp3,
        "router_latch_active": latch_active,
        "router_asset": router_asset,
        "router_entry_date": router_entry_date,
        "execution_target": post_n1_target,
    }
    state_hash = stable_hash(state_out)

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "validation_class": validation_class,
        "signal_date": signal_date.strftime("%Y-%m-%d"),
        "execution_date": next_execution_date,
        "new_completed_us_session": bool(new_session),
        "price_source_id": provider,
        "qqq_adjusted_close": close,
        "sma20": sma20,
        "sma50": sma50,
        "sma200": sma200,
        "wilder_rsi14": rsi,
        "trend200_state": trend,
        "recovery_state": recovery,
        "liquidity_p_raw_source_week": p_row["p_raw_source_week"],
        "liquidity_p_applied_row_week": applicable.index[-1].strftime("%Y-%m-%d"),
        "liquidity_p_applied": p_applied,
        "liquidity_state": liquidity_state,
        "comparison1_raw_state": raw1,
        "comparison1_raw_streak": raw_streak,
        "comparison1_confirmed_state": confirmed1,
        "comparison1_confirmed_target": comp1_target,
        "comparison3_target": comp3,
        "red_router_active": latch_active,
        "router_asset": router_asset,
        "router_entry_date": router_entry_date,
        "final_regime": final_regime,
        "active_engine": active_engine,
        "base_execution_target": base_target,
        "n1_overlay_active": n1_active,
        "n1_overlay_reason_code": "N1_BULL_COMPARISON3_QLD_TO_QQQ" if n1_active else None,
        "post_n1_execution_target": post_n1_target,
        "execution_target": post_n1_target,
        "entry_filter": "NA_NO_NEW_CASH_EVENT",
        "action": "SHADOW_TARGET_UPDATE" if new_session else "HOLD_PREVIOUS_VALIDATED_TARGET",
        "reason_codes": (["NEW_COMPLETED_US_SESSION"] if new_session else ["NO_NEW_COMPLETED_US_SESSION"]) + (["N1_BULL_COMPARISON3_QLD_TO_QQQ"] if n1_active else []),
        "data_missing": False,
        "warnings": list(dict.fromkeys(warnings)),
        "rules_sha256": rules_digest,
        "input_sha256": stable_hash({"signal_date": str(signal_date.date()), "close": close, "p": p_applied, "provider": provider}),
        "state_sha256": state_hash,
    }
    validate_checkpoint(output, state_out, rules_digest)
    return output, state_out


if __name__ == "__main__":
    raise SystemExit("Use n1_meta_signal.py; core calculations never publish state directly.")
