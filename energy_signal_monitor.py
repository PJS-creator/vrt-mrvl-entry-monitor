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
# CONFIG (EDIT HERE)
# =========================

# FRED series (stable, no API key). Used for vol/credit/USD + as backup for spot prices.
FRED_SERIES = [
    # Energy spot prices (backup)
    "DCOILWTICO",       # WTI spot $/bbl
    "DCOILBRENTEU",     # Brent spot $/bbl
    "DHHNGSP",          # Henry Hub gas spot $/MMBtu

    # Volatility
    "OVXCLS",           # CBOE Crude Oil ETF Volatility Index
    "VIXCLS",           # VIX

    # Credit / USD / liquidity
    "BAMLH0A0HYM2",     # HY OAS
    "BAMLC0A0CM",       # IG OAS
    "DTWEXBGS",         # Broad USD index
    "NFCI",             # Chicago Fed NFCI (weekly)

    # Brazil risk (for PBR)
    "VXEWZCLS",         # CBOE Brazil ETF Vol Index
]

# Yahoo Finance tickers (EOD). For "more timely" oil/gas, we also pull futures tickers.
PRICE_TICKERS = [
    # Target stocks
    "PBR", "OXY", "VG", "RIG",

    # Benchmarks / peers
    "XLE", "OIH", "EWZ", "LNG", "SPY",

    # FX / commodity futures (yfinance-only)
    "BRL=X", "CL=F", "BZ=F", "NG=F",
]
YF_ONLY = {"BRL=X", "CL=F", "BZ=F", "NG=F"}

OUTPUT_JSON = Path("latest_energy_signal.json")
OUTPUT_MD = Path("latest_energy_signal.md")

# ---- thresholds (tune to taste) ----
TH = {
    # risk gate
    "VIX_MAX_STRICT": 25.0,
    "VIX_MAX_SOFT": 30.0,
    "OVX_MAX": 70.0,
    "DXY_5D_MAX_STRICT": 0.015,   # +1.5%
    "DXY_5D_MAX_SOFT": 0.020,     # +2.0%
    "HY_4W_BP_MAX_STRICT": 100.0,
    "HY_4W_BP_MAX_SOFT": 150.0,

    # Brazil gate
    "VXEWZ_MAX": 35.0,
    "BRL_5D_MIN": -0.01,          # BRL=X 5d change > -1% (avoid sharp BRL weakening)

    # pullback / extension controls
    "PULLBACK_GAP20_MIN": -0.08,  # -8%
    "PULLBACK_GAP20_MAX": 0.02,   # +2%
    "PULLBACK_GAP60_MIN": -0.07,  # -7%
    "PULLBACK_GAP60_MAX": 0.02,   # +2%

    # relative strength controls
    "REL_GAP_MAX_OXY": 0.10,      # +10% vs 60d MA
    "REL_GAP_MAX_PBR": 0.10,
    "REL_GAP_MAX_RIG": 0.15,
    "REL_GAP_BAND_VG_MIN": -0.10, # -10%
    "REL_GAP_BAND_VG_MAX": 0.05,  # +5%

    # breakout/volume confirm
    "VOL_RATIO_MIN": 1.20,        # volume / vol_ma20
}


# =========================
# DATA STRUCTURES
# =========================

@dataclass
class RatioMetrics:
    ratio: Optional[float]
    ma60: Optional[float]
    gap: Optional[float]
    slope_proxy: Optional[float] = None


@dataclass
class TrendMetrics:
    close: Optional[float]
    ma20: Optional[float]
    ma60: Optional[float]
    ma200: Optional[float]
    gap20: Optional[float]
    gap60: Optional[float]
    ret5d: Optional[float]
    high20: Optional[float]
    low20: Optional[float]


@dataclass
class VolumeMetrics:
    vol: Optional[float]
    ma20: Optional[float]
    ratio: Optional[float]


# =========================
# UTIL
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


def pct(v: Optional[float], digits: int = 2) -> str:
    return "N/A" if v is None else f"{v*100:.{digits}f}%"


def fmt(v: Optional[float], digits: int = 2) -> str:
    return "N/A" if v is None else f"{v:.{digits}f}"


def oil_tier(brent: Optional[float]) -> Optional[str]:
    if brent is None:
        return None
    if brent < 60:
        return "<60"
    if brent < 70:
        return "60-70"
    if brent < 80:
        return "70-80"
    if brent < 90:
        return "80-90"
    return ">=90"


# =========================
# FRED
# =========================

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


def latest_and_change(s: pd.Series, lookback_obs: int = 5) -> Tuple[Optional[float], Optional[float], Optional[str]]:
    if s.empty:
        return None, None, None
    last_date = s.index[-1]
    last_val = float(s.iloc[-1])
    chg = None
    if len(s) > lookback_obs:
        old_val = float(s.iloc[-1 - lookback_obs])
        if old_val != 0:
            chg = (last_val / old_val) - 1.0
    return last_val, chg, last_date.strftime("%Y-%m-%d")


def latest_and_4w_change_bp(s: pd.Series) -> Tuple[Optional[float], Optional[float], Optional[str]]:
    if s.empty:
        return None, None, None
    last_date = s.index[-1]
    last_val = float(s.iloc[-1])
    base_date = last_date - timedelta(days=28)
    old = s.loc[s.index <= base_date]
    old_val = float(old.iloc[-1]) if not old.empty else float(s.iloc[0])
    return last_val, (last_val - old_val) * 100.0, last_date.strftime("%Y-%m-%d")


# =========================
# PRICES (yfinance + stooq fallback for US stocks/ETFs)
# =========================

def fetch_yf_ohlcv(ticker: str) -> pd.DataFrame:
    df = yf.download(
        ticker,
        period="2y",
        interval="1d",
        progress=False,
        auto_adjust=False,
        threads=False,
    )
    if df.empty:
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

    df.index = pd.to_datetime(df.index)
    return df.sort_index()


def fetch_stooq_ohlcv(ticker: str) -> pd.DataFrame:
    # stooq uses "ticker.us" for US-listed stocks/ETFs
    url = f"https://stooq.com/q/d/l/?s={ticker.lower()}.us&i=d"
    res = requests.get(url, timeout=20)
    res.raise_for_status()
    df = pd.read_csv(io.StringIO(res.text))
    if "Date" not in df.columns:
        return pd.DataFrame()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.set_index("Date").sort_index()

    # stooq typical columns: Open, High, Low, Close, Volume
    for c in ["Close", "Volume"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    cols = [c for c in ["Close", "Volume"] if c in df.columns]
    return df[cols].dropna(how="all")


def fetch_ohlcv(ticker: str, warnings: List[str]) -> pd.DataFrame:
    # yfinance-only tickers (FX / futures)
    if ticker in YF_ONLY:
        try:
            df = fetch_yf_ohlcv(ticker)
            if df.empty:
                warnings.append(f"{ticker}: yfinance returned empty.")
            return df
        except Exception as e:
            warnings.append(f"{ticker}: yfinance failed ({e}).")
            return pd.DataFrame()

    # normal path: yfinance -> stooq fallback
    try:
        df = fetch_yf_ohlcv(ticker)
        if len(df) >= 120:
            return df
        warnings.append(f"{ticker}: yfinance insufficient history ({len(df)} rows), fallback to Stooq.")
    except Exception as e:
        warnings.append(f"{ticker}: yfinance failed ({e}), fallback to Stooq.")

    try:
        df2 = fetch_stooq_ohlcv(ticker)
        if df2.empty:
            warnings.append(f"{ticker}: Stooq returned empty.")
        return df2
    except Exception as e:
        warnings.append(f"{ticker}: Stooq failed ({e}).")
        return pd.DataFrame()


def extract_close(df: pd.DataFrame) -> pd.Series:
    if df is None or df.empty:
        return pd.Series(dtype=float)
    if "Adj Close" in df.columns:
        s = df["Adj Close"]
    elif "Close" in df.columns:
        s = df["Close"]
    else:
        return pd.Series(dtype=float)
    s = pd.to_numeric(s, errors="coerce").dropna()
    s.index = pd.to_datetime(s.index)
    return s.sort_index()


def extract_volume(df: pd.DataFrame) -> pd.Series:
    if df is None or df.empty or "Volume" not in df.columns:
        return pd.Series(dtype=float)
    s = pd.to_numeric(df["Volume"], errors="coerce").dropna()
    s.index = pd.to_datetime(s.index)
    return s.sort_index()


# =========================
# METRICS
# =========================

def trend_metrics(s: pd.Series) -> TrendMetrics:
    if s.empty:
        return TrendMetrics(None, None, None, None, None, None, None, None, None)

    s = s.dropna().sort_index()
    close = float(s.iloc[-1])

    ma20 = float(s.rolling(20).mean().iloc[-1]) if len(s) >= 20 else None
    ma60 = float(s.rolling(60).mean().iloc[-1]) if len(s) >= 60 else None
    ma200 = float(s.rolling(200).mean().iloc[-1]) if len(s) >= 200 else None

    gap20 = (close / ma20 - 1.0) if (ma20 not in (None, 0)) else None
    gap60 = (close / ma60 - 1.0) if (ma60 not in (None, 0)) else None

    ret5d = float(s.pct_change(5).iloc[-1]) if len(s) >= 6 else None

    high20 = float(s.rolling(20).max().iloc[-1]) if len(s) >= 20 else None
    low20 = float(s.rolling(20).min().iloc[-1]) if len(s) >= 20 else None

    return TrendMetrics(close, ma20, ma60, ma200, gap20, gap60, ret5d, high20, low20)


def volume_metrics(v: pd.Series) -> VolumeMetrics:
    if v.empty or len(v) < 20:
        return VolumeMetrics(None, None, None)
    v = v.dropna().sort_index()
    vol = float(v.iloc[-1])
    ma20 = float(v.rolling(20).mean().iloc[-1])
    ratio = (vol / ma20) if ma20 != 0 else None
    return VolumeMetrics(vol, ma20, ratio)


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


def choose_more_recent(a: pd.Series, b: pd.Series) -> Tuple[pd.Series, str]:
    """
    Returns (chosen_series, source_label)
    If both exist, chooses the one with more recent last date.
    """
    a_ok = (a is not None) and (not a.empty)
    b_ok = (b is not None) and (not b.empty)
    if not a_ok and not b_ok:
        return pd.Series(dtype=float), "N/A"
    if a_ok and not b_ok:
        return a, "PRIMARY"
    if b_ok and not a_ok:
        return b, "BACKUP"
    # both ok
    return (a, "PRIMARY") if a.index[-1] >= b.index[-1] else (b, "BACKUP")


# =========================
# MAIN
# =========================

def main() -> None:
    now = datetime.now(timezone.utc)
    warnings: List[str] = []
    prev = load_previous()

    # ---- fetch FRED ----
    fred_series: Dict[str, pd.Series] = {}
    macro: Dict[str, Dict[str, Optional[float]]] = {}

    SPREAD_SERIES = {"BAMLH0A0HYM2", "BAMLC0A0CM"}
    for sid in FRED_SERIES:
        try:
            s = fetch_fred_series(sid)
            fred_series[sid] = s
            latest, chg5d, d = latest_and_change(s, lookback_obs=5)
            chg4w_bp = None
            if sid in SPREAD_SERIES:
                _, chg4w_bp, _ = latest_and_4w_change_bp(s)
        except Exception as e:
            warnings.append(f"FRED {sid} failed ({e}), using cached values if available.")
            cached = prev.get("macro", {}).get(sid, {})
            latest, chg5d, d = cached.get("latest"), cached.get("change_5d_pct"), cached.get("latest_date")
            chg4w_bp = cached.get("change_4w_bp")

        macro[sid] = {
            "latest": safe_num(latest, 4),
            "change_5d_pct": safe_num(chg5d, 6),
            "change_4w_bp": safe_num(chg4w_bp, 2),
            "latest_date": d,
        }

    # ---- fetch prices ----
    close_series: Dict[str, pd.Series] = {}
    vol_series: Dict[str, pd.Series] = {}
    price_meta: Dict[str, Dict[str, Optional[float]]] = {}

    for t in PRICE_TICKERS:
        df = fetch_ohlcv(t, warnings)
        s_close = extract_close(df)
        s_vol = extract_volume(df)

        # fallback: cached last close/vol (does not rebuild history, but keeps reporting alive)
        if s_close.empty:
            cached = prev.get("prices", {}).get(t, {})
            c = cached.get("close")
            d = cached.get("latest_date")
            if c is not None and d is not None:
                s_close = pd.Series([float(c)], index=pd.to_datetime([d]))
                warnings.append(f"{t}: using cached close only (no history).")

        close_series[t] = s_close
        vol_series[t] = s_vol

        price_meta[t] = {
            "close": safe_num(float(s_close.iloc[-1]), 4) if not s_close.empty else None,
            "latest_date": s_close.index[-1].strftime("%Y-%m-%d") if not s_close.empty else None,
        }
        if not s_vol.empty:
            price_meta[t]["volume"] = safe_num(float(s_vol.iloc[-1]), 2)
        else:
            price_meta[t]["volume"] = None

    # ---- choose reference oil/gas series ----
    wti_primary = close_series.get("CL=F", pd.Series(dtype=float))
    wti_backup = fred_series.get("DCOILWTICO", pd.Series(dtype=float))
    wti_ref, wti_src_flag = choose_more_recent(wti_primary, wti_backup)
    wti_src = "CL=F" if wti_src_flag == "PRIMARY" else "DCOILWTICO"

    brent_primary = close_series.get("BZ=F", pd.Series(dtype=float))
    brent_backup = fred_series.get("DCOILBRENTEU", pd.Series(dtype=float))
    brent_ref, brent_src_flag = choose_more_recent(brent_primary, brent_backup)
    brent_src = "BZ=F" if brent_src_flag == "PRIMARY" else "DCOILBRENTEU"

    gas_primary = close_series.get("NG=F", pd.Series(dtype=float))
    gas_backup = fred_series.get("DHHNGSP", pd.Series(dtype=float))
    gas_ref, gas_src_flag = choose_more_recent(gas_primary, gas_backup)
    gas_src = "NG=F" if gas_src_flag == "PRIMARY" else "DHHNGSP"

    wti_tm = trend_metrics(wti_ref)
    brent_tm = trend_metrics(brent_ref)
    gas_tm = trend_metrics(gas_ref)

    spread_brent_wti = (brent_tm.close - wti_tm.close) if (brent_tm.close is not None and wti_tm.close is not None) else None
    tier = oil_tier(brent_tm.close)

    # ---- macro gates ----
    vix = macro.get("VIXCLS", {}).get("latest")
    ovx = macro.get("OVXCLS", {}).get("latest")
    ovx_5d = macro.get("OVXCLS", {}).get("change_5d_pct")
    hy_4w_bp = macro.get("BAMLH0A0HYM2", {}).get("change_4w_bp")
    dxy_5d = macro.get("DTWEXBGS", {}).get("change_5d_pct")

    ovx_ok = (ovx is not None and ovx < TH["OVX_MAX"]) or (ovx_5d is not None and ovx_5d <= 0)

    risk_ok_strict = (
        vix is not None and vix < TH["VIX_MAX_STRICT"]
        and hy_4w_bp is not None and hy_4w_bp < TH["HY_4W_BP_MAX_STRICT"]
        and dxy_5d is not None and dxy_5d < TH["DXY_5D_MAX_STRICT"]
        and ovx_ok
    )
    risk_ok_soft = (
        vix is not None and vix < TH["VIX_MAX_SOFT"]
        and hy_4w_bp is not None and hy_4w_bp < TH["HY_4W_BP_MAX_SOFT"]
        and dxy_5d is not None and dxy_5d < TH["DXY_5D_MAX_SOFT"]
    )

    wti_trend_up = (wti_tm.close is not None and wti_tm.ma20 is not None and wti_tm.ma60 is not None
                    and (wti_tm.close > wti_tm.ma20) and (wti_tm.ma20 > wti_tm.ma60))
    brent_trend_up = (brent_tm.close is not None and brent_tm.ma20 is not None and brent_tm.ma60 is not None
                      and (brent_tm.close > brent_tm.ma20) and (brent_tm.ma20 > brent_tm.ma60))
    oil_trend_up = wti_trend_up or brent_trend_up

    # Brazil gate (PBR)
    vxewz = macro.get("VXEWZCLS", {}).get("latest")
    vxewz_5d = macro.get("VXEWZCLS", {}).get("change_5d_pct")
    brl_tm = trend_metrics(close_series.get("BRL=X", pd.Series(dtype=float)))
    brl_ok = (brl_tm.ret5d is not None and brl_tm.ret5d > TH["BRL_5D_MIN"])
    brazil_risk_ok = (
        vxewz is not None and vxewz < TH["VXEWZ_MAX"]
        and vxewz_5d is not None and vxewz_5d <= 0
        and brl_ok
    )

    # ---- per stock metrics ----
    def get_cached_metrics(ticker: str) -> Dict:
        return prev.get("signals", {}).get(ticker, {})

    def tm_or_cache(ticker: str, tm: TrendMetrics) -> TrendMetrics:
        if tm.close is not None and (tm.ma20 is not None or tm.ma60 is not None):
            return tm
        c = get_cached_metrics(ticker).get("trend", {})
        if not c:
            return tm
        warnings.append(f"{ticker}: trend metrics using cache.")
        return TrendMetrics(
            c.get("close"), c.get("ma20"), c.get("ma60"), c.get("ma200"),
            c.get("gap20"), c.get("gap60"), c.get("ret5d"), c.get("high20"), c.get("low20")
        )

    def rm_or_cache(ticker: str, rm: RatioMetrics) -> RatioMetrics:
        if rm.ratio is not None and rm.ma60 is not None:
            return rm
        c = get_cached_metrics(ticker).get("ratio", {})
        if not c:
            return rm
        warnings.append(f"{ticker}: ratio metrics using cache.")
        return RatioMetrics(c.get("ratio"), c.get("ma60"), c.get("gap"), c.get("slope_proxy"))

    def vm_or_cache(ticker: str, vm: VolumeMetrics) -> VolumeMetrics:
        if vm.vol is not None and vm.ma20 is not None:
            return vm
        c = get_cached_metrics(ticker).get("volume", {})
        if not c:
            return vm
        warnings.append(f"{ticker}: volume metrics using cache.")
        return VolumeMetrics(c.get("vol"), c.get("ma20"), c.get("ratio"))

    # Build metrics
    tm_stock: Dict[str, TrendMetrics] = {}
    vm_stock: Dict[str, VolumeMetrics] = {}

    for t in ["PBR", "OXY", "VG", "RIG", "XLE", "OIH", "EWZ", "LNG"]:
        tm_stock[t] = tm_or_cache(t, trend_metrics(close_series.get(t, pd.Series(dtype=float))))
        vm_stock[t] = vm_or_cache(t, volume_metrics(vol_series.get(t, pd.Series(dtype=float))))

    # Relative ratios
    oxy_rm = rm_or_cache("OXY", ratio_metrics(close_series.get("OXY", pd.Series(dtype=float)), close_series.get("XLE", pd.Series(dtype=float))))
    pbr_rm = rm_or_cache("PBR", ratio_metrics(close_series.get("PBR", pd.Series(dtype=float)), close_series.get("EWZ", pd.Series(dtype=float))))
    rig_rm = rm_or_cache("RIG", ratio_metrics(close_series.get("RIG", pd.Series(dtype=float)), close_series.get("OIH", pd.Series(dtype=float))))
    vg_rm  = rm_or_cache("VG",  ratio_metrics(close_series.get("VG", pd.Series(dtype=float)),  close_series.get("LNG", pd.Series(dtype=float))))

    # ---- Entry rules ----
    # OXY
    oxy_trend_up = (tm_stock["OXY"].close is not None and tm_stock["OXY"].ma20 is not None and tm_stock["OXY"].ma60 is not None
                    and tm_stock["OXY"].close > tm_stock["OXY"].ma20 and tm_stock["OXY"].ma20 > tm_stock["OXY"].ma60)
    oxy_pullback_ok = (tm_stock["OXY"].gap20 is not None
                       and TH["PULLBACK_GAP20_MIN"] <= tm_stock["OXY"].gap20 <= TH["PULLBACK_GAP20_MAX"])
    oxy_relative_ok = (oxy_rm.gap is not None and oxy_rm.slope_proxy is not None
                       and oxy_rm.gap <= TH["REL_GAP_MAX_OXY"] and oxy_rm.slope_proxy > 0)
    oxy_entry = (risk_ok_strict and wti_trend_up and oxy_trend_up and oxy_pullback_ok and oxy_relative_ok)

    # PBR
    pbr_trend_ok = (tm_stock["PBR"].close is not None and tm_stock["PBR"].ma60 is not None and tm_stock["PBR"].ma200 is not None
                    and tm_stock["PBR"].close > tm_stock["PBR"].ma60 and tm_stock["PBR"].ma60 > tm_stock["PBR"].ma200)
    pbr_pullback_ok = (tm_stock["PBR"].gap60 is not None
                       and TH["PULLBACK_GAP60_MIN"] <= tm_stock["PBR"].gap60 <= TH["PULLBACK_GAP60_MAX"])
    pbr_relative_ok = (pbr_rm.gap is not None and pbr_rm.slope_proxy is not None
                       and pbr_rm.gap <= TH["REL_GAP_MAX_PBR"] and pbr_rm.slope_proxy > 0)
    pbr_entry = (risk_ok_soft and brent_trend_up and brazil_risk_ok and pbr_trend_ok and pbr_pullback_ok and pbr_relative_ok)

    # RIG
    oih_trend_up = (tm_stock["OIH"].close is not None and tm_stock["OIH"].ma20 is not None and tm_stock["OIH"].ma60 is not None
                    and tm_stock["OIH"].close > tm_stock["OIH"].ma20 and tm_stock["OIH"].ma20 > tm_stock["OIH"].ma60)
    rig_breakout = (tm_stock["RIG"].close is not None and tm_stock["RIG"].high20 is not None
                    and tm_stock["RIG"].close >= tm_stock["RIG"].high20)
    rig_volume_confirm = (vm_stock["RIG"].ratio is not None and vm_stock["RIG"].ratio >= TH["VOL_RATIO_MIN"])
    rig_relative_ok = (rig_rm.gap is not None and rig_rm.slope_proxy is not None
                       and rig_rm.slope_proxy > 0 and rig_rm.gap <= TH["REL_GAP_MAX_RIG"])
    rig_entry = (risk_ok_strict and oil_trend_up and oih_trend_up and rig_breakout and rig_volume_confirm and rig_relative_ok)

    # VG
    lng_peer_trend_up = (tm_stock["LNG"].close is not None and tm_stock["LNG"].ma20 is not None and tm_stock["LNG"].ma60 is not None
                         and tm_stock["LNG"].close > tm_stock["LNG"].ma20 and tm_stock["LNG"].ma20 > tm_stock["LNG"].ma60)
    vg_trend_up = (tm_stock["VG"].close is not None and tm_stock["VG"].ma20 is not None and tm_stock["VG"].ma60 is not None
                   and tm_stock["VG"].close > tm_stock["VG"].ma20 and tm_stock["VG"].ma20 > tm_stock["VG"].ma60)
    vg_relative_turn_up = (vg_rm.gap is not None and vg_rm.slope_proxy is not None
                           and TH["REL_GAP_BAND_VG_MIN"] <= vg_rm.gap <= TH["REL_GAP_BAND_VG_MAX"]
                           and vg_rm.slope_proxy > 0)
    vg_not_extended = (tm_stock["VG"].gap20 is not None and tm_stock["VG"].gap20 <= 0.05)
    vg_entry = (risk_ok_strict and lng_peer_trend_up and vg_trend_up and vg_relative_turn_up and vg_not_extended)

    # ---- verdict ----
    entries = []
    if oxy_entry:
        entries.append("OXY")
    if pbr_entry:
        entries.append("PBR")
    if vg_entry:
        entries.append("VG")
    if rig_entry:
        entries.append("RIG")

    verdict = "⏸ No entry today" if not entries else f"✅ Entry condition met: {', '.join(entries)}"

    # ---- output JSON ----
    out = {
        "generated_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "as_of": {
            "run_time_utc": now.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "data_warning": bool(warnings),
        "warnings": warnings,

        "macro": macro,

        "commodity_refs": {
            "WTI": {
                "source": wti_src,
                "close": safe_num(wti_tm.close, 4),
                "ret5d": safe_num(wti_tm.ret5d, 6),
            },
            "Brent": {
                "source": brent_src,
                "close": safe_num(brent_tm.close, 4),
                "ret5d": safe_num(brent_tm.ret5d, 6),
                "tier": tier,
            },
            "HenryHub_or_NG": {
                "source": gas_src,
                "close": safe_num(gas_tm.close, 4),
                "ret5d": safe_num(gas_tm.ret5d, 6),
            },
            "Brent_WTI_spread": safe_num(spread_brent_wti, 4),
        },

        "gates": {
            "RISK_OK_STRICT": risk_ok_strict,
            "RISK_OK_SOFT": risk_ok_soft,
            "OVX_OK": ovx_ok,
            "WTI_TREND_UP": wti_trend_up,
            "BRENT_TREND_UP": brent_trend_up,
            "OIL_TREND_UP": oil_trend_up,
            "BRAZIL_RISK_OK": brazil_risk_ok,
        },

        "prices": price_meta,

        "signals": {
            "OXY": {
                "trend": {k: safe_num(getattr(tm_stock["OXY"], k), 6) for k in tm_stock["OXY"].__dataclass_fields__.keys()},
                "ratio": {"ratio": safe_num(oxy_rm.ratio), "ma60": safe_num(oxy_rm.ma60), "gap": safe_num(oxy_rm.gap), "slope_proxy": safe_num(oxy_rm.slope_proxy)},
                "volume": {"vol": safe_num(vm_stock["OXY"].vol), "ma20": safe_num(vm_stock["OXY"].ma20), "ratio": safe_num(vm_stock["OXY"].ratio)},
                "checks": {
                    "RISK_OK_STRICT": risk_ok_strict,
                    "WTI_TREND_UP": wti_trend_up,
                    "OXY_TREND_UP": oxy_trend_up,
                    "OXY_PULLBACK_OK": oxy_pullback_ok,
                    "OXY_RELATIVE_OK": oxy_relative_ok,
                },
                "entry": bool(oxy_entry),
            },
            "PBR": {
                "trend": {k: safe_num(getattr(tm_stock["PBR"], k), 6) for k in tm_stock["PBR"].__dataclass_fields__.keys()},
                "ratio": {"ratio": safe_num(pbr_rm.ratio), "ma60": safe_num(pbr_rm.ma60), "gap": safe_num(pbr_rm.gap), "slope_proxy": safe_num(pbr_rm.slope_proxy)},
                "volume": {"vol": safe_num(vm_stock["PBR"].vol), "ma20": safe_num(vm_stock["PBR"].ma20), "ratio": safe_num(vm_stock["PBR"].ratio)},
                "checks": {
                    "RISK_OK_SOFT": risk_ok_soft,
                    "BRENT_TREND_UP": brent_trend_up,
                    "BRAZIL_RISK_OK": brazil_risk_ok,
                    "PBR_TREND_OK": pbr_trend_ok,
                    "PBR_PULLBACK_OK": pbr_pullback_ok,
                    "PBR_RELATIVE_OK": pbr_relative_ok,
                },
                "entry": bool(pbr_entry),
            },
            "RIG": {
                "trend": {k: safe_num(getattr(tm_stock["RIG"], k), 6) for k in tm_stock["RIG"].__dataclass_fields__.keys()},
                "ratio": {"ratio": safe_num(rig_rm.ratio), "ma60": safe_num(rig_rm.ma60), "gap": safe_num(rig_rm.gap), "slope_proxy": safe_num(rig_rm.slope_proxy)},
                "volume": {"vol": safe_num(vm_stock["RIG"].vol), "ma20": safe_num(vm_stock["RIG"].ma20), "ratio": safe_num(vm_stock["RIG"].ratio)},
                "checks": {
                    "RISK_OK_STRICT": risk_ok_strict,
                    "OIL_TREND_UP": oil_trend_up,
                    "OIH_TREND_UP": oih_trend_up,
                    "RIG_BREAKOUT": rig_breakout,
                    "RIG_VOLUME_CONFIRM": rig_volume_confirm,
                    "RIG_RELATIVE_OK": rig_relative_ok,
                },
                "entry": bool(rig_entry),
            },
            "VG": {
                "trend": {k: safe_num(getattr(tm_stock["VG"], k), 6) for k in tm_stock["VG"].__dataclass_fields__.keys()},
                "ratio": {"ratio": safe_num(vg_rm.ratio), "ma60": safe_num(vg_rm.ma60), "gap": safe_num(vg_rm.gap), "slope_proxy": safe_num(vg_rm.slope_proxy)},
                "volume": {"vol": safe_num(vm_stock["VG"].vol), "ma20": safe_num(vm_stock["VG"].ma20), "ratio": safe_num(vm_stock["VG"].ratio)},
                "checks": {
                    "RISK_OK_STRICT": risk_ok_strict,
                    "LNG_PEER_TREND_UP": lng_peer_trend_up,
                    "VG_TREND_UP": vg_trend_up,
                    "VG_RELATIVE_TURN_UP": vg_relative_turn_up,
                    "VG_NOT_EXTENDED": vg_not_extended,
                },
                "entry": bool(vg_entry),
            },
        },

        "verdict": verdict,
    }

    OUTPUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- output MD ----
    lines = []
    lines += ["# Energy Daily Signal Monitor", ""]
    lines += [f"- 실행시간(UTC): **{out['as_of']['run_time_utc']}**", ""]
    if out["data_warning"]:
        lines += ["## ⚠️ DATA WARNING", ""]
        lines += [f"- {w}" for w in warnings]
        lines += [""]

    # Commodity refs
    lines += ["## Commodity Regime", ""]
    lines += [
        f"- WTI ref ({out['commodity_refs']['WTI']['source']}): {fmt(out['commodity_refs']['WTI']['close'])} / 5D {pct(out['commodity_refs']['WTI']['ret5d'])}",
        f"- Brent ref ({out['commodity_refs']['Brent']['source']}): {fmt(out['commodity_refs']['Brent']['close'])} / 5D {pct(out['commodity_refs']['Brent']['ret5d'])}",
        f"- Brent Tier: **{out['commodity_refs']['Brent']['tier']}**",
        f"- Brent-WTI spread: {fmt(out['commodity_refs']['Brent_WTI_spread'])}",
        f"- Gas ref ({out['commodity_refs']['HenryHub_or_NG']['source']}): {fmt(out['commodity_refs']['HenryHub_or_NG']['close'])} / 5D {pct(out['commodity_refs']['HenryHub_or_NG']['ret5d'])}",
        "",
    ]

    # Gates
    lines += ["## Gates", ""]
    for k, v in out["gates"].items():
        lines += [f"- **{k}**: **{v}**"]
    lines += [""]

    # Per-stock
    def stock_block(t: str) -> List[str]:
        s = out["signals"][t]
        tm = s["trend"]
        rm = s["ratio"]
        vm = s["volume"]
        blk = []
        blk += [f"## {t}", ""]
        blk += [f"- **ENTRY**: **{s['entry']}**", ""]
        blk += ["### Trend", ""]
        blk += [
            f"- close: {fmt(tm.get('close'))}",
            f"- MA20 / MA60 / MA200: {fmt(tm.get('ma20'))} / {fmt(tm.get('ma60'))} / {fmt(tm.get('ma200'))}",
            f"- gap20 / gap60: {pct(tm.get('gap20'))} / {pct(tm.get('gap60'))}",
            f"- 5D return: {pct(tm.get('ret5d'))}",
            f"- 20D high/low: {fmt(tm.get('high20'))} / {fmt(tm.get('low20'))}",
            "",
        ]
        blk += ["### Relative Strength", ""]
        blk += [
            f"- ratio: {fmt(rm.get('ratio'), 6)}",
            f"- ratio_MA60: {fmt(rm.get('ma60'), 6)}",
            f"- ratio_gap: {pct(rm.get('gap'))}",
            f"- ratio_slope_proxy(20d): {fmt(rm.get('slope_proxy'), 6)}",
            "",
        ]
        blk += ["### Volume (if available)", ""]
        blk += [
            f"- volume: {fmt(vm.get('vol'))}",
            f"- volume_MA20: {fmt(vm.get('ma20'))}",
            f"- volume_ratio: {fmt(vm.get('ratio'))}",
            "",
        ]
        blk += ["### Checks", ""]
        for ck, cv in s["checks"].items():
            blk += [f"- {ck}: **{cv}**"]
        blk += [""]
        return blk

    for t in ["OXY", "PBR", "RIG", "VG"]:
        lines += stock_block(t)

    lines += ["## Verdict", "", out["verdict"], ""]
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
