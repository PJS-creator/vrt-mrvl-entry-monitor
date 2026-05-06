# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-05**
- 실행시간(UTC): **2026-05-06 03:00:50**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.78 / 4주 변화 -27.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.95 / 4주 변화 -3.0 bp
- VIX (VIXCLS): 18.29
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.748999
- MA60: 8.230317
- gap: 18.45%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.322849
- MA60: 0.250633
- gap: 28.81%
- MA60_slope_proxy: 0.036106
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-05**
- 실행시간(UTC): **2026-05-06 03:01:04**

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
- TERM_SPREAD_10Y_POLICY: 121.09 bp / 4주 변화 18.29 bp
- CURVE_10s5s: 46.73 bp / 4주 변화 4.4 bp

## NWG Price
- close: 545.0
- MA50: 582.6907 / gap50: -6.47%
- MA200: 582.051 / gap200: -6.37%

## Relative Strength
- RS vs FTSE gap: -5.46% / slope_proxy: -0.002468
- RS vs Peers gap: -6.51% / slope_proxy: -0.03891

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-06 03:01:13**

## Commodity Regime

- WTI ref (CL=F): 100.71 / 5D 0.78%
- Brent ref (BZ=F): 108.14 / 5D -2.80%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.43
- Gas ref (NG=F): 2.77 / 5D 8.44%

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

- close: 59.34
- MA20 / MA60 / MA200: 57.73 / 56.26 / 46.97
- gap20 / gap60: 2.79% / 5.47%
- 5D return: 1.25%
- 20D high/low: 60.76 / 53.79

### Relative Strength

- ratio: 0.998150
- ratio_MA60: 0.983326
- ratio_gap: 1.51%
- ratio_slope_proxy(20d): 0.037449

### Volume (if available)

- volume: 9135957.00
- volume_MA20: 13176717.85
- volume_ratio: 0.69

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.77
- MA20 / MA60 / MA200: 21.16 / 18.99 / 14.40
- gap20 / gap60: 2.89% / 14.67%
- 5D return: 2.54%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.548225
- ratio_MA60: 0.492523
- ratio_gap: 11.31%
- ratio_slope_proxy(20d): 0.045507

### Volume (if available)

- volume: 12779492.00
- volume_MA20: 22263824.60
- volume_ratio: 0.57

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

- close: 6.25
- MA20 / MA60 / MA200: 6.41 / 6.38 / 4.52
- gap20 / gap60: -2.54% / -1.97%
- 5D return: -7.95%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.014182
- ratio_MA60: 0.015935
- ratio_gap: -11.00%
- ratio_slope_proxy(20d): 0.000445

### Volume (if available)

- volume: 60346896.00
- volume_MA20: 33654494.80
- volume_ratio: 1.79

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.02
- MA20 / MA60 / MA200: 12.65 / 12.57 / 10.99
- gap20 / gap60: 2.92% / 3.59%
- 5D return: 7.07%
- 20D high/low: 14.44 / 11.45

### Relative Strength

- ratio: 0.048308
- ratio_MA60: 0.048675
- ratio_gap: -0.75%
- ratio_slope_proxy(20d): 0.001547

### Volume (if available)

- volume: 14256149.00
- volume_MA20: 22633207.45
- volume_ratio: 0.63

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-05**
- 실행시간(UTC): **2026-05-06 03:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -27.0 bp / latest 2.78
- IG OAS 4주 변화: -5.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -3.0 bp / latest 1.95
- VIX: 18.29
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -4.59% / slope_proxy: 0.011546
- GDXJ/GLD gap: -5.71% / slope_proxy: -0.003842

## VZLA (Vizsla Silver)
- close: 3.23 | RSI14: 42.006251 | ATR14%: 6.21%
- MA20 gap: -4.55% | MA50 gap: -8.48% | MA200 gap: -23.26%
- vol_ratio(Volume/Vol20): 0.568498 | gap_open: 1.49%
- RS vs SILJ gap: 1.50% / slope_proxy: -0.019585
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
- close: 7.78 | RSI14: 41.918332 | ATR14%: 7.91%
- MA20 gap: -7.47% | MA50 gap: -13.14% | MA200 gap: -1.47%
- vol_ratio(Volume/Vol20): 0.622958 | gap_open: 1.90%
- SilverMarginGate: SI=75.605003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.63% / slope_proxy: -0.031182
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
- close: 35.369999 | RSI14: 44.904056 | ATR14%: 9.19%
- MA20 gap: -8.65% | MA50 gap: -9.73% | MA200 gap: 67.47%
- vol_ratio(Volume/Vol20): 0.71031 | gap_open: 1.91%
- RS vs SILJ gap: 2.47% / slope_proxy: 0.033331
- RS vs GDXJ gap: 2.79% / slope_proxy: 0.004615
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
