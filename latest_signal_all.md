# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-23**
- 실행시간(UTC): **2026-04-24 03:00:38**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.84 / 4주 변화 -33.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 -10.0 bp
- VIX (VIXCLS): 18.92
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.12766
- MA60: 7.818792
- gap: 16.74%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.343592
- MA60: 0.234019
- gap: 46.82%
- MA60_slope_proxy: 0.023672
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-23**
- 실행시간(UTC): **2026-04-24 03:00:41**

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
- TERM_SPREAD_10Y_POLICY: 107.42 bp / 4주 변화 -4.57 bp
- CURVE_10s5s: 48.2 bp / 4주 변화 6.16 bp

## NWG Price
- close: 584.6
- MA50: 587.8489 / gap50: -0.55%
- MA200: 579.3675 / gap200: 0.90%

## Relative Strength
- RS vs FTSE gap: -2.89% / slope_proxy: -0.002558
- RS vs Peers gap: -5.19% / slope_proxy: -0.037991

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-24 03:00:47**

## Commodity Regime

- WTI ref (CL=F): 96.55 / 5D 1.96%
- Brent ref (BZ=F): 105.95 / 5D 6.60%
- Brent Tier: **>=90**
- Brent-WTI spread: 9.40
- Gas ref (NG=F): 2.72 / 5D 2.91%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 57.83
- MA20 / MA60 / MA200: 59.70 / 54.40 / 46.36
- gap20 / gap60: -3.12% / 6.30%
- 5D return: 1.69%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 1.014918
- ratio_MA60: 0.966333
- ratio_gap: 5.03%
- ratio_slope_proxy(20d): 0.039123

### Volume (if available)

- volume: 9322342.00
- volume_MA20: 17474937.10
- volume_ratio: 0.53

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.27
- MA20 / MA60 / MA200: 20.84 / 18.23 / 14.11
- gap20 / gap60: 2.04% / 16.69%
- 5D return: -1.07%
- 20D high/low: 21.97 / 19.98

### Relative Strength

- ratio: 0.530556
- ratio_MA60: 0.476051
- ratio_gap: 11.45%
- ratio_slope_proxy(20d): 0.050776

### Volume (if available)

- volume: 11223579.00
- volume_MA20: 30299443.95
- volume_ratio: 0.37

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

- close: 6.06
- MA20 / MA60 / MA200: 6.43 / 6.16 / 4.36
- gap20 / gap60: -5.72% / -1.62%
- 5D return: -4.57%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.014243
- ratio_MA60: 0.015829
- ratio_gap: -10.02%
- ratio_slope_proxy(20d): 0.000661

### Volume (if available)

- volume: 24176616.00
- volume_MA20: 29985990.80
- volume_ratio: 0.81

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

- close: 12.95
- MA20 / MA60 / MA200: 13.95 / 12.14 / 11.14
- gap20 / gap60: -7.19% / 6.72%
- 5D return: 2.13%
- 20D high/low: 17.53 / 11.45

### Relative Strength

- ratio: 0.050352
- ratio_MA60: 0.048344
- ratio_gap: 4.15%
- ratio_slope_proxy(20d): 0.003891

### Volume (if available)

- volume: 23380829.00
- volume_MA20: 27052576.45
- volume_ratio: 0.86

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

- 데이터 기준일(주가): **2026-04-23**
- 실행시간(UTC): **2026-04-24 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -33.0 bp / latest 2.84
- IG OAS 4주 변화: -8.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -10.0 bp / latest 1.92
- VIX: 18.92
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.52% / slope_proxy: 0.01307
- GDXJ/GLD gap: -1.85% / slope_proxy: -0.004082

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 43.982553 | ATR14%: 6.14%
- MA20 gap: -0.48% | MA50 gap: -8.23% | MA200 gap: -21.44%
- vol_ratio(Volume/Vol20): 1.262239 | gap_open: 2.31%
- RS vs SILJ gap: -7.89% / slope_proxy: -0.025889
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
- close: 8.61 | RSI14: 48.462767 | ATR14%: 8.30%
- MA20 gap: 3.03% | MA50 gap: -7.87% | MA200 gap: 11.44%
- vol_ratio(Volume/Vol20): 0.778508 | gap_open: 2.11%
- SilverMarginGate: SI=74.949997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.97% / slope_proxy: -0.02919
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
- close: 37.860001 | RSI14: 48.198153 | ATR14%: 10.03%
- MA20 gap: 0.26% | MA50 gap: -3.93% | MA200 gap: 91.15%
- vol_ratio(Volume/Vol20): 0.971299 | gap_open: 2.71%
- RS vs SILJ gap: 2.72% / slope_proxy: 0.059661
- RS vs GDXJ gap: 2.55% / slope_proxy: 0.012462
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
