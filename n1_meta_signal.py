#!/usr/bin/env python3
"""Validated, idempotent N1 publishing with explicit historical recovery."""
from __future__ import annotations

import argparse
import copy
import hashlib
import io
import json
import re
import subprocess
from datetime import datetime, timezone

import pandas as pd

import n1_meta_signal_core as core
from n1_data_quality import (
    DataQualityError, completed_session, json_bytes, number, publish_files,
    sessions_between, strict_loads, validate_checkpoint,
)

STATUS_PATH = core.ROOT / "n1_run_status.json"
AUDIT_DIR = core.ROOT / "n1_audit"
MAX_REPLAY_SESSIONS = 120


def rules_hash() -> str:
    return core.rules_hash()


def git_text(*args: str) -> str:
    result = subprocess.run(["git", "-C", str(core.ROOT), *args], capture_output=True, text=True, encoding="utf-8")
    if result.returncode:
        raise DataQualityError("RECOVERY_GIT_HISTORY_UNAVAILABLE")
    return result.stdout


def load_checkpoint(repair_from: str | None = None) -> tuple[dict, dict]:
    if repair_from:
        if not re.fullmatch(r"[0-9a-f]{40}", repair_from):
            raise DataQualityError("RECOVERY_REQUIRES_FULL_COMMIT_SHA")
        signal = strict_loads(git_text("show", f"{repair_from}:n1_latest_signal.json"))
        state = strict_loads(git_text("show", f"{repair_from}:n1_latest_state_snapshot.json"))
    else:
        signal = strict_loads(core.SIGNAL_PATH.read_text(encoding="utf-8"))
        state = strict_loads(core.STATE_PATH.read_text(encoding="utf-8"))
    validate_checkpoint(signal, state, rules_hash())
    return signal, state


def archived_lineages(days: pd.DatetimeIndex) -> dict[str, tuple[pd.DataFrame, str]]:
    """Use each day's first committed lineage, not today's revised FRED history.

    Old malformed signals are read ONLY to locate a date; their numerical
    values, targets and state counters are never used in the replay.
    """
    needed = {day.strftime("%Y-%m-%d") for day in days}
    found = {}
    commits = git_text("log", "--reverse", "--format=%H", "--", "n1_latest_signal.json").splitlines()
    for commit in commits:
        metadata = json.loads(git_text("show", f"{commit}:n1_latest_signal.json"), parse_constant=lambda _: None)
        date = metadata.get("signal_date")
        if date not in needed or date in found:
            continue
        csv = git_text("show", f"{commit}:n1_liquidity_p_lineage.csv")
        panel = pd.read_csv(io.StringIO(csv), index_col="applied_row_week", parse_dates=True)
        found[date] = (panel, commit)
        if len(found) == len(needed):
            break
    return found


def validate_lineage(panel: pd.DataFrame, signal: dict) -> None:
    if panel.empty or panel.index.has_duplicates or not panel.index.is_monotonic_increasing:
        raise DataQualityError("INVALID_LIQUIDITY_INDEX")
    day = pd.Timestamp(signal["signal_date"])
    applicable = panel.loc[panel.index <= day]
    if applicable.empty:
        raise DataQualityError("P_APPLIED_MISSING")
    row = applicable.iloc[-1]
    value = number(row["p_applied"], "p_applied", bounded=True)
    if (abs(value - signal["liquidity_p_applied"]) > 1e-10
            or applicable.index[-1].strftime("%Y-%m-%d") != signal["liquidity_p_applied_row_week"]
            or row["p_raw_source_week"] != signal["liquidity_p_raw_source_week"]):
        raise DataQualityError("SIGNAL_LINEAGE_MISMATCH")


def render_report(signal: dict) -> str:
    parts = [
        "# N1 QQQ Meta Daily Shadow Signal", "",
        f"- Validation: **{signal['validation_class']}**",
        f"- Signal date: **{signal['signal_date']}**",
        f"- Next execution session: **{signal['execution_date']}**",
        "- QQQ / SMA20 / SMA50 / SMA200 / RSI14: **" + " / ".join(
            f"{signal[key]:.4f}" for key in ("qqq_adjusted_close", "sma20", "sma50", "sma200", "wilder_rsi14")
        ) + "**",
        f"- Applied liquidity P: **{signal['liquidity_p_applied']:.4f}**",
        f"- Trend200 / Recovery / Liquidity: **{signal['trend200_state']} / {'ON' if signal['recovery_state'] else 'OFF'} / {signal['liquidity_state']}**",
        f"- Comparison1 / Comparison3: **{signal['comparison1_confirmed_target']} / {signal['comparison3_target']}**",
        f"- Regime / engine: **{signal['final_regime']} / {signal['active_engine']}**",
        f"- B0 base target: **{signal['base_execution_target']}**",
        f"- N1 overlay: **{'ON' if signal['n1_overlay_active'] else 'OFF'}**",
        f"- N1 shadow target: **{signal['execution_target']}**",
        f"- Router: **{signal['router_asset'] if signal['red_router_active'] else 'OFF'}**",
        f"- Action: **{signal['action']}**",
        f"- Rules SHA-256: {signal['rules_sha256']}",
    ]
    if signal.get("recovery"):
        recovery = signal["recovery"]
        parts += [f"- Recovery checkpoint: {recovery['checkpoint_commit']}",
                  f"- Replayed sessions: **{recovery['sessions']}**",
                  "- Recovery uses currently available adjusted prices and archived daily liquidity vintages; it is not an exact historical price-vintage reconstruction."]
    if signal["warnings"]:
        parts += ["", "## Data warnings", *[f"- {note}" for note in signal["warnings"]]]
    parts += ["", "This is a shadow signal only. No broker order was submitted.", ""]
    return "\n".join(parts)


def publish_checkpoint(signal: dict, state: dict, lineage: pd.DataFrame | None, now: datetime) -> None:
    validate_checkpoint(signal, state, rules_hash())
    if lineage is not None:
        validate_lineage(lineage, signal)
    encoded = json_bytes(signal)
    status = {
        "attempted_at": now.isoformat(), "status": "VALIDATED", "data_missing": False,
        "signal_date": signal["signal_date"], "execution_target": signal["execution_target"],
        "signal_sha256": hashlib.sha256(encoded).hexdigest(), "state_sha256": signal["state_sha256"],
    }
    payloads = {
        core.STATE_PATH: json_bytes(state), core.SIGNAL_PATH: encoded,
        core.MD_PATH: render_report(signal).encode("utf-8"),
    }
    if lineage is not None:
        payloads[core.LINEAGE_PATH] = lineage.reset_index().to_csv(index=False).encode("utf-8")
    # Status is the final commit marker; a stale hash cannot certify a partial write.
    payloads[STATUS_PATH] = json_bytes(status)
    publish_files(payloads)


def execute(*, repair_from: str | None = None, now: datetime | None = None,
            dry_run: bool = False) -> dict:
    now = now or datetime.now(timezone.utc)
    asof = completed_session(now)
    previous, state = load_checkpoint(repair_from)
    prior = pd.Timestamp(state["signal_date"])
    if prior > asof:
        raise DataQualityError("CHECKPOINT_AHEAD_OF_COMPLETED_SESSION")
    days = sessions_between(prior, asof)
    days = days[days > prior]
    if len(days) > 1 and not repair_from:
        raise DataQualityError("UNPROCESSED_SESSIONS_REQUIRE_EXPLICIT_RECOVERY")
    if len(days) > MAX_REPLAY_SESSIONS:
        raise DataQualityError("RECOVERY_SESSION_LIMIT_EXCEEDED")
    if repair_from and len(days) == 0:
        raise DataQualityError("RECOVERY_HAS_NO_SESSIONS")

    if len(days) == 0:
        output = copy.deepcopy(previous)
        output.update(generated_at=now.isoformat(), new_completed_us_session=False,
                      action="HOLD_PREVIOUS_VALIDATED_TARGET",
                      reason_codes=["NO_NEW_COMPLETED_US_SESSION"] + (
                          ["N1_BULL_COMPARISON3_QLD_TO_QQQ"] if previous["n1_overlay_active"] else []
                      ),
                      validation_class="B_WARN_NO_NEW_SESSION" if previous["warnings"] else "NO_NEW_COMPLETED_US_SESSION")
        lineage = pd.read_csv(core.LINEAGE_PATH, index_col="applied_row_week", parse_dates=True)
        validate_lineage(lineage, output)
        if not dry_run:
            publish_checkpoint(output, state, None, now)
        return output

    price_data = {symbol: core.fetch_prices(symbol, asof=asof) for symbol in ("QQQ", "GLD", "XLV", "^VIX")}
    history = archived_lineages(days) if repair_from else {}
    # Missing historical vintages must not be replaced with today's revised FRED data.
    if repair_from and any(day.strftime("%Y-%m-%d") not in history for day in days[:-1]):
        raise DataQualityError("RECOVERY_LIQUIDITY_VINTAGE_MISSING")
    current_lineage = None
    records = []
    for day in days:
        key = day.strftime("%Y-%m-%d")
        if key in history:
            lineage, lineage_commit = history[key]
        else:
            if current_lineage is None:
                current_lineage = core.liquidity_panel()
            lineage, lineage_commit = current_lineage, None
        output, candidate = core.calculate_signal(state, price_data, lineage, day, allow_router_fetch=not bool(repair_from))
        validate_lineage(lineage, output)
        records.append({"signal": copy.deepcopy(output), "state": candidate, "liquidity_commit": lineage_commit})
        state = candidate

    if repair_from:
        output["recovery"] = {"checkpoint_commit": repair_from, "from_signal_date": previous["signal_date"],
                              "sessions": len(days), "price_vintage": "CURRENT_ADJUSTED_HISTORY"}
        output["warnings"] = list(dict.fromkeys(output["warnings"] + ["RECOVERY_CURRENT_PRICE_VINTAGE"]))
        output["validation_class"] = "B_WARN"
    output["generated_at"] = now.isoformat()
    validate_checkpoint(output, state, rules_hash())
    AUDIT_DIR.mkdir(exist_ok=True)
    publish_files({AUDIT_DIR / "calculation.json": json_bytes({
        "attempted_at": now.isoformat(), "dry_run": dry_run,
        "checkpoint_commit": repair_from, "sessions": records,
    })})
    for symbol, (frame, _, _) in price_data.items():
        frame.to_csv(AUDIT_DIR / f"prices_{symbol.replace('^', '')}.csv", index_label="Date")
    if not dry_run:
        publish_checkpoint(output, state, lineage, now)
    return output


def record_failure(exc: Exception, now: datetime) -> dict:
    code = str(exc) if isinstance(exc, DataQualityError) else type(exc).__name__
    status = {"attempted_at": now.isoformat(), "status": "BLOCKED", "data_missing": True,
              "reason": code, "execution_target": None, "checkpoint_preserved": True}
    try:
        previous, _ = load_checkpoint()
        status.update(previous_signal_date=previous["signal_date"], previous_execution_target=previous["execution_target"])
    except Exception:
        status["reason"] += "|EXISTING_CHECKPOINT_INVALID_RECOVERY_REQUIRED"
    publish_files({STATUS_PATH: json_bytes(status)})
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repair-from", help="Full commit SHA of a finite, matching signal/state checkpoint")
    parser.add_argument("--dry-run", action="store_true", help="Validate/replay without publishing latest files")
    args = parser.parse_args()
    now = datetime.now(timezone.utc)
    try:
        output = execute(repair_from=args.repair_from, now=now, dry_run=args.dry_run)
        print(json_bytes(output).decode("utf-8"))
        return 0
    except Exception as exc:
        if args.dry_run:
            code = str(exc) if isinstance(exc, DataQualityError) else type(exc).__name__
            print(f"N1 DRY RUN BLOCKED: {code}")
        else:
            print(json_bytes(record_failure(exc, now)).decode("utf-8"))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
