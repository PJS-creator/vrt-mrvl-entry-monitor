# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-10**
- 실행시간(UTC): **2026-03-10 15:00:38**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.19 / 4주 변화 35.0 bp
- IG OAS (BAMLC0A0CM): 0.85 / 4주 변화 9.0 bp
- 10Y Real Yield (DFII10): 1.8 / 4주 변화 -8.0 bp
- VIX (VIXCLS): 25.5
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.392109
- MA60: 6.449983
- gap: 30.11%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.233783
- MA60: 0.21215
- gap: 10.20%
- MA60_slope_proxy: -0.017169
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-10**
- 실행시간(UTC): **2026-03-10 15:00:55**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 85.89 bp / 4주 변화 8.69 bp
- CURVE_10s5s: 53.01 bp / 4주 변화 -7.14 bp

## NWG Price
- close: 592.8
- MA50: 632.08 / gap50: -6.21%
- MA200: 569.4085 / gap200: 4.11%

## Relative Strength
- RS vs FTSE gap: -8.10% / slope_proxy: -0.00209
- RS vs Peers gap: -5.63% / slope_proxy: -0.058341

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-10 15:01:02**

## Commodity Regime

- WTI ref (CL=F): 84.44 / 5D 13.25%
- Brent ref (BZ=F): 84.83 / 5D 4.21%
- Brent Tier: **80-90**
- Brent-WTI spread: 0.39
- Gas ref (NG=F): 3.03 / 5D -0.79%

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

- close: 53.74
- MA20 / MA60 / MA200: 50.95 / 45.39 / 43.93
- gap20 / gap60: 5.47% / 18.41%
- 5D return: 0.11%
- 20D high/low: 55.02 / 45.49

### Relative Strength

- ratio: 0.952668
- ratio_MA60: 0.906823
- ratio_gap: 5.06%
- ratio_slope_proxy(20d): -0.002619

### Volume (if available)

- volume: 7350856.00
- volume_MA20: 16618962.80
- volume_ratio: 0.44

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.14
- MA20 / MA60 / MA200: 16.39 / 14.11 / 12.81
- gap20 / gap60: 10.69% / 28.56%
- 5D return: 6.96%
- 20D high/low: 18.16 / 15.02

### Relative Strength

- ratio: 0.480395
- ratio_MA60: 0.397252
- ratio_gap: 20.93%
- ratio_slope_proxy(20d): 0.010244

### Volume (if available)

- volume: 10215116.00
- volume_MA20: 27042060.80
- volume_ratio: 0.38

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

- close: 6.26
- MA20 / MA60 / MA200: 6.23 / 5.04 / 3.80
- gap20 / gap60: 0.43% / 24.11%
- 5D return: 2.46%
- 20D high/low: 6.54 / 5.44

### Relative Strength

- ratio: 0.016245
- ratio_MA60: 0.014720
- ratio_gap: 10.36%
- ratio_slope_proxy(20d): 0.000485

### Volume (if available)

- volume: 7526596.00
- volume_MA20: 58522229.80
- volume_ratio: 0.13

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

- close: 11.39
- MA20 / MA60 / MA200: 10.27 / 8.68 / 11.31
- gap20 / gap60: 10.97% / 31.32%
- 5D return: -0.57%
- 20D high/low: 12.48 / 8.77

### Relative Strength

- ratio: 0.045771
- ratio_MA60: 0.040863
- ratio_gap: 12.01%
- ratio_slope_proxy(20d): 0.003143

### Volume (if available)

- volume: 6844359.00
- volume_MA20: 17652887.95
- volume_ratio: 0.39

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

- 데이터 기준일(주가): **2026-03-10**
- 실행시간(UTC): **2026-03-10 15:01:17**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 35.0 bp / latest 3.19
- IG OAS 4주 변화: 9.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.8
- VIX: 25.5
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 0.33% / slope_proxy: -0.002729
- GDXJ/GLD gap: -0.60% / slope_proxy: 0.012995

## VZLA (Vizsla Silver)
- close: 4.215 | RSI14: 46.704306 | ATR14%: 7.73%
- MA20 gap: 5.59% | MA50 gap: -16.05% | MA200 gap: 1.17%
- vol_ratio(Volume/Vol20): 0.148324 | gap_open: 2.26%
- RS vs SILJ gap: -25.22% / slope_proxy: -0.029159
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

## SCZM (Santacruz Silver)
- close: 10.85 | RSI14: 48.030494 | ATR14%: 9.66%
- MA20 gap: -0.83% | MA50 gap: -5.62% | MA200 gap: 58.43%
- vol_ratio(Volume/Vol20): 0.243582 | gap_open: 4.75%
- SilverMarginGate: SI=89.519997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.47% / slope_proxy: 0.006915
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
- close: 43.884998 | RSI14: 52.372009 | ATR14%: 13.17%
- MA20 gap: 2.92% | MA50 gap: 13.97% | MA200 gap: 201.45%
- vol_ratio(Volume/Vol20): 0.380362 | gap_open: 3.10%
- RS vs SILJ gap: 17.92% / slope_proxy: 0.246389
- RS vs GDXJ gap: 18.74% / slope_proxy: 0.064723
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
