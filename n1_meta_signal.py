#!/usr/bin/env python3
"""Idempotent completed-session entrypoint for the N1 QQQ Meta shadow runner.

Persistent strategy state advances at most once per completed US regular session.
Intraday bars are never treated as completed sessions. Repeated runs for the same
completed signal date refresh the report only and do not mutate persistent state.
If more than one completed session is unprocessed, fail closed instead of skipping
intermediate state transitions.
"""
from __future__ import annotations

import json
from datetime import datetime, time, timezone
from typing import Any, Callable
from zoneinfo import ZoneInfo

import pandas as pd

import n1_meta_signal_core as core

NY = ZoneInfo("America/New_York")
REGULAR_CLOSE_ET = time(16, 0)
CLOSE_SETTLE_BUFFER_MINUTES = 15


def _dedupe(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


def _latest_completed_session(index: pd.DatetimeIndex, now_utc: datetime | None = None) -> pd.Timestamp:
    if len(index) == 0:
        raise RuntimeError("EMPTY_QQQ_PRICE_INDEX")

    now_utc = now_utc or datetime.now(timezone.utc)
    now_et = now_utc.astimezone(NY)
    latest = pd.Timestamp(index.max()).tz_localize(None).normalize()

    if latest.date() == now_et.date():
        close_minutes = REGULAR_CLOSE_ET.hour * 60 + REGULAR_CLOSE_ET.minute + CLOSE_SETTLE_BUFFER_MINUTES
        now_minutes = now_et.hour * 60 + now_et.minute
        if now_minutes < close_minutes:
            prior = pd.DatetimeIndex(index)[pd.DatetimeIndex(index).normalize() < latest]
            if len(prior) == 0:
                raise RuntimeError("NO_PRIOR_COMPLETED_QQQ_SESSION")
            latest = pd.Timestamp(prior.max()).tz_localize(None).normalize()

    return latest


def _write_no_new_session_report(
    state: dict[str, Any], signal_date: pd.Timestamp, detection_warnings: list[str]
) -> None:
    if not core.SIGNAL_PATH.exists():
        raise RuntimeError("NO_EXISTING_SIGNAL_FOR_IDEMPOTENT_RERUN")

    output = json.loads(core.SIGNAL_PATH.read_text(encoding="utf-8"))
    if output.get("signal_date") != signal_date.strftime("%Y-%m-%d"):
        raise RuntimeError("SIGNAL_STATE_DATE_MISMATCH_ON_IDEMPOTENT_RERUN")

    warnings = _dedupe(list(output.get("warnings") or []) + detection_warnings)
    output["generated_at"] = datetime.now(timezone.utc).isoformat()
    output["validation_class"] = (
        "B_WARN_NO_NEW_SESSION" if warnings else "NO_NEW_COMPLETED_US_SESSION"
    )
    output["new_completed_us_session"] = False
    output["action"] = "HOLD_PREVIOUS_VALIDATED_TARGET"
    output["reason_codes"] = ["NO_NEW_COMPLETED_US_SESSION"] + (
        ["N1_BULL_COMPARISON3_QLD_TO_QQQ"] if output.get("n1_overlay_active") else []
    )
    output["warnings"] = warnings
    output["state_sha256"] = core.stable_hash(state)
    core.save_json(core.SIGNAL_PATH, output)

    md = f"""# N1 QQQ Meta Daily Shadow Signal\n\n- Validation: **{output['validation_class']}**\n- Signal date: **{output['signal_date']}**\n- Next execution session: **{output['execution_date']}**\n- QQQ / SMA20 / SMA50 / SMA200 / RSI14: **{output['qqq_adjusted_close']:.4f} / {output['sma20']:.4f} / {output['sma50']:.4f} / {output['sma200']:.4f} / {output['wilder_rsi14']:.4f}**\n- Trend200 / Recovery / Liquidity: **{output['trend200_state']} / {'ON' if output['recovery_state'] else 'OFF'} / {output['liquidity_state']}**\n- Comparison1 / Comparison3: **{output['comparison1_confirmed_target']} / {output['comparison3_target']}**\n- Regime / engine: **{output['final_regime']} / {output['active_engine']}**\n- B0 base target: **{output['base_execution_target']}**\n- N1 overlay: **{'ON' if output['n1_overlay_active'] else 'OFF'}**\n- N1 shadow target: **{output['execution_target']}**\n- Router: **{output['router_asset'] if output['red_router_active'] else 'OFF'}**\n- Rules SHA-256: `{output['rules_sha256']}`\n\nNo new completed US regular session. Persistent state was not mutated.\nThis is a shadow signal only. No broker order was submitted.\n"""
    core.MD_PATH.write_text(md, encoding="utf-8")
    print(json.dumps(output, ensure_ascii=False, indent=2))


def _completed_only_fetch(
    original_fetch: Callable[..., tuple[pd.DataFrame, str, list[str]]],
    completed_signal_date: pd.Timestamp,
) -> Callable[..., tuple[pd.DataFrame, str, list[str]]]:
    def fetch(symbol: str, start: str = "2005-01-01") -> tuple[pd.DataFrame, str, list[str]]:
        df, provider, warnings = original_fetch(symbol, start)
        df = df.loc[df.index <= completed_signal_date].copy()
        if df.empty:
            raise RuntimeError(f"NO_COMPLETED_PRICE_ROWS:{symbol}:{completed_signal_date.date()}")
        return df, provider, warnings

    return fetch


def main() -> None:
    state = core.read_state()
    prior_signal_date = pd.Timestamp(state.get("signal_date", core.ANCHOR_DATE)).normalize()

    qqq, _, detection_warnings = core.fetch_prices("QQQ")
    completed_signal_date = _latest_completed_session(qqq.index)

    if completed_signal_date < prior_signal_date:
        raise RuntimeError(
            f"PRICE_HISTORY_BEHIND_STATE: price={completed_signal_date.date()} state={prior_signal_date.date()}"
        )

    completed_index = pd.DatetimeIndex(qqq.index).normalize()
    unseen_sessions = completed_index[
        (completed_index > prior_signal_date) & (completed_index <= completed_signal_date)
    ].unique()

    if len(unseen_sessions) == 0:
        _write_no_new_session_report(state, completed_signal_date, detection_warnings)
        return

    if len(unseen_sessions) > 1:
        missing = ",".join(pd.Timestamp(ts).strftime("%Y-%m-%d") for ts in unseen_sessions)
        raise RuntimeError(f"MULTIPLE_UNPROCESSED_US_SESSIONS:{missing}")

    original_fetch = core.fetch_prices
    core.fetch_prices = _completed_only_fetch(original_fetch, completed_signal_date)
    try:
        core.main()
    finally:
        core.fetch_prices = original_fetch


if __name__ == "__main__":
    main()
