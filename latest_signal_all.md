# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-06**
- 실행시간(UTC): **2026-03-07 15:00:37**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.0 / 4주 변화 3.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 1.82 / 4주 변화 -7.0 bp
- VIX (VIXCLS): 23.75
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.550906
- MA60: 6.381527
- gap: 18.32%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.235364
- MA60: 0.212493
- gap: 10.76%
- MA60_slope_proxy: -0.018713
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-06**
- 실행시간(UTC): **2026-03-07 15:00:39**

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
- TERM_SPREAD_10Y_POLICY: 68.12 bp / 4주 변화 -10.24 bp
- CURVE_10s5s: 58.29 bp / 4주 변화 2.0 bp

## NWG Price
- close: 575.6
- MA50: 634.564 / gap50: -9.29%
- MA200: 568.7835 / gap200: 1.20%

## Relative Strength
- RS vs FTSE gap: -9.92% / slope_proxy: -0.00198
- RS vs Peers gap: -6.02% / slope_proxy: -0.059417

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-07 15:00:46**

## Commodity Regime

- WTI ref (CL=F): 90.90 / 5D 35.63%
- Brent ref (BZ=F): 92.69 / 5D 27.88%
- Brent Tier: **>=90**
- Brent-WTI spread: 1.79
- Gas ref (NG=F): 3.19 / 5D 11.44%

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

- close: 54.19
- MA20 / MA60 / MA200: 50.16 / 44.96 / 43.79
- gap20 / gap60: 8.03% / 20.54%
- 5D return: 2.09%
- 20D high/low: 54.21 / 45.49

### Relative Strength

- ratio: 0.957928
- ratio_MA60: 0.905053
- ratio_gap: 5.84%
- ratio_slope_proxy(20d): -0.006141

### Volume (if available)

- volume: 30396300.00
- volume_MA20: 15388385.00
- volume_ratio: 1.98

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.60
- MA20 / MA60 / MA200: 16.08 / 13.91 / 12.74
- gap20 / gap60: 9.45% / 26.49%
- 5D return: 5.83%
- 20D high/low: 17.60 / 14.87

### Relative Strength

- ratio: 0.485116
- ratio_MA60: 0.394017
- ratio_gap: 23.12%
- ratio_slope_proxy(20d): 0.006433

### Volume (if available)

- volume: 42114200.00
- volume_MA20: 24366325.00
- volume_ratio: 1.73

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

- close: 5.93
- MA20 / MA60 / MA200: 6.17 / 4.98 / 3.76
- gap20 / gap60: -3.84% / 19.02%
- 5D return: -8.49%
- 20D high/low: 6.54 / 5.39

### Relative Strength

- ratio: 0.015884
- ratio_MA60: 0.014662
- ratio_gap: 8.34%
- ratio_slope_proxy(20d): 0.000437

### Volume (if available)

- volume: 38494000.00
- volume_MA20: 67251890.00
- volume_ratio: 0.57

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

- close: 12.48
- MA20 / MA60 / MA200: 10.13 / 8.51 / 11.30
- gap20 / gap60: 23.23% / 46.71%
- 5D return: 28.79%
- 20D high/low: 12.48 / 8.77

### Relative Strength

- ratio: 0.048912
- ratio_MA60: 0.040480
- ratio_gap: 20.83%
- ratio_slope_proxy(20d): 0.002965

### Volume (if available)

- volume: 28689000.00
- volume_MA20: 16822240.00
- volume_ratio: 1.71

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

- 데이터 기준일(주가): **2026-03-06**
- 실행시간(UTC): **2026-03-07 15:00:52**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 3.0 bp / latest 3.0
- IG OAS 4주 변화: 6.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -7.0 bp / latest 1.82
- VIX: 23.75
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 1.20% / slope_proxy: -0.002788
- GDXJ/GLD gap: -2.46% / slope_proxy: 0.013665

## VZLA (Vizsla Silver)
- close: 4.0 | RSI14: 41.262588 | ATR14%: 8.40%
- MA20 gap: -0.39% | MA50 gap: -21.35% | MA200 gap: -3.64%
- vol_ratio(Volume/Vol20): 0.831519 | gap_open: 3.69%
- RS vs SILJ gap: -26.58% / slope_proxy: -0.02828
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 10.03 | RSI14: 42.163706 | ATR14%: 10.72%
- MA20 gap: -9.19% | MA50 gap: -12.50% | MA200 gap: 48.35%
- vol_ratio(Volume/Vol20): 0.81074 | gap_open: 1.91%
- SilverMarginGate: SI=83.816002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.37% / slope_proxy: 0.012371
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
- close: 38.790001 | RSI14: 46.162813 | ATR14%: 15.44%
- MA20 gap: -7.83% | MA50 gap: 2.46% | MA200 gap: 173.87%
- vol_ratio(Volume/Vol20): 0.900302 | gap_open: 1.29%
- RS vs SILJ gap: 12.49% / slope_proxy: 0.2457
- RS vs GDXJ gap: 11.14% / slope_proxy: 0.064631
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
