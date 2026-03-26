# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-25**
- 실행시간(UTC): **2026-03-26 03:00:38**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.19 / 4주 변화 22.0 bp
- IG OAS (BAMLC0A0CM): 0.87 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.06 / 4주 변화 28.0 bp
- VIX (VIXCLS): 26.95
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.869761
- MA60: 6.922037
- gap: 28.14%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.246729
- MA60: 0.210452
- gap: 17.24%
- MA60_slope_proxy: -0.009194
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-25**
- 실행시간(UTC): **2026-03-26 03:00:50**

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
- TERM_SPREAD_10Y_POLICY: 112.03 bp / 4주 변화 52.49 bp
- CURVE_10s5s: 41.77 bp / 4주 변화 -17.11 bp

## NWG Price
- close: 543.0
- MA50: 612.1023 / gap50: -11.29%
- MA200: 570.9884 / gap200: -4.90%

## Relative Strength
- RS vs FTSE gap: -10.35% / slope_proxy: -0.003128
- RS vs Peers gap: -6.53% / slope_proxy: -0.051212

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-26 03:00:56**

## Commodity Regime

- WTI ref (CL=F): 91.65 / 5D -4.85%
- Brent ref (BZ=F): 98.45 / 5D -8.32%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.80
- Gas ref (NG=F): 2.92 / 5D -4.83%

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

- close: 61.85
- MA20 / MA60 / MA200: 56.42 / 48.66 / 44.72
- gap20 / gap60: 9.62% / 27.12%
- 5D return: 5.94%
- 20D high/low: 61.85 / 51.19

### Relative Strength

- ratio: 1.021133
- ratio_MA60: 0.927210
- ratio_gap: 10.13%
- ratio_slope_proxy(20d): 0.023033

### Volume (if available)

- volume: 13945148.00
- volume_MA20: 21306697.40
- volume_ratio: 0.65

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.82
- MA20 / MA60 / MA200: 18.36 / 15.47 / 13.26
- gap20 / gap60: 7.96% / 28.09%
- 5D return: 0.25%
- 20D high/low: 19.82 / 16.61

### Relative Strength

- ratio: 0.527970
- ratio_MA60: 0.425274
- ratio_gap: 24.15%
- ratio_slope_proxy(20d): 0.038804

### Volume (if available)

- volume: 22787644.00
- volume_MA20: 36879607.20
- volume_ratio: 0.62

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

- close: 6.77
- MA20 / MA60 / MA200: 6.33 / 5.48 / 4.01
- gap20 / gap60: 7.04% / 23.54%
- 5D return: 8.32%
- 20D high/low: 6.77 / 5.93

### Relative Strength

- ratio: 0.016548
- ratio_MA60: 0.015168
- ratio_gap: 9.10%
- ratio_slope_proxy(20d): 0.000640

### Volume (if available)

- volume: 34557872.00
- volume_MA20: 38334068.60
- volume_ratio: 0.90

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

- close: 16.71
- MA20 / MA60 / MA200: 12.91 / 10.12 / 11.39
- gap20 / gap60: 29.40% / 65.11%
- 5D return: 12.53%
- 20D high/low: 16.71 / 9.46

### Relative Strength

- ratio: 0.058757
- ratio_MA60: 0.044453
- ratio_gap: 32.18%
- ratio_slope_proxy(20d): 0.005428

### Volume (if available)

- volume: 27986614.00
- volume_MA20: 37202120.70
- volume_ratio: 0.75

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

- 데이터 기준일(주가): **2026-03-25**
- 실행시간(UTC): **2026-03-26 03:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 22.0 bp / latest 3.19
- IG OAS 4주 변화: 6.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.06
- VIX: 26.95
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.10% / slope_proxy: -0.005684
- GDXJ/GLD gap: -6.94% / slope_proxy: 0.001809

## VZLA (Vizsla Silver)
- close: 3.24 | RSI14: 34.855126 | ATR14%: 8.53%
- MA20 gap: -13.83% | MA50 gap: -28.42% | MA200 gap: -22.63%
- vol_ratio(Volume/Vol20): 0.833242 | gap_open: 5.43%
- RS vs SILJ gap: -20.55% / slope_proxy: -0.027446
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
- close: 8.05 | RSI14: 37.605524 | ATR14%: 11.18%
- MA20 gap: -16.19% | MA50 gap: -27.43% | MA200 gap: 12.00%
- vol_ratio(Volume/Vol20): 0.674575 | gap_open: 7.46%
- SilverMarginGate: SI=71.595001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.06% / slope_proxy: -0.014757
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
- close: 34.470001 | RSI14: 44.164534 | ATR14%: 13.58%
- MA20 gap: -15.47% | MA50 gap: -15.17% | MA200 gap: 110.63%
- vol_ratio(Volume/Vol20): 0.678891 | gap_open: 9.45%
- RS vs SILJ gap: 5.61% / slope_proxy: 0.223504
- RS vs GDXJ gap: 4.87% / slope_proxy: 0.058743
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
