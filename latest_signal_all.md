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
- 실행시간(UTC): **2026-03-20 15:00:38**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.27 / 4주 변화 39.0 bp
- IG OAS (BAMLC0A0CM): 0.9 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 1.86 / 4주 변화 6.0 bp
- VIX (VIXCLS): 24.06
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.324367
- MA60: 6.786936
- gap: 22.65%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.231694
- MA60: 0.21056
- gap: 10.04%
- MA60_slope_proxy: -0.012107
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-20**
- 실행시간(UTC): **2026-03-20 15:00:42**

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
- close: 527.2
- MA50: 618.0792 / gap50: -14.70%
- MA200: 570.714 / gap200: -7.62%

## Relative Strength
- RS vs FTSE gap: -12.58% / slope_proxy: -0.002913
- RS vs Peers gap: -5.71% / slope_proxy: -0.054203

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-20 15:00:50**

## Commodity Regime

- WTI ref (CL=F): 96.65 / 5D -2.09%
- Brent ref (BZ=F): 105.23 / 5D 2.03%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.58
- Gas ref (NG=F): 3.08 / 5D -1.50%

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

- close: 60.91
- MA20 / MA60 / MA200: 54.99 / 47.59 / 44.43
- gap20 / gap60: 10.76% / 27.98%
- 5D return: 5.24%
- 20D high/low: 60.91 / 50.70

### Relative Strength

- ratio: 1.014744
- ratio_MA60: 0.915575
- ratio_gap: 10.83%
- ratio_slope_proxy(20d): 0.017642

### Volume (if available)

- volume: 8444731.00
- volume_MA20: 19426761.55
- volume_ratio: 0.43

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.01
- MA20 / MA60 / MA200: 17.90 / 15.08 / 13.13
- gap20 / gap60: 6.23% / 26.05%
- 5D return: 2.38%
- 20D high/low: 19.78 / 16.14

### Relative Strength

- ratio: 0.536215
- ratio_MA60: 0.417391
- ratio_gap: 28.47%
- ratio_slope_proxy(20d): 0.031835

### Volume (if available)

- volume: 13776105.00
- volume_MA20: 33792005.25
- volume_ratio: 0.41

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

- close: 6.38
- MA20 / MA60 / MA200: 6.31 / 5.35 / 3.95
- gap20 / gap60: 1.16% / 19.19%
- 5D return: 0.32%
- 20D high/low: 6.58 / 5.93

### Relative Strength

- ratio: 0.016321
- ratio_MA60: 0.015066
- ratio_gap: 8.33%
- ratio_slope_proxy(20d): 0.000612

### Volume (if available)

- volume: 6103418.00
- volume_MA20: 36641290.90
- volume_ratio: 0.17

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

- close: 15.54
- MA20 / MA60 / MA200: 11.85 / 9.65 / 11.36
- gap20 / gap60: 31.13% / 60.97%
- 5D return: 18.75%
- 20D high/low: 15.54 / 9.30

### Relative Strength

- ratio: 0.053810
- ratio_MA60: 0.043434
- ratio_gap: 23.89%
- ratio_slope_proxy(20d): 0.004810

### Volume (if available)

- volume: 19619415.00
- volume_MA20: 29136400.75
- volume_ratio: 0.67

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

- 데이터 기준일(주가): **2026-03-20**
- 실행시간(UTC): **2026-03-20 15:01:00**

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
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.86
- VIX: 24.06
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -3.05% / slope_proxy: -0.00703
- GDXJ/GLD gap: -13.62% / slope_proxy: 0.005116

## VZLA (Vizsla Silver)
- close: 3.09 | RSI14: 27.82125 | ATR14%: 9.41%
- MA20 gap: -20.31% | MA50 gap: -33.99% | MA200 gap: -26.28%
- vol_ratio(Volume/Vol20): 0.190133 | gap_open: 0.31%
- RS vs SILJ gap: -21.45% / slope_proxy: -0.027537
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
- close: 7.27 | RSI14: 29.012132 | ATR14%: 12.76%
- MA20 gap: -29.17% | MA50 gap: -35.43% | MA200 gap: 2.19%
- vol_ratio(Volume/Vol20): 0.223989 | gap_open: 2.51%
- SilverMarginGate: SI=69.474998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.95% / slope_proxy: -0.008072
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
- close: 31.0375 | RSI14: 38.005574 | ATR14%: 15.80%
- MA20 gap: -27.34% | MA50 gap: -23.14% | MA200 gap: 94.81%
- vol_ratio(Volume/Vol20): 0.224142 | gap_open: 0.91%
- RS vs SILJ gap: 2.91% / slope_proxy: 0.247901
- RS vs GDXJ gap: 2.12% / slope_proxy: 0.065062
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
