# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-09**
- 실행시간(UTC): **2026-04-10 03:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.94 / 4주 변화 -15.0 bp
- IG OAS (BAMLC0A0CM): 0.83 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 11.0 bp
- VIX (VIXCLS): 21.04
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.593965
- MA60: 7.320187
- gap: 17.40%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.278706
- MA60: 0.21669
- gap: 28.62%
- MA60_slope_proxy: 0.004792
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-09**
- 실행시간(UTC): **2026-04-10 03:00:54**

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
- TERM_SPREAD_10Y_POLICY: 112.4 bp / 4주 변화 37.3 bp
- CURVE_10s5s: 41.7 bp / 4주 변화 -9.1 bp

## NWG Price
- close: 605.2
- MA50: 597.2887 / gap50: 1.32%
- MA200: 573.5542 / gap200: 5.52%

## Relative Strength
- RS vs FTSE gap: -2.54% / slope_proxy: -0.003288
- RS vs Peers gap: -3.43% / slope_proxy: -0.041693

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-10 03:01:01**

## Commodity Regime

- WTI ref (CL=F): 98.68 / 5D -1.44%
- Brent ref (BZ=F): 96.58 / 5D -4.53%
- Brent Tier: **>=90**
- Brent-WTI spread: -2.10
- Gas ref (NG=F): 2.67 / 5D -5.18%

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

- close: 58.53
- MA20 / MA60 / MA200: 61.18 / 52.23 / 45.67
- gap20 / gap60: -4.34% / 12.07%
- 5D return: -5.95%
- 20D high/low: 66.24 / 57.25

### Relative Strength

- ratio: 1.020931
- ratio_MA60: 0.949327
- ratio_gap: 7.54%
- ratio_slope_proxy(20d): 0.039503

### Volume (if available)

- volume: 15380758.00
- volume_MA20: 20937437.90
- volume_ratio: 0.73

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.69
- MA20 / MA60 / MA200: 19.95 / 16.94 / 13.68
- gap20 / gap60: 3.72% / 22.15%
- 5D return: 3.04%
- 20D high/low: 20.86 / 18.57

### Relative Strength

- ratio: 0.510360
- ratio_MA60: 0.454564
- ratio_gap: 12.27%
- ratio_slope_proxy(20d): 0.055235

### Volume (if available)

- volume: 29189931.00
- volume_MA20: 36294541.55
- volume_ratio: 0.80

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

- close: 6.56
- MA20 / MA60 / MA200: 6.55 / 5.89 / 4.19
- gap20 / gap60: 0.21% / 11.40%
- 5D return: 0.92%
- 20D high/low: 6.93 / 6.20

### Relative Strength

- ratio: 0.015960
- ratio_MA60: 0.015579
- ratio_gap: 2.44%
- ratio_slope_proxy(20d): 0.000823

### Volume (if available)

- volume: 20493742.00
- volume_MA20: 35743047.10
- volume_ratio: 0.57

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

- close: 12.99
- MA20 / MA60 / MA200: 15.04 / 11.54 / 11.31
- gap20 / gap60: -13.64% / 12.57%
- 5D return: -11.51%
- 20D high/low: 17.53 / 12.28

### Relative Strength

- ratio: 0.048877
- ratio_MA60: 0.047560
- ratio_gap: 2.77%
- ratio_slope_proxy(20d): 0.006391

### Volume (if available)

- volume: 39226539.00
- volume_MA20: 38327016.95
- volume_ratio: 1.02

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

- 데이터 기준일(주가): **2026-04-09**
- 실행시간(UTC): **2026-04-10 03:01:14**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -15.0 bp / latest 2.94
- IG OAS 4주 변화: -5.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 11.0 bp / latest 1.96
- VIX: 21.04
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 3.62% / slope_proxy: 0.001888
- GDXJ/GLD gap: 0.47% / slope_proxy: -0.004642

## VZLA (Vizsla Silver)
- close: 3.27 | RSI14: 41.200512 | ATR14%: 6.98%
- MA20 gap: -1.00% | MA50 gap: -16.53% | MA200 gap: -21.74%
- vol_ratio(Volume/Vol20): 0.660132 | gap_open: 0.61%
- RS vs SILJ gap: -19.03% / slope_proxy: -0.02743
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
- close: 8.13 | RSI14: 44.551418 | ATR14%: 9.96%
- MA20 gap: 0.34% | MA50 gap: -19.02% | MA200 gap: 9.31%
- vol_ratio(Volume/Vol20): 0.358157 | gap_open: 0.50%
- SilverMarginGate: SI=75.599998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.62% / slope_proxy: -0.022582
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
- close: 38.970001 | RSI14: 54.072179 | ATR14%: 10.78%
- MA20 gap: 10.55% | MA50 gap: -0.58% | MA200 gap: 117.27%
- vol_ratio(Volume/Vol20): 0.686621 | gap_open: 0.49%
- RS vs SILJ gap: 4.62% / slope_proxy: 0.133664
- RS vs GDXJ gap: 1.14% / slope_proxy: 0.034933
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
