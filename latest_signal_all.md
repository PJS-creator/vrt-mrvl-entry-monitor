# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-05**
- 실행시간(UTC): **2026-03-06 03:00:34**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.97 / 4주 변화 11.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 7.0 bp
- 10Y Real Yield (DFII10): 1.8 / 4주 변화 -14.0 bp
- VIX (VIXCLS): 21.15
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.741786
- MA60: 6.317487
- gap: 22.55%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.191425
- MA60: 0.21274
- gap: -10.02%
- MA60_slope_proxy: -0.019583
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-05**
- 실행시간(UTC): **2026-03-06 03:00:38**

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
- TERM_SPREAD_10Y_POLICY: 73.12 bp / 4주 변화 -2.92 bp
- CURVE_10s5s: 56.65 bp / 4주 변화 1.42 bp

## NWG Price
- close: 586.0
- MA50: 636.024 / gap50: -7.87%
- MA200: 568.5211 / gap200: 3.07%

## Relative Strength
- RS vs FTSE gap: -9.63% / slope_proxy: -0.001823
- RS vs Peers gap: -7.14% / slope_proxy: -0.058273

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-06 03:00:45**

## Commodity Regime

- WTI ref (CL=F): 79.56 / 5D 22.01%
- Brent ref (BZ=F): 84.23 / 5D 19.05%
- Brent Tier: **80-90**
- Brent-WTI spread: 4.67
- Gas ref (NG=F): 2.98 / 5D 5.31%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 53.24
- MA20 / MA60 / MA200: 49.71 / 44.74 / 43.73
- gap20 / gap60: 7.11% / 19.00%
- 5D return: 3.52%
- 20D high/low: 54.21 / 45.09

### Relative Strength

- ratio: 0.942635
- ratio_MA60: 0.904306
- ratio_gap: 4.24%
- ratio_slope_proxy(20d): -0.007915

### Volume (if available)

- volume: 17637300.00
- volume_MA20: 14464035.00
- volume_ratio: 1.22

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.73
- MA20 / MA60 / MA200: 15.95 / 13.82 / 12.71
- gap20 / gap60: 4.92% / 21.01%
- 5D return: 0.72%
- 20D high/low: 17.32 / 14.87

### Relative Strength

- ratio: 0.460121
- ratio_MA60: 0.392379
- ratio_gap: 17.26%
- ratio_slope_proxy(20d): 0.004655

### Volume (if available)

- volume: 30014400.00
- volume_MA20: 23331335.00
- volume_ratio: 1.29

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.13
- MA20 / MA60 / MA200: 6.12 / 4.96 / 3.75
- gap20 / gap60: 0.20% / 23.65%
- 5D return: -3.92%
- 20D high/low: 6.54 / 4.94

### Relative Strength

- ratio: 0.016190
- ratio_MA60: 0.014646
- ratio_gap: 10.54%
- ratio_slope_proxy(20d): 0.000420

### Volume (if available)

- volume: 37730400.00
- volume_MA20: 67273625.00
- volume_ratio: 0.56

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.28
- MA20 / MA60 / MA200: 9.97 / 8.41 / 11.29
- gap20 / gap60: 23.18% / 46.04%
- 5D return: 29.67%
- 20D high/low: 12.28 / 8.77

### Relative Strength

- ratio: 0.049211
- ratio_MA60: 0.040213
- ratio_gap: 22.38%
- ratio_slope_proxy(20d): 0.002797

### Volume (if available)

- volume: 42695200.00
- volume_MA20: 16002755.00
- volume_ratio: 2.67

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-05**
- 실행시간(UTC): **2026-03-06 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 11.0 bp / latest 2.97
- IG OAS 4주 변화: 7.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -14.0 bp / latest 1.8
- VIX: 21.15
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 4.62% / slope_proxy: -0.002946
- GDXJ/GLD gap: -0.40% / slope_proxy: 0.013744

## VZLA (Vizsla Silver)
- close: 4.07 | RSI14: 42.469471 | ATR14%: 8.32%
- MA20 gap: 0.99% | MA50 gap: -20.53% | MA200 gap: -1.77%
- vol_ratio(Volume/Vol20): 0.63126 | gap_open: 2.40%
- RS vs SILJ gap: -26.81% / slope_proxy: -0.027576
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 9.97 | RSI14: 41.746265 | ATR14%: 11.03%
- MA20 gap: -9.86% | MA50 gap: -12.88% | MA200 gap: 48.41%
- vol_ratio(Volume/Vol20): 1.125092 | gap_open: 1.64%
- SilverMarginGate: SI=83.730003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.04% / slope_proxy: 0.014514
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 41.060001 | RSI14: 48.663452 | ATR14%: 14.83%
- MA20 gap: -1.84% | MA50 gap: 9.28% | MA200 gap: 193.64%
- vol_ratio(Volume/Vol20): 1.178895 | gap_open: 2.17%
- RS vs SILJ gap: 19.02% / slope_proxy: 0.246764
- RS vs GDXJ gap: 18.53% / slope_proxy: 0.06496
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
