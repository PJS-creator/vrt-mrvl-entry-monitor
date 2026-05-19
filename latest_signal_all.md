# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-18**
- 실행시간(UTC): **2026-05-19 03:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.8 / 4주 변화 -3.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 2.1 / 4주 변화 20.0 bp
- VIX (VIXCLS): 18.43
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.054158
- MA60: 8.701964
- gap: 15.54%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.309305
- MA60: 0.267234
- gap: 15.74%
- MA60_slope_proxy: 0.039719
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-18**
- 실행시간(UTC): **2026-05-19 03:00:50**

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
- TERM_SPREAD_10Y_POLICY: 121.61 bp / 4주 변화 17.49 bp
- CURVE_10s5s: 45.34 bp / 4주 변화 -2.88 bp

## NWG Price
- close: 566.0
- MA50: 575.9191 / gap50: -1.72%
- MA200: 584.6311 / gap200: -3.19%

## Relative Strength
- RS vs FTSE gap: -1.97% / slope_proxy: -0.002155
- RS vs Peers gap: -5.22% / slope_proxy: -0.03648

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-19 03:00:56**

## Commodity Regime

- WTI ref (CL=F): 102.80 / 5D 4.82%
- Brent ref (BZ=F): 109.86 / 5D 5.42%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.06
- Gas ref (NG=F): 3.02 / 5D 3.95%

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

- close: 59.70
- MA20 / MA60 / MA200: 57.49 / 57.59 / 47.53
- gap20 / gap60: 3.85% / 3.66%
- 5D return: 8.27%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.985474
- ratio_MA60: 0.997943
- ratio_gap: -1.25%
- ratio_slope_proxy(20d): 0.037304

### Volume (if available)

- volume: 12245155.00
- volume_MA20: 12203357.75
- volume_ratio: 1.00

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.70
- MA20 / MA60 / MA200: 20.94 / 19.73 / 14.77
- gap20 / gap60: -1.12% / 4.89%
- 5D return: -0.24%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.563419
- ratio_MA60: 0.513108
- ratio_gap: 9.81%
- ratio_slope_proxy(20d): 0.046336

### Volume (if available)

- volume: 22466710.00
- volume_MA20: 17519740.50
- volume_ratio: 1.28

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 7.58
- MA20 / MA60 / MA200: 6.57 / 6.46 / 4.69
- gap20 / gap60: 15.39% / 17.34%
- 5D return: 15.73%
- 20D high/low: 7.58 / 6.05

### Relative Strength

- ratio: 0.016699
- ratio_MA60: 0.015827
- ratio_gap: 5.51%
- ratio_slope_proxy(20d): 0.000015

### Volume (if available)

- volume: 58991868.00
- volume_MA20: 37421063.40
- volume_ratio: 1.58

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.17
- MA20 / MA60 / MA200: 12.70 / 13.03 / 10.89
- gap20 / gap60: 11.57% / 8.72%
- 5D return: 21.94%
- 20D high/low: 14.23 / 11.45

### Relative Strength

- ratio: 0.057197
- ratio_MA60: 0.050045
- ratio_gap: 14.29%
- ratio_slope_proxy(20d): 0.001733

### Volume (if available)

- volume: 20435417.00
- volume_MA20: 21582075.85
- volume_ratio: 0.95

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-18**
- 실행시간(UTC): **2026-05-19 03:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.8
- IG OAS 4주 변화: -5.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 20.0 bp / latest 2.1
- VIX: 18.43
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -5.44% / slope_proxy: -0.000906
- GDXJ/GLD gap: -3.53% / slope_proxy: -0.00363

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 46.458854 | ATR14%: 6.53%
- MA20 gap: -1.96% | MA50 gap: -0.55% | MA200 gap: -19.10%
- vol_ratio(Volume/Vol20): 0.714351 | gap_open: 1.14%
- RS vs SILJ gap: 3.62% / slope_proxy: -0.008415
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
- close: 8.56 | RSI14: 47.30804 | ATR14%: 8.10%
- MA20 gap: -1.31% | MA50 gap: -0.04% | MA200 gap: 5.16%
- vol_ratio(Volume/Vol20): 0.809172 | gap_open: 1.21%
- SilverMarginGate: SI=76.705002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 2.21% / slope_proxy: -0.021944
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
- close: 34.830002 | RSI14: 43.045632 | ATR14%: 10.63%
- MA20 gap: -9.58% | MA50 gap: -7.93% | MA200 gap: 53.06%
- vol_ratio(Volume/Vol20): 0.895754 | gap_open: 0.95%
- RS vs SILJ gap: -4.49% / slope_proxy: 0.027265
- RS vs GDXJ gap: -3.02% / slope_proxy: 0.006597
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
