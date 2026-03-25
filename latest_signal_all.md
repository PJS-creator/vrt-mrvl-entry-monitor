# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-24**
- 실행시간(UTC): **2026-03-25 03:00:38**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.19 / 4주 변화 24.0 bp
- IG OAS (BAMLC0A0CM): 0.88 / 4주 변화 8.0 bp
- 10Y Real Yield (DFII10): 2.01 / 4주 변화 24.0 bp
- VIX (VIXCLS): 26.15
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.738388
- MA60: 6.872151
- gap: 27.16%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.234066
- MA60: 0.21027
- gap: 11.32%
- MA60_slope_proxy: -0.010426
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-24**
- 실행시간(UTC): **2026-03-25 03:00:47**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 117.67 bp / 4주 변화 55.35 bp
- CURVE_10s5s: 38.39 bp / 4주 변화 -20.27 bp

## NWG Price
- close: 533.8
- MA50: 613.8373 / gap50: -13.04%
- MA200: 570.858 / gap200: -6.49%

## Relative Strength
- RS vs FTSE gap: -10.92% / slope_proxy: -0.003063
- RS vs Peers gap: -6.03% / slope_proxy: -0.052694

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-25 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 88.46 / 5D -8.06%
- Brent ref (BZ=F): 98.94 / 5D -4.33%
- Brent Tier: **>=90**
- Brent-WTI spread: 10.48
- Gas ref (NG=F): 2.84 / 5D -6.26%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 61.25
- MA20 / MA60 / MA200: 55.87 / 48.29 / 44.62
- gap20 / gap60: 9.64% / 26.85%
- 5D return: 6.10%
- 20D high/low: 61.25 / 50.70

### Relative Strength

- ratio: 1.006739
- ratio_MA60: 0.919456
- ratio_gap: 9.49%
- ratio_slope_proxy(20d): 0.021115

### Volume (if available)

- volume: 14251439.00
- volume_MA20: 21019846.95
- volume_ratio: 0.68

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.75
- MA20 / MA60 / MA200: 18.20 / 15.34 / 13.21
- gap20 / gap60: 8.50% / 28.79%
- 5D return: 1.23%
- 20D high/low: 19.78 / 16.61

### Relative Strength

- ratio: 0.538587
- ratio_MA60: 0.422562
- ratio_gap: 27.46%
- ratio_slope_proxy(20d): 0.036602

### Volume (if available)

- volume: 27150543.00
- volume_MA20: 36547202.15
- volume_ratio: 0.74

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

- close: 6.63
- MA20 / MA60 / MA200: 6.31 / 5.43 / 3.99
- gap20 / gap60: 5.12% / 22.00%
- 5D return: 0.76%
- 20D high/low: 6.63 / 5.93

### Relative Strength

- ratio: 0.016302
- ratio_MA60: 0.015130
- ratio_gap: 7.74%
- ratio_slope_proxy(20d): 0.000616

### Volume (if available)

- volume: 32650665.00
- volume_MA20: 37663093.25
- volume_ratio: 0.87

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 16.60
- MA20 / MA60 / MA200: 12.54 / 9.96 / 11.38
- gap20 / gap60: 32.34% / 66.70%
- 5D return: 27.99%
- 20D high/low: 16.60 / 9.30

### Relative Strength

- ratio: 0.056351
- ratio_MA60: 0.044086
- ratio_gap: 27.82%
- ratio_slope_proxy(20d): 0.005187

### Volume (if available)

- volume: 47256283.00
- volume_MA20: 35947039.15
- volume_ratio: 1.31

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

- 데이터 기준일(주가): **2026-03-24**
- 실행시간(UTC): **2026-03-25 03:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 24.0 bp / latest 3.19
- IG OAS 4주 변화: 8.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.01
- VIX: 26.15
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: 1.40% / slope_proxy: -0.006475
- GDXJ/GLD gap: -7.21% / slope_proxy: 0.002863

## VZLA (Vizsla Silver)
- close: 3.13 | RSI14: 31.092333 | ATR14%: 9.02%
- MA20 gap: -17.51% | MA50 gap: -31.64% | MA200 gap: -25.28%
- vol_ratio(Volume/Vol20): 0.591533 | gap_open: 2.26%
- RS vs SILJ gap: -22.23% / slope_proxy: -0.027456
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
- close: 7.91 | RSI14: 36.224454 | ATR14%: 11.55%
- MA20 gap: -19.44% | MA50 gap: -29.12% | MA200 gap: 10.44%
- vol_ratio(Volume/Vol20): 0.605228 | gap_open: 1.19%
- SilverMarginGate: SI=73.959999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.97% / slope_proxy: -0.012427
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
- close: 33.220001 | RSI14: 42.162058 | ATR14%: 14.30%
- MA20 gap: -19.92% | MA50 gap: -18.19% | MA200 gap: 104.88%
- vol_ratio(Volume/Vol20): 0.504803 | gap_open: 2.77%
- RS vs SILJ gap: 4.73% / slope_proxy: 0.231618
- RS vs GDXJ gap: 4.88% / slope_proxy: 0.060879
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
