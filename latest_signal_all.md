# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-31**
- 실행시간(UTC): **2026-04-01 03:00:34**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.46 / 4주 변화 43.0 bp
- IG OAS (BAMLC0A0CM): 0.93 / 4주 변화 8.0 bp
- 10Y Real Yield (DFII10): 2.04 / 4주 변화 28.0 bp
- VIX (VIXCLS): 30.61
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.026265
- MA60: 7.07034
- gap: 13.52%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.258346
- MA60: 0.211478
- gap: 22.16%
- MA60_slope_proxy: -0.003882
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-31**
- 실행시간(UTC): **2026-04-01 03:00:48**

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
- TERM_SPREAD_10Y_POLICY: 114.35 bp / 4주 변화 60.0 bp
- CURVE_10s5s: 39.75 bp / 4주 변화 -19.88 bp

## NWG Price
- close: 553.2
- MA50: 603.7988 / gap50: -8.38%
- MA200: 571.4794 / gap200: -3.20%

## Relative Strength
- RS vs FTSE gap: -8.08% / slope_proxy: -0.00336
- RS vs Peers gap: -4.04% / slope_proxy: -0.04671

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-01 03:00:54**

## Commodity Regime

- WTI ref (CL=F): 102.79 / 5D 11.30%
- Brent ref (BZ=F): 105.40 / 5D 0.87%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.61
- Gas ref (NG=F): 2.87 / 5D -2.45%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **False**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 65.00
- MA20 / MA60 / MA200: 58.90 / 50.26 / 45.16
- gap20 / gap60: 10.36% / 29.32%
- 5D return: 6.12%
- 20D high/low: 66.24 / 52.99

### Relative Strength

- ratio: 1.061051
- ratio_MA60: 0.936177
- ratio_gap: 13.34%
- ratio_slope_proxy(20d): 0.030971

### Volume (if available)

- volume: 33831050.00
- volume_MA20: 22132277.50
- volume_ratio: 1.53

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.75
- MA20 / MA60 / MA200: 19.12 / 16.06 / 13.44
- gap20 / gap60: 8.55% / 29.17%
- 5D return: 5.06%
- 20D high/low: 20.81 / 16.73

### Relative Strength

- ratio: 0.540505
- ratio_MA60: 0.437639
- ratio_gap: 23.50%
- ratio_slope_proxy(20d): 0.047552

### Volume (if available)

- volume: 50697402.00
- volume_MA20: 38638600.10
- volume_ratio: 1.31

### Checks

- RISK_OK_SOFT: **False**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.63
- MA20 / MA60 / MA200: 6.42 / 5.66 / 4.08
- gap20 / gap60: 3.29% / 17.23%
- 5D return: 0.00%
- 20D high/low: 6.93 / 5.93

### Relative Strength

- ratio: 0.016402
- ratio_MA60: 0.015313
- ratio_gap: 7.12%
- ratio_slope_proxy(20d): 0.000723

### Volume (if available)

- volume: 35964559.00
- volume_MA20: 37487882.95
- volume_ratio: 0.96

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 15.76
- MA20 / MA60 / MA200: 14.17 / 10.77 / 11.39
- gap20 / gap60: 11.25% / 46.29%
- 5D return: -5.06%
- 20D high/low: 17.53 / 11.14

### Relative Strength

- ratio: 0.055540
- ratio_MA60: 0.045890
- ratio_gap: 21.03%
- ratio_slope_proxy(20d): 0.006184

### Volume (if available)

- volume: 44475918.00
- volume_MA20: 37432135.90
- volume_ratio: 1.19

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

- 데이터 기준일(주가): **2026-03-31**
- 실행시간(UTC): **2026-04-01 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 43.0 bp / latest 3.46
- IG OAS 4주 변화: 8.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.04
- VIX: 30.61
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -0.60% / slope_proxy: -0.00441
- GDXJ/GLD gap: -4.23% / slope_proxy: -0.002244

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 40.337176 | ATR14%: 7.81%
- MA20 gap: -6.81% | MA50 gap: -23.27% | MA200 gap: -21.07%
- vol_ratio(Volume/Vol20): 1.21327 | gap_open: 2.24%
- RS vs SILJ gap: -18.96% / slope_proxy: -0.027268
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.57 | RSI14: 45.853456 | ATR14%: 10.07%
- MA20 gap: -2.20% | MA50 gap: -20.74% | MA200 gap: 17.65%
- vol_ratio(Volume/Vol20): 1.414339 | gap_open: 2.50%
- SilverMarginGate: SI=74.184998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.66% / slope_proxy: -0.019469
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 35.200001 | RSI14: 47.618437 | ATR14%: 12.81%
- MA20 gap: -4.99% | MA50 gap: -13.06% | MA200 gap: 107.88%
- vol_ratio(Volume/Vol20): 0.85693 | gap_open: 3.45%
- RS vs SILJ gap: 1.83% / slope_proxy: 0.186934
- RS vs GDXJ gap: -0.81% / slope_proxy: 0.04907
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
