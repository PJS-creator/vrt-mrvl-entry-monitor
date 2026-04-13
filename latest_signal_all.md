# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-13**
- 실행시간(UTC): **2026-04-13 15:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.94 / 4주 변화 -34.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 -11.0 bp
- 10Y Real Yield (DFII10): 1.95 / 4주 변화 6.0 bp
- VIX (VIXCLS): 19.23
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.90182
- MA60: 7.424635
- gap: 19.90%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.298792
- MA60: 0.219446
- gap: 36.16%
- MA60_slope_proxy: 0.008081
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-13**
- 실행시간(UTC): **2026-04-13 15:00:48**

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
- TERM_SPREAD_10Y_POLICY: 99.72 bp / 4주 변화 2.14 bp
- CURVE_10s5s: 45.38 bp / 4주 변화 -4.26 bp

## NWG Price
- close: 611.8
- MA50: 595.6111 / gap50: 2.72%
- MA200: 574.6361 / gap200: 6.47%

## Relative Strength
- RS vs FTSE gap: -1.13% / slope_proxy: -0.003169
- RS vs Peers gap: -2.10% / slope_proxy: -0.040242

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-13 15:00:56**

## Commodity Regime

- WTI ref (CL=F): 102.40 / 5D -8.90%
- Brent ref (BZ=F): 100.89 / 5D -8.09%
- Brent Tier: **>=90**
- Brent-WTI spread: -1.51
- Gas ref (NG=F): 2.67 / 5D -5.16%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 58.41
- MA20 / MA60 / MA200: 61.19 / 52.71 / 45.83
- gap20 / gap60: -4.54% / 10.81%
- 5D return: -7.23%
- 20D high/low: 66.24 / 57.25

### Relative Strength

- ratio: 1.021600
- ratio_MA60: 0.952540
- ratio_gap: 7.25%
- ratio_slope_proxy(20d): 0.039021

### Volume (if available)

- volume: 4731793.00
- volume_MA20: 18918134.65
- volume_ratio: 0.25

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.77
- MA20 / MA60 / MA200: 20.23 / 17.24 / 13.77
- gap20 / gap60: 7.61% / 26.28%
- 5D return: 4.39%
- 20D high/low: 21.77 / 18.80

### Relative Strength

- ratio: 0.531227
- ratio_MA60: 0.459446
- ratio_gap: 15.62%
- ratio_slope_proxy(20d): 0.055206

### Volume (if available)

- volume: 6562087.00
- volume_MA20: 33646884.35
- volume_ratio: 0.20

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

- close: 6.66
- MA20 / MA60 / MA200: 6.57 / 5.96 / 4.23
- gap20 / gap60: 1.32% / 11.67%
- 5D return: 1.06%
- 20D high/low: 6.93 / 6.20

### Relative Strength

- ratio: 0.016097
- ratio_MA60: 0.015665
- ratio_gap: 2.75%
- ratio_slope_proxy(20d): 0.000810

### Volume (if available)

- volume: 5634996.00
- volume_MA20: 33720809.80
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

- close: 13.14
- MA20 / MA60 / MA200: 15.05 / 11.71 / 11.27
- gap20 / gap60: -12.72% / 12.19%
- 5D return: -17.57%
- 20D high/low: 17.53 / 12.28

### Relative Strength

- ratio: 0.049370
- ratio_MA60: 0.047856
- ratio_gap: 3.16%
- ratio_slope_proxy(20d): 0.006051

### Volume (if available)

- volume: 8837315.00
- volume_MA20: 37347770.75
- volume_ratio: 0.24

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

- 데이터 기준일(주가): **2026-04-13**
- 실행시간(UTC): **2026-04-13 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.94
- IG OAS 4주 변화: -11.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.95
- VIX: 19.23
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 4.52% / slope_proxy: 0.005337
- GDXJ/GLD gap: 1.10% / slope_proxy: -0.004616

## VZLA (Vizsla Silver)
- close: 3.2699 | RSI14: 41.507914 | ATR14%: 6.54%
- MA20 gap: 0.44% | MA50 gap: -13.81% | MA200 gap: -21.80%
- vol_ratio(Volume/Vol20): 0.165292 | gap_open: 1.54%
- RS vs SILJ gap: -16.65% / slope_proxy: -0.027518
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.285 | RSI14: 46.526016 | ATR14%: 9.21%
- MA20 gap: 4.13% | MA50 gap: -15.31% | MA200 gap: 10.59%
- vol_ratio(Volume/Vol20): 0.380044 | gap_open: 1.00%
- SilverMarginGate: SI=73.879997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.57% / slope_proxy: -0.023274
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
- close: 38.290001 | RSI14: 52.654532 | ATR14%: 10.42%
- MA20 gap: 8.97% | MA50 gap: -1.22% | MA200 gap: 109.43%
- vol_ratio(Volume/Vol20): 0.163596 | gap_open: 0.83%
- RS vs SILJ gap: 3.21% / slope_proxy: 0.115014
- RS vs GDXJ gap: -0.32% / slope_proxy: 0.029626
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
