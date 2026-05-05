# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-04**
- 실행시간(UTC): **2026-05-05 03:00:37**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.77 / 4주 변화 -36.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.91 / 4주 변화 -8.0 bp
- VIX (VIXCLS): 16.99
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.450885
- MA60: 8.173378
- gap: 15.63%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.322935
- MA60: 0.248582
- gap: 29.91%
- MA60_slope_proxy: 0.034946
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-01**
- 실행시간(UTC): **2026-05-05 03:00:39**

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
- close: 565.6
- MA50: 584.1298 / gap50: -3.17%
- MA200: 581.8056 / gap200: -2.79%

## Relative Strength
- RS vs FTSE gap: -3.54% / slope_proxy: -0.002456
- RS vs Peers gap: -8.24% / slope_proxy: -0.037537

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-05 03:00:47**

## Commodity Regime

- WTI ref (CL=F): 104.27 / 5D 8.20%
- Brent ref (BZ=F): 113.14 / 5D 4.54%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.87
- Gas ref (NG=F): 2.83 / 5D 11.02%

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

- close: 60.27
- MA20 / MA60 / MA200: 57.91 / 56.04 / 46.89
- gap20 / gap60: 4.08% / 7.54%
- 5D return: 5.24%
- 20D high/low: 62.94 / 53.79

### Relative Strength

- ratio: 1.014817
- ratio_MA60: 0.981210
- ratio_gap: 3.43%
- ratio_slope_proxy(20d): 0.037265

### Volume (if available)

- volume: 8671871.00
- volume_MA20: 13308453.55
- volume_ratio: 0.65

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 22.01
- MA20 / MA60 / MA200: 21.10 / 18.87 / 14.35
- gap20 / gap60: 4.32% / 16.65%
- 5D return: 5.01%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.563781
- ratio_MA60: 0.489946
- ratio_gap: 15.07%
- ratio_slope_proxy(20d): 0.045905

### Volume (if available)

- volume: 11504303.00
- volume_MA20: 22343840.15
- volume_ratio: 0.51

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

- close: 6.88
- MA20 / MA60 / MA200: 6.43 / 6.36 / 4.50
- gap20 / gap60: 6.92% / 8.16%
- 5D return: 5.52%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015513
- ratio_MA60: 0.015944
- ratio_gap: -2.70%
- ratio_slope_proxy(20d): 0.000501

### Volume (if available)

- volume: 32257433.00
- volume_MA20: 31953496.65
- volume_ratio: 1.01

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

- close: 13.77
- MA20 / MA60 / MA200: 12.80 / 12.52 / 11.00
- gap20 / gap60: 7.59% / 10.02%
- 5D return: 12.96%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.050467
- ratio_MA60: 0.048643
- ratio_gap: 3.75%
- ratio_slope_proxy(20d): 0.001814

### Volume (if available)

- volume: 24093086.00
- volume_MA20: 23097819.30
- volume_ratio: 1.04

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-04**
- 실행시간(UTC): **2026-05-05 03:00:51**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -36.0 bp / latest 2.77
- IG OAS 4주 변화: -5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.91
- VIX: 16.99
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.89% / slope_proxy: 0.012799
- GDXJ/GLD gap: -5.03% / slope_proxy: -0.003803

## VZLA (Vizsla Silver)
- close: 3.36 | RSI14: 46.691234 | ATR14%: 5.91%
- MA20 gap: -0.71% | MA50 gap: -5.16% | MA200 gap: -20.17%
- vol_ratio(Volume/Vol20): 0.725238 | gap_open: 1.73%
- RS vs SILJ gap: 4.21% / slope_proxy: -0.020532
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
- close: 7.88 | RSI14: 42.927633 | ATR14%: 7.94%
- MA20 gap: -6.32% | MA50 gap: -12.88% | MA200 gap: 0.04%
- vol_ratio(Volume/Vol20): 0.952685 | gap_open: 1.59%
- SilverMarginGate: SI=73.480003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.64% / slope_proxy: -0.031358
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
- close: 36.09 | RSI14: 46.212744 | ATR14%: 9.16%
- MA20 gap: -6.94% | MA50 gap: -8.20% | MA200 gap: 72.18%
- vol_ratio(Volume/Vol20): 0.702971 | gap_open: 4.47%
- RS vs SILJ gap: 3.88% / slope_proxy: 0.035372
- RS vs GDXJ gap: 5.20% / slope_proxy: 0.005243
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
