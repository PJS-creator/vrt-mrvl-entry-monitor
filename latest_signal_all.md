# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-05-26 03:01:12**
- 데이터 기준일(일봉): **2026-05-22**
- 데이터 기준일(주봉): **2026-05-18**
- VXN 기준일: **2026-05-21** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 717.54
- Weekly RSI14: **74.70**
- 52W MA: 599.37 / gap: **19.71%**
- 104W MA gap: **32.13%**
- 52W MA 13W slope: **7.10%**
- VXN: **22.74** / 5D change: -1.34

## Daily trigger: 실제 매수 타이밍

- QQQ close: 717.54
- Daily RSI14: **71.38**
- 20D gap: **3.26%**
- 50D gap: **11.76%**
- 200D gap: **16.94%**
- MACD hist: -1.3572 / change: -0.0658
- ATR14%: **1.49%**
- 20D high drawdown: **-0.31%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-22**
- 실행시간(UTC): **2026-05-26 03:00:39**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.78 / 4주 변화 -8.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 2.18 / 4주 변화 26.0 bp
- VIX (VIXCLS): 16.76
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.533042
- MA60: 8.818857
- gap: 8.10%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.340661
- MA60: 0.2768
- gap: 23.07%
- MA60_slope_proxy: 0.040717
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-22**
- 실행시간(UTC): **2026-05-26 03:00:46**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 120.54 bp / 4주 변화 11.72 bp
- CURVE_10s5s: 46.61 bp / 4주 변화 -0.06 bp

## NWG Price
- close: 584.2
- MA50: 575.6976 / gap50: 1.48%
- MA200: 585.7781 / gap200: -0.27%

## Relative Strength
- RS vs FTSE gap: 0.02% / slope_proxy: -0.001764
- RS vs Peers gap: -4.76% / slope_proxy: -0.033419

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-26 03:00:56**

## Commodity Regime

- WTI ref (CL=F): 91.57 / 5D -15.73%
- Brent ref (BZ=F): 94.98 / 5D -15.27%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.41
- Gas ref (NG=F): 3.06 / 5D 1.19%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 58.81
- MA20 / MA60 / MA200: 57.93 / 58.12 / 47.87
- gap20 / gap60: 1.52% / 1.20%
- 5D return: -1.36%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.988570
- ratio_MA60: 1.001202
- ratio_gap: -1.26%
- ratio_slope_proxy(20d): 0.033083

### Volume (if available)

- volume: 7904200.00
- volume_MA20: 12435485.00
- volume_ratio: 0.64

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.90
- MA20 / MA60 / MA200: 20.74 / 19.98 / 14.92
- gap20 / gap60: -4.05% / -0.39%
- 5D return: -0.15%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.547154
- ratio_MA60: 0.521845
- ratio_gap: 4.85%
- ratio_slope_proxy(20d): 0.046509

### Volume (if available)

- volume: 10814900.00
- volume_MA20: 17994480.00
- volume_ratio: 0.60

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.81
- MA20 / MA60 / MA200: 6.78 / 6.50 / 4.77
- gap20 / gap60: 0.50% / 4.69%
- 5D return: -3.27%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.015339
- ratio_MA60: 0.015804
- ratio_gap: -2.94%
- ratio_slope_proxy(20d): -0.000022

### Volume (if available)

- volume: 31888200.00
- volume_MA20: 38712530.00
- volume_ratio: 0.82

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.83
- MA20 / MA60 / MA200: 13.05 / 13.35 / 10.87
- gap20 / gap60: 6.00% / 3.63%
- 5D return: -2.81%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.057422
- ratio_MA60: 0.051106
- ratio_gap: 12.36%
- ratio_slope_proxy(20d): 0.002642

### Volume (if available)

- volume: 11161900.00
- volume_MA20: 20567760.00
- volume_ratio: 0.54

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-25**
- 실행시간(UTC): **2026-05-26 03:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.78
- IG OAS 4주 변화: -5.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.18
- VIX: 16.76
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -4.97% / slope_proxy: -0.008262
- GDXJ/GLD gap: -4.77% / slope_proxy: -0.004815

## VZLA (Vizsla Silver)
- close: 3.37 | RSI14: 45.843016 | ATR14%: 6.20%
- MA20 gap: -3.34% | MA50 gap: -0.44% | MA200 gap: -20.38%
- vol_ratio(Volume/Vol20): 0.593593 | gap_open: 0.00%
- RS vs SILJ gap: 4.07% / slope_proxy: -0.003406
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.03 | RSI14: 42.580766 | ATR14%: 7.94%
- MA20 gap: -6.45% | MA50 gap: -4.46% | MA200 gap: -2.39%
- vol_ratio(Volume/Vol20): 0.803816 | gap_open: 0.24%
- SilverMarginGate: SI=76.949997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.73% / slope_proxy: -0.016187
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 32.32 | RSI14: 39.758028 | ATR14%: 10.16%
- MA20 gap: -13.52% | MA50 gap: -12.94% | MA200 gap: 38.42%
- vol_ratio(Volume/Vol20): 0.610742 | gap_open: 1.47%
- RS vs SILJ gap: -8.65% / slope_proxy: 0.026713
- RS vs GDXJ gap: -6.54% / slope_proxy: 0.007832
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
