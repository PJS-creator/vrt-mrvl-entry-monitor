# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: OXY, VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-01**
- 실행시간(UTC): **2026-05-01 15:00:35**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.83 / 4주 변화 -34.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 -6.0 bp
- VIX (VIXCLS): 16.89
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.257523
- MA60: 8.114201
- gap: 14.09%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.321723
- MA60: 0.246413
- gap: 30.56%
- MA60_slope_proxy: 0.033725
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-01**
- 실행시간(UTC): **2026-05-01 15:00:38**

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
- TERM_SPREAD_10Y_POLICY: 125.53 bp / 4주 변화 22.51 bp
- CURVE_10s5s: 44.29 bp / 4주 변화 0.86 bp

## NWG Price
- close: 564.0
- MA50: 584.0978 / gap50: -3.44%
- MA200: 581.7976 / gap200: -3.06%

## Relative Strength
- RS vs FTSE gap: -3.81% / slope_proxy: -0.002458
- RS vs Peers gap: -8.31% / slope_proxy: -0.037547

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-01 15:00:45**

## Commodity Regime

- WTI ref (CL=F): 101.51 / 5D 7.53%
- Brent ref (BZ=F): 108.38 / 5D 2.90%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.87
- Gas ref (NG=F): 2.77 / 5D 9.75%

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

- close: 58.97
- MA20 / MA60 / MA200: 58.05 / 55.79 / 46.80
- gap20 / gap60: 1.58% / 5.70%
- 5D return: 3.24%
- 20D high/low: 62.96 / 53.79

### Relative Strength

- ratio: 0.999576
- ratio_MA60: 0.978748
- ratio_gap: 2.13%
- ratio_slope_proxy(20d): 0.037221

### Volume (if available)

- volume: 4955582.00
- volume_MA20: 13012144.10
- volume_ratio: 0.38

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.76
- MA20 / MA60 / MA200: 21.03 / 18.75 / 14.30
- gap20 / gap60: 3.48% / 16.07%
- 5D return: 4.26%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.552635
- ratio_MA60: 0.487192
- ratio_gap: 13.43%
- ratio_slope_proxy(20d): 0.046272

### Volume (if available)

- volume: 3257455.00
- volume_MA20: 22226792.75
- volume_ratio: 0.15

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

- close: 6.65
- MA20 / MA60 / MA200: 6.41 / 6.33 / 4.48
- gap20 / gap60: 3.74% / 5.13%
- 5D return: 8.84%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015067
- ratio_MA60: 0.015914
- ratio_gap: -5.33%
- ratio_slope_proxy(20d): 0.000516

### Volume (if available)

- volume: 7522630.00
- volume_MA20: 30190036.50
- volume_ratio: 0.25

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

- close: 12.94
- MA20 / MA60 / MA200: 12.92 / 12.45 / 11.01
- gap20 / gap60: 0.17% / 3.97%
- 5D return: 8.74%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.048050
- ratio_MA60: 0.048556
- ratio_gap: -1.04%
- ratio_slope_proxy(20d): 0.002081

### Volume (if available)

- volume: 8085267.00
- volume_MA20: 22577913.35
- volume_ratio: 0.36

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: OXY, VG


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-01**
- 실행시간(UTC): **2026-05-01 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.83
- IG OAS 4주 변화: -5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -6.0 bp / latest 1.96
- VIX: 16.89
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -5.64% / slope_proxy: 0.01381
- GDXJ/GLD gap: -5.13% / slope_proxy: -0.003953

## VZLA (Vizsla Silver)
- close: 3.365 | RSI14: 46.744853 | ATR14%: 5.81%
- MA20 gap: -0.33% | MA50 gap: -5.25% | MA200 gap: -20.03%
- vol_ratio(Volume/Vol20): 0.206496 | gap_open: 0.59%
- RS vs SILJ gap: 2.02% / slope_proxy: -0.021639
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
- close: 8.1 | RSI14: 45.064467 | ATR14%: 7.68%
- MA20 gap: -3.83% | MA50 gap: -11.11% | MA200 gap: 3.09%
- vol_ratio(Volume/Vol20): 0.27808 | gap_open: 0.64%
- SilverMarginGate: SI=76.294998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.24% / slope_proxy: -0.031536
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
- close: 37.259998 | RSI14: 48.362365 | ATR14%: 8.95%
- MA20 gap: -3.73% | MA50 gap: -5.39% | MA200 gap: 79.20%
- vol_ratio(Volume/Vol20): 0.366925 | gap_open: 0.03%
- RS vs SILJ gap: 5.45% / slope_proxy: 0.035145
- RS vs GDXJ gap: 6.37% / slope_proxy: 0.005153
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
