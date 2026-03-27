# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-26**
- 실행시간(UTC): **2026-03-27 03:00:34**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.17 / 4주 변화 23.0 bp
- IG OAS (BAMLC0A0CM): 0.87 / 4주 변화 7.0 bp
- 10Y Real Yield (DFII10): 2.02 / 4주 변화 25.0 bp
- VIX (VIXCLS): 25.33
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.245671
- MA60: 6.962816
- gap: 18.42%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.256486
- MA60: 0.210805
- gap: 21.67%
- MA60_slope_proxy: -0.007808
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-26**
- 실행시간(UTC): **2026-03-27 03:00:41**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 111.99 bp / 4주 변화 51.45 bp
- CURVE_10s5s: 42.04 bp / 4주 변화 -17.11 bp

## NWG Price
- close: 535.0
- MA50: 610.0273 / gap50: -12.30%
- MA200: 571.0979 / gap200: -6.32%

## Relative Strength
- RS vs FTSE gap: -10.18% / slope_proxy: -0.003206
- RS vs Peers gap: -6.28% / slope_proxy: -0.050043

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-27 03:00:49**

## Commodity Regime

- WTI ref (CL=F): 93.48 / 5D -2.77%
- Brent ref (BZ=F): 100.66 / 5D -7.35%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.18
- Gas ref (NG=F): 2.93 / 5D -7.55%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 64.36
- MA20 / MA60 / MA200: 57.08 / 49.06 / 44.83
- gap20 / gap60: 12.75% / 31.19%
- 5D return: 8.02%
- 20D high/low: 64.36 / 52.83

### Relative Strength

- ratio: 1.046164
- ratio_MA60: 0.923933
- ratio_gap: 13.23%
- ratio_slope_proxy(20d): 0.025575

### Volume (if available)

- volume: 18568524.00
- volume_MA20: 21671986.20
- volume_ratio: 0.86

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.33
- MA20 / MA60 / MA200: 18.54 / 15.62 / 13.30
- gap20 / gap60: 9.63% / 30.16%
- 5D return: 2.78%
- 20D high/low: 20.33 / 16.63

### Relative Strength

- ratio: 0.552446
- ratio_MA60: 0.428313
- ratio_gap: 28.98%
- ratio_slope_proxy(20d): 0.041199

### Volume (if available)

- volume: 32525153.00
- volume_MA20: 37645217.65
- volume_ratio: 0.86

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

- close: 6.89
- MA20 / MA60 / MA200: 6.35 / 5.53 / 4.03
- gap20 / gap60: 8.50% / 24.66%
- 5D return: 6.66%
- 20D high/low: 6.89 / 5.93

### Relative Strength

- ratio: 0.016673
- ratio_MA60: 0.015206
- ratio_gap: 9.64%
- ratio_slope_proxy(20d): 0.000667

### Volume (if available)

- volume: 31434036.00
- volume_MA20: 38293361.80
- volume_ratio: 0.82

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 16.82
- MA20 / MA60 / MA200: 13.28 / 10.28 / 11.39
- gap20 / gap60: 26.64% / 63.55%
- 5D return: 17.70%
- 20D high/low: 16.82 / 9.68

### Relative Strength

- ratio: 0.057721
- ratio_MA60: 0.044806
- ratio_gap: 28.82%
- ratio_slope_proxy(20d): 0.005700

### Volume (if available)

- volume: 26098785.00
- volume_MA20: 38123059.25
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

- 데이터 기준일(주가): **2026-03-26**
- 실행시간(UTC): **2026-03-27 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.17
- IG OAS 4주 변화: 7.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 25.0 bp / latest 2.02
- VIX: 25.33
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.28% / slope_proxy: -0.005233
- GDXJ/GLD gap: -9.49% / slope_proxy: 0.000696

## VZLA (Vizsla Silver)
- close: 3.06 | RSI14: 31.795467 | ATR14%: 8.84%
- MA20 gap: -17.36% | MA50 gap: -31.55% | MA200 gap: -26.88%
- vol_ratio(Volume/Vol20): 0.790454 | gap_open: 4.63%
- RS vs SILJ gap: -18.89% / slope_proxy: -0.0273
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
- close: 7.3 | RSI14: 33.429112 | ATR14%: 12.26%
- MA20 gap: -21.99% | MA50 gap: -33.72% | MA200 gap: 1.27%
- vol_ratio(Volume/Vol20): 0.586822 | gap_open: 3.60%
- SilverMarginGate: SI=68.845001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.18% / slope_proxy: -0.017042
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

## HYMC (Hycroft Mining)
- close: 31.18 | RSI14: 40.217753 | ATR14%: 14.71%
- MA20 gap: -21.74% | MA50 gap: -23.17% | MA200 gap: 88.98%
- vol_ratio(Volume/Vol20): 0.475516 | gap_open: 5.83%
- RS vs SILJ gap: 1.76% / slope_proxy: 0.215594
- RS vs GDXJ gap: 0.94% / slope_proxy: 0.056646
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
