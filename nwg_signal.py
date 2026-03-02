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

# =========================
# Config
# =========================

# --- Global risk (FRED, daily) ---
FRED_SERIES = {
    "BAMLH0A0HYM2": {"name": "HY OAS", "scale_change": 100.0},   # % -> bp
    "BAMLC0A0CM": {"name": "IG OAS", "scale_change": 100.0},     # % -> bp
    "VIXCLS": {"name": "VIX", "scale_change": 1.0},
    "NFCI": {"name": "NFCI", "scale_change": 1.0},
}

# --- UK rates / demand (BoE Database) ---
# Bank Rate, SONIA, 10y/5y par yields, mortgage approvals, M4 growth
# Series codes:
# - IUDBEDR: Official Bank Rate
# - IUDSOIA: SONIA
# - IUDMNPY: 10y nominal par yield
# - IUDSNPY: 5y nominal par yield
# - LPMVTVX: mortgage approvals (house purchase)
# - LPMVQJW: M4 12-month growth rate
BOE_SERIES = {
    "IUDBEDR": {"name": "BoE Bank Rate", "scale_change": 100.0},
    "IUDSOIA": {"name": "SONIA", "scale_change": 100.0},
    "IUDMNPY": {"name": "UK 10Y Nominal Par Yield", "scale_change": 100.0},
    "IUDSNPY": {"name": "UK 5Y Nominal Par Yield", "scale_change": 100.0},
    "LPMVTVX": {"name": "Mortgage approvals (house purchase)", "scale_change": 1.0},
    "LPMVQJW": {"name": "M4 12m growth rate", "scale_change": 1.0},
}

# --- Prices (daily) ---
NWG_TICKER = "NWG.L"
FTSE_TICKER = "^FTSE"
PEER_TICKERS = ["LLOY.L", "BARC.L", "HSBA.L"]

PRICE_TICKERS = [NWG_TICKER, FTSE_TICKER] + PEER_TICKERS

OUTPUT_JSON = Path("nwg_latest_signal.json")
OUTPUT_MD = Path("nwg_latest_signal.md")

# =========================
# Thresholds (tweakable)
# =========================
TH = {
    # RiskGreen
    "VIX_MAX": 25.0,
    "HY_4W_CHG_BP_MAX": 100.0,
    "IG_4W_CHG_BP_MAX": 50.0,
    "NFCI_MAX": 0.0,

    # CurveGreen
    "TERM_SPREAD_10Y_POLICY_MIN_BP": 25.0,     # 10y - policy > 25bp
    "TERM_SPREAD_10Y_POLICY_4W_CHG_MIN_BP": -15.0,
    "UK10Y_4W_CHG_MIN_BP": -25.0,              # avoid sharp long-end drop
    "CURVE_10S5S_MIN_BP": 0.0,
    "CURVE_10S5S_4W_CHG_MIN_BP": -10.0,

    # DemandGreen (monthly)
    # approvals: 3m MA >= 12m MA
    # M4: latest >= 3m ago
    "M4_TREND_MIN": 0.0,  # latest - 3m_ago >= 0

    # PriceConfirm
    "NWG_GAP200_MIN": -0.10,
    "NWG_GAP200_MAX": 0.05,
    "NWG_GAP50_MAX": 0.08,

    # RelativeTurn
    "RS_GAP_MAX": 0.05,
    "RS_SLOPE_MIN": 0.0,
}

BOE_CSV_BASE = "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp"
FRED_CSV_BASE = "https://fred.stlouisfed.org/graph/fredgraph.csv?id="


# =========================
# Data classes
# =========================

@dataclass
class RatioMetrics:
    ratio: Optional[float]
    ma60: Optional[float]
    gap: Optional[float]
    slope_proxy: Optional[float] = None  # MA60 - MA60.shift(20)

@dataclass
class PriceMetrics:
    close: Optional[float]
    ma50: Optional[float]
    ma200: Optional[float]
    gap50: Optional[float]
    gap200: Optional[float]


# =========================
# Utils
# =========================

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

def pct(v: Optional[float]) -> str:
    return "N/A" if v is None else f"{v*100:.2f}%"

def latest_and_change(
    s: pd.Series,
    days: int = 28,
    scale_change: float = 1.0,
) -> Tuple[Optional[float], Optional[float], Optional[str]]:
    """
    Returns:
      latest, (latest-old)*scale_change, latest_date(YYYY-MM-DD)
    """
    if s.empty:
        return None, None, None
    s = s.dropna().sort_index()
    last_date = s.index[-1]
    last_val = float(s.iloc[-1])

    base_date = last_date - timedelta(days=days)
    old = s.loc[s.index <= base_date]
    old_val = float(old.iloc[-1]) if not old.empty else float(s.iloc[0])

    return last_val, (last_val - old_val) * scale_change, last_date.strftime("%Y-%m-%d")


# =========================
# Fetchers
# =========================

def fetch_fred_series(series_id: str) -> pd.Series:
    url = f"{FRED_CSV_BASE}{series_id}"
    res = requests.get(url, timeout=20)
    res.raise_for_status()
    df = pd.read_csv(io.StringIO(res.text))
    date_col, val_col = df.columns[0], df.columns[1]
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df[val_col] = pd.to_numeric(df[val_col], errors="coerce")
    return df.set_index(date_col)[val_col].dropna().sort_index()

def fetch_boe_series(series_code: str, datefrom: str = "01/Jan/2015") -> pd.Series:
    """
    BoE Database CSV auto download format:
    _iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=...&Dateto=now&SeriesCodes=...&UsingCodes=Y&CSVF=TN

    NOTE:
    - Some environments get 403 unless we send a browser-like User-Agent.
    - We also do a light "HTML detection" to avoid silently parsing a cookie/blocked page as CSV.
    """
    params = {
        "csv.x": "yes",
        "Datefrom": datefrom,
        "Dateto": "now",
        "SeriesCodes": series_code,
        "UsingCodes": "Y",
        "CSVF": "TN",   # tabular no titles
        "VPD": "Y",
        "VFD": "N",     # optional, but harmless and sometimes helps consistency
    }

    headers = {
        # browser-like UA (BoE can block python-requests UA in some environments)
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/csv,text/plain;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.9",
        "Referer": "https://www.bankofengland.co.uk/boeapps/database/",
    }

    res = requests.get(BOE_CSV_BASE, params=params, headers=headers, timeout=20)
    res.raise_for_status()

    # If BoE serves an HTML block/cookie page, don't parse it as CSV
    low = res.text[:300].lower()
    if "<html" in low or "our use of cookies" in low:
        raise ValueError("BoE returned HTML instead of CSV (likely blocked/cookie page).")

    df = pd.read_csv(io.StringIO(res.text))
    if df.shape[1] < 2:
        return pd.Series(dtype=float)

    date_col, val_col = df.columns[0], df.columns[1]
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce", dayfirst=True)
    df[val_col] = pd.to_numeric(df[val_col], errors="coerce")

    return df.set_index(date_col)[val_col].dropna().sort_index()

def fetch_yf_close(ticker: str) -> pd.Series:
    df = yf.download(ticker, period="2y", interval="1d", progress=False, auto_adjust=False, threads=False)
    if df.empty:
        return pd.Series(dtype=float)

    # Normalize multi-index columns from yfinance into a single-ticker frame.
    if isinstance(df.columns, pd.MultiIndex):
        levels0 = set(df.columns.get_level_values(0))
        levels1 = set(df.columns.get_level_values(1))
        if ticker in levels1:
            df = df.xs(ticker, axis=1, level=1)
        elif ticker in levels0:
            df = df.xs(ticker, axis=1, level=0)
        else:
            df.columns = df.columns.get_level_values(0)

    close_like = None
    if "Adj Close" in df.columns:
        close_like = df["Adj Close"]
    elif "Close" in df.columns:
        close_like = df["Close"]
    if close_like is None:
        return pd.Series(dtype=float)

    if isinstance(close_like, pd.DataFrame):
        if close_like.shape[1] == 0:
            return pd.Series(dtype=float)
        close_like = close_like.iloc[:, 0]

    s = pd.to_numeric(close_like.squeeze(), errors="coerce").dropna()
    s.index = pd.to_datetime(s.index)
    return s.sort_index()

def yf_to_stooq_symbol(ticker: str) -> str:
    # FTSE100 index
    if ticker.upper() == "^FTSE":
        return "^ukx"
    # UK stocks: "NWG.L" -> "nwg.uk"
    if ticker.upper().endswith(".L"):
        return ticker[:-2].lower() + ".uk"
    # fallback: treat as US
    return ticker.lower() + ".us"

def fetch_stooq_close(ticker: str) -> pd.Series:
    sym = yf_to_stooq_symbol(ticker)
    url = f"https://stooq.com/q/d/l/?s={sym}&i=d"
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


# =========================
# Metrics
# =========================

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

def price_metrics(close: pd.Series) -> PriceMetrics:
    if close.empty or len(close) < 200:
        return PriceMetrics(None, None, None, None, None)
    s = close.dropna().sort_index()
    c = float(s.iloc[-1])
    ma50 = float(s.rolling(50).mean().iloc[-1])
    ma200 = float(s.rolling(200).mean().iloc[-1])
    gap50 = (c / ma50 - 1.0) if ma50 != 0 else None
    gap200 = (c / ma200 - 1.0) if ma200 != 0 else None
    return PriceMetrics(c, ma50, ma200, gap50, gap200)


# =========================
# Main
# =========================

def main() -> None:
    now = datetime.now(timezone.utc)
    warnings: List[str] = []
    prev = load_previous()

    # --- 1) Fetch FRED macro ---
    fred: Dict[str, Dict[str, Optional[float]]] = {}
    fred_series_cache: Dict[str, pd.Series] = {}

    for sid, meta in FRED_SERIES.items():
        try:
            s = fetch_fred_series(sid)
            fred_series_cache[sid] = s
            latest, change, d = latest_and_change(s, days=28, scale_change=meta["scale_change"])
        except Exception as e:
            warnings.append(f"FRED {sid} failed ({e}), using cached values if available.")
            cached = prev.get("fred", {}).get(sid, {})
            latest, change, d = cached.get("latest"), cached.get("change_4w"), cached.get("latest_date")

        fred[sid] = {
            "latest": safe_num(latest, 6),
            "change_4w": safe_num(change, 3),
            "latest_date": d,
        }

    # --- 2) Fetch BoE series ---
    boe: Dict[str, Dict[str, Optional[float]]] = {}
    boe_series_cache: Dict[str, pd.Series] = {}

    for code, meta in BOE_SERIES.items():
        try:
            s = fetch_boe_series(code, datefrom="01/Jan/2015")
            boe_series_cache[code] = s
            latest, change, d = latest_and_change(s, days=28, scale_change=meta["scale_change"])
        except Exception as e:
            warnings.append(f"BoE {code} failed ({e}), using cached values if available.")
            cached = prev.get("boe", {}).get(code, {})
            latest, change, d = cached.get("latest"), cached.get("change_4w"), cached.get("latest_date")

        boe[code] = {
            "latest": safe_num(latest, 6),
            "change_4w": safe_num(change, 3),
            "latest_date": d,
        }

    # --- 3) Derived curve metrics ---
    # term_spread_10y_policy = 10y - policy
    term_spread_bp = None
    term_spread_4w_bp = None

    try:
        s10 = boe_series_cache.get("IUDMNPY", pd.Series(dtype=float))
        spr = boe_series_cache.get("IUDBEDR", pd.Series(dtype=float))
        term = (s10 - spr).dropna().sort_index()
        if not term.empty:
            t_latest, t_chg_bp, t_date = latest_and_change(term, days=28, scale_change=100.0)
            term_spread_bp = safe_num(t_latest * 100.0, 2) if t_latest is not None else None
            term_spread_4w_bp = safe_num(t_chg_bp, 2)
        else:
            t_date = None
    except Exception:
        t_date = None

    # 10s5s spread
    curve_10s5s_bp = None
    curve_10s5s_4w_bp = None
    try:
        s5 = boe_series_cache.get("IUDSNPY", pd.Series(dtype=float))
        s10 = boe_series_cache.get("IUDMNPY", pd.Series(dtype=float))
        c = (s10 - s5).dropna().sort_index()
        if not c.empty:
            c_latest, c_chg_bp, c_date = latest_and_change(c, days=28, scale_change=100.0)
            curve_10s5s_bp = safe_num(c_latest * 100.0, 2) if c_latest is not None else None
            curve_10s5s_4w_bp = safe_num(c_chg_bp, 2)
        else:
            c_date = None
    except Exception:
        c_date = None

    # --- 4) Fetch prices ---
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

    # peer basket
    peer_df = pd.concat([prices.get(t, pd.Series(dtype=float)).rename(t) for t in PEER_TICKERS], axis=1).dropna()
    peer_mean = peer_df.mean(axis=1) if not peer_df.empty else pd.Series(dtype=float)

    # --- 5) Compute signals ---
    nwg_close = prices.get(NWG_TICKER, pd.Series(dtype=float))
    ftse_close = prices.get(FTSE_TICKER, pd.Series(dtype=float))

    nwg_px = price_metrics(nwg_close)
    rs_ftse = ratio_metrics(nwg_close, ftse_close)
    rs_peer = ratio_metrics(nwg_close, peer_mean)

    # RiskGreen
    vix = fred.get("VIXCLS", {}).get("latest")
    hy_chg = fred.get("BAMLH0A0HYM2", {}).get("change_4w")
    ig_chg = fred.get("BAMLC0A0CM", {}).get("change_4w")
    nfci = fred.get("NFCI", {}).get("latest")

    risk_green = (
        (vix is not None and vix < TH["VIX_MAX"]) and
        (hy_chg is not None and hy_chg < TH["HY_4W_CHG_BP_MAX"]) and
        (ig_chg is not None and ig_chg < TH["IG_4W_CHG_BP_MAX"]) and
        (nfci is not None and nfci <= TH["NFCI_MAX"])
    )

    # CurveGreen
    uk10_4w_bp = boe.get("IUDMNPY", {}).get("change_4w")  # already bp-scaled in boe dict
    curve_green = (
        (term_spread_bp is not None and term_spread_bp > TH["TERM_SPREAD_10Y_POLICY_MIN_BP"]) and
        (term_spread_4w_bp is not None and term_spread_4w_bp > TH["TERM_SPREAD_10Y_POLICY_4W_CHG_MIN_BP"]) and
        (uk10_4w_bp is not None and uk10_4w_bp > TH["UK10Y_4W_CHG_MIN_BP"]) and
        (curve_10s5s_bp is not None and curve_10s5s_bp >= TH["CURVE_10S5S_MIN_BP"]) and
        (curve_10s5s_4w_bp is not None and curve_10s5s_4w_bp > TH["CURVE_10S5S_4W_CHG_MIN_BP"])
    )

    # DemandGreen (monthly; uses rolling averages)
    approvals = boe_series_cache.get("LPMVTVX", pd.Series(dtype=float))
    m4 = boe_series_cache.get("LPMVQJW", pd.Series(dtype=float))

    approvals_green = False
    if len(approvals.dropna()) >= 12:
        a3 = approvals.rolling(3).mean().iloc[-1]
        a12 = approvals.rolling(12).mean().iloc[-1]
        approvals_green = pd.notna(a3) and pd.notna(a12) and (a3 >= a12)

    m4_green = False
    if len(m4.dropna()) >= 4:
        m4_green = pd.notna(m4.iloc[-1]) and pd.notna(m4.shift(3).iloc[-1]) and ((m4.iloc[-1] - m4.shift(3).iloc[-1]) >= TH["M4_TREND_MIN"])

    demand_green = approvals_green and m4_green

    macro_green = risk_green and curve_green and demand_green

    # PriceConfirm
    pullback_ok = (
        (nwg_px.gap200 is not None) and (TH["NWG_GAP200_MIN"] <= nwg_px.gap200 <= TH["NWG_GAP200_MAX"]) and
        (nwg_px.gap50 is not None) and (nwg_px.gap50 <= TH["NWG_GAP50_MAX"])
    )

    rs_ok = (
        (rs_ftse.gap is not None and rs_ftse.gap <= TH["RS_GAP_MAX"]) and
        (rs_ftse.slope_proxy is not None and rs_ftse.slope_proxy > TH["RS_SLOPE_MIN"]) and
        (rs_peer.gap is not None and rs_peer.gap <= TH["RS_GAP_MAX"]) and
        (rs_peer.slope_proxy is not None and rs_peer.slope_proxy > TH["RS_SLOPE_MIN"])
    )

    price_confirm = pullback_ok and rs_ok

    entry_strict = macro_green and price_confirm
    entry_loose = (risk_green and curve_green) and price_confirm

    verdict = "⏸ No entry today"
    if entry_strict:
        verdict = "✅ ENTRY (STRICT): MacroGreen + PriceConfirm"
    elif entry_loose:
        verdict = "🟡 ENTRY (LOOSE): Risk+Curve + PriceConfirm (Demand monthly not confirmed)"

    # collect fail reasons (nice for daily debugging)
    fails = []
    if not risk_green:
        fails.append("RiskGreen=FALSE")
    if not curve_green:
        fails.append("CurveGreen=FALSE")
    if not demand_green:
        fails.append("DemandGreen=FALSE (monthly)")
    if not pullback_ok:
        fails.append("PullbackZone=FALSE")
    if not rs_ok:
        fails.append("RelativeTurn=FALSE")

    # best available price date
    date_candidates = [meta["latest_date"] for meta in price_meta.values() if meta.get("latest_date")]
    price_date = max(date_candidates) if date_candidates else prev.get("as_of", {}).get("price_date")

    out = {
        "generated_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "as_of": {"price_date": price_date, "run_time_utc": now.strftime("%Y-%m-%d %H:%M:%S")},
        "data_warning": bool(warnings),
        "warnings": warnings,
        "fred": fred,
        "boe": boe,
        "derived": {
            "TERM_SPREAD_10Y_POLICY_bp": term_spread_bp,
            "TERM_SPREAD_10Y_POLICY_4w_change_bp": term_spread_4w_bp,
            "CURVE_10s5s_bp": curve_10s5s_bp,
            "CURVE_10s5s_4w_change_bp": curve_10s5s_4w_bp,
        },
        "prices": price_meta,
        "signals": {
            "NWG": {
                "close": safe_num(nwg_px.close, 4),
                "ma50": safe_num(nwg_px.ma50, 4),
                "ma200": safe_num(nwg_px.ma200, 4),
                "gap50": safe_num(nwg_px.gap50, 6),
                "gap200": safe_num(nwg_px.gap200, 6),
            },
            "RS_FTSE": {
                "ratio": safe_num(rs_ftse.ratio),
                "ma60": safe_num(rs_ftse.ma60),
                "gap": safe_num(rs_ftse.gap),
                "ma60_slope_proxy": safe_num(rs_ftse.slope_proxy),
            },
            "RS_PEERS": {
                "ratio": safe_num(rs_peer.ratio),
                "ma60": safe_num(rs_peer.ma60),
                "gap": safe_num(rs_peer.gap),
                "ma60_slope_proxy": safe_num(rs_peer.slope_proxy),
            },
        },
        "checks": {
    "RiskGreen": bool(risk_green),
    "CurveGreen": bool(curve_green),
    "DemandGreen": bool(demand_green),
    "MacroGreen": bool(macro_green),
    "PriceConfirm": bool(price_confirm),
    "ENTRY_STRICT": bool(entry_strict),
    "ENTRY_LOOSE": bool(entry_loose),
},
        "fails": fails,
        "verdict": verdict,
    }

    OUTPUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    # Markdown summary
    lines = [
        "# NatWest Daily Entry Monitor",
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
        "## Verdict",
        verdict,
        "",
        "## Checks",
        f"- RiskGreen: **{risk_green}**",
        f"- CurveGreen: **{curve_green}**",
        f"- DemandGreen(monthly): **{demand_green}**",
        f"- MacroGreen: **{macro_green}**",
        f"- PriceConfirm: **{price_confirm}**",
        f"- ENTRY_STRICT: **{entry_strict}**",
        f"- ENTRY_LOOSE: **{entry_loose}**",
        "",
        "## Derived (UK rates/curve)",
        f"- TERM_SPREAD_10Y_POLICY: {out['derived']['TERM_SPREAD_10Y_POLICY_bp']} bp / 4주 변화 {out['derived']['TERM_SPREAD_10Y_POLICY_4w_change_bp']} bp",
        f"- CURVE_10s5s: {out['derived']['CURVE_10s5s_bp']} bp / 4주 변화 {out['derived']['CURVE_10s5s_4w_change_bp']} bp",
        "",
        "## NWG Price",
        f"- close: {out['signals']['NWG']['close']}",
        f"- MA50: {out['signals']['NWG']['ma50']} / gap50: {pct(out['signals']['NWG']['gap50'])}",
        f"- MA200: {out['signals']['NWG']['ma200']} / gap200: {pct(out['signals']['NWG']['gap200'])}",
        "",
        "## Relative Strength",
        f"- RS vs FTSE gap: {pct(out['signals']['RS_FTSE']['gap'])} / slope_proxy: {out['signals']['RS_FTSE']['ma60_slope_proxy']}",
        f"- RS vs Peers gap: {pct(out['signals']['RS_PEERS']['gap'])} / slope_proxy: {out['signals']['RS_PEERS']['ma60_slope_proxy']}",
        "",
    ]

    if fails:
        lines += ["## Why not today?", *(f"- {x}" for x in fails), ""]

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
