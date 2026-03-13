# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-13**
- 실행시간(UTC): **2026-03-13 15:00:40**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.09 / 4주 변화 25.0 bp
- IG OAS (BAMLC0A0CM): 0.88 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 1.85 / 4주 변화 -1.0 bp
- VIX (VIXCLS): 27.29
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.018266
- MA60: 6.568113
- gap: 22.08%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.226011
- MA60: 0.211457
- gap: 6.88%
- MA60_slope_proxy: -0.015094
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-13**
- 실행시간(UTC): **2026-03-13 15:00:52**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 88.88 bp / 4주 변화 14.99 bp
- CURVE_10s5s: 49.5 bp / 4주 변화 -9.46 bp

## NWG Price
- close: 572.4
- MA50: 627.452 / gap50: -8.77%
- MA200: 570.1899 / gap200: 0.39%

## Relative Strength
- RS vs FTSE gap: -9.60% / slope_proxy: -0.002287
- RS vs Peers gap: -1.65% / slope_proxy: -0.056526

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-13 15:01:00**

## Commodity Regime

- WTI ref (CL=F): 95.08 / 5D 4.60%
- Brent ref (BZ=F): 100.25 / 5D 8.16%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.17
- Gas ref (NG=F): 3.14 / 5D -1.32%

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

- close: 57.12
- MA20 / MA60 / MA200: 52.33 / 45.99 / 43.97
- gap20 / gap60: 9.15% / 24.21%
- 5D return: 5.90%
- 20D high/low: 58.41 / 45.72

### Relative Strength

- ratio: 0.995417
- ratio_MA60: 0.907461
- ratio_gap: 9.69%
- ratio_slope_proxy(20d): 0.006122

### Volume (if available)

- volume: 6407880.00
- volume_MA20: 19196084.00
- volume_ratio: 0.33

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.76
- MA20 / MA60 / MA200: 16.90 / 14.44 / 12.92
- gap20 / gap60: 11.06% / 29.91%
- 5D return: 6.62%
- 20D high/low: 18.99 / 15.02

### Relative Strength

- ratio: 0.519590
- ratio_MA60: 0.404179
- ratio_gap: 28.55%
- ratio_slope_proxy(20d): 0.017571

### Volume (if available)

- volume: 10818294.00
- volume_MA20: 29827829.70
- volume_ratio: 0.36

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

- close: 6.31
- MA20 / MA60 / MA200: 6.30 / 5.15 / 3.86
- gap20 / gap60: 0.16% / 22.55%
- 5D return: 6.41%
- 20D high/low: 6.54 / 5.93

### Relative Strength

- ratio: 0.017121
- ratio_MA60: 0.014855
- ratio_gap: 15.26%
- ratio_slope_proxy(20d): 0.000567

### Volume (if available)

- volume: 10499560.00
- volume_MA20: 45629713.00
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.09
- MA20 / MA60 / MA200: 10.72 / 9.01 / 11.33
- gap20 / gap60: 22.01% / 45.20%
- 5D return: 4.85%
- 20D high/low: 13.09 / 8.77

### Relative Strength

- ratio: 0.051617
- ratio_MA60: 0.041858
- ratio_gap: 23.32%
- ratio_slope_proxy(20d): 0.003682

### Volume (if available)

- volume: 5770612.00
- volume_MA20: 19824135.60
- volume_ratio: 0.29

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

- 데이터 기준일(주가): **2026-03-13**
- 실행시간(UTC): **2026-03-13 15:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 25.0 bp / latest 3.09
- IG OAS 4주 변화: 11.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: -1.0 bp / latest 1.85
- VIX: 27.29
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -1.71% / slope_proxy: -0.003796
- GDXJ/GLD gap: -7.89% / slope_proxy: 0.010808

## VZLA (Vizsla Silver)
- close: 3.63 | RSI14: 35.480119 | ATR14%: 8.48%
- MA20 gap: -8.97% | MA50 gap: -26.08% | MA200 gap: -13.20%
- vol_ratio(Volume/Vol20): 0.176845 | gap_open: 0.77%
- RS vs SILJ gap: -25.50% / slope_proxy: -0.028457
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
- close: 9.415 | RSI14: 39.426732 | ATR14%: 10.18%
- MA20 gap: -12.46% | MA50 gap: -17.76% | MA200 gap: 35.12%
- vol_ratio(Volume/Vol20): 0.613145 | gap_open: 1.62%
- SilverMarginGate: SI=81.785004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.38% / slope_proxy: -0.000537
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
- close: 37.330002 | RSI14: 44.532507 | ATR14%: 14.48%
- MA20 gap: -14.00% | MA50 gap: -5.47% | MA200 gap: 146.94%
- vol_ratio(Volume/Vol20): 0.26278 | gap_open: 0.09%
- RS vs SILJ gap: 9.31% / slope_proxy: 0.251437
- RS vs GDXJ gap: 8.71% / slope_proxy: 0.066034
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
