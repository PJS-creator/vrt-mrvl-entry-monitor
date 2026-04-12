# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-10**
- 실행시간(UTC): **2026-04-12 03:00:39**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.9 / 4주 변화 -27.0 bp
- IG OAS (BAMLC0A0CM): 0.83 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 1.95 / 4주 변화 6.0 bp
- VIX (VIXCLS): 19.49
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.815305
- MA60: 7.370836
- gap: 19.60%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.294108
- MA60: 0.21795
- gap: 34.94%
- MA60_slope_proxy: 0.006376
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-10**
- 실행시간(UTC): **2026-04-12 03:00:41**

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
- TERM_SPREAD_10Y_POLICY: 90.99 bp / 4주 변화 2.11 bp
- CURVE_10s5s: 44.14 bp / 4주 변화 -5.36 bp

## NWG Price
- close: 614.4
- MA50: 596.4379 / gap50: 3.01%
- MA200: 574.1267 / gap200: 7.01%

## Relative Strength
- RS vs FTSE gap: -0.92% / slope_proxy: -0.003242
- RS vs Peers gap: -2.59% / slope_proxy: -0.040886

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-12 03:00:48**

## Commodity Regime

- WTI ref (CL=F): 96.57 / 5D -13.42%
- Brent ref (BZ=F): 95.20 / 5D -12.68%
- Brent Tier: **>=90**
- Brent-WTI spread: -1.37
- Gas ref (NG=F): 2.65 / 5D -5.43%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 57.97
- MA20 / MA60 / MA200: 61.16 / 52.47 / 45.75
- gap20 / gap60: -5.22% / 10.48%
- 5D return: -7.94%
- 20D high/low: 66.24 / 57.25

### Relative Strength

- ratio: 1.018089
- ratio_MA60: 0.950910
- ratio_gap: 7.06%
- ratio_slope_proxy(20d): 0.039243

### Volume (if available)

- volume: 10466100.00
- volume_MA20: 19496710.00
- volume_ratio: 0.54

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.51
- MA20 / MA60 / MA200: 20.07 / 17.09 / 13.72
- gap20 / gap60: 7.15% / 25.85%
- 5D return: 4.62%
- 20D high/low: 21.51 / 18.57

### Relative Strength

- ratio: 0.520445
- ratio_MA60: 0.456956
- ratio_gap: 13.89%
- ratio_slope_proxy(20d): 0.055179

### Volume (if available)

- volume: 27484600.00
- volume_MA20: 35031040.00
- volume_ratio: 0.78

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.52
- MA20 / MA60 / MA200: 6.56 / 5.93 / 4.21
- gap20 / gap60: -0.59% / 10.03%
- 5D return: -1.06%
- 20D high/low: 6.93 / 6.20

### Relative Strength

- ratio: 0.015911
- ratio_MA60: 0.015621
- ratio_gap: 1.86%
- ratio_slope_proxy(20d): 0.000818

### Volume (if available)

- volume: 21201100.00
- volume_MA20: 35266125.00
- volume_ratio: 0.60

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.97
- MA20 / MA60 / MA200: 15.05 / 11.62 / 11.29
- gap20 / gap60: -13.83% / 11.57%
- 5D return: -11.41%
- 20D high/low: 17.53 / 12.28

### Relative Strength

- ratio: 0.048844
- ratio_MA60: 0.047695
- ratio_gap: 2.41%
- ratio_slope_proxy(20d): 0.006230

### Volume (if available)

- volume: 24742600.00
- volume_MA20: 38375345.00
- volume_ratio: 0.64

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-10**
- 실행시간(UTC): **2026-04-12 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -27.0 bp / latest 2.9
- IG OAS 4주 변화: -8.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.95
- VIX: 19.49
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 2.44% / slope_proxy: 0.003438
- GDXJ/GLD gap: 1.44% / slope_proxy: -0.004706

## VZLA (Vizsla Silver)
- close: 3.25 | RSI14: 40.610788 | ATR14%: 6.83%
- MA20 gap: -0.66% | MA50 gap: -15.48% | MA200 gap: -22.24%
- vol_ratio(Volume/Vol20): 0.641437 | gap_open: 1.53%
- RS vs SILJ gap: -18.72% / slope_proxy: -0.027499
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.99 | RSI14: 43.405859 | ATR14%: 9.77%
- MA20 gap: -0.24% | MA50 gap: -19.26% | MA200 gap: 7.05%
- vol_ratio(Volume/Vol20): 0.625312 | gap_open: 0.12%
- SilverMarginGate: SI=76.323997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.66% / slope_proxy: -0.022885
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 37.5 | RSI14: 51.198048 | ATR14%: 11.12%
- MA20 gap: 6.78% | MA50 gap: -3.63% | MA200 gap: 107.09%
- vol_ratio(Volume/Vol20): 0.7082 | gap_open: 0.41%
- RS vs SILJ gap: 0.45% / slope_proxy: 0.124203
- RS vs GDXJ gap: -3.53% / slope_proxy: 0.032231
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
