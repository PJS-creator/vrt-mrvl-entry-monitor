#!/usr/bin/env python3
"""Idempotent entrypoint for the N1 QQQ Meta shadow runner.

The state machine advances at most once for each newly completed US session.
Repeated runs for the same signal date refresh the report only and never mutate
persistent strategy state. If more than one session is missing, fail closed
instead of skipping intermediate state transitions.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

import pandas as pd

import n1_meta_signal_core as core


def _dedupe(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


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
        ["N1_BULL_COMPARISON3_QLD_TO_QQQ"]
        if output.get("n1_overlay_active")
        else []
    )
    output["warnings"] = warnings
    output["state_sha256"] = core.stable_hash(state)
    core.save_json(core.SIGNAL_PATH, output)

    md = f"""# N1 QQQ Meta Daily Shadow Signal\n\n- Validation: **{output['validation_class']}**\n- Signal date: **{output['signal_date']}**\n- Next execution session: **{output['execution_date']}**\n- QQQ / SMA20 / SMA50 / SMA200 / RSI14: **{output['qqq_adjusted_close']:.4f} / {output['sma20']:.4f} / {output['sma50']:.4f} / {output['sma200']:.4f} / {output['wilder_rsi14']:.4f}**\n- Trend200 / Recovery / Liquidity: **{output['trend200_state']} / {'ON' if output['recovery_state'] else 'OFF'} / {output['liquidity_state']}**\n- Comparison1 / Comparison3: **{output['comparison1_confirmed_target']} / {output['comparison3_target']}**\n- Regime / engine: **{output['final_regime']} / {output['active_engine']}**\n- B0 base target: **{output['base_execution_target']}**\n- N1 overlay: **{'ON' if output['n1_overlay_active'] else 'OFF'}**\n- N1 shadow target: **{output['execution_target']}**\n- Router: **{output['router_asset'] if output['red_router_active'] else 'OFF'}**\n- Rules SHA-256: `{output['rules_sha256']}`\n\nNo new completed US regular session. Persistent state was not mutated.\nThis is a shadow signal only. No broker order was submitted.\n"""
    core.MD_PATH.write_text(md, encoding="utf-8")
    print(json.dumps(output, ensure_ascii=False, indent=2))


def main() -> None:
    state = core.read_state()
    prior_signal_date = pd.Timestamp(state.get("signal_date", core.ANCHOR_DATE))

    qqq, _, detection_warnings = core.fetch_prices("QQQ")
    signal_date = qqq.index.max()

    if signal_date < prior_signal_date:
        raise RuntimeError(
            f"PRICE_HISTORY_BEHIND_STATE: price={signal_date.date()} state={prior_signal_date.date()}"
        )

    unseen_sessions = qqq.index[qqq.index > prior_signal_date]
    if len(unseen_sessions) == 0:
        _write_no_new_session_report(state, signal_date, detection_warnings)
        return

    if len(unseen_sessions) > 1:
        missing = ",".join(ts.strftime("%Y-%m-%d") for ts in unseen_sessions)
        raise RuntimeError(f"MULTIPLE_UNPROCESSED_US_SESSIONS:{missing}")

    # Exactly one new completed session: let the original state machine advance once.
    core.main()


if __name__ == "__main__":
    main()
