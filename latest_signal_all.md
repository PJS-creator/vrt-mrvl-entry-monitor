# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-06**
- 실행시간(UTC): **2026-04-07 03:00:39**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.13 / 4주 변화 0.0 bp
- IG OAS (BAMLC0A0CM): 0.86 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 1.99 / 4주 변화 19.0 bp
- VIX (VIXCLS): 23.87
- NFCI: -0.4337

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.022636
- MA60: 7.180548
- gap: 11.73%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.276554
- MA60: 0.213743
- gap: 29.39%
- MA60_slope_proxy: 0.00125
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-02**
- 실행시간(UTC): **2026-04-07 03:00:41**

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
- TERM_SPREAD_10Y_POLICY: 111.15 bp / 4주 변화 38.03 bp
- CURVE_10s5s: 42.25 bp / 4주 변화 -14.4 bp

## NWG Price
- close: 575.4
- MA50: 600.9212 / gap50: -4.25%
- MA200: 572.1824 / gap200: 0.56%

## Relative Strength
- RS vs FTSE gap: -6.36% / slope_proxy: -0.003359
- RS vs Peers gap: -4.12% / slope_proxy: -0.044092

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-07 03:00:47**

## Commodity Regime

- WTI ref (CL=F): 114.75 / 5D 15.16%
- Brent ref (BZ=F): 111.05 / 5D -1.35%
- Brent Tier: **>=90**
- Brent-WTI spread: -3.70
- Gas ref (NG=F): 2.79 / 5D -9.79%

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

- close: 62.96
- MA20 / MA60 / MA200: 60.29 / 51.34 / 45.42
- gap20 / gap60: 4.42% / 22.63%
- 5D return: -3.61%
- 20D high/low: 66.24 / 53.12

### Relative Strength

- ratio: 1.054960
- ratio_MA60: 0.943945
- ratio_gap: 11.76%
- ratio_slope_proxy(20d): 0.037283

### Volume (if available)

- volume: 11658357.00
- volume_MA20: 22145277.85
- volume_ratio: 0.53

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.86
- MA20 / MA60 / MA200: 19.64 / 16.51 / 13.56
- gap20 / gap60: 6.24% / 26.36%
- 5D return: 0.43%
- 20D high/low: 20.86 / 17.99

### Relative Strength

- ratio: 0.541256
- ratio_MA60: 0.446644
- ratio_gap: 21.18%
- ratio_slope_proxy(20d): 0.052627

### Volume (if available)

- volume: 15157715.00
- volume_MA20: 39262785.75
- volume_ratio: 0.39

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

- close: 6.59
- MA20 / MA60 / MA200: 6.48 / 5.77 / 4.13
- gap20 / gap60: 1.67% / 14.22%
- 5D return: -4.91%
- 20D high/low: 6.93 / 6.16

### Relative Strength

- ratio: 0.016492
- ratio_MA60: 0.015443
- ratio_gap: 6.79%
- ratio_slope_proxy(20d): 0.000781

### Volume (if available)

- volume: 21441828.00
- volume_MA20: 37256531.40
- volume_ratio: 0.58

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 15.94
- MA20 / MA60 / MA200: 14.64 / 11.18 / 11.36
- gap20 / gap60: 8.91% / 42.52%
- 5D return: -9.07%
- 20D high/low: 17.53 / 11.38

### Relative Strength

- ratio: 0.056117
- ratio_MA60: 0.046830
- ratio_gap: 19.83%
- ratio_slope_proxy(20d): 0.006405

### Volume (if available)

- volume: 24910921.00
- volume_MA20: 36735726.05
- volume_ratio: 0.68

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-06**
- 실행시간(UTC): **2026-04-07 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 3.13
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 19.0 bp / latest 1.99
- VIX: 23.87
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 4.41% / slope_proxy: -0.001671
- GDXJ/GLD gap: -2.57% / slope_proxy: -0.003903

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 41.125801 | ATR14%: 7.24%
- MA20 gap: -3.62% | MA50 gap: -19.88% | MA200 gap: -21.01%
- vol_ratio(Volume/Vol20): 0.893422 | gap_open: 0.00%
- RS vs SILJ gap: -18.24% / slope_proxy: -0.0275
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
- close: 8.15 | RSI14: 43.875411 | ATR14%: 10.24%
- MA20 gap: -3.56% | MA50 gap: -22.44% | MA200 gap: 10.71%
- vol_ratio(Volume/Vol20): 0.625872 | gap_open: 0.89%
- SilverMarginGate: SI=72.699997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.96% / slope_proxy: -0.021624
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
- close: 35.990002 | RSI14: 48.869594 | ATR14%: 11.78%
- MA20 gap: -0.09% | MA50 gap: -10.13% | MA200 gap: 106.58%
- vol_ratio(Volume/Vol20): 0.537736 | gap_open: 0.58%
- RS vs SILJ gap: 0.86% / slope_proxy: 0.159002
- RS vs GDXJ gap: -0.41% / slope_proxy: 0.041814
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
