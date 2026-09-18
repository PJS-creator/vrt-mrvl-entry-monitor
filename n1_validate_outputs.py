"""Strict CI contract; no broker calls and no output mutations."""
import hashlib

import pandas as pd

import n1_meta_signal as runner
import n1_meta_signal_core as core
from n1_data_quality import DataQualityError, strict_loads


def validate_outputs() -> dict:
    signal, state = runner.load_checkpoint()
    lineage = pd.read_csv(core.LINEAGE_PATH, index_col="applied_row_week", parse_dates=True)
    runner.validate_lineage(lineage, signal)
    status = strict_loads(runner.STATUS_PATH.read_text(encoding="utf-8"))
    if (status.get("status") != "VALIDATED" or status.get("data_missing") is not False
            or status.get("signal_sha256") != hashlib.sha256(core.SIGNAL_PATH.read_bytes()).hexdigest()
            or status.get("state_sha256") != signal["state_sha256"]):
        raise DataQualityError("RUN_STATUS_NOT_VALIDATED_OR_HASH_MISMATCH")
    return signal


if __name__ == "__main__":
    result = validate_outputs()
    print(f"N1 finite output contract PASS: {result['signal_date']} -> {result['execution_target']}")
