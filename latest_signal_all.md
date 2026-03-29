# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-27**
- 실행시간(UTC): **2026-03-29 03:00:34**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.21 / 4주 변화 23.0 bp
- IG OAS (BAMLC0A0CM): 0.88 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.08 / 4주 변화 34.0 bp
- VIX (VIXCLS): 27.44
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.232344
- MA60: 7.004319
- gap: 17.53%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.25352
- MA60: 0.211053
- gap: 20.12%
- MA60_slope_proxy: -0.006599
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-27**
- 실행시간(UTC): **2026-03-29 03:00:38**

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
- TERM_SPREAD_10Y_POLICY: 102.21 bp / 4주 변화 40.77 bp
- CURVE_10s5s: 39.75 bp / 4주 변화 -19.39 bp

## NWG Price
- close: 539.8
- MA50: 607.7725 / gap50: -11.18%
- MA200: 571.1814 / gap200: -5.49%

## Relative Strength
- RS vs FTSE gap: -9.03% / slope_proxy: -0.003251
- RS vs Peers gap: -5.06% / slope_proxy: -0.048616

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-29 03:00:43**

## Commodity Regime

- WTI ref (CL=F): 99.64 / 5D 1.34%
- Brent ref (BZ=F): 112.57 / 5D 0.34%
- Brent Tier: **>=90**
- Brent-WTI spread: 12.93
- Gas ref (NG=F): 3.10 / 5D 0.00%

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

- close: 65.32
- MA20 / MA60 / MA200: 57.71 / 49.46 / 44.94
- gap20 / gap60: 13.19% / 32.07%
- 5D return: 7.59%
- 20D high/low: 65.32 / 52.99

### Relative Strength

- ratio: 1.044118
- ratio_MA60: 0.926039
- ratio_gap: 12.75%
- ratio_slope_proxy(20d): 0.027358

### Volume (if available)

- volume: 20133800.00
- volume_MA20: 22127035.00
- volume_ratio: 0.91

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.77
- MA20 / MA60 / MA200: 18.75 / 15.77 / 13.35
- gap20 / gap60: 10.76% / 31.73%
- 5D return: 10.48%
- 20D high/low: 20.77 / 16.73

### Relative Strength

- ratio: 0.567022
- ratio_MA60: 0.431584
- ratio_gap: 31.38%
- ratio_slope_proxy(20d): 0.043796

### Volume (if available)

- volume: 29808500.00
- volume_MA20: 38199705.00
- volume_ratio: 0.78

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

- close: 6.93
- MA20 / MA60 / MA200: 6.37 / 5.57 / 4.05
- gap20 / gap60: 8.74% / 24.33%
- 5D return: 11.41%
- 20D high/low: 6.93 / 5.93

### Relative Strength

- ratio: 0.016651
- ratio_MA60: 0.015244
- ratio_gap: 9.23%
- ratio_slope_proxy(20d): 0.000685

### Volume (if available)

- volume: 38356700.00
- volume_MA20: 38442660.00
- volume_ratio: 1.00

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

- close: 17.53
- MA20 / MA60 / MA200: 13.67 / 10.46 / 11.39
- gap20 / gap60: 28.19% / 67.59%
- 5D return: 10.88%
- 20D high/low: 17.53 / 11.14

### Relative Strength

- ratio: 0.059041
- ratio_MA60: 0.045186
- ratio_gap: 30.66%
- ratio_slope_proxy(20d): 0.005938

### Volume (if available)

- volume: 27021200.00
- volume_MA20: 38894775.00
- volume_ratio: 0.69

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

- 데이터 기준일(주가): **2026-03-27**
- 실행시간(UTC): **2026-03-29 03:00:49**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.21
- IG OAS 4주 변화: 6.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 34.0 bp / latest 2.08
- VIX: 27.44
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.12% / slope_proxy: -0.004493
- GDXJ/GLD gap: -8.59% / slope_proxy: -0.000526

## VZLA (Vizsla Silver)
- close: 3.15 | RSI14: 34.873812 | ATR14%: 8.49%
- MA20 gap: -13.50% | MA50 gap: -28.65% | MA200 gap: -24.70%
- vol_ratio(Volume/Vol20): 0.802854 | gap_open: 0.00%
- RS vs SILJ gap: -19.15% / slope_proxy: -0.027254
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
- close: 7.73 | RSI14: 37.701043 | ATR14%: 11.29%
- MA20 gap: -15.21% | MA50 gap: -29.39% | MA200 gap: 6.88%
- vol_ratio(Volume/Vol20): 0.60972 | gap_open: 0.14%
- SilverMarginGate: SI=69.544998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.56% / slope_proxy: -0.018248
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

## HYMC (Hycroft Mining)
- close: 33.049999 | RSI14: 43.318327 | ATR14%: 13.58%
- MA20 gap: -15.20% | MA50 gap: -18.51% | MA200 gap: 98.58%
- vol_ratio(Volume/Vol20): 0.522497 | gap_open: 1.51%
- RS vs SILJ gap: 2.84% / slope_proxy: 0.208319
- RS vs GDXJ gap: 1.93% / slope_proxy: 0.054714
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
