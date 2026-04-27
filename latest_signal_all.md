# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-27**
- 실행시간(UTC): **2026-04-27 15:00:48**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.86 / 4주 변화 -56.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -11.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 -16.0 bp
- VIX (VIXCLS): 18.71
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.122444
- MA60: 7.916195
- gap: 15.24%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.309721
- MA60: 0.238
- gap: 30.14%
- MA60_slope_proxy: 0.027052
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-27**
- 실행시간(UTC): **2026-04-27 15:00:53**

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
- TERM_SPREAD_10Y_POLICY: 112.1 bp / 4주 변화 -2.25 bp
- CURVE_10s5s: 46.59 bp / 4주 변화 6.84 bp

## NWG Price
- close: 575.4
- MA50: 586.8425 / gap50: -1.95%
- MA200: 580.1869 / gap200: -0.83%

## Relative Strength
- RS vs FTSE gap: -2.84% / slope_proxy: -0.00245
- RS vs Peers gap: -5.38% / slope_proxy: -0.037162

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-27 15:01:01**

## Commodity Regime

- WTI ref (CL=F): 96.45 / 5D 7.63%
- Brent ref (BZ=F): 101.59 / 5D 6.40%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.14
- Gas ref (NG=F): 2.79 / 5D 3.90%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 57.17
- MA20 / MA60 / MA200: 58.93 / 54.81 / 46.48
- gap20 / gap60: -2.97% / 4.31%
- 5D return: 4.95%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 1.002982
- ratio_MA60: 0.969821
- ratio_gap: 3.42%
- ratio_slope_proxy(20d): 0.038290

### Volume (if available)

- volume: 2672397.00
- volume_MA20: 15979294.85
- volume_ratio: 0.17

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.20
- MA20 / MA60 / MA200: 20.78 / 18.31 / 14.11
- gap20 / gap60: 2.01% / 15.78%
- 5D return: 2.72%
- 20D high/low: 21.84 / 19.86

### Relative Strength

- ratio: 0.528481
- ratio_MA60: 0.477398
- ratio_gap: 10.70%
- ratio_slope_proxy(20d): 0.048329

### Volume (if available)

- volume: 6792724.00
- volume_MA20: 28279276.20
- volume_ratio: 0.24

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

- close: 6.43
- MA20 / MA60 / MA200: 6.36 / 6.21 / 4.40
- gap20 / gap60: 1.12% / 3.70%
- 5D return: 9.25%
- 20D high/low: 6.70 / 5.89

### Relative Strength

- ratio: 0.014686
- ratio_MA60: 0.015836
- ratio_gap: -7.26%
- ratio_slope_proxy(20d): 0.000592

### Volume (if available)

- volume: 14202946.00
- volume_MA20: 28909627.30
- volume_ratio: 0.49

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.26
- MA20 / MA60 / MA200: 13.44 / 12.22 / 11.09
- gap20 / gap60: -8.84% / 0.30%
- 5D return: 7.03%
- 20D high/low: 16.89 / 11.45

### Relative Strength

- ratio: 0.047441
- ratio_MA60: 0.048385
- ratio_gap: -1.95%
- ratio_slope_proxy(20d): 0.003200

### Volume (if available)

- volume: 4927832.00
- volume_MA20: 25839816.60
- volume_ratio: 0.19

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-27**
- 실행시간(UTC): **2026-04-27 15:01:36**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -56.0 bp / latest 2.86
- IG OAS 4주 변화: -11.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -16.0 bp / latest 1.92
- VIX: 18.71
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.86% / slope_proxy: 0.015183
- GDXJ/GLD gap: -1.63% / slope_proxy: -0.003779

## VZLA (Vizsla Silver)
- close: 3.345 | RSI14: 45.895014 | ATR14%: 5.65%
- MA20 gap: 0.14% | MA50 gap: -6.56% | MA200 gap: -20.44%
- vol_ratio(Volume/Vol20): 0.301664 | gap_open: 0.60%
- RS vs SILJ gap: -4.59% / slope_proxy: -0.02495
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
- close: 8.21 | RSI14: 44.640196 | ATR14%: 8.21%
- MA20 gap: -2.73% | MA50 gap: -11.24% | MA200 gap: 5.57%
- vol_ratio(Volume/Vol20): 0.412193 | gap_open: 0.12%
- SilverMarginGate: SI=75.154999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.77% / slope_proxy: -0.029788
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
- close: 37.275002 | RSI14: 47.07879 | ATR14%: 9.53%
- MA20 gap: -2.72% | MA50 gap: -5.72% | MA200 gap: 85.01%
- vol_ratio(Volume/Vol20): 0.163301 | gap_open: 1.41%
- RS vs SILJ gap: 1.80% / slope_proxy: 0.046673
- RS vs GDXJ gap: 1.54% / slope_proxy: 0.008578
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
