# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: OXY**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-29**
- 실행시간(UTC): **2026-04-29 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.85 / 4주 변화 -43.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -9.0 bp
- 10Y Real Yield (DFII10): 1.91 / 4주 변화 -13.0 bp
- VIX (VIXCLS): 17.83
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.896788
- MA60: 8.008598
- gap: 11.09%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.309128
- MA60: 0.241927
- gap: 27.78%
- MA60_slope_proxy: 0.030555
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-29**
- 실행시간(UTC): **2026-04-29 15:00:52**

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
- TERM_SPREAD_10Y_POLICY: 116.95 bp / 4주 변화 3.89 bp
- CURVE_10s5s: 47.02 bp / 4주 변화 5.21 bp

## NWG Price
- close: 570.6
- MA50: 586.0199 / gap50: -2.63%
- MA200: 580.9842 / gap200: -1.79%

## Relative Strength
- RS vs FTSE gap: -1.84% / slope_proxy: -0.002365
- RS vs Peers gap: -6.32% / slope_proxy: -0.036479

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-29 15:01:00**

## Commodity Regime

- WTI ref (CL=F): 105.24 / 5D 13.21%
- Brent ref (BZ=F): 109.67 / 5D 7.61%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.43
- Gas ref (NG=F): 2.65 / 5D -2.50%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **True**

### Trend

- close: 59.24
- MA20 / MA60 / MA200: 58.26 / 55.30 / 46.62
- gap20 / gap60: 1.68% / 7.13%
- 5D return: 3.84%
- 20D high/low: 62.97 / 53.79

### Relative Strength

- ratio: 1.014123
- ratio_MA60: 0.974290
- ratio_gap: 4.09%
- ratio_slope_proxy(20d): 0.038113

### Volume (if available)

- volume: 3118118.00
- volume_MA20: 14117540.90
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.59
- MA20 / MA60 / MA200: 20.85 / 18.52 / 14.20
- gap20 / gap60: 3.59% / 16.62%
- 5D return: 2.56%
- 20D high/low: 21.84 / 19.86

### Relative Strength

- ratio: 0.550893
- ratio_MA60: 0.481931
- ratio_gap: 14.31%
- ratio_slope_proxy(20d): 0.046844

### Volume (if available)

- volume: 3492495.00
- volume_MA20: 24888359.75
- volume_ratio: 0.14

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.80
- MA20 / MA60 / MA200: 6.38 / 6.27 / 4.44
- gap20 / gap60: 6.60% / 8.53%
- 5D return: 12.29%
- 20D high/low: 6.80 / 5.89

### Relative Strength

- ratio: 0.015295
- ratio_MA60: 0.015882
- ratio_gap: -3.70%
- ratio_slope_proxy(20d): 0.000570

### Volume (if available)

- volume: 9682978.00
- volume_MA20: 30746348.90
- volume_ratio: 0.31

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.80
- MA20 / MA60 / MA200: 13.06 / 12.32 / 11.04
- gap20 / gap60: -1.92% / 3.93%
- 5D return: 3.77%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.047427
- ratio_MA60: 0.048436
- ratio_gap: -2.08%
- ratio_slope_proxy(20d): 0.002545

### Volume (if available)

- volume: 6129910.00
- volume_MA20: 23837760.50
- volume_ratio: 0.26

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: OXY


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-29**
- 실행시간(UTC): **2026-04-29 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -43.0 bp / latest 2.85
- IG OAS 4주 변화: -9.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -13.0 bp / latest 1.91
- VIX: 17.83
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.38% / slope_proxy: 0.015223
- GDXJ/GLD gap: -4.52% / slope_proxy: -0.003666

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 50.367287 | ATR14%: 5.60%
- MA20 gap: 2.62% | MA50 gap: -3.11% | MA200 gap: -17.76%
- vol_ratio(Volume/Vol20): 0.22561 | gap_open: 0.88%
- RS vs SILJ gap: 6.51% / slope_proxy: -0.023334
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 7.7 | RSI14: 39.972235 | ATR14%: 8.50%
- MA20 gap: -8.56% | MA50 gap: -16.19% | MA200 gap: -1.50%
- vol_ratio(Volume/Vol20): 0.544217 | gap_open: 1.65%
- SilverMarginGate: SI=72.160004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.64% / slope_proxy: -0.030995
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
- close: 34.174999 | RSI14: 41.348491 | ATR14%: 10.10%
- MA20 gap: -11.39% | MA50 gap: -13.63% | MA200 gap: 67.02%
- vol_ratio(Volume/Vol20): 0.292898 | gap_open: 1.32%
- RS vs SILJ gap: -0.59% / slope_proxy: 0.039945
- RS vs GDXJ gap: -1.33% / slope_proxy: 0.006612
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
