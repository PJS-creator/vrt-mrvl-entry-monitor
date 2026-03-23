# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-20**
- 실행시간(UTC): **2026-03-23 03:00:34**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.27 / 4주 변화 39.0 bp
- IG OAS (BAMLC0A0CM): 0.9 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 1.88 / 4주 변화 9.0 bp
- VIX (VIXCLS): 24.06
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.232947
- MA60: 6.785412
- gap: 21.33%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.228492
- MA60: 0.210506
- gap: 8.54%
- MA60_slope_proxy: -0.01216
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-20**
- 실행시간(UTC): **2026-03-23 03:00:45**

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
- TERM_SPREAD_10Y_POLICY: 95.02 bp / 4주 변화 31.05 bp
- CURVE_10s5s: 48.83 bp / 4주 변화 -9.38 bp

## NWG Price
- close: 519.6
- MA50: 617.9272 / gap50: -15.91%
- MA200: 570.676 / gap200: -8.95%

## Relative Strength
- RS vs FTSE gap: -13.45% / slope_proxy: -0.002922
- RS vs Peers gap: -6.17% / slope_proxy: -0.054284

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-23 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 98.82 / 5D 5.69%
- Brent ref (BZ=F): 107.59 / 5D 7.36%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.77
- Gas ref (NG=F): 3.05 / 5D 0.96%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 60.71
- MA20 / MA60 / MA200: 54.98 / 47.59 / 44.43
- gap20 / gap60: 10.42% / 27.57%
- 5D return: 4.89%
- 20D high/low: 60.71 / 50.70

### Relative Strength

- ratio: 1.023605
- ratio_MA60: 0.915723
- ratio_gap: 11.78%
- ratio_slope_proxy(20d): 0.017789

### Volume (if available)

- volume: 25049026.00
- volume_MA20: 20257901.30
- volume_ratio: 1.24

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.80
- MA20 / MA60 / MA200: 17.89 / 15.08 / 13.13
- gap20 / gap60: 5.11% / 24.68%
- 5D return: 1.24%
- 20D high/low: 19.78 / 16.14

### Relative Strength

- ratio: 0.536224
- ratio_MA60: 0.417391
- ratio_gap: 28.47%
- ratio_slope_proxy(20d): 0.031835

### Volume (if available)

- volume: 38216941.00
- volume_MA20: 35017357.05
- volume_ratio: 1.09

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

- close: 6.22
- MA20 / MA60 / MA200: 6.30 / 5.35 / 3.95
- gap20 / gap60: -1.25% / 16.26%
- 5D return: -2.20%
- 20D high/low: 6.58 / 5.93

### Relative Strength

- ratio: 0.016074
- ratio_MA60: 0.015062
- ratio_gap: 6.72%
- ratio_slope_proxy(20d): 0.000608

### Volume (if available)

- volume: 36338484.00
- volume_MA20: 38155279.20
- volume_ratio: 0.95

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 15.81
- MA20 / MA60 / MA200: 11.86 / 9.66 / 11.36
- gap20 / gap60: 33.29% / 63.74%
- 5D return: 20.85%
- 20D high/low: 15.81 / 9.30

### Relative Strength

- ratio: 0.056285
- ratio_MA60: 0.043476
- ratio_gap: 29.46%
- ratio_slope_proxy(20d): 0.004852

### Volume (if available)

- volume: 67514936.00
- volume_MA20: 31538011.80
- volume_ratio: 2.14

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-22**
- 실행시간(UTC): **2026-03-23 03:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 39.0 bp / latest 3.27
- IG OAS 4주 변화: 11.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.88
- VIX: 24.06
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -2.22% / slope_proxy: -0.006969
- GDXJ/GLD gap: -13.60% / slope_proxy: 0.005117

## VZLA (Vizsla Silver)
- close: 3.0 | RSI14: 26.701477 | ATR14%: 9.91%
- MA20 gap: -22.54% | MA50 gap: -35.88% | MA200 gap: -28.42%
- vol_ratio(Volume/Vol20): 0.743796 | gap_open: 0.31%
- RS vs SILJ gap: -22.45% / slope_proxy: -0.027562
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
- close: 7.14 | RSI14: 28.476701 | ATR14%: 13.11%
- MA20 gap: -30.40% | MA50 gap: -36.57% | MA200 gap: 0.38%
- vol_ratio(Volume/Vol20): 1.303587 | gap_open: 2.51%
- SilverMarginGate: SI=65.540001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.07% / slope_proxy: -0.008078
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
- close: 30.0 | RSI14: 37.019241 | ATR14%: 16.67%
- MA20 gap: -29.68% | MA50 gap: -25.68% | MA200 gap: 88.36%
- vol_ratio(Volume/Vol20): 2.496138 | gap_open: 0.91%
- RS vs SILJ gap: 1.16% / slope_proxy: 0.247567
- RS vs GDXJ gap: 0.17% / slope_proxy: 0.064967
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
