from __future__ import annotations

import io
import json
import math
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd
import requests
import yfinance as yf

FRED_SERIES = ["BAMLH0A0HYM2", "BAMLC0A0CM", "DFII10", "VIXCLS", "NFCI"]
PRICE_TICKERS = ["VRT", "MRVL", "SRVR", "SMH", "NVDA", "AVGO"]
OUTPUT_JSON = Path("latest_signal.json")
OUTPUT_MD = Path("latest_signal.md")
MIN_HISTORY = 120


@dataclass
class RatioMetrics:
    ratio: Optional[float]
    ma60: Optional[float]
    gap: Optional[float]
    slope_proxy: Optional[float] = None
    price_date: Optional[str] = None


def load_previous_output() -> Dict:
    if OUTPUT_JSON.exists():
        try:
            return json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def safe_float(value: Optional[float], digits: int = 6) -> Optional[float]:
    if value is None:
        return None
    try:
        v = float(value)
    except Exception:
        return None
    if math.isnan(v) or math.isinf(v):
        return None
    return round(v, digits)


def fetch_fred_series(series_id: str, warnings: List[str]) -> pd.Series:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    try:
        res = requests.get(url, timeout=20)
        res.raise_for_status()
        df = pd.read_csv(io.StringIO(res.text))
        if len(df.columns) < 2:
            raise ValueError("unexpected FRED CSV shape")
        date_col, value_col = df.columns[0], df.columns[1]
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
        series = df.set_index(date_col)[value_col].dropna().sort_index()
        if series.empty:
            raise ValueError("empty FRED series")
        return series
    except Exception as exc:
        warnings.append(f"FRED {series_id} download failed; using cached values when available ({exc}).")
        return pd.Series(dtype=float)


def fred_latest_and_4w(series: pd.Series) -> Tuple[Optional[float], Optional[float], Optional[str]]:
    if series.empty:
        return None, None, None

    latest_date = series.index[-1]
    latest_val = float(series.iloc[-1])

    target_date = latest_date - timedelta(days=28)
    history = series.loc[series.index <= target_date]
    prior_val = float(history.iloc[-1]) if not history.empty else float(series.iloc[0])

    return latest_val, (latest_val - prior_val) * 100.0, latest_date.strftime("%Y-%m-%d")


def fetch_yfinance_close(ticker: str) -> pd.Series:
```python
def fetch_yfinance_close(ticker: str) -> pd.Series:
    data = yf.download(
        ticker,
        period="2y",
        interval="1d",
        auto_adjust=False,
        progress=False,
        threads=False,
    )
    if data.empty:
        return pd.Series(dtype=float)

    frame = data.copy()

    # yfinance may return MultiIndex columns depending on version/options.
    if isinstance(frame.columns, pd.MultiIndex):
        if ticker in frame.columns.get_level_values(-1):
            frame = frame.xs(ticker, axis=1, level=-1)
        elif ticker in frame.columns.get_level_values(0):
            frame = frame.xs(ticker, axis=1, level=0)

    # yfinance can return MultiIndex columns depending on version/options.
    # Normalize to a single-ticker 2D frame with OHLCV-like columns.
    if isinstance(frame.columns, pd.MultiIndex):
        # Common shape: (field, ticker) e.g. ('Close', 'VRT')
        if ticker in frame.columns.get_level_values(-1):
            frame = frame.xs(ticker, axis=1, level=-1)
        # Alternative shape: (ticker, field)
        elif ticker in frame.columns.get_level_values(0):
            frame = frame.xs(ticker, axis=1, level=0)

    # After normalization, select Adj Close first, else Close.
    if "Adj Close" in frame.columns:
        close_like = frame["Adj Close"]
    elif "Close" in frame.columns:
        close_like = frame["Close"]
    else:
        return pd.Series(dtype=float)

    if isinstance(close_like, pd.DataFrame):
        # Defensive fallback in case duplicate columns remain.
        close_like = close_like.iloc[:, 0]

    series = pd.to_numeric(close_like, errors="coerce").dropna()
    series.index = pd.to_datetime(series.index)
    return series.sort_index()
```


def fetch_stooq_close(ticker: str) -> pd.Series:
    url = f"https://stooq.com/q/d/l/?s={ticker.lower()}.us&i=d"
    res = requests.get(url, timeout=20)
    res.raise_for_status()

    df = pd.read_csv(io.StringIO(res.text))
    if "Date" not in df.columns or "Close" not in df.columns:
        return pd.Series(dtype=float)

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    series = df.set_index("Date")["Close"].dropna().sort_index()
    return series


def fetch_price_series(ticker: str, warnings: List[str]) -> pd.Series:
    try:
        series = fetch_yfinance_close(ticker)
        if len(series) >= MIN_HISTORY:
            return series
        warnings.append(f"{ticker}: yfinance history insufficient ({len(series)} rows); trying Stooq fallback.")
    except Exception as exc:
        warnings.append(f"{ticker}: yfinance failed ({exc}); trying Stooq fallback.")

    try:
        series = fetch_stooq_close(ticker)
        if len(series) >= MIN_HISTORY:
            return series
        warnings.append(f"{ticker}: Stooq history insufficient ({len(series)} rows).")
        return series
    except Exception as exc:
        warnings.append(f"{ticker}: Stooq fallback failed ({exc}).")
        return pd.Series(dtype=float)


def compute_ratio_metrics(numer: pd.Series, denom: pd.Series) -> RatioMetrics:
    merged = pd.concat([numer.rename("numer"), denom.rename("denom")], axis=1).dropna()
    if len(merged) < 60:
        return RatioMetrics(None, None, None, None, None)

    ratio = merged["numer"] / merged["denom"]
    ma60 = ratio.rolling(60).mean()

    ratio_last = float(ratio.iloc[-1])
    ma60_last = float(ma60.iloc[-1]) if pd.notna(ma60.iloc[-1]) else None
    gap = (ratio_last / ma60_last - 1.0) if ma60_last not in (None, 0.0) else None

    slope_proxy = None
    if len(ma60.dropna()) >= 21:
        m_now = ma60.iloc[-1]
        m_prev = ma60.shift(20).iloc[-1]
        if pd.notna(m_now) and pd.notna(m_prev):
            slope_proxy = float(m_now - m_prev)

    return RatioMetrics(
        ratio=ratio_last,
        ma60=ma60_last,
        gap=gap,
        slope_proxy=slope_proxy,
        price_date=merged.index[-1].strftime("%Y-%m-%d"),
    )


def cache_ratio_metrics(prev: Dict, key: str) -> RatioMetrics:
    item = prev.get("signals", {}).get(key, {})
    return RatioMetrics(
        ratio=item.get("ratio"),
        ma60=item.get("ma60"),
        gap=item.get("gap"),
        slope_proxy=item.get("ma60_slope_proxy"),
        price_date=prev.get("as_of", {}).get("price_date"),
    )


def main() -> None:
    now_utc = datetime.now(timezone.utc)
    warnings: List[str] = []
    prev = load_previous_output()

    # Macro data
    macro: Dict[str, Dict[str, Optional[float]]] = {}
    for sid in FRED_SERIES:
        s = fetch_fred_series(sid, warnings)
        latest, chg_bp, latest_date = fred_latest_and_4w(s)
        if latest is None:
            cached = prev.get("macro", {}).get(sid, {})
            latest = cached.get("latest")
            chg_bp = cached.get("change_4w_bp")
            latest_date = cached.get("latest_date")

        macro[sid] = {
            "latest": safe_float(latest, 4),
            "change_4w_bp": safe_float(chg_bp, 2),
            "latest_date": latest_date,
        }

    # Price data
    prices: Dict[str, pd.Series] = {}
    price_meta: Dict[str, Dict[str, Optional[float]]] = {}

    for ticker in PRICE_TICKERS:
        series = fetch_price_series(ticker, warnings)
        if series.empty:
            cached_price = prev.get("prices", {}).get(ticker, {})
            close = cached_price.get("close")
            date = cached_price.get("latest_date")
            if close is not None and date is not None:
                idx = pd.to_datetime([date], errors="coerce")
                if not pd.isna(idx[0]):
                    series = pd.Series([float(close)], index=idx, dtype=float)
                    warnings.append(f"{ticker}: using cached close due to download failure.")
            else:
                warnings.append(f"{ticker}: no downloadable data and no cache available.")

        prices[ticker] = series
        price_meta[ticker] = {
            "close": safe_float(float(series.iloc[-1]), 4) if not series.empty else None,
            "latest_date": series.index[-1].strftime("%Y-%m-%d") if not series.empty else None,
        }

    # Signal metrics
    vrt = compute_ratio_metrics(prices.get("VRT", pd.Series(dtype=float)), prices.get("SRVR", pd.Series(dtype=float)))
    mrvl = compute_ratio_metrics(prices.get("MRVL", pd.Series(dtype=float)), prices.get("SMH", pd.Series(dtype=float)))

    if vrt.ratio is None:
        warnings.append("VRT/SRVR metrics unavailable from live data; using cached metrics when available.")
        vrt = cache_ratio_metrics(prev, "VRT")
    if mrvl.ratio is None:
        warnings.append("MRVL/SMH metrics unavailable from live data; using cached metrics when available.")
        mrvl = cache_ratio_metrics(prev, "MRVL")

    # Macro rule
    hy_ok = macro["BAMLH0A0HYM2"]["change_4w_bp"] is not None and macro["BAMLH0A0HYM2"]["change_4w_bp"] < 100
    ig_ok = macro["BAMLC0A0CM"]["change_4w_bp"] is not None and macro["BAMLC0A0CM"]["change_4w_bp"] < 50
    real_ok = macro["DFII10"]["change_4w_bp"] is not None and macro["DFII10"]["change_4w_bp"] < 50
    vix_ok = macro["VIXCLS"]["latest"] is not None and macro["VIXCLS"]["latest"] < 25
    nfci_ok = macro["NFCI"]["latest"] is not None and macro["NFCI"]["latest"] <= 0
    macro_green = hy_ok and ig_ok and real_ok and vix_ok and nfci_ok

    vrt_entry = macro_green and vrt.gap is not None and vrt.gap <= 0.10
    mrvl_entry = (
        macro_green
        and mrvl.gap is not None
        and mrvl.gap >= -0.05
        and mrvl.slope_proxy is not None
        and mrvl.slope_proxy > 0
    )

    if vrt_entry and mrvl_entry:
        verdict = "✅ Entry condition met: BOTH"
    elif vrt_entry:
        verdict = "✅ Entry condition met: VRT"
    elif mrvl_entry:
        verdict = "✅ Entry condition met: MRVL"
    else:
        verdict = "⏸ No entry today"

    # Prefer the ratio computation date as the price reference date
    price_ref_date = vrt.price_date or mrvl.price_date
    if price_ref_date is None:
        dates = [x["latest_date"] for x in price_meta.values() if x.get("latest_date")]
        price_ref_date = max(dates) if dates else prev.get("as_of", {}).get("price_date")

    output = {
        "generated_at_utc": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "as_of": {
            "price_date": price_ref_date,
            "run_time_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "data_warning": bool(warnings),
        "warnings": warnings,
        "macro": macro,
        "checks": {
            "HY_4w_change_bp_lt_100": hy_ok,
            "IG_4w_change_bp_lt_50": ig_ok,
            "DFII10_4w_change_bp_lt_50": real_ok,
            "VIX_lt_25": vix_ok,
            "NFCI_lte_0": nfci_ok,
            "MacroGreen": macro_green,
        },
        "prices": price_meta,
        "signals": {
            "VRT": {
                "ratio": safe_float(vrt.ratio),
                "ma60": safe_float(vrt.ma60),
                "gap": safe_float(vrt.gap),
                "entry": bool(vrt_entry),
            },
            "MRVL": {
                "ratio": safe_float(mrvl.ratio),
                "ma60": safe_float(mrvl.ma60),
                "gap": safe_float(mrvl.gap),
                "ma60_slope_proxy": safe_float(mrvl.slope_proxy),
                "entry": bool(mrvl_entry),
            },
        },
        "verdict": verdict,
    }

    OUTPUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    def fmt_pct(x: Optional[float]) -> str:
        return "N/A" if x is None else f"{x * 100:.2f}%"

    lines: List[str] = [
        "# Daily Signal Monitor",
        "",
        f"- 데이터 기준일(주가): **{output['as_of']['price_date']}**",
        f"- 실행시간(UTC): **{output['as_of']['run_time_utc']}**",
        "",
    ]

    if output["data_warning"]:
        lines.extend(
            [
                "## ⚠️ DATA WARNING",
                "일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.",
                "",
            ]
        )
        lines.extend(f"- {w}" for w in warnings)
        lines.append("")

    lines.extend(
        [
            "## MacroGreen",
            f"- **MacroGreen**: **{macro_green}**",
            "",
            "### 핵심 수치",
            f"- HY OAS (BAMLH0A0HYM2): {macro['BAMLH0A0HYM2']['latest']} / 4주 변화 {macro['BAMLH0A0HYM2']['change_4w_bp']} bp",
            f"- IG OAS (BAMLC0A0CM): {macro['BAMLC0A0CM']['latest']} / 4주 변화 {macro['BAMLC0A0CM']['change_4w_bp']} bp",
            f"- 10Y Real Yield (DFII10): {macro['DFII10']['latest']} / 4주 변화 {macro['DFII10']['change_4w_bp']} bp",
            f"- VIX (VIXCLS): {macro['VIXCLS']['latest']}",
            f"- NFCI: {macro['NFCI']['latest']}",
            "",
            "## VRT 신규진입 룰",
            f"- ratio (VRT/SRVR): {output['signals']['VRT']['ratio']}",
            f"- MA60: {output['signals']['VRT']['ma60']}",
            f"- gap: {fmt_pct(output['signals']['VRT']['gap'])}",
            f"- **VRT_ENTRY**: **{output['signals']['VRT']['entry']}**",
            "",
            "## MRVL 신규진입 룰 (확인형)",
            f"- ratio (MRVL/SMH): {output['signals']['MRVL']['ratio']}",
            f"- MA60: {output['signals']['MRVL']['ma60']}",
            f"- gap: {fmt_pct(output['signals']['MRVL']['gap'])}",
            f"- MA60_slope_proxy: {output['signals']['MRVL']['ma60_slope_proxy']}",
            f"- **MRVL_ENTRY**: **{output['signals']['MRVL']['entry']}**",
            "",
            f"## Verdict\n{verdict}",
            "",
        ]
    )

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
