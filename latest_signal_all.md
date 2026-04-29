# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: OXY, RIG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-28**
- 실행시간(UTC): **2026-04-29 03:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.84 / 4주 변화 -62.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -12.0 bp
- 10Y Real Yield (DFII10): 1.91 / 4주 변화 -13.0 bp
- VIX (VIXCLS): 18.02
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.841449
- MA60: 7.964908
- gap: 11.00%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.311944
- MA60: 0.239987
- gap: 29.98%
- MA60_slope_proxy: 0.028932
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-28**
- 실행시간(UTC): **2026-04-29 03:00:47**

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
- TERM_SPREAD_10Y_POLICY: 112.9 bp / 4주 변화 -1.45 bp
- CURVE_10s5s: 46.01 bp / 4주 변화 6.26 bp

## NWG Price
- close: 577.6
- MA50: 586.7591 / gap50: -1.56%
- MA200: 580.5888 / gap200: -0.51%

## Relative Strength
- RS vs FTSE gap: -2.15% / slope_proxy: -0.002406
- RS vs Peers gap: -5.34% / slope_proxy: -0.036578

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-29 03:00:54**

## Commodity Regime

- WTI ref (CL=F): 99.05 / 5D 7.51%
- Brent ref (BZ=F): 103.87 / 5D 5.47%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.82
- Gas ref (NG=F): 2.67 / 5D -0.93%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **True**

### Trend

- close: 58.61
- MA20 / MA60 / MA200: 58.55 / 55.04 / 46.54
- gap20 / gap60: 0.10% / 6.49%
- 5D return: 4.05%
- 20D high/low: 65.00 / 53.79

### Relative Strength

- ratio: 1.015595
- ratio_MA60: 0.971999
- ratio_gap: 4.49%
- ratio_slope_proxy(20d): 0.038007

### Volume (if available)

- volume: 10417943.00
- volume_MA20: 15593867.15
- volume_ratio: 0.67

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.23
- MA20 / MA60 / MA200: 20.80 / 18.41 / 14.16
- gap20 / gap60: 2.08% / 15.34%
- 5D return: 0.97%
- 20D high/low: 21.84 / 19.86

### Relative Strength

- ratio: 0.534895
- ratio_MA60: 0.479400
- ratio_gap: 11.58%
- ratio_slope_proxy(20d): 0.047134

### Volume (if available)

- volume: 13616232.00
- volume_MA20: 27080661.60
- volume_ratio: 0.50

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **True**

### Trend

- close: 6.79
- MA20 / MA60 / MA200: 6.38 / 6.24 / 4.42
- gap20 / gap60: 6.51% / 8.86%
- 5D return: 12.23%
- 20D high/low: 6.79 / 5.89

### Relative Strength

- ratio: 0.015376
- ratio_MA60: 0.015857
- ratio_gap: -3.04%
- ratio_slope_proxy(20d): 0.000579

### Volume (if available)

- volume: 53641748.00
- volume_MA20: 31903912.40
- volume_ratio: 1.68

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.16
- MA20 / MA60 / MA200: 13.20 / 12.26 / 11.06
- gap20 / gap60: -7.90% / -0.79%
- 5D return: 0.58%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.045890
- ratio_MA60: 0.048370
- ratio_gap: -5.13%
- ratio_slope_proxy(20d): 0.002811

### Volume (if available)

- volume: 14238365.00
- volume_MA20: 25761773.25
- volume_ratio: 0.55

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: OXY, RIG


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-28**
- 실행시간(UTC): **2026-04-29 03:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -62.0 bp / latest 2.84
- IG OAS 4주 변화: -12.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -13.0 bp / latest 1.91
- VIX: 18.02
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -2.87% / slope_proxy: 0.015475
- GDXJ/GLD gap: -3.90% / slope_proxy: -0.003489

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 48.850132 | ATR14%: 5.82%
- MA20 gap: 1.68% | MA50 gap: -4.33% | MA200 gap: -18.69%
- vol_ratio(Volume/Vol20): 0.868294 | gap_open: 3.41%
- RS vs SILJ gap: 2.48% / slope_proxy: -0.024188
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
- close: 7.88 | RSI14: 41.536836 | ATR14%: 8.52%
- MA20 gap: -6.91% | MA50 gap: -14.46% | MA200 gap: 1.05%
- vol_ratio(Volume/Vol20): 0.808807 | gap_open: 3.57%
- SilverMarginGate: SI=74.214996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.96% / slope_proxy: -0.030344
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
- close: 35.66 | RSI14: 43.969588 | ATR14%: 9.90%
- MA20 gap: -7.66% | MA50 gap: -9.85% | MA200 gap: 75.58%
- vol_ratio(Volume/Vol20): 0.879205 | gap_open: 2.64%
- RS vs SILJ gap: 1.66% / slope_proxy: 0.043554
- RS vs GDXJ gap: 1.16% / slope_proxy: 0.007666
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
