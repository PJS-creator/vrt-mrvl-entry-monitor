"""Official ALFRED daily vintages for explicit N1 historical recovery."""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from n1_data_quality import DataQualityError, json_bytes, publish_files
from n1_meta_signal_core import build_liquidity_panel

SERIES = ("WALCL", "WDTGAL", "RRPONTSYD")
VINTAGE_URL = "https://alfred.stlouisfed.org/graph/alfredgraph.csv"


def parse_vintage(text: str, series_id: str, day: pd.Timestamp) -> pd.Series:
    """Reject a current-series response or a different requested vintage."""
    expected = f"{series_id}_{day.strftime('%Y%m%d')}"
    frame = pd.read_csv(StringIO(text), keep_default_na=False)
    if list(frame.columns) != ["observation_date", expected]:
        raise DataQualityError(f"ALFRED_VINTAGE_HEADER_MISMATCH:{series_id}")
    dates = pd.DatetimeIndex(pd.to_datetime(frame["observation_date"], errors="raise"))
    if dates.empty or dates.has_duplicates or not dates.is_monotonic_increasing or (dates > day).any():
        raise DataQualityError(f"ALFRED_VINTAGE_DATES_INVALID:{series_id}")
    raw = frame[expected]
    missing = raw.isin(["", "."])
    values = pd.to_numeric(raw.mask(missing), errors="coerce")
    if values[~missing].isna().any() or not np.isfinite(values[~missing]).all():
        raise DataQualityError(f"ALFRED_VINTAGE_VALUES_INVALID:{series_id}")
    result = pd.Series(values.to_numpy(), index=dates, name=series_id).dropna()
    if result.empty or (result < 0).any() or (series_id == "WALCL" and (result <= 0).any()):
        raise DataQualityError(f"ALFRED_VINTAGE_VALUES_INVALID:{series_id}")
    # H.4.1 is weekly; reverse repos are business daily. Do not accept stale feeds.
    max_age = 8 if series_id in {"WALCL", "WDTGAL"} else 4
    if day - result.index[-1] > pd.Timedelta(days=max_age):
        raise DataQualityError(f"ALFRED_VINTAGE_STALE:{series_id}")
    return result


def fetch_liquidity_vintage(day: pd.Timestamp, audit_dir: Path) -> tuple[pd.DataFrame, dict]:
    """Use only values available on this date; retain raw responses and hashes."""
    day = pd.Timestamp(day).normalize()
    series = {}
    payloads = {}
    sources = []
    for series_id in SERIES:
        try:
            response = requests.get(VINTAGE_URL, params={
                "id": series_id, "vintage_date": day.strftime("%Y-%m-%d"),
            }, timeout=45)
            response.raise_for_status()
            series[series_id] = parse_vintage(response.text, series_id, day)
        except Exception as exc:
            code = str(exc) if isinstance(exc, DataQualityError) else type(exc).__name__
            raise DataQualityError(f"RECOVERY_LIQUIDITY_VINTAGE_UNAVAILABLE:{series_id}:{code}") from exc
        name = f"{series_id}-{day.date()}.csv"
        payloads[audit_dir / name] = response.content
        sources.append({"series": series_id, "file": name, "url": response.url,
                        "sha256": hashlib.sha256(response.content).hexdigest()})
    panel = build_liquidity_panel(series)
    metadata = {"provider": "alfred", "vintage_date": str(day.date()),
                "retrieved_at": datetime.now(timezone.utc).isoformat(), "sources": sources}
    audit_dir.mkdir(parents=True, exist_ok=True)
    payloads[audit_dir / f"manifest-{day.date()}.json"] = json_bytes(metadata)
    publish_files(payloads)
    return panel, metadata
