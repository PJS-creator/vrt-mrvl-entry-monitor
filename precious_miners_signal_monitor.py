from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import pandas as pd
import requests
import yfinance as yf


OUT_JSON = Path("latest_precious_miners_signal.json")
OUT_MD = Path("latest_precious_miners_signal.md")

# ------------------------------------------------------------
# Static strategy map
# ------------------------------------------------------------
# The scores below are NOT price targets. They are a static checklist score from
# the strategy we built together: production growth, current margin/FCF, M&A
# attractiveness, jurisdiction quality, and known project/permit/security risk.
# Daily prices then decide whether the market is giving an actionable entry.

ASSETS: dict[str, dict[str, Any]] = {
    # Gold miners / developers
    "MAKO": {
        "name": "Mako Mining",
        "group": "gold",
        "tickers": ["MAKO"],
        "benchmark": "GDXJ",
        "static_rank": 1,
        "fundamental_score": 88,
        "risk_tier": "Medium-High",
        "max_signal": "ENTRY",
        "style": "생산+성장 핵심 알파",
        "why": "San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.",
        "watch": "Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.",
    },
    "JAG.TO": {
        "name": "Jaguar Mining",
        "group": "gold",
        "tickers": ["JAG.TO"],
        "benchmark": "GDXJ",
        "static_rank": 2,
        "fundamental_score": 82,
        "risk_tier": "Medium",
        "max_signal": "ENTRY",
        "style": "저평가 FCF/램프업 후보",
        "why": "Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.",
        "watch": "Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.",
    },
    "TSK.TO": {
        "name": "Talisker Resources",
        "group": "gold",
        "tickers": ["TSK.TO"],
        "benchmark": "GDXJ",
        "static_rank": 3,
        "fundamental_score": 70,
        "risk_tier": "Medium",
        "max_signal": "WATCH",
        "style": "BC 고품위 M&A 콜옵션",
        "why": "Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.",
        "watch": "PEA economics, AISC 공개, inferred→indicated 전환.",
    },
    "ORV.TO": {
        "name": "Orvana Minerals",
        "group": "gold",
        "tickers": ["ORV.TO"],
        "benchmark": "GDXJ",
        "static_rank": 4,
        "fundamental_score": 55,
        "risk_tier": "High",
        "max_signal": "WATCH",
        "style": "고위험 턴어라운드",
        "why": "금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.",
        "watch": "Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.",
    },

    # Silver miners / developers
    "AYA": {
        "name": "Aya Gold & Silver",
        "group": "silver",
        "tickers": ["AYA", "AYA.TO"],
        "benchmark": "SILJ",
        "static_rank": 1,
        "fundamental_score": 86,
        "risk_tier": "Medium",
        "max_signal": "ENTRY",
        "style": "품질형 은광 코어",
        "why": "Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.",
        "watch": "Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.",
    },
    "EXK": {
        "name": "Endeavour Silver",
        "group": "silver",
        "tickers": ["EXK"],
        "benchmark": "SILJ",
        "static_rank": 2,
        "fundamental_score": 82,
        "risk_tier": "Medium",
        "max_signal": "ENTRY",
        "style": "밸류/베타 균형형 은광",
        "why": "8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.",
        "watch": "Terronera 램프업, AISC, 멕시코/페루 운영 리스크.",
    },
    "SCZM": {
        "name": "Santacruz Silver",
        "group": "silver",
        "tickers": ["SCZM", "SCZ.V", "SCZMF"],
        "benchmark": "SILJ",
        "static_rank": 3,
        "fundamental_score": 74,
        "risk_tier": "High",
        "max_signal": "ENTRY",
        "style": "공격형 은 가격 레버리지",
        "why": "볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.",
        "watch": "Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.",
    },
    "HL": {
        "name": "Hecla Mining",
        "group": "silver",
        "tickers": ["HL"],
        "benchmark": "SILJ",
        "static_rank": 4,
        "fundamental_score": 78,
        "risk_tier": "Low-Medium",
        "max_signal": "ENTRY",
        "style": "방어형 은광 코어",
        "why": "북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.",
        "watch": "은 가격 대비 상대강도, 비용 인플레이션.",
    },
    "USAS": {
        "name": "Americas Gold and Silver",
        "group": "silver",
        "tickers": ["USAS"],
        "benchmark": "SILJ",
        "static_rank": 5,
        "fundamental_score": 68,
        "risk_tier": "Medium-High",
        "max_signal": "ENTRY",
        "style": "고품위 북미/antimony 옵션",
        "why": "Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.",
        "watch": "AISC $30~35, capex, Idaho 생산 확대.",
    },
    "ASM": {
        "name": "Avino Silver & Gold",
        "group": "silver",
        "tickers": ["ASM"],
        "benchmark": "SILJ",
        "static_rank": 6,
        "fundamental_score": 60,
        "risk_tier": "Medium",
        "max_signal": "ENTRY",
        "style": "재무 안정형 소형 은광",
        "why": "재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.",
        "watch": "La Preciosa 개발 속도, 생산량 회복.",
    },
    "VZLA": {
        "name": "Vizsla Silver",
        "group": "silver",
        "tickers": ["VZLA"],
        "benchmark": "SILJ",
        "static_rank": 7,
        "fundamental_score": 72,
        "risk_tier": "Very High",
        "max_signal": "WATCH",
        "style": "최고 명목 업사이드 / 보안 리스크",
        "why": "Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.",
        "watch": "MIA 허가, 보안계획, 현장 정상화, financing.",
    },
    "HYMC": {
        "name": "Hycroft Mining",
        "group": "silver",
        "tickers": ["HYMC"],
        "benchmark": "SILJ",
        "static_rank": 8,
        "fundamental_score": 42,
        "risk_tier": "Very High",
        "max_signal": "WATCH",
        "style": "네바다 대형 자원 옵션",
        "why": "생산주가 아니라 PEA/공정 선택 전 개발 옵션.",
        "watch": "PEA, 공정 선택, capex, 회수율.",
    },
}

MARKET_TICKERS = {
    "GC=F": ["GC=F"],
    "SI=F": ["SI=F"],
    "GLD": ["GLD"],
    "SLV": ["SLV"],
    "GDX": ["GDX"],
    "GDXJ": ["GDXJ"],
    "SILJ": ["SILJ"],
}

GOLD_BREADTH = ["GDX", "GDXJ", "AEM", "NEM", "WPM", "FNV", "KGC", "AGI", "AU", "GFI", "HMY", "BTG", "EQX"]
SILVER_BREADTH = ["SILJ", "SLV", "AYA", "EXK", "SCZM", "HL", "USAS", "ASM", "VZLA", "HYMC", "PAAS", "AG", "FSM"]


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def now_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def fmt_num(x: Any, digits: int = 2) -> str:
    if x is None:
        return "N/A"
    try:
        if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
            return "N/A"
        return f"{float(x):,.{digits}f}"
    except Exception:
        return "N/A"


def fmt_pct(x: Any, digits: int = 2) -> str:
    if x is None:
        return "N/A"
    try:
        if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
            return "N/A"
        return f"{float(x):,.{digits}f}%"
    except Exception:
        return "N/A"


def safe_float(x: Any) -> float | None:
    try:
        v = float(x)
        if math.isnan(v) or math.isinf(v):
            return None
        return v
    except Exception:
        return None


def first_existing_history(aliases: list[str], period: str = "18mo") -> tuple[str | None, pd.DataFrame]:
    """Return the first yfinance history that has enough data."""
    last_err: str | None = None
    for ticker in aliases:
        try:
            df = yf.download(
                ticker,
                period=period,
                interval="1d",
                progress=False,
                auto_adjust=False,
                threads=False,
            )
            if df is None or df.empty:
                continue
            # yfinance can return MultiIndex even for one ticker in some versions.
            if isinstance(df.columns, pd.MultiIndex):
                # If columns are (Price, Ticker), drop ticker level. If reverse, try both.
                if ticker in df.columns.get_level_values(-1):
                    df = df.xs(ticker, axis=1, level=-1)
                elif ticker in df.columns.get_level_values(0):
                    df = df.xs(ticker, axis=1, level=0)
            df = df.dropna(subset=["Close"])
            if len(df) >= 60:
                return ticker, df
        except Exception as e:
            last_err = str(e)
            continue
    return None, pd.DataFrame()


def rsi(series: pd.Series, window: int = 14) -> float | None:
    s = series.dropna()
    if len(s) < window + 2:
        return None
    delta = s.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain / avg_loss.replace(0, pd.NA)
    out = 100 - (100 / (1 + rs))
    return safe_float(out.iloc[-1])


def atr_pct(df: pd.DataFrame, window: int = 14) -> float | None:
    if len(df) < window + 2 or not all(c in df.columns for c in ["High", "Low", "Close"]):
        return None
    high = df["High"]
    low = df["Low"]
    close = df["Close"]
    tr = pd.concat(
        [
            (high - low),
            (high - close.shift()).abs(),
            (low - close.shift()).abs(),
        ],
        axis=1,
    ).max(axis=1)
    atr = tr.rolling(window).mean().iloc[-1]
    last = close.iloc[-1]
    if not last:
        return None
    return safe_float(atr / last * 100)


def slope_proxy(series: pd.Series, window: int = 20) -> float | None:
    s = series.dropna()
    if len(s) < window + 1:
        return None
    base = s.iloc[-window]
    if base == 0:
        return None
    return safe_float((s.iloc[-1] / base) - 1)


def price_metrics(df: pd.DataFrame) -> dict[str, Any]:
    close = df["Close"].dropna()
    if close.empty:
        return {"ok": False}

    volume = df["Volume"] if "Volume" in df.columns else pd.Series(dtype=float)
    ma20 = close.rolling(20).mean().iloc[-1] if len(close) >= 20 else None
    ma50 = close.rolling(50).mean().iloc[-1] if len(close) >= 50 else None
    ma60 = close.rolling(60).mean().iloc[-1] if len(close) >= 60 else None
    ma200 = close.rolling(200).mean().iloc[-1] if len(close) >= 200 else None
    last = close.iloc[-1]

    high20 = close.tail(20).max() if len(close) >= 20 else None
    low20 = close.tail(20).min() if len(close) >= 20 else None
    ret5 = (last / close.iloc[-6] - 1) * 100 if len(close) >= 6 and close.iloc[-6] else None
    drawdown20 = (last / high20 - 1) * 100 if high20 else None

    vol_last = volume.dropna().iloc[-1] if len(volume.dropna()) else None
    vol_ma20 = volume.dropna().rolling(20).mean().iloc[-1] if len(volume.dropna()) >= 20 else None
    vol_ratio = vol_last / vol_ma20 if vol_last is not None and vol_ma20 not in [None, 0] else None

    return {
        "ok": True,
        "date": str(close.index[-1].date()) if hasattr(close.index[-1], "date") else str(close.index[-1]),
        "close": safe_float(last),
        "ma20": safe_float(ma20),
        "ma50": safe_float(ma50),
        "ma60": safe_float(ma60),
        "ma200": safe_float(ma200),
        "gap20": safe_float((last / ma20 - 1) * 100) if ma20 else None,
        "gap50": safe_float((last / ma50 - 1) * 100) if ma50 else None,
        "gap200": safe_float((last / ma200 - 1) * 100) if ma200 else None,
        "rsi14": rsi(close, 14),
        "atr14_pct": atr_pct(df, 14),
        "ret5": safe_float(ret5),
        "high20": safe_float(high20),
        "low20": safe_float(low20),
        "drawdown20": safe_float(drawdown20),
        "volume": safe_float(vol_last),
        "volume_ma20": safe_float(vol_ma20),
        "volume_ratio": safe_float(vol_ratio),
        "slope20": slope_proxy(close, 20),
        "slope60": slope_proxy(close, 60),
    }


def ratio_metrics(left_df: pd.DataFrame, right_df: pd.DataFrame, ma_window: int = 60) -> dict[str, Any]:
    if left_df.empty or right_df.empty:
        return {"ok": False}
    left = left_df["Close"].dropna()
    right = right_df["Close"].dropna()
    aligned = pd.concat([left, right], axis=1, join="inner").dropna()
    if len(aligned) < ma_window + 2:
        return {"ok": False}
    ratio = aligned.iloc[:, 0] / aligned.iloc[:, 1]
    ma = ratio.rolling(ma_window).mean()
    last = ratio.iloc[-1]
    last_ma = ma.iloc[-1]
    return {
        "ok": True,
        "ratio": safe_float(last),
        "ma": safe_float(last_ma),
        "gap": safe_float((last / last_ma - 1) * 100) if last_ma else None,
        "slope_proxy": slope_proxy(ratio, 20),
    }


def fred_series(series_id: str) -> dict[str, Any]:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        from io import StringIO
        df = pd.read_csv(StringIO(r.text))
        if df.empty:
            return {"ok": False}
        date_col = df.columns[0]
        val_col = df.columns[1]
        df[val_col] = pd.to_numeric(df[val_col].replace(".", pd.NA), errors="coerce")
        df = df.dropna(subset=[val_col])
        if df.empty:
            return {"ok": False}
        latest = df.iloc[-1]
        n_back = min(20, len(df) - 1)
        prev = df.iloc[-1 - n_back]
        return {
            "ok": True,
            "date": str(latest[date_col]),
            "latest": safe_float(latest[val_col]),
            "change_approx_4w": safe_float(latest[val_col] - prev[val_col]),
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


def calc_breadth(symbols: list[str], histories: dict[str, pd.DataFrame]) -> dict[str, Any]:
    rows = []
    for sym in symbols:
        df = histories.get(sym)
        if df is None or df.empty:
            continue
        m = price_metrics(df)
        if not m.get("ok"):
            continue
        close = m.get("close")
        ma50 = m.get("ma50")
        ma200 = m.get("ma200")
        rows.append({
            "symbol": sym,
            "above50": close is not None and ma50 is not None and close > ma50,
            "above200": close is not None and ma200 is not None and close > ma200,
            "rsi_gt50": (m.get("rsi14") or 0) > 50,
        })
    if not rows:
        return {"ok": False, "count": 0}
    count = len(rows)
    return {
        "ok": True,
        "count": count,
        "pct_above50": sum(r["above50"] for r in rows) / count * 100,
        "pct_above200": sum(r["above200"] for r in rows) / count * 100,
        "pct_rsi_gt50": sum(r["rsi_gt50"] for r in rows) / count * 100,
    }


# ------------------------------------------------------------
# Main logic
# ------------------------------------------------------------

def main() -> None:
    # Collect all ticker aliases that may be needed.
    all_aliases: dict[str, list[str]] = {}
    all_aliases.update(MARKET_TICKERS)
    for key, cfg in ASSETS.items():
        all_aliases[key] = cfg["tickers"]
    for sym in sorted(set(GOLD_BREADTH + SILVER_BREADTH)):
        all_aliases.setdefault(sym, [sym])

    histories: dict[str, pd.DataFrame] = {}
    resolved_tickers: dict[str, str | None] = {}
    for logical, aliases in all_aliases.items():
        resolved, df = first_existing_history(aliases)
        resolved_tickers[logical] = resolved
        histories[logical] = df

    metrics = {k: price_metrics(v) for k, v in histories.items() if v is not None and not v.empty}

    # Macro risk / liquidity gate.
    fred_ids = {
        "HY_OAS": "BAMLH0A0HYM2",
        "IG_OAS": "BAMLC0A0CM",
        "REAL10Y": "DFII10",
        "VIX": "VIXCLS",
        "NFCI": "NFCI",
    }
    fred = {name: fred_series(sid) for name, sid in fred_ids.items()}
    hy = fred.get("HY_OAS", {})
    ig = fred.get("IG_OAS", {})
    vix = fred.get("VIX", {})
    nfci = fred.get("NFCI", {})
    real = fred.get("REAL10Y", {})

    risk_green = (
        (hy.get("latest") is None or hy.get("change_approx_4w", 0) <= 0.35 or hy.get("latest", 99) < 4.0)
        and (ig.get("latest") is None or ig.get("change_approx_4w", 0) <= 0.20 or ig.get("latest", 99) < 1.3)
        and (vix.get("latest") is None or vix.get("latest", 99) < 25)
        and (nfci.get("latest") is None or nfci.get("latest", 99) < 0.20)
    )
    real_yield_headwind = real.get("change_approx_4w") is not None and real.get("change_approx_4w") > 0.25

    # Regime checks.
    def uptrend(sym: str) -> bool:
        m = metrics.get(sym, {})
        c, ma50, ma200 = m.get("close"), m.get("ma50"), m.get("ma200")
        slope20 = m.get("slope20")
        if c is None or ma50 is None or ma200 is None:
            return False
        return (c > ma50 > ma200) or (c > ma200 and (slope20 or 0) > 0)

    gold_uptrend = uptrend("GC=F") or uptrend("GLD")
    silver_uptrend = uptrend("SI=F") or uptrend("SLV")

    gdx_gld = ratio_metrics(histories.get("GDX", pd.DataFrame()), histories.get("GLD", pd.DataFrame()))
    gdxj_gld = ratio_metrics(histories.get("GDXJ", pd.DataFrame()), histories.get("GLD", pd.DataFrame()))
    silj_slv = ratio_metrics(histories.get("SILJ", pd.DataFrame()), histories.get("SLV", pd.DataFrame()))

    gold_miners_leadership = (
        (gdx_gld.get("ok") and (gdx_gld.get("gap") or 0) > 0 and (gdx_gld.get("slope_proxy") or 0) > 0)
        or (gdxj_gld.get("ok") and (gdxj_gld.get("gap") or 0) > 0 and (gdxj_gld.get("slope_proxy") or 0) > 0)
    )
    silver_miners_leadership = silj_slv.get("ok") and (silj_slv.get("gap") or 0) > 0 and (silj_slv.get("slope_proxy") or 0) > 0

    gold_breadth = calc_breadth(GOLD_BREADTH, histories)
    silver_breadth = calc_breadth(SILVER_BREADTH, histories)
    gold_breadth_ok = gold_breadth.get("ok") and gold_breadth.get("pct_above50", 0) >= 45
    silver_breadth_ok = silver_breadth.get("ok") and silver_breadth.get("pct_above50", 0) >= 45

    regime = {
        "risk_green": risk_green,
        "real_yield_headwind": real_yield_headwind,
        "gold_uptrend": gold_uptrend,
        "silver_uptrend": silver_uptrend,
        "gold_miners_leadership": gold_miners_leadership,
        "silver_miners_leadership": silver_miners_leadership,
        "gold_breadth_ok": bool(gold_breadth_ok),
        "silver_breadth_ok": bool(silver_breadth_ok),
        "gdx_gld": gdx_gld,
        "gdxj_gld": gdxj_gld,
        "silj_slv": silj_slv,
        "gold_breadth": gold_breadth,
        "silver_breadth": silver_breadth,
        "fred": fred,
    }

    results: dict[str, dict[str, Any]] = {}
    confirmed: list[str] = []
    candidates: list[str] = []
    watch_only: list[str] = []

    for logical, cfg in ASSETS.items():
        df = histories.get(logical, pd.DataFrame())
        m = price_metrics(df) if df is not None and not df.empty else {"ok": False}
        bmk = cfg["benchmark"]
        rs = ratio_metrics(df, histories.get(bmk, pd.DataFrame())) if m.get("ok") else {"ok": False}

        group = cfg["group"]
        sector_ok = (
            risk_green
            and (gold_uptrend if group == "gold" else silver_uptrend)
            and (gold_miners_leadership if group == "gold" else silver_miners_leadership)
        )
        breadth_ok = gold_breadth_ok if group == "gold" else silver_breadth_ok

        c, ma20, ma50, ma200 = m.get("close"), m.get("ma20"), m.get("ma50"), m.get("ma200")
        rsi14 = m.get("rsi14")
        gap20 = m.get("gap20")
        trend_ok = bool(c is not None and ma50 is not None and ma200 is not None and ((c > ma50 > ma200) or (c > ma200 and (m.get("slope20") or 0) > 0)))
        rs_ok = bool(rs.get("ok") and (rs.get("gap") or 0) > 0 and (rs.get("slope_proxy") or 0) > 0)
        not_extended = bool(rsi14 is None or rsi14 < 75) and bool(gap20 is None or gap20 < 12)
        pullback = bool(trend_ok and rsi14 is not None and 38 <= rsi14 <= 62 and gap20 is not None and -8 <= gap20 <= 3)
        breakout = bool(m.get("high20") and c is not None and c >= m["high20"] * 0.995 and (m.get("volume_ratio") or 0) >= 1.10 and not_extended)
        trigger_ok = pullback or breakout
        strategic_ok = cfg["fundamental_score"] >= 60

        # Point score is deliberately transparent and simple.
        technical_score = 0
        technical_score += 25 if trend_ok else 0
        technical_score += 25 if rs_ok else 0
        technical_score += 20 if trigger_ok else 0
        technical_score += 15 if not_extended else 0
        technical_score += 15 if (m.get("volume_ratio") or 0) >= 1.0 else 0
        regime_score = 0
        regime_score += 30 if risk_green else 0
        regime_score += 25 if (gold_uptrend if group == "gold" else silver_uptrend) else 0
        regime_score += 25 if (gold_miners_leadership if group == "gold" else silver_miners_leadership) else 0
        regime_score += 20 if breadth_ok else 0
        overall_score = round(cfg["fundamental_score"] * 0.45 + technical_score * 0.35 + regime_score * 0.20, 1)

        max_signal = cfg["max_signal"]
        entry_confirmed = bool(max_signal == "ENTRY" and sector_ok and breadth_ok and strategic_ok and trend_ok and rs_ok and trigger_ok and not_extended)
        entry_candidate = bool(max_signal == "ENTRY" and risk_green and strategic_ok and (trend_ok or rs_ok) and not_extended and overall_score >= 55)
        watch = bool(max_signal != "ENTRY" or (strategic_ok and overall_score >= 45))

        reasons_no: list[str] = []
        if not risk_green:
            reasons_no.append("RiskGreen=FALSE")
        if group == "gold" and not gold_uptrend:
            reasons_no.append("GoldUptrend=FALSE")
        if group == "silver" and not silver_uptrend:
            reasons_no.append("SilverUptrend=FALSE")
        if group == "gold" and not gold_miners_leadership:
            reasons_no.append("GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE")
        if group == "silver" and not silver_miners_leadership:
            reasons_no.append("SilverMinerLeadership(SILJ/SLV)=FALSE")
        if not breadth_ok:
            reasons_no.append("SectorBreadthProxy=FALSE")
        if not trend_ok:
            reasons_no.append("PriceTrend=FALSE")
        if not rs_ok:
            reasons_no.append(f"RelativeStrength(vs {bmk})=FALSE")
        if not trigger_ok:
            reasons_no.append("Trigger(Pullback/Breakout)=FALSE")
        if not not_extended:
            reasons_no.append("Overextended=TRUE")
        if max_signal != "ENTRY":
            reasons_no.append("StaticRiskPolicy=WATCH_ONLY")

        if entry_confirmed:
            confirmed.append(logical)
        elif entry_candidate:
            candidates.append(logical)
        elif watch:
            watch_only.append(logical)

        results[logical] = {
            "name": cfg["name"],
            "group": group,
            "resolved_ticker": resolved_tickers.get(logical),
            "benchmark": bmk,
            "static_rank": cfg["static_rank"],
            "fundamental_score": cfg["fundamental_score"],
            "technical_score": technical_score,
            "regime_score": regime_score,
            "overall_score": overall_score,
            "risk_tier": cfg["risk_tier"],
            "style": cfg["style"],
            "why": cfg["why"],
            "watch": cfg["watch"],
            "max_signal": max_signal,
            "metrics": m,
            "relative_strength": rs,
            "checks": {
                "sector_ok": bool(sector_ok),
                "breadth_ok": bool(breadth_ok),
                "strategic_ok": bool(strategic_ok),
                "trend_ok": trend_ok,
                "rs_ok": rs_ok,
                "pullback": pullback,
                "breakout": breakout,
                "not_extended": not_extended,
                "entry_candidate": entry_candidate,
                "entry_confirmed": entry_confirmed,
            },
            "why_not": reasons_no,
        }

    if confirmed:
        verdict = "✅ Precious miners entry confirmed: " + ", ".join(confirmed)
    elif candidates:
        verdict = "🟡 Precious miners watch/add-on candidates: " + ", ".join(candidates)
    elif watch_only:
        verdict = "⏸ No confirmed entry; watchlist only"
    else:
        verdict = "⏸ No entry today"

    obj = {
        "verdict": verdict,
        "generated_utc": now_utc_str(),
        "regime": regime,
        "results": results,
        "confirmed": confirmed,
        "candidates": candidates,
        "watch_only": watch_only,
    }
    OUT_JSON.write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    OUT_MD.write_text(render_markdown(obj), encoding="utf-8")


def render_bool(v: Any) -> str:
    return "True" if bool(v) else "False"


def render_markdown(obj: dict[str, Any]) -> str:
    regime = obj["regime"]
    results = obj["results"]

    lines: list[str] = []
    lines += ["# Precious Miners Daily Entry Monitor (Gold / Silver)", ""]
    lines += [f"- 실행시간(UTC): **{obj['generated_utc']}**"]

    # Find one representative data date.
    dates = [r.get("metrics", {}).get("date") for r in results.values() if r.get("metrics", {}).get("date")]
    if dates:
        lines += [f"- 데이터 기준일(주가): **{max(dates)}**"]
    lines += [""]
    lines += ["## Verdict", f"**{obj['verdict']}**", ""]

    lines += ["## Regime / 공통 게이트", ""]
    lines += [f"- RiskGreen: **{render_bool(regime.get('risk_green'))}**"]
    lines += [f"- RealYieldHeadwind: **{render_bool(regime.get('real_yield_headwind'))}**"]
    lines += [f"- GoldUptrend(GC=F/GLD): **{render_bool(regime.get('gold_uptrend'))}**"]
    lines += [f"- SilverUptrend(SI=F/SLV): **{render_bool(regime.get('silver_uptrend'))}**"]
    lines += [f"- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **{render_bool(regime.get('gold_miners_leadership'))}**"]
    lines += [f"- SilverMinerLeadership(SILJ/SLV): **{render_bool(regime.get('silver_miners_leadership'))}**"]
    lines += [f"- GoldBreadthProxy >=45% above MA50: **{render_bool(regime.get('gold_breadth_ok'))}**"]
    lines += [f"- SilverBreadthProxy >=45% above MA50: **{render_bool(regime.get('silver_breadth_ok'))}**"]
    lines += [""]

    fred = regime.get("fred", {})
    lines += ["### Macro (FRED, if available)", ""]
    for label, key in [("HY OAS", "HY_OAS"), ("IG OAS", "IG_OAS"), ("10Y Real Yield", "REAL10Y"), ("VIX", "VIX"), ("NFCI", "NFCI")]:
        f = fred.get(key, {})
        if f.get("ok"):
            change = f.get("change_approx_4w")
            suffix = " bp-ish" if key in ["HY_OAS", "IG_OAS", "REAL10Y"] else ""
            lines += [f"- {label}: {fmt_num(f.get('latest'), 2)} / 4주 변화 {fmt_num(change, 2)}{suffix} / {f.get('date')}"]
        else:
            lines += [f"- {label}: N/A"]
    lines += [""]

    lines += ["### Leadership ratios", ""]
    for title, key in [("GDX/GLD", "gdx_gld"), ("GDXJ/GLD", "gdxj_gld"), ("SILJ/SLV", "silj_slv")]:
        r = regime.get(key, {})
        lines += [f"- {title}: gap {fmt_pct(r.get('gap'))} / slope_proxy {fmt_pct((r.get('slope_proxy') or 0) * 100)}"]
    gb = regime.get("gold_breadth", {})
    sb = regime.get("silver_breadth", {})
    lines += [f"- Gold breadth proxy: above50 {fmt_pct(gb.get('pct_above50'))}, above200 {fmt_pct(gb.get('pct_above200'))}, count {gb.get('count', 0)}"]
    lines += [f"- Silver breadth proxy: above50 {fmt_pct(sb.get('pct_above50'))}, above200 {fmt_pct(sb.get('pct_above200'))}, count {sb.get('count', 0)}"]
    lines += ["", "---", ""]

    for group_name in ["gold", "silver"]:
        title = "Gold miners" if group_name == "gold" else "Silver miners"
        lines += [f"## {title}", ""]
        sorted_items = sorted(
            [(sym, r) for sym, r in results.items() if r["group"] == group_name],
            key=lambda x: (not x[1]["checks"].get("entry_confirmed"), not x[1]["checks"].get("entry_candidate"), -x[1]["overall_score"]),
        )
        for sym, r in sorted_items:
            m = r["metrics"]
            rs = r["relative_strength"]
            c = r["checks"]
            lines += [f"### {sym} ({r['name']})"]
            lines += [f"- Style: **{r['style']}** | Static rank: {r['static_rank']} | Risk: {r['risk_tier']} | Max signal: {r['max_signal']}"]
            if m.get("ok"):
                lines += [
                    f"- close: {fmt_num(m.get('close'))} | RSI14: {fmt_num(m.get('rsi14'))} | ATR14%: {fmt_pct(m.get('atr14_pct'))}",
                    f"- MA20/50/200 gap: {fmt_pct(m.get('gap20'))} / {fmt_pct(m.get('gap50'))} / {fmt_pct(m.get('gap200'))}",
                    f"- 5D return: {fmt_pct(m.get('ret5'))} | 20D drawdown: {fmt_pct(m.get('drawdown20'))} | vol_ratio: {fmt_num(m.get('volume_ratio'))}",
                ]
            else:
                lines += ["- price data: N/A"]
            lines += [f"- RS vs {r['benchmark']}: gap {fmt_pct(rs.get('gap'))} / slope_proxy {fmt_pct((rs.get('slope_proxy') or 0) * 100)}"]
            lines += [f"- FundamentalScore: {r['fundamental_score']} | TechnicalScore: {r['technical_score']} | RegimeScore: {r['regime_score']} | OverallScore: **{r['overall_score']}**"]
            lines += ["- Checks:"]
            for k in ["sector_ok", "breadth_ok", "strategic_ok", "trend_ok", "rs_ok", "pullback", "breakout", "not_extended", "entry_candidate", "entry_confirmed"]:
                lines += [f"  - {k}: **{render_bool(c.get(k))}**"]
            lines += [f"- Thesis: {r['why']}"]
            lines += [f"- Watch: {r['watch']}"]
            if not c.get("entry_confirmed"):
                lines += ["- Why not today: " + (", ".join(r.get("why_not") or []) or "N/A")]
            lines += [""]
        lines += ["---", ""]

    lines += ["## Rule notes", ""]
    lines += ["- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다."]
    lines += ["- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다."]
    lines += ["- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다."]
    lines += ["- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다."]
    return "\n".join(lines).strip() + "\n"


if __name__ == "__main__":
    main()
