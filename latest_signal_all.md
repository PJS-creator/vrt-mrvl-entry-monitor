# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-02-27**
- 실행시간(UTC): **2026-03-02 09:56:03**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.98 / 4주 변화 21.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 8.0 bp
- 10Y Real Yield (DFII10): 1.74 / 4주 변화 -15.0 bp
- VIX (VIXCLS): 18.63
- NFCI: -0.5629

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.575866
- MA60: 6.236109
- gap: 21.48%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.201024
- MA60: 0.217652
- gap: -7.64%
- MA60_slope_proxy: -0.018845
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-02**
- 실행시간(UTC): **2026-03-02 09:56:08**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 58.5 bp / 4주 변화 -16.33 bp
- CURVE_10s5s: 61.23 bp / 4주 변화 6.06 bp

## NWG Price
- close: 595.4
- MA50: 639.204 / gap50: -6.85%
- MA200: 567.4527 / gap200: 4.93%

## Relative Strength
- RS vs FTSE gap: -12.16% / slope_proxy: -0.001247
- RS vs Peers gap: -9.98% / slope_proxy: -0.052429

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-02 09:56:15**

## Commodity Regime

- WTI ref (CL=F): 72.04 / 5D 8.64%
- Brent ref (BZ=F): 78.70 / 5D 10.09%
- Brent Tier: **70-80**
- Brent-WTI spread: 6.66
- Gas ref (NG=F): 3.01 / 5D 0.80%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 53.08
- MA20 / MA60 / MA200: 48.03 / 43.97 / 43.52
- gap20 / gap60: 10.52% / 20.72%
- 5D return: 2.39%
- 20D high/low: 53.08 / 43.80

### Relative Strength

- ratio: 0.949213
- ratio_MA60: 0.902948
- ratio_gap: 5.12%
- ratio_slope_proxy(20d): -0.011878

### Volume (if available)

- volume: 13106500.00
- volume_MA20: 12661490.00
- volume_ratio: 1.04

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.63
- MA20 / MA60 / MA200: 15.60 / 13.54 / 12.60
- gap20 / gap60: 6.63% / 22.86%
- 5D return: 5.32%
- 20D high/low: 16.71 / 14.87

### Relative Strength

- ratio: 0.429383
- ratio_MA60: 0.387788
- ratio_gap: 10.73%
- ratio_slope_proxy(20d): 0.001099

### Volume (if available)

- volume: 19920100.00
- volume_MA20: 22999310.00
- volume_ratio: 0.87

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

- close: 6.48
- MA20 / MA60 / MA200: 5.88 / 4.84 / 3.68
- gap20 / gap60: 10.20% / 33.96%
- 5D return: -0.61%
- 20D high/low: 6.54 / 4.82

### Relative Strength

- ratio: 0.016324
- ratio_MA60: 0.014559
- ratio_gap: 12.12%
- ratio_slope_proxy(20d): 0.000345

### Volume (if available)

- volume: 35511100.00
- volume_MA20: 67434595.00
- volume_ratio: 0.53

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **True**

### Trend

- close: 9.69
- MA20 / MA60 / MA200: 9.55 / 8.09 / 11.26
- gap20 / gap60: 1.46% / 19.75%
- 5D return: 0.00%
- 20D high/low: 10.17 / 8.77

### Relative Strength

- ratio: 0.041106
- ratio_MA60: 0.039301
- ratio_gap: 4.59%
- ratio_slope_proxy(20d): 0.002324

### Volume (if available)

- volume: 11739400.00
- volume_MA20: 9413225.00
- volume_ratio: 1.25

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG
