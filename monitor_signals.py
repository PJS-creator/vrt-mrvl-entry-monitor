from __future__ import annotations

import io
import json
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


@dataclass
class RatioMetrics:
    ratio: Optional[float]
    ma60: Optional[float]
    gap: Optional[float]
    slope_proxy: Optional[float] = None


def load_previous() -> Dict:
    if not OUTPUT_JSON.exists():
        return {}
    try:
        return json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}


def safe_num(v: Optional[float], digits: int = 6) -> Optional[float]:
    if v is None:
        return None
    try:
        val = float(v)
    except Exception:
        return None
    if pd.isna(val):
        return None
    return round(val, digits)


def fetch_fred_series(series_id: str) -> pd.Series:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    res = requests.get(url, timeout=20)
    res.raise_for_status()
    df = pd.read_csv(io.StringIO(res.text))
    date_col, val_col = df.columns[0], df.columns[1]
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df[val_col] = pd.to_numeric(df[val_col], errors="coerce")
    s = df.set_index(date_col)[val_col].dropna().sort_index()
    return s


def latest_and_4w_change_bp(s: pd.Series) -> Tuple[Optional[float], Optional[float], Optional[str]]:
    if s.empty:
        return None, None, None
    last_date = s.index[-1]
    last_val = float(s.iloc[-1])
    base_date = last_date - timedelta(days=28)
    old = s.loc[s.index <= base_date]
    old_val = float(old.iloc[-1]) if not old.empty else float(s.iloc[0])
    return last_val, (last_val - old_val) * 100.0, last_date.strftime("%Y-%m-%d")


def fetch_yf_close(ticker: str) -> pd.Series:
    df = yf.download(ticker, period="2y", interval="1d", progress=False, auto_adjust=False, threads=False)
    if df.empty:
        return pd.Series(dtype=float)

    if isinstance(df.columns, pd.MultiIndex):
        if ticker in df.columns.get_level_values(-1):
            df = df.xs(ticker, axis=1, level=-1)
        elif ticker in df.columns.get_level_values(0):
            df = df.xs(ticker, axis=1, level=0)

    if "Adj Close" in df.columns:
        close = df["Adj Close"]
    elif "Close" in df.columns:
        close = df["Close"]
    else:
        return pd.Series(dtype=float)

    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    s = pd.to_numeric(close, errors="coerce").dropna()
    s.index = pd.to_datetime(s.index)
    return s.sort_index()


def fetch_stooq_close(ticker: str) -> pd.Series:
    url = f"https://stooq.com/q/d/l/?s={ticker.lower()}.us&i=d"
    res = requests.get(url, timeout=20)
    res.raise_for_status()
    df = pd.read_csv(io.StringIO(res.text))
    if "Date" not in df.columns or "Close" not in df.columns:
        return pd.Series(dtype=float)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    return df.set_index("Date")["Close"].dropna().sort_index()


def fetch_price(ticker: str, warnings: List[str]) -> pd.Series:
    try:
        s = fetch_yf_close(ticker)
        if len(s) >= 120:
            return s
        warnings.append(f"{ticker}: yfinance insufficient history ({len(s)} rows), fallback to Stooq.")
    except Exception as e:
        warnings.append(f"{ticker}: yfinance failed ({e}), fallback to Stooq.")

    try:
        s = fetch_stooq_close(ticker)
        if len(s) >= 120:
            return s
        warnings.append(f"{ticker}: Stooq insufficient history ({len(s)} rows).")
        return s
    except Exception as e:
        warnings.append(f"{ticker}: Stooq failed ({e}).")
        return pd.Series(dtype=float)


def ratio_metrics(numer: pd.Series, denom: pd.Series) -> RatioMetrics:
    df = pd.concat([numer.rename("n"), denom.rename("d")], axis=1).dropna()
    if len(df) < 60:
        return RatioMetrics(None, None, None, None)

    ratio = df["n"] / df["d"]
    ma60 = ratio.rolling(60).mean()

    r = float(ratio.iloc[-1])
    m = float(ma60.iloc[-1]) if pd.notna(ma60.iloc[-1]) else None
    gap = (r / m - 1.0) if (m not in (None, 0)) else None

    slope = None
    if len(ma60.dropna()) >= 21:
        now = ma60.iloc[-1]
        prev = ma60.shift(20).iloc[-1]
        if pd.notna(now) and pd.notna(prev):
            slope = float(now - prev)

    return RatioMetrics(r, m, gap, slope)


def pct(v: Optional[float]) -> str:
    return "N/A" if v is None else f"{v*100:.2f}%"


def main() -> None:
    now = datetime.now(timezone.utc)
    warnings: List[str] = []
    prev = load_previous()

    macro: Dict[str, Dict[str, Optional[float]]] = {}
    for sid in FRED_SERIES:
        try:
            s = fetch_fred_series(sid)
            latest, change_bp, d = latest_and_4w_change_bp(s)
        except Exception as e:
            warnings.append(f"FRED {sid} failed ({e}), using cached values if available.")
            cached = prev.get("macro", {}).get(sid, {})
            latest, change_bp, d = cached.get("latest"), cached.get("change_4w_bp"), cached.get("latest_date")

        macro[sid] = {
            "latest": safe_num(latest, 4),
            "change_4w_bp": safe_num(change_bp, 2),
            "latest_date": d,
        }

    prices: Dict[str, pd.Series] = {}
    price_meta: Dict[str, Dict[str, Optional[float]]] = {}
    for t in PRICE_TICKERS:
        s = fetch_price(t, warnings)
        if s.empty:
            c = prev.get("prices", {}).get(t, {}).get("close")
            d = prev.get("prices", {}).get(t, {}).get("latest_date")
            if c is not None and d is not None:
                s = pd.Series([float(c)], index=pd.to_datetime([d]))
                warnings.append(f"{t}: using cached price.")
        prices[t] = s
        price_meta[t] = {
            "close": safe_num(float(s.iloc[-1]), 4) if not s.empty else None,
            "latest_date": s.index[-1].strftime("%Y-%m-%d") if not s.empty else None,
        }

    hy = macro["BAMLH0A0HYM2"]["change_4w_bp"]
    ig = macro["BAMLC0A0CM"]["change_4w_bp"]
    ry = macro["DFII10"]["change_4w_bp"]
    vix = macro["VIXCLS"]["latest"]
    nfci = macro["NFCI"]["latest"]

    macro_green = (
        hy is not None and hy < 100 and
        ig is not None and ig < 50 and
        ry is not None and ry < 50 and
        vix is not None and vix < 25 and
        nfci is not None and nfci <= 0
    )

    vrt = ratio_metrics(prices.get("VRT", pd.Series(dtype=float)), prices.get("SRVR", pd.Series(dtype=float)))
    mrvl = ratio_metrics(prices.get("MRVL", pd.Series(dtype=float)), prices.get("SMH", pd.Series(dtype=float)))

    if vrt.ratio is None:
        c = prev.get("signals", {}).get("VRT", {})
        vrt = RatioMetrics(c.get("ratio"), c.get("ma60"), c.get("gap"), None)
        warnings.append("VRT metrics using cache.")

    if mrvl.ratio is None:
        c = prev.get("signals", {}).get("MRVL", {})
        mrvl = RatioMetrics(c.get("ratio"), c.get("ma60"), c.get("gap"), c.get("ma60_slope_proxy"))
        warnings.append("MRVL metrics using cache.")

    vrt_entry = macro_green and (vrt.gap is not None) and (vrt.gap <= 0.10)
    mrvl_entry = macro_green and (mrvl.gap is not None) and (mrvl.gap >= -0.05) and (mrvl.slope_proxy is not None) and (mrvl.slope_proxy > 0)

    verdict = "⏸ No entry today"
    if vrt_entry and mrvl_entry:
        verdict = "✅ Entry condition met: BOTH"
    elif vrt_entry:
        verdict = "✅ Entry condition met: VRT"
    elif mrvl_entry:
        verdict = "✅ Entry condition met: MRVL"

    date_candidates = [meta["latest_date"] for meta in price_meta.values() if meta["latest_date"]]
    price_date = max(date_candidates) if date_candidates else prev.get("as_of", {}).get("price_date")

    out = {
        "generated_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "as_of": {
            "price_date": price_date,
            "run_time_utc": now.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "data_warning": bool(warnings),
        "warnings": warnings,
        "macro": macro,
        "checks": {
            "MacroGreen": macro_green,
            "HY_4w_change_bp_lt_100": hy is not None and hy < 100,
            "IG_4w_change_bp_lt_50": ig is not None and ig < 50,
            "DFII10_4w_change_bp_lt_50": ry is not None and ry < 50,
            "VIX_lt_25": vix is not None and vix < 25,
            "NFCI_lte_0": nfci is not None and nfci <= 0,
        },
        "prices": price_meta,
        "signals": {
            "VRT": {
                "ratio": safe_num(vrt.ratio),
                "ma60": safe_num(vrt.ma60),
                "gap": safe_num(vrt.gap),
                "entry": bool(vrt_entry),
            },
            "MRVL": {
                "ratio": safe_num(mrvl.ratio),
                "ma60": safe_num(mrvl.ma60),
                "gap": safe_num(mrvl.gap),
                "ma60_slope_proxy": safe_num(mrvl.slope_proxy),
                "entry": bool(mrvl_entry),
            },
        },
        "verdict": verdict,
    }

    OUTPUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Daily Signal Monitor",
        "",
        f"- 데이터 기준일(주가): **{out['as_of']['price_date']}**",
        f"- 실행시간(UTC): **{out['as_of']['run_time_utc']}**",
        "",
    ]

    if out["data_warning"]:
        lines += ["## ⚠️ DATA WARNING", "일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.", ""]
        lines += [f"- {w}" for w in warnings]
        lines.append("")

    lines += [
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
        f"- ratio (VRT/SRVR): {out['signals']['VRT']['ratio']}",
        f"- MA60: {out['signals']['VRT']['ma60']}",
        f"- gap: {pct(out['signals']['VRT']['gap'])}",
        f"- **VRT_ENTRY**: **{out['signals']['VRT']['entry']}**",
        "",
        "## MRVL 신규진입 룰 (확인형)",
        f"- ratio (MRVL/SMH): {out['signals']['MRVL']['ratio']}",
        f"- MA60: {out['signals']['MRVL']['ma60']}",
        f"- gap: {pct(out['signals']['MRVL']['gap'])}",
        f"- MA60_slope_proxy: {out['signals']['MRVL']['ma60_slope_proxy']}",
        f"- **MRVL_ENTRY**: **{out['signals']['MRVL']['entry']}**",
        "",
        f"## Verdict\n{verdict}",
        "",
    ]

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
