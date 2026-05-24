from __future__ import annotations

import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import requests
import yfinance as yf

OUT_JSON = Path("qqq_qld_timing_signal.json")
OUT_MD = Path("qqq_qld_timing_signal.md")

# 월 적립 예산. GitHub Actions에서 환경변수로 바꿀 수 있습니다.
# 예: MONTHLY_BUDGET_KRW=2000000
MONTHLY_BUDGET_KRW = int(os.environ.get("MONTHLY_BUDGET_KRW", "2000000"))

QQQ = "QQQ"
QLD = "QLD"

# 국내 실행용 ETF 이름. 실제 매수 판단은 QQQ 지표로 합니다.
KR_QQQ_NAME = "TIGER 미국나스닥100"
KR_QQQ_CODE = "133690"
KR_QLD_NAME = "TIGER 미국나스닥100레버리지(합성)"
KR_QLD_CODE = "418660"


def safe_float(x: Any) -> float | None:
    """JSON/Markdown에 쓰기 좋게 float를 정리합니다."""
    try:
        v = float(x)
        if math.isnan(v) or math.isinf(v):
            return None
        return v
    except Exception:
        return None


def fmt(v: float | None, digits: int = 2, suffix: str = "") -> str:
    if v is None:
        return "N/A"
    return f"{v:.{digits}f}{suffix}"


def won(n: int | float | None) -> str:
    if n is None:
        return "N/A"
    return f"{int(round(n)):,}원"


def download_ohlcv(symbol: str, period: str, interval: str) -> pd.DataFrame:
    """yfinance에서 OHLCV를 가져옵니다. MultiIndex 컬럼도 단일 컬럼으로 정리합니다."""
    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        auto_adjust=True,
        progress=False,
        threads=False,
    )
    if df is None or df.empty:
        raise RuntimeError(f"No price data downloaded for {symbol}")

    # yfinance가 가끔 MultiIndex 컬럼을 반환합니다.
    if isinstance(df.columns, pd.MultiIndex):
        try:
            df = df.xs(symbol, axis=1, level=-1)
        except Exception:
            df.columns = df.columns.get_level_values(0)

    df = df.rename(columns={str(c): str(c).title() for c in df.columns})
    needed = ["Open", "High", "Low", "Close"]
    for col in needed:
        if col not in df.columns:
            raise RuntimeError(f"Missing {col} column for {symbol}")

    df = df.dropna(subset=["Close"]).copy()
    df.index = pd.to_datetime(df.index)
    return df


def rsi_wilder(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
    rs = avg_gain / avg_loss.replace(0, pd.NA)
    return 100 - (100 / (1 + rs))


def add_daily_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    close = out["Close"]
    out["rsi14"] = rsi_wilder(close, 14)
    out["ma20"] = close.rolling(20).mean()
    out["ma50"] = close.rolling(50).mean()
    out["ma200"] = close.rolling(200).mean()

    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    out["macd"] = ema12 - ema26
    out["macd_signal"] = out["macd"].ewm(span=9, adjust=False).mean()
    out["macd_hist"] = out["macd"] - out["macd_signal"]
    out["macd_hist_chg"] = out["macd_hist"].diff()

    prev_close = close.shift(1)
    tr = pd.concat(
        [
            out["High"] - out["Low"],
            (out["High"] - prev_close).abs(),
            (out["Low"] - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    out["atr14"] = tr.ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()
    out["high20"] = close.rolling(20).max()
    return out


def add_weekly_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    close = out["Close"]
    out["rsi14"] = rsi_wilder(close, 14)
    out["ma52"] = close.rolling(52).mean()
    out["ma104"] = close.rolling(104).mean()
    out["ma52_slope_13w"] = out["ma52"] / out["ma52"].shift(13) - 1
    return out


def fetch_vxn() -> dict[str, Any]:
    """FRED VXNCLS를 우선 사용하고, 실패하면 yfinance ^VXN으로 보완합니다."""
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=VXNCLS"
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        from io import StringIO

        df = pd.read_csv(StringIO(r.text))
        df["DATE"] = pd.to_datetime(df["DATE"])
        df["VXNCLS"] = pd.to_numeric(df["VXNCLS"], errors="coerce")
        df = df.dropna(subset=["VXNCLS"]).sort_values("DATE")
        if df.empty:
            raise RuntimeError("FRED VXNCLS returned no numeric data")
        last = df.iloc[-1]
        prev5 = df.iloc[-6] if len(df) >= 6 else df.iloc[0]
        return {
            "value": float(last["VXNCLS"]),
            "date": str(last["DATE"].date()),
            "change_5d": float(last["VXNCLS"] - prev5["VXNCLS"]),
            "source": "FRED: VXNCLS",
        }
    except Exception as fred_error:
        try:
            vdf = download_ohlcv("^VXN", period="1y", interval="1d")
            last = vdf.iloc[-1]
            prev5 = vdf.iloc[-6] if len(vdf) >= 6 else vdf.iloc[0]
            return {
                "value": float(last["Close"]),
                "date": str(vdf.index[-1].date()),
                "change_5d": float(last["Close"] - prev5["Close"]),
                "source": f"Yahoo Finance ^VXN fallback; FRED error={fred_error}",
            }
        except Exception as yf_error:
            return {
                "value": None,
                "date": None,
                "change_5d": None,
                "source": f"VXN unavailable; FRED error={fred_error}; yfinance error={yf_error}",
            }


def latest_metrics() -> dict[str, Any]:
    daily = add_daily_indicators(download_ohlcv(QQQ, period="3y", interval="1d"))
    weekly = add_weekly_indicators(download_ohlcv(QQQ, period="20y", interval="1wk"))
    vxn = fetch_vxn()

    d = daily.dropna().iloc[-1]
    w = weekly.dropna().iloc[-1]

    d_close = float(d["Close"])
    w_close = float(w["Close"])

    metrics = {
        "data_date_daily": str(daily.dropna().index[-1].date()),
        "data_date_weekly": str(weekly.dropna().index[-1].date()),
        "qqq_close_daily": d_close,
        "qqq_close_weekly": w_close,
        "daily_rsi14": float(d["rsi14"]),
        "daily_ma20": float(d["ma20"]),
        "daily_ma50": float(d["ma50"]),
        "daily_ma200": float(d["ma200"]),
        "daily_gap20_pct": (d_close / float(d["ma20"]) - 1) * 100,
        "daily_gap50_pct": (d_close / float(d["ma50"]) - 1) * 100,
        "daily_gap200_pct": (d_close / float(d["ma200"]) - 1) * 100,
        "daily_macd_hist": float(d["macd_hist"]),
        "daily_macd_hist_chg": float(d["macd_hist_chg"]),
        "daily_atr14_pct": float(d["atr14"] / d_close * 100),
        "daily_drawdown20_pct": (d_close / float(d["high20"]) - 1) * 100,
        "weekly_rsi14": float(w["rsi14"]),
        "weekly_ma52": float(w["ma52"]),
        "weekly_ma104": float(w["ma104"]),
        "weekly_gap52_pct": (w_close / float(w["ma52"]) - 1) * 100,
        "weekly_gap104_pct": (w_close / float(w["ma104"]) - 1) * 100,
        "weekly_ma52_slope_13w_pct": float(w["ma52_slope_13w"] * 100),
        "vxn": vxn["value"],
        "vxn_date": vxn["date"],
        "vxn_change_5d": vxn["change_5d"],
        "vxn_source": vxn["source"],
    }
    return metrics


def decide(metrics: dict[str, Any]) -> dict[str, Any]:
    wrsi = metrics["weekly_rsi14"]
    wgap = metrics["weekly_gap52_pct"]
    wslope = metrics["weekly_ma52_slope_13w_pct"]
    drsi = metrics["daily_rsi14"]
    dgap20 = metrics["daily_gap20_pct"]
    dgap50 = metrics["daily_gap50_pct"]
    macd_hist = metrics["daily_macd_hist"]
    macd_chg = metrics["daily_macd_hist_chg"]
    dd20 = metrics["daily_drawdown20_pct"]
    vxn = metrics["vxn"]
    vxn_chg = metrics["vxn_change_5d"]

    vxn_num = 999.0 if vxn is None else float(vxn)
    vxn_chg_num = 0.0 if vxn_chg is None else float(vxn_chg)

    # 주봉: QLD를 사도 되는 큰 환경인지 판단합니다.
    weekly_good = 45 <= wrsi <= 65 and -5 <= wgap <= 10 and vxn_num <= 24 and wslope > 0
    weekly_small = 50 <= wrsi <= 68 and 0 <= wgap <= 15 and vxn_num <= 24 and wslope > 0
    weekly_overheated = wrsi >= 68 or wgap >= 15
    weekly_panic = wrsi <= 35 or wgap <= -10 or vxn_num >= 30

    # 일봉: 실제 매수 타이밍입니다.
    daily_a = (
        40 <= drsi <= 60
        and -2 <= dgap20 <= 2
        and 0 <= dgap50 <= 8
        and (macd_hist > 0 or macd_chg > 0)
        and vxn_num <= 24
    )
    daily_b = (
        40 <= drsi <= 65
        and -4 <= dgap20 <= 2
        and -2 <= dgap50 <= 8
        and macd_chg > 0
        and vxn_num <= 26
    )
    daily_overheated = drsi >= 68 or dgap20 >= 3 or dgap50 >= 10 or dd20 > -1
    rebound_after_panic = drsi >= 40 and macd_chg > 0 and dgap20 >= -1 and vxn_chg_num <= 0

    checks = {
        "weekly_good": weekly_good,
        "weekly_small": weekly_small,
        "weekly_overheated": weekly_overheated,
        "weekly_panic": weekly_panic,
        "daily_a": daily_a,
        "daily_b": daily_b,
        "daily_overheated": daily_overheated,
        "rebound_after_panic": rebound_after_panic,
    }

    reasons: list[str] = []
    if weekly_overheated:
        reasons.append("주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한")
    if weekly_panic and not rebound_after_panic:
        reasons.append("공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선")
    if daily_overheated:
        reasons.append("일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합")
    if vxn_num > 24:
        reasons.append("VXN이 24 초과라 레버리지 비중 확대에는 불리")

    # 월 적립금 기준 비중. 기존 보유분 매도/리밸런싱 지시는 아닙니다.
    if weekly_good and daily_a:
        qld_pct, qqq_pct = 0.40, 0.60
        regime = "A: QLD 본격 허용"
    elif weekly_good and daily_b:
        qld_pct, qqq_pct = 0.25, 0.75
        regime = "B: QLD 부분 허용"
    elif weekly_small and daily_b:
        qld_pct, qqq_pct = 0.10, 0.75
        regime = "C: QLD 소액 테스트만 허용"
    elif weekly_panic:
        if rebound_after_panic:
            qld_pct, qqq_pct = 0.10, 0.60
            regime = "D: 급락 후 반등 확인, QLD 소액만"
        else:
            qld_pct, qqq_pct = 0.00, 0.50
            regime = "E: 급락 진행/공포, QLD 대기"
    elif weekly_overheated:
        qld_pct = 0.00
        qqq_pct = 0.50 if daily_overheated else 0.75
        regime = "F: 과열권, QLD 대기"
    else:
        qld_pct = 0.00
        qqq_pct = 0.75 if not daily_overheated else 0.50
        regime = "G: 중립, QQQ 중심"

    cash_pct = max(0.0, 1.0 - qld_pct - qqq_pct)

    qld_amt = round(MONTHLY_BUDGET_KRW * qld_pct)
    qqq_amt = round(MONTHLY_BUDGET_KRW * qqq_pct)
    cash_amt = MONTHLY_BUDGET_KRW - qld_amt - qqq_amt

    if qld_pct >= 0.35:
        verdict = "✅ QLD/TIGER 레버리지 매수 허용"
    elif qld_pct > 0:
        verdict = "🟡 QLD/TIGER 레버리지 소액만 허용"
    else:
        verdict = "⏸ QLD/TIGER 레버리지 대기"

    if not reasons:
        reasons.append("주봉과 일봉 조건이 과열/공포를 크게 보이지 않음")

    return {
        "verdict": verdict,
        "regime": regime,
        "checks": checks,
        "reasons": reasons,
        "allocation": {
            "monthly_budget_krw": MONTHLY_BUDGET_KRW,
            "qqq_pct": qqq_pct,
            "qld_pct": qld_pct,
            "cash_pct": cash_pct,
            "qqq_amount_krw": qqq_amt,
            "qld_amount_krw": qld_amt,
            "cash_amount_krw": cash_amt,
            "korea_qqq_etf": {"name": KR_QQQ_NAME, "code": KR_QQQ_CODE, "amount_krw": qqq_amt},
            "korea_qld_etf": {"name": KR_QLD_NAME, "code": KR_QLD_CODE, "amount_krw": qld_amt},
        },
    }


def build_markdown(metrics: dict[str, Any], decision: dict[str, Any]) -> str:
    alloc = decision["allocation"]
    checks = decision["checks"]
    reasons = decision["reasons"]

    lines: list[str] = []
    lines += ["# QQQ / QLD Timing Monitor", ""]
    lines += [f"- 실행시간(UTC): **{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}**"]
    lines += [f"- 데이터 기준일(일봉): **{metrics['data_date_daily']}**"]
    lines += [f"- 데이터 기준일(주봉): **{metrics['data_date_weekly']}**"]
    lines += [f"- VXN 기준일: **{metrics.get('vxn_date') or 'N/A'}** / source: `{metrics.get('vxn_source')}`"]
    lines += [""]
    lines += ["## Verdict", ""]
    lines += [f"**{decision['verdict']}**"]
    lines += [f"- Regime: **{decision['regime']}**"]
    lines += [""]
    lines += ["## Recommended monthly buy amount", ""]
    lines += [f"- 월 적립 예산: **{won(alloc['monthly_budget_krw'])}**"]
    lines += [f"- {KR_QQQ_NAME} ({KR_QQQ_CODE}) / QQQ 역할: **{won(alloc['qqq_amount_krw'])}** ({alloc['qqq_pct']*100:.0f}%)"]
    lines += [f"- {KR_QLD_NAME} ({KR_QLD_CODE}) / QLD 역할: **{won(alloc['qld_amount_krw'])}** ({alloc['qld_pct']*100:.0f}%)"]
    lines += [f"- 대기자금: **{won(alloc['cash_amount_krw'])}** ({alloc['cash_pct']*100:.0f}%)"]
    lines += [""]
    lines += ["## Weekly gate: 큰 환경", ""]
    lines += [f"- QQQ close: {fmt(metrics['qqq_close_weekly'], 2)}"]
    lines += [f"- Weekly RSI14: **{fmt(metrics['weekly_rsi14'], 2)}**"]
    lines += [f"- 52W MA: {fmt(metrics['weekly_ma52'], 2)} / gap: **{fmt(metrics['weekly_gap52_pct'], 2, '%')}**"]
    lines += [f"- 104W MA gap: **{fmt(metrics['weekly_gap104_pct'], 2, '%')}**"]
    lines += [f"- 52W MA 13W slope: **{fmt(metrics['weekly_ma52_slope_13w_pct'], 2, '%')}**"]
    lines += [f"- VXN: **{fmt(metrics['vxn'], 2)}** / 5D change: {fmt(metrics['vxn_change_5d'], 2)}"]
    lines += [""]
    lines += ["## Daily trigger: 실제 매수 타이밍", ""]
    lines += [f"- QQQ close: {fmt(metrics['qqq_close_daily'], 2)}"]
    lines += [f"- Daily RSI14: **{fmt(metrics['daily_rsi14'], 2)}**"]
    lines += [f"- 20D gap: **{fmt(metrics['daily_gap20_pct'], 2, '%')}**"]
    lines += [f"- 50D gap: **{fmt(metrics['daily_gap50_pct'], 2, '%')}**"]
    lines += [f"- 200D gap: **{fmt(metrics['daily_gap200_pct'], 2, '%')}**"]
    lines += [f"- MACD hist: {fmt(metrics['daily_macd_hist'], 4)} / change: {fmt(metrics['daily_macd_hist_chg'], 4)}"]
    lines += [f"- ATR14%: **{fmt(metrics['daily_atr14_pct'], 2, '%')}**"]
    lines += [f"- 20D high drawdown: **{fmt(metrics['daily_drawdown20_pct'], 2, '%')}**"]
    lines += [""]
    lines += ["## Checks", ""]
    for k, v in checks.items():
        lines += [f"- {k}: **{v}**"]
    lines += [""]
    lines += ["## Why", ""]
    for reason in reasons:
        lines += [f"- {reason}"]
    lines += [""]
    lines += ["## Rule note", ""]
    lines += ["- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다."]
    lines += ["- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다."]
    lines += ["- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다."]
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    metrics = latest_metrics()
    decision = decide(metrics)
    result = {
        "verdict": decision["verdict"],
        "regime": decision["regime"],
        "run_utc": datetime.now(timezone.utc).isoformat(),
        "metrics": {k: safe_float(v) if isinstance(v, (float, int)) else v for k, v in metrics.items()},
        "checks": decision["checks"],
        "reasons": decision["reasons"],
        "allocation": decision["allocation"],
    }

    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_MD.write_text(build_markdown(metrics, decision), encoding="utf-8")


if __name__ == "__main__":
    main()
