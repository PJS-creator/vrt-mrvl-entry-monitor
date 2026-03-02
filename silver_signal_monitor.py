from __future__ import annotations

import io
import json
import re
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
    # OAS series are in %, we scale to bp for readability.
    "BAMLH0A0HYM2": {"name": "HY OAS", "scale_change": 100.0},
    "BAMLC0A0CM": {"name": "IG OAS", "scale_change": 100.0},
    # 10Y real yield (%). We scale changes to bp.
    "DFII10": {"name": "10Y Real Yield", "scale_change": 100.0},
    "VIXCLS": {"name": "VIX", "scale_change": 1.0},
    "NFCI": {"name": "NFCI", "scale_change": 1.0},
}

# --- Prices / OHLCV (daily) ---
TICKERS = {
    # Targets
    "VZLA": "Vizsla Silver",
    "SCZM": "Santacruz Silver",
    "HYMC": "Hycroft Mining",
    # Regime / sector
    "SI=F": "Silver futures (COMEX)",
    "GC=F": "Gold futures (COMEX)",
    "SILJ": "Silver Miners Junior ETF",
    "SLV": "Silver ETF",
    "GDXJ": "Junior Gold Miners ETF",
    "GLD": "Gold ETF",
}

PRICE_TICKERS = list(TICKERS.keys())

OUTPUT_JSON = Path("latest_silver_signal.json")
OUTPUT_MD = Path("latest_silver_signal.md")


# =========================
# Thresholds (tweakable)
# =========================

TH: Dict[str, Dict[str, float]] = {
    "RISK": {
        # More tolerant than the core tech monitor because miners are inherently higher beta.
        "VIX_MAX": 30.0,
        "HY_4W_CHG_BP_MAX": 150.0,
        "IG_4W_CHG_BP_MAX": 80.0,
        "REALYIELD_4W_CHG_BP_MAX": 50.0,  # avoid sharp real-yield spike
        "NFCI_MAX": 0.5,
    },
    "REGIME": {
        # Leadership = SILJ outperforming SLV
        "MINERS_RS_GAP_MIN": 0.0,
        "MINERS_RS_SLOPE_MIN": 0.0,
        # Metals trend (optional; MA checks handle)
        "METALS_MA_SLOPE_LOOKBACK": 20.0,
    },
    "VZLA": {
        "ATR14_PCT_MAX": 0.15,
        "GAP_OPEN_MAX": 0.08,
        "SHOCK_DOWN_RET": -0.12,
        "SHOCK_DOWN_VOL": 2.0,
        "SHOCK_UP_RET": 0.25,
        "SHOCK_UP_VOL": 3.0,
        "PULLBACK_GAP20_MIN": -0.02,
        "PULLBACK_GAP20_MAX": 0.05,
        "PULLBACK_RSI_MIN": 40.0,
        "PULLBACK_RSI_MAX": 60.0,
        "BREAKOUT_WIN": 60.0,
        "BREAKOUT_BUFFER": 1.01,
        "BREAKOUT_VOL_MIN": 2.0,
        "BREAKOUT_RSI_MIN": 60.0,
        "RS_GAP_MIN": 0.00,
        "RS_SLOPE_MIN": 0.00,
        "GAP20_OVERHEAT_MAX": 0.15,
    },
    "SCZM": {
        # "Silver margin" gate, inspired by the break-even commentary in your text.
        "SILVER_WATCH": 32.0,
        "SILVER_ENTRY": 35.0,
        "ATR14_PCT_MAX": 0.20,
        "GAP_OPEN_MAX": 0.10,
        "SHOCK_DOWN_RET": -0.12,
        "SHOCK_DOWN_VOL": 2.0,
        "PULLBACK_GAP20_MIN": -0.02,
        "PULLBACK_GAP20_MAX": 0.07,
        "PULLBACK_RSI_MIN": 35.0,
        "PULLBACK_RSI_MAX": 60.0,
        "PULLBACK_VOL_MIN": 1.2,
        "BREAKOUT_WIN": 40.0,
        "BREAKOUT_BUFFER": 1.01,
        "BREAKOUT_VOL_MIN": 1.5,
        "BREAKOUT_RSI_MIN": 55.0,
        "RS_GAP_MIN": 0.00,
        "RS_SLOPE_MIN": 0.00,
        "GAP20_OVERHEAT_MAX": 0.18,
    },
    "HYMC": {
        "ATR14_PCT_MAX": 0.25,
        "GAP_OPEN_MAX": 0.12,
        "SHOCK_DOWN_RET": -0.15,
        "SHOCK_DOWN_VOL": 2.5,
        "SHOCK_UP_RET": 0.30,
        "SHOCK_UP_VOL": 4.0,
        "BREAKOUT_WIN": 120.0,
        "BREAKOUT_BUFFER": 1.01,
        "BREAKOUT_VOL_MIN": 2.0,
        "BREAKOUT_VOL_MAX": 8.0,
        "BREAKOUT_RSI_MIN": 55.0,
        "RETEST_GAP50_MAX": 0.05,
        "RETEST_RSI_MIN": 50.0,
        "RS_GAP_MIN": 0.00,
        "RS_SLOPE_MIN": 0.00,
        "GAP20_OVERHEAT_MAX": 0.20,
    },
}


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
    """Return latest, (latest-old)*scale_change, latest_date."""
    if s.empty:
        return None, None, None
    s = s.dropna().sort_index()
    last_date = s.index[-1]
    last_val = float(s.iloc[-1])

    base_date = last_date - timedelta(days=days)
    old = s.loc[s.index <= base_date]
    old_val = float(old.iloc[-1]) if not old.empty else float(s.iloc[0])

    return last_val, (last_val - old_val) * scale_change, last_date.strftime("%Y-%m-%d")


def safe_last(s: pd.Series) -> Optional[float]:
    if s is None or len(s) == 0:
        return None
    v = s.iloc[-1]
    return None if pd.isna(v) else float(v)


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


def _normalize_yf_ohlcv(df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """Normalize yfinance output (possible MultiIndex cols) into OHLCV DataFrame."""
    if df is None or df.empty:
        return pd.DataFrame()

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

    # Standardize columns
    cols = {c: str(c).title() for c in df.columns}
    df = df.rename(columns=cols)

    needed = ["Open", "High", "Low", "Close", "Volume"]
    missing = [c for c in needed if c not in df.columns]
    if missing:
        # Some tickers (rarely) miss volume; allow OHLC-only but ATR/vol rules will degrade.
        if all(c in df.columns for c in ["Open", "High", "Low", "Close"]):
            if "Volume" not in df.columns:
                df["Volume"] = 0.0
        else:
            return pd.DataFrame()

    out = df[["Open", "High", "Low", "Close", "Volume"]].copy()
    out.index = pd.to_datetime(out.index)
    for c in ["Open", "High", "Low", "Close", "Volume"]:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    out = out.dropna(subset=["Close"]).sort_index()
    return out


def fetch_yf_ohlcv(ticker: str) -> pd.DataFrame:
    # NOTE: auto_adjust=True makes OHLC consistent for splits.
    df = yf.download(
        ticker,
        period="2y",
        interval="1d",
        progress=False,
        auto_adjust=True,
        threads=False,
    )
    return _normalize_yf_ohlcv(df, ticker)


_STOOQ_OK = re.compile(r"^[A-Z0-9]+$")


def yf_to_stooq_symbol(ticker: str) -> Optional[str]:
    """Best-effort mapping for US-listed tickers to Stooq.

    We intentionally do NOT attempt to map futures (e.g. SI=F) or complex symbols.
    """
    t = ticker.upper()
    if not _STOOQ_OK.match(t):
        return None
    return t.lower() + ".us"


def fetch_stooq_ohlcv(ticker: str) -> pd.DataFrame:
    sym = yf_to_stooq_symbol(ticker)
    if sym is None:
        return pd.DataFrame()
    url = f"https://stooq.com/q/d/l/?s={sym}&i=d"
    res = requests.get(url, timeout=20)
    res.raise_for_status()
    df = pd.read_csv(io.StringIO(res.text))
    # Stooq columns: Date, Open, High, Low, Close, Volume
    if "Date" not in df.columns or "Close" not in df.columns:
        return pd.DataFrame()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for c in ["Open", "High", "Low", "Close", "Volume"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
        else:
            df[c] = pd.NA
    out = df.set_index("Date")[["Open", "High", "Low", "Close", "Volume"]].dropna(subset=["Close"]).sort_index()
    return out


def fetch_ohlcv(ticker: str, warnings: List[str]) -> pd.DataFrame:
    """Fetch OHLCV. Prefer yfinance; fallback to Stooq for simple US symbols."""
    try:
        df = fetch_yf_ohlcv(ticker)
        if len(df) >= 120:
            return df
        warnings.append(f"{ticker}: yfinance insufficient history ({len(df)} rows), fallback to Stooq.")
    except Exception as e:
        warnings.append(f"{ticker}: yfinance failed ({e}), fallback to Stooq.")

    try:
        df = fetch_stooq_ohlcv(ticker)
        if len(df) >= 120:
            return df
        warnings.append(f"{ticker}: Stooq insufficient history ({len(df)} rows).")
        return df
    except Exception as e:
        warnings.append(f"{ticker}: Stooq failed ({e}).")
        return pd.DataFrame()


# =========================
# Indicators
# =========================


def ma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    delta = close.diff()
    up = delta.clip(lower=0)
    down = (-delta).clip(lower=0)

    # Wilder smoothing (EMA with alpha=1/n)
    roll_up = up.ewm(alpha=1 / n, adjust=False).mean()
    roll_down = down.ewm(alpha=1 / n, adjust=False).mean()

    rs = roll_up / roll_down.replace(0, pd.NA)
    out = 100 - (100 / (1 + rs))
    return out


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    high = df["High"]
    low = df["Low"]
    close = df["Close"]
    prev_close = close.shift(1)

    tr = pd.concat(
        [(high - low).abs(), (high - prev_close).abs(), (low - prev_close).abs()],
        axis=1,
    ).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def prior_high(close: pd.Series, n: int) -> pd.Series:
    # avoid look-ahead: shift(1)
    return close.shift(1).rolling(n, min_periods=n).max()


def ratio_metrics(numer: pd.Series, denom: pd.Series) -> RatioMetrics:
    df = pd.concat([numer.rename("n"), denom.rename("d")], axis=1).dropna()
    if len(df) < 60:
        return RatioMetrics(None, None, None, None)

    ratio = df["n"] / df["d"]
    ma60 = ratio.rolling(60, min_periods=60).mean()

    r = float(ratio.iloc[-1])
    m = float(ma60.iloc[-1]) if pd.notna(ma60.iloc[-1]) else None
    gap = (r / m - 1.0) if (m not in (None, 0)) else None

    slope = None
    if len(ma60.dropna()) >= 81:  # 60 for MA + 20 for slope + buffer
        now = ma60.iloc[-1]
        prev = ma60.shift(20).iloc[-1]
        if pd.notna(now) and pd.notna(prev):
            slope = float(now - prev)

    return RatioMetrics(r, m, gap, slope)


def calc_ta(df: pd.DataFrame) -> Dict[str, Optional[float]]:
    if df is None or df.empty:
        return {
            "close": None,
            "ma20": None,
            "ma50": None,
            "ma120": None,
            "ma200": None,
            "gap20": None,
            "gap50": None,
            "gap200": None,
            "ma50_slope20": None,
            "ma200_slope20": None,
            "rsi14": None,
            "atr14": None,
            "atr14_pct": None,
            "vol_ratio": None,
            "ret1d": None,
            "gap_open": None,
        }

    c = df["Close"].dropna()
    o = df["Open"].dropna() if "Open" in df.columns else c * 0.0
    v = df["Volume"].dropna() if "Volume" in df.columns else pd.Series(0.0, index=c.index)

    ma20 = ma(c, 20)
    ma50 = ma(c, 50)
    ma120 = ma(c, 120)
    ma200 = ma(c, 200)

    c_last = safe_last(c)
    ma20_last = safe_last(ma20)
    ma50_last = safe_last(ma50)
    ma120_last = safe_last(ma120)
    ma200_last = safe_last(ma200)

    gap20 = None if (c_last is None or ma20_last in (None, 0)) else (c_last / ma20_last - 1.0)
    gap50 = None if (c_last is None or ma50_last in (None, 0)) else (c_last / ma50_last - 1.0)
    gap200 = None if (c_last is None or ma200_last in (None, 0)) else (c_last / ma200_last - 1.0)

    # slope proxies (20 trading days)
    ma50_slope = safe_last(ma50 - ma50.shift(20))
    ma200_slope = safe_last(ma200 - ma200.shift(20))

    rsi14 = safe_last(rsi(c, 14))
    atr14 = safe_last(atr(df, 14))
    atr14_pct = None if (atr14 is None or c_last in (None, 0)) else (atr14 / c_last)

    vol20 = v.rolling(20, min_periods=20).mean()
    vol_ratio = None if safe_last(vol20) in (None, 0) else (safe_last(v) / safe_last(vol20))

    ret1d = safe_last(c.pct_change())
    prev_close = c.shift(1)
    gap_open = safe_last((o - prev_close).abs() / prev_close) if not o.empty else None

    return {
        "close": c_last,
        "ma20": ma20_last,
        "ma50": ma50_last,
        "ma120": ma120_last,
        "ma200": ma200_last,
        "gap20": gap20,
        "gap50": gap50,
        "gap200": gap200,
        "ma50_slope20": ma50_slope,
        "ma200_slope20": ma200_slope,
        "rsi14": rsi14,
        "atr14": atr14,
        "atr14_pct": atr14_pct,
        "vol_ratio": vol_ratio,
        "ret1d": ret1d,
        "gap_open": gap_open,
    }


# =========================
# Entry logic helpers
# =========================


def bool_or_none(v: Optional[bool]) -> bool:
    return bool(v) if v is not None else False


def is_risk_green(macro: Dict[str, Dict[str, Optional[float]]]) -> Tuple[bool, Dict[str, bool]]:
    """Risk gate using 4w changes and levels."""
    vix = macro.get("VIXCLS", {}).get("latest")
    hy_chg = macro.get("BAMLH0A0HYM2", {}).get("change_4w")
    ig_chg = macro.get("BAMLC0A0CM", {}).get("change_4w")
    ry_chg = macro.get("DFII10", {}).get("change_4w")
    nfci = macro.get("NFCI", {}).get("latest")

    checks = {
        "VIX_lt_max": vix is not None and vix < TH["RISK"]["VIX_MAX"],
        "HY_4w_chg_bp_lt_max": hy_chg is not None and hy_chg < TH["RISK"]["HY_4W_CHG_BP_MAX"],
        "IG_4w_chg_bp_lt_max": ig_chg is not None and ig_chg < TH["RISK"]["IG_4W_CHG_BP_MAX"],
        "RealYield_4w_chg_bp_lt_max": ry_chg is not None and ry_chg < TH["RISK"]["REALYIELD_4W_CHG_BP_MAX"],
        "NFCI_lte_max": nfci is not None and nfci <= TH["RISK"]["NFCI_MAX"],
    }
    return all(checks.values()), checks


def metals_uptrend(ta: Dict[str, Optional[float]]) -> bool:
    # close > MA200 and MA50 > MA200 and MA50 slope positive
    c = ta.get("close")
    ma50_ = ta.get("ma50")
    ma200_ = ta.get("ma200")
    slope50 = ta.get("ma50_slope20")
    if any(x is None for x in [c, ma50_, ma200_, slope50]):
        return False
    return (c > ma200_) and (ma50_ > ma200_) and (slope50 > 0)


def leaders_ok(rs: RatioMetrics, rs_gap_min: float, rs_slope_min: float) -> bool:
    return (
        (rs.gap is not None and rs.gap >= rs_gap_min)
        and (rs.slope_proxy is not None and rs.slope_proxy > rs_slope_min)
    )


def shock_flags(ta: Dict[str, Optional[float]], p: Dict[str, float]) -> Tuple[bool, bool]:
    """Return shock_down, shock_up."""
    ret1d = ta.get("ret1d")
    vr = ta.get("vol_ratio")
    shock_down = (
        ret1d is not None
        and vr is not None
        and (ret1d <= p.get("SHOCK_DOWN_RET", -0.12))
        and (vr >= p.get("SHOCK_DOWN_VOL", 2.0))
    )
    shock_up = (
        ret1d is not None
        and vr is not None
        and (ret1d >= p.get("SHOCK_UP_RET", 0.25))
        and (vr >= p.get("SHOCK_UP_VOL", 3.0))
    )
    return shock_down, shock_up


def pullback_trigger(ta: Dict[str, Optional[float]], p: Dict[str, float], require_vol_min: Optional[float] = None) -> bool:
    gap20 = ta.get("gap20")
    rsi14 = ta.get("rsi14")
    close = ta.get("close")
    ma20_ = ta.get("ma20")
    vr = ta.get("vol_ratio")

    if any(x is None for x in [gap20, rsi14, close, ma20_]):
        return False
    if not (p["PULLBACK_GAP20_MIN"] <= gap20 <= p["PULLBACK_GAP20_MAX"]):
        return False
    if not (p["PULLBACK_RSI_MIN"] <= rsi14 <= p["PULLBACK_RSI_MAX"]):
        return False
    if not (close > ma20_):
        return False
    if require_vol_min is not None:
        if vr is None or vr < require_vol_min:
            return False
    return True


def breakout_trigger(df: pd.DataFrame, ta: Dict[str, Optional[float]], p: Dict[str, float]) -> bool:
    close = ta.get("close")
    rsi14 = ta.get("rsi14")
    vr = ta.get("vol_ratio")
    gap20 = ta.get("gap20")

    if df is None or df.empty:
        return False
    if any(x is None for x in [close, rsi14, vr]):
        return False

    win = int(p["BREAKOUT_WIN"])
    ph = prior_high(df["Close"].dropna(), win)
    ph_last = safe_last(ph)
    if ph_last is None:
        return False

    if not (close > ph_last * p.get("BREAKOUT_BUFFER", 1.01)):
        return False
    if vr < p.get("BREAKOUT_VOL_MIN", 2.0):
        return False
    if rsi14 < p.get("BREAKOUT_RSI_MIN", 55.0):
        return False

    # overheating guard
    if gap20 is not None and gap20 > p.get("GAP20_OVERHEAT_MAX", 0.20):
        return False

    # HYMC-style: exclude ultra-crazy volume days
    if "BREAKOUT_VOL_MAX" in p and vr > p["BREAKOUT_VOL_MAX"]:
        return False

    return True


# =========================
# Main
# =========================


def main() -> None:
    now = datetime.now(timezone.utc)
    warnings: List[str] = []
    prev = load_previous()

    # --- 1) Macro (FRED) ---
    macro: Dict[str, Dict[str, Optional[float]]] = {}
    for sid, meta in FRED_SERIES.items():
        try:
            s = fetch_fred_series(sid)
            latest, change, d = latest_and_change(s, days=28, scale_change=meta["scale_change"])
        except Exception as e:
            warnings.append(f"FRED {sid} failed ({e}), using cached values if available.")
            cached = prev.get("macro", {}).get(sid, {})
            latest, change, d = cached.get("latest"), cached.get("change_4w"), cached.get("latest_date")

        macro[sid] = {
            "latest": safe_num(latest, 6),
            "change_4w": safe_num(change, 3),
            "latest_date": d,
        }

    risk_green, risk_checks = is_risk_green(macro)

    # --- 2) Prices / OHLCV ---
    prices: Dict[str, pd.DataFrame] = {}
    price_meta: Dict[str, Dict[str, Optional[float]]] = {}
    ta_cache: Dict[str, Dict[str, Optional[float]]] = {}

    for t in PRICE_TICKERS:
        df = fetch_ohlcv(t, warnings)
        if df.empty:
            # fallback to cached close-only
            c = prev.get("prices", {}).get(t, {}).get("close")
            d = prev.get("prices", {}).get(t, {}).get("latest_date")
            if c is not None and d is not None:
                idx = pd.to_datetime([d])
                df = pd.DataFrame(
                    {
                        "Open": [float(c)],
                        "High": [float(c)],
                        "Low": [float(c)],
                        "Close": [float(c)],
                        "Volume": [0.0],
                    },
                    index=idx,
                )
                warnings.append(f"{t}: using cached price.")

        prices[t] = df
        ta = calc_ta(df)
        ta_cache[t] = ta

        close_val = ta.get("close")
        latest_date = df.index[-1].strftime("%Y-%m-%d") if not df.empty else None
        price_meta[t] = {
            "close": safe_num(close_val, 6) if close_val is not None else None,
            "latest_date": latest_date,
        }

    # --- 3) Regime metrics (metals + miners leadership) ---
    si_ta = ta_cache.get("SI=F", {})
    gc_ta = ta_cache.get("GC=F", {})
    silver_up = metals_uptrend(si_ta)
    gold_up = metals_uptrend(gc_ta)

    silj_close = prices.get("SILJ", pd.DataFrame()).get("Close", pd.Series(dtype=float))
    slv_close = prices.get("SLV", pd.DataFrame()).get("Close", pd.Series(dtype=float))
    gdxj_close = prices.get("GDXJ", pd.DataFrame()).get("Close", pd.Series(dtype=float))
    gld_close = prices.get("GLD", pd.DataFrame()).get("Close", pd.Series(dtype=float))

    miners_rs = ratio_metrics(silj_close, slv_close)
    miners_lead = leaders_ok(miners_rs, TH["REGIME"]["MINERS_RS_GAP_MIN"], TH["REGIME"]["MINERS_RS_SLOPE_MIN"])

    jg_rs = ratio_metrics(gdxj_close, gld_close)
    jg_lead = leaders_ok(jg_rs, 0.0, 0.0)  # simple

    regime = {
        "risk_green": bool(risk_green),
        "silver_uptrend": bool(silver_up),
        "gold_uptrend": bool(gold_up),
        "miners_leadership": bool(miners_lead),
        "junior_gold_leadership": bool(jg_lead),
        "SILJ_over_SLV": {
            "ratio": safe_num(miners_rs.ratio),
            "ma60": safe_num(miners_rs.ma60),
            "gap": safe_num(miners_rs.gap),
            "ma60_slope_proxy": safe_num(miners_rs.slope_proxy),
        },
        "GDXJ_over_GLD": {
            "ratio": safe_num(jg_rs.ratio),
            "ma60": safe_num(jg_rs.ma60),
            "gap": safe_num(jg_rs.gap),
            "ma60_slope_proxy": safe_num(jg_rs.slope_proxy),
        },
        "metals": {
            "SI": {k: safe_num(v, 6) for k, v in si_ta.items()},
            "GC": {k: safe_num(v, 6) for k, v in gc_ta.items()},
        },
    }

    # --- 4) Per-ticker signals ---
    signals: Dict[str, Dict] = {}

    def rs_vs(series_a: pd.Series, series_b: pd.Series) -> RatioMetrics:
        return ratio_metrics(series_a, series_b)

    # helper close series
    vzla_close = prices.get("VZLA", pd.DataFrame()).get("Close", pd.Series(dtype=float))
    sczm_close = prices.get("SCZM", pd.DataFrame()).get("Close", pd.Series(dtype=float))
    hymc_close = prices.get("HYMC", pd.DataFrame()).get("Close", pd.Series(dtype=float))

    rs_vzla_silj = rs_vs(vzla_close, silj_close)
    rs_sczm_silj = rs_vs(sczm_close, silj_close)
    rs_hymc_silj = rs_vs(hymc_close, silj_close)
    rs_hymc_gdxj = rs_vs(hymc_close, gdxj_close)

    # --- VZLA ---
    vz_p = TH["VZLA"]
    vz_ta = ta_cache.get("VZLA", {})
    vz_shock_down, vz_shock_up = shock_flags(vz_ta, vz_p)
    vz_risk_ok = (
        (vz_ta.get("atr14_pct") is not None and vz_ta["atr14_pct"] <= vz_p["ATR14_PCT_MAX"])
        and ((vz_ta.get("gap_open") is None) or (vz_ta["gap_open"] <= vz_p["GAP_OPEN_MAX"]))
        and (not vz_shock_down)
        and (not vz_shock_up)
    )

    vz_trend_ok = (
        vz_ta.get("close") is not None
        and vz_ta.get("ma200") is not None
        and vz_ta.get("ma50") is not None
        and (vz_ta["close"] > vz_ta["ma200"])
        and (vz_ta["ma50"] > vz_ta["ma200"])
        and (vz_ta.get("ma200_slope20") is None or vz_ta["ma200_slope20"] >= 0)
    )

    vz_rs_ok = leaders_ok(rs_vzla_silj, vz_p["RS_GAP_MIN"], vz_p["RS_SLOPE_MIN"])

    vz_pullback = pullback_trigger(vz_ta, vz_p)
    vz_breakout = breakout_trigger(prices.get("VZLA", pd.DataFrame()), vz_ta, vz_p)

    vz_entry_candidate = bool(risk_green) and bool(silver_up) and bool(miners_lead) and vz_trend_ok and vz_rs_ok and vz_risk_ok and (vz_pullback or vz_breakout)
    vz_prev_candidate = bool(prev.get("signals", {}).get("VZLA", {}).get("entry_candidate", False))
    vz_entry_confirmed = bool(vz_entry_candidate and vz_prev_candidate)

    vz_fails: List[str] = []
    if not risk_green:
        vz_fails.append("RiskGreen=FALSE")
    if not silver_up:
        vz_fails.append("SilverUptrend=FALSE")
    if not miners_lead:
        vz_fails.append("MinersLeadership(SILJ/SLV)=FALSE")
    if not vz_trend_ok:
        vz_fails.append("Trend(MA200/MA50)=FALSE")
    if not vz_rs_ok:
        vz_fails.append("RelativeStrength(vs SILJ)=FALSE")
    if not vz_risk_ok:
        vz_fails.append("RiskFilter(ATR/Gap/Shock)=FALSE")
    if not (vz_pullback or vz_breakout):
        vz_fails.append("Trigger(Pullback/Breakout)=FALSE")

    signals["VZLA"] = {
        "name": TICKERS["VZLA"],
        "ta": {k: safe_num(v, 6) for k, v in vz_ta.items()},
        "rs_vs_SILJ": {
            "ratio": safe_num(rs_vzla_silj.ratio),
            "ma60": safe_num(rs_vzla_silj.ma60),
            "gap": safe_num(rs_vzla_silj.gap),
            "ma60_slope_proxy": safe_num(rs_vzla_silj.slope_proxy),
        },
        "checks": {
            "trend_ok": bool(vz_trend_ok),
            "rs_ok": bool(vz_rs_ok),
            "risk_ok": bool(vz_risk_ok),
            "shock_down": bool(vz_shock_down),
            "shock_up": bool(vz_shock_up),
            "pullback": bool(vz_pullback),
            "breakout": bool(vz_breakout),
        },
        "entry_candidate": bool(vz_entry_candidate),
        "entry_confirmed": bool(vz_entry_confirmed),
        "fails": vz_fails,
    }

    # --- SCZM ---
    sc_p = TH["SCZM"]
    sc_ta = ta_cache.get("SCZM", {})
    sc_shock_down, _ = shock_flags(sc_ta, sc_p)
    sc_risk_ok = (
        (sc_ta.get("atr14_pct") is not None and sc_ta["atr14_pct"] <= sc_p["ATR14_PCT_MAX"])
        and ((sc_ta.get("gap_open") is None) or (sc_ta["gap_open"] <= sc_p["GAP_OPEN_MAX"]))
        and (not sc_shock_down)
    )

    # dynamic long MA: SCZM history may be shorter; fall back to MA120.
    sc_df = prices.get("SCZM", pd.DataFrame())
    sc_len = len(sc_df) if sc_df is not None else 0
    sc_ma_long = 200 if sc_len >= 220 else 120
    sc_ma_long_val = sc_ta.get("ma200") if sc_ma_long == 200 else sc_ta.get("ma120")

    sc_trend_ok = (
        sc_ta.get("close") is not None
        and sc_ma_long_val is not None
        and sc_ta.get("ma50") is not None
        and (sc_ta["close"] > sc_ma_long_val)
        and (sc_ta["ma50"] > sc_ma_long_val)
        and (sc_ta.get("ma50_slope20") is not None and sc_ta["ma50_slope20"] > 0)
    )

    sc_rs_ok = leaders_ok(rs_sczm_silj, sc_p["RS_GAP_MIN"], sc_p["RS_SLOPE_MIN"])

    # Silver margin gate
    si_close = si_ta.get("close")
    silver_watch = bool(si_close is not None and si_close >= sc_p["SILVER_WATCH"])
    silver_entry = bool(si_close is not None and si_close >= sc_p["SILVER_ENTRY"])

    sc_pullback = pullback_trigger(sc_ta, sc_p, require_vol_min=sc_p["PULLBACK_VOL_MIN"])
    sc_breakout = breakout_trigger(sc_df, sc_ta, sc_p)

    sc_entry_candidate = bool(risk_green) and bool(miners_lead) and bool(silver_up) and bool(silver_entry) and sc_trend_ok and sc_rs_ok and sc_risk_ok and (sc_pullback or sc_breakout)
    sc_prev_candidate = bool(prev.get("signals", {}).get("SCZM", {}).get("entry_candidate", False))
    sc_entry_confirmed = bool(sc_entry_candidate and sc_prev_candidate)

    sc_fails: List[str] = []
    if not risk_green:
        sc_fails.append("RiskGreen=FALSE")
    if not silver_up:
        sc_fails.append("SilverUptrend=FALSE")
    if not miners_lead:
        sc_fails.append("MinersLeadership(SILJ/SLV)=FALSE")
    if not silver_entry:
        sc_fails.append(f"SilverMarginGate=FALSE (SI<{sc_p['SILVER_ENTRY']})")
    if not sc_trend_ok:
        sc_fails.append(f"Trend(MA{sc_ma_long}/MA50)=FALSE")
    if not sc_rs_ok:
        sc_fails.append("RelativeStrength(vs SILJ)=FALSE")
    if not sc_risk_ok:
        sc_fails.append("RiskFilter(ATR/Gap/Shock)=FALSE")
    if not (sc_pullback or sc_breakout):
        sc_fails.append("Trigger(Pullback/Breakout)=FALSE")

    signals["SCZM"] = {
        "name": TICKERS["SCZM"],
        "ta": {k: safe_num(v, 6) for k, v in sc_ta.items()},
        "ma_long": sc_ma_long,
        "silver_margin": {
            "SI_close": safe_num(si_close, 6) if si_close is not None else None,
            "watch_ge": sc_p["SILVER_WATCH"],
            "entry_ge": sc_p["SILVER_ENTRY"],
            "watch": bool(silver_watch),
            "entry": bool(silver_entry),
        },
        "rs_vs_SILJ": {
            "ratio": safe_num(rs_sczm_silj.ratio),
            "ma60": safe_num(rs_sczm_silj.ma60),
            "gap": safe_num(rs_sczm_silj.gap),
            "ma60_slope_proxy": safe_num(rs_sczm_silj.slope_proxy),
        },
        "checks": {
            "trend_ok": bool(sc_trend_ok),
            "rs_ok": bool(sc_rs_ok),
            "risk_ok": bool(sc_risk_ok),
            "shock_down": bool(sc_shock_down),
            "pullback": bool(sc_pullback),
            "breakout": bool(sc_breakout),
        },
        "entry_candidate": bool(sc_entry_candidate),
        "entry_confirmed": bool(sc_entry_confirmed),
        "fails": sc_fails,
    }

    # --- HYMC ---
    hy_p = TH["HYMC"]
    hy_ta = ta_cache.get("HYMC", {})
    hy_shock_down, hy_shock_up = shock_flags(hy_ta, hy_p)
    hy_risk_ok = (
        (hy_ta.get("atr14_pct") is not None and hy_ta["atr14_pct"] <= hy_p["ATR14_PCT_MAX"])
        and ((hy_ta.get("gap_open") is None) or (hy_ta["gap_open"] <= hy_p["GAP_OPEN_MAX"]))
        and (not hy_shock_down)
        and (not hy_shock_up)
    )

    hy_trend_ok = (
        hy_ta.get("close") is not None
        and hy_ta.get("ma200") is not None
        and hy_ta.get("ma50") is not None
        and (hy_ta["close"] > hy_ta["ma200"])
        and (hy_ta["ma50"] > hy_ta["ma200"])
    )

    # HYMC is better compared vs GDXJ too.
    hy_rs_ok = leaders_ok(rs_hymc_gdxj, hy_p["RS_GAP_MIN"], hy_p["RS_SLOPE_MIN"]) or leaders_ok(
        rs_hymc_silj, hy_p["RS_GAP_MIN"], hy_p["RS_SLOPE_MIN"]
    )

    metals_ok = bool(silver_up and gold_up)
    sector_ok = bool(miners_lead or jg_lead)

    hy_breakout = breakout_trigger(prices.get("HYMC", pd.DataFrame()), hy_ta, hy_p)

    # Retest: within 5% of MA50 while above MA200
    hy_retest = False
    if hy_ta.get("close") is not None and hy_ta.get("ma50") is not None and hy_ta.get("ma200") is not None:
        gap50 = (hy_ta["close"] / hy_ta["ma50"] - 1.0) if hy_ta["ma50"] else None
        if gap50 is not None and abs(gap50) <= hy_p["RETEST_GAP50_MAX"]:
            if hy_ta["close"] > hy_ta["ma200"]:
                if hy_ta.get("rsi14") is not None and hy_ta["rsi14"] >= hy_p["RETEST_RSI_MIN"]:
                    hy_retest = True

    hy_entry_candidate = bool(risk_green) and metals_ok and sector_ok and hy_trend_ok and hy_rs_ok and hy_risk_ok and (hy_breakout or hy_retest)
    hy_prev_candidate = bool(prev.get("signals", {}).get("HYMC", {}).get("entry_candidate", False))
    hy_entry_confirmed = bool(hy_entry_candidate and hy_prev_candidate)

    hy_fails: List[str] = []
    if not risk_green:
        hy_fails.append("RiskGreen=FALSE")
    if not metals_ok:
        hy_fails.append("MetalsUptrend(SI&GC)=FALSE")
    if not sector_ok:
        hy_fails.append("SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE")
    if not hy_trend_ok:
        hy_fails.append("Trend(MA200/MA50)=FALSE")
    if not hy_rs_ok:
        hy_fails.append("RelativeStrength(vs GDXJ/SILJ)=FALSE")
    if not hy_risk_ok:
        hy_fails.append("RiskFilter(ATR/Gap/Shock)=FALSE")
    if not (hy_breakout or hy_retest):
        hy_fails.append("Trigger(Breakout/Retest)=FALSE")

    signals["HYMC"] = {
        "name": TICKERS["HYMC"],
        "ta": {k: safe_num(v, 6) for k, v in hy_ta.items()},
        "rs_vs_SILJ": {
            "ratio": safe_num(rs_hymc_silj.ratio),
            "ma60": safe_num(rs_hymc_silj.ma60),
            "gap": safe_num(rs_hymc_silj.gap),
            "ma60_slope_proxy": safe_num(rs_hymc_silj.slope_proxy),
        },
        "rs_vs_GDXJ": {
            "ratio": safe_num(rs_hymc_gdxj.ratio),
            "ma60": safe_num(rs_hymc_gdxj.ma60),
            "gap": safe_num(rs_hymc_gdxj.gap),
            "ma60_slope_proxy": safe_num(rs_hymc_gdxj.slope_proxy),
        },
        "checks": {
            "metals_ok": bool(metals_ok),
            "sector_ok": bool(sector_ok),
            "trend_ok": bool(hy_trend_ok),
            "rs_ok": bool(hy_rs_ok),
            "risk_ok": bool(hy_risk_ok),
            "shock_down": bool(hy_shock_down),
            "shock_up": bool(hy_shock_up),
            "breakout": bool(hy_breakout),
            "retest": bool(hy_retest),
        },
        "entry_candidate": bool(hy_entry_candidate),
        "entry_confirmed": bool(hy_entry_confirmed),
        "fails": hy_fails,
    }

    # --- Verdict ---
    confirmed = [t for t in ["VZLA", "SCZM", "HYMC"] if signals.get(t, {}).get("entry_confirmed")]
    candidates = [t for t in ["VZLA", "SCZM", "HYMC"] if signals.get(t, {}).get("entry_candidate")]

    verdict = "⏸ No entry today"
    if confirmed:
        verdict = "✅ ENTRY CONFIRMED: " + ", ".join(confirmed)
    elif candidates:
        verdict = "🟡 ENTRY CANDIDATE: " + ", ".join(candidates)

    # best available price date
    date_candidates = [meta["latest_date"] for meta in price_meta.values() if meta.get("latest_date")]
    price_date = max(date_candidates) if date_candidates else prev.get("as_of", {}).get("price_date")

    out = {
        "generated_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "as_of": {"price_date": price_date, "run_time_utc": now.strftime("%Y-%m-%d %H:%M:%S")},
        "data_warning": bool(warnings),
        "warnings": warnings,
        "thresholds": TH,
        "macro": macro,
        "risk_checks": risk_checks,
        "prices": price_meta,
        "regime": regime,
        "signals": signals,
        "verdict": verdict,
    }

    OUTPUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    # --- Markdown summary ---
    lines: List[str] = []
    lines += [
        "# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)",
        "",
        f"- 데이터 기준일(주가): **{out['as_of']['price_date']}**",
        f"- 실행시간(UTC): **{out['as_of']['run_time_utc']}**",
        "",
    ]

    if out["data_warning"]:
        lines += ["## ⚠️ DATA WARNING", "일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.", ""]
        lines += [f"- {w}" for w in warnings]
        lines.append("")

    lines += ["## Verdict", verdict, ""]

    lines += [
        "## Regime (공통 게이트)",
        f"- RiskGreen: **{risk_green}**",
        f"- SilverUptrend(SI=F): **{silver_up}**",
        f"- GoldUptrend(GC=F): **{gold_up}**",
        f"- MinersLeadership(SILJ/SLV): **{miners_lead}**",
        f"- JuniorGoldLeadership(GDXJ/GLD): **{jg_lead}**",
        "",
        "### Macro (FRED)",
        f"- HY OAS 4주 변화: {macro['BAMLH0A0HYM2']['change_4w']} bp / latest {macro['BAMLH0A0HYM2']['latest']}",
        f"- IG OAS 4주 변화: {macro['BAMLC0A0CM']['change_4w']} bp / latest {macro['BAMLC0A0CM']['latest']}",
        f"- 10Y Real Yield 4주 변화: {macro['DFII10']['change_4w']} bp / latest {macro['DFII10']['latest']}",
        f"- VIX: {macro['VIXCLS']['latest']}",
        f"- NFCI: {macro['NFCI']['latest']}",
        "",
        "### Leadership ratios",
        f"- SILJ/SLV gap: {pct(regime['SILJ_over_SLV']['gap'])} / slope_proxy: {regime['SILJ_over_SLV']['ma60_slope_proxy']}",
        f"- GDXJ/GLD gap: {pct(regime['GDXJ_over_GLD']['gap'])} / slope_proxy: {regime['GDXJ_over_GLD']['ma60_slope_proxy']}",
        "",
    ]

    def render_ticker_block(t: str) -> List[str]:
        s = signals.get(t, {})
        ta = s.get("ta", {})

        block = [
            f"## {t} ({s.get('name','')})",
            f"- close: {ta.get('close')} | RSI14: {ta.get('rsi14')} | ATR14%: {pct(ta.get('atr14_pct'))}",
            f"- MA20 gap: {pct(ta.get('gap20'))} | MA50 gap: {pct(ta.get('gap50'))} | MA200 gap: {pct(ta.get('gap200'))}",
            f"- vol_ratio(Volume/Vol20): {ta.get('vol_ratio')} | gap_open: {pct(ta.get('gap_open'))}",
        ]

        if t == "SCZM":
            sm = s.get("silver_margin", {})
            block += [
                f"- SilverMarginGate: SI={sm.get('SI_close')} / watch>={sm.get('watch_ge')}:{sm.get('watch')} / entry>={sm.get('entry_ge')}:{sm.get('entry')}",
            ]

        if "rs_vs_SILJ" in s:
            rs = s["rs_vs_SILJ"]
            block += [
                f"- RS vs SILJ gap: {pct(rs.get('gap'))} / slope_proxy: {rs.get('ma60_slope_proxy')}",
            ]
        if t == "HYMC" and "rs_vs_GDXJ" in s:
            rs = s["rs_vs_GDXJ"]
            block += [
                f"- RS vs GDXJ gap: {pct(rs.get('gap'))} / slope_proxy: {rs.get('ma60_slope_proxy')}",
            ]

        ck = s.get("checks", {})
        block += [
            "- Checks:",
            f"  - trend_ok: **{ck.get('trend_ok')}**",
            f"  - rs_ok: **{ck.get('rs_ok')}**",
            f"  - risk_ok: **{ck.get('risk_ok')}**",
        ]
        # triggers
        trig = []
        if ck.get("pullback") is not None:
            trig.append(f"pullback={ck.get('pullback')}")
        if ck.get("breakout") is not None:
            trig.append(f"breakout={ck.get('breakout')}")
        if ck.get("retest") is not None:
            trig.append(f"retest={ck.get('retest')}")
        if trig:
            block += [f"  - triggers: {', '.join(trig)}"]

        block += [
            f"- **ENTRY_CANDIDATE**: **{s.get('entry_candidate')}**",
            f"- **ENTRY_CONFIRMED**: **{s.get('entry_confirmed')}**",
            "",
        ]

        fails = s.get("fails", [])
        if fails:
            block += ["### Why not today?", *(f"- {x}" for x in fails), ""]
        return block

    for t in ["VZLA", "SCZM", "HYMC"]:
        lines += render_ticker_block(t)

    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
