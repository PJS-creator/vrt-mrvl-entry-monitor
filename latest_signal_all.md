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
- 실행시간(UTC): **2026-03-26 15:00:46**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.17 / 4주 변화 23.0 bp
- IG OAS (BAMLC0A0CM): 0.87 / 4주 변화 7.0 bp
- 10Y Real Yield (DFII10): 2.06 / 4주 변화 28.0 bp
- VIX (VIXCLS): 25.33
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.367466
- MA60: 6.964846
- gap: 20.14%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.255763
- MA60: 0.210793
- gap: 21.33%
- MA60_slope_proxy: -0.00782
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-26**
- 실행시간(UTC): **2026-03-26 15:00:55**

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
- close: 539.4
- MA50: 610.1153 / gap50: -11.59%
- MA200: 571.1199 / gap200: -5.55%

## Relative Strength
- RS vs FTSE gap: -9.76% / slope_proxy: -0.003202
- RS vs Peers gap: -5.91% / slope_proxy: -0.049979

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-26 15:01:02**

## Commodity Regime

- WTI ref (CL=F): 93.62 / 5D -2.62%
- Brent ref (BZ=F): 101.39 / 5D -6.68%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.77
- Gas ref (NG=F): 2.96 / 5D -6.60%

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

- close: 62.72
- MA20 / MA60 / MA200: 57.00 / 49.03 / 44.83
- gap20 / gap60: 10.03% / 27.92%
- 5D return: 5.27%
- 20D high/low: 62.72 / 52.83

### Relative Strength

- ratio: 1.026484
- ratio_MA60: 0.929197
- ratio_gap: 10.47%
- ratio_slope_proxy(20d): 0.024969

### Volume (if available)

- volume: 4501714.00
- volume_MA20: 20967645.70
- volume_ratio: 0.21

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.23
- MA20 / MA60 / MA200: 18.54 / 15.62 / 13.30
- gap20 / gap60: 9.09% / 29.51%
- 5D return: 2.25%
- 20D high/low: 20.23 / 16.63

### Relative Strength

- ratio: 0.543537
- ratio_MA60: 0.428164
- ratio_gap: 26.95%
- ratio_slope_proxy(20d): 0.041051

### Volume (if available)

- volume: 9361649.00
- volume_MA20: 36484442.45
- volume_ratio: 0.26

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

- close: 6.86
- MA20 / MA60 / MA200: 6.35 / 5.53 / 4.03
- gap20 / gap60: 7.97% / 24.04%
- 5D return: 6.11%
- 20D high/low: 6.86 / 5.93

### Relative Strength

- ratio: 0.016676
- ratio_MA60: 0.015206
- ratio_gap: 9.67%
- ratio_slope_proxy(20d): 0.000667

### Volume (if available)

- volume: 7046119.00
- volume_MA20: 37071745.95
- volume_ratio: 0.19

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

- close: 16.95
- MA20 / MA60 / MA200: 13.29 / 10.29 / 11.39
- gap20 / gap60: 27.59% / 64.83%
- 5D return: 18.65%
- 20D high/low: 16.95 / 9.68

### Relative Strength

- ratio: 0.058609
- ratio_MA60: 0.044821
- ratio_gap: 30.76%
- ratio_slope_proxy(20d): 0.005714

### Volume (if available)

- volume: 8943083.00
- volume_MA20: 37260919.15
- volume_ratio: 0.24

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
- 실행시간(UTC): **2026-03-26 15:01:17**

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
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.06
- VIX: 25.33
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.86% / slope_proxy: -0.00519
- GDXJ/GLD gap: -7.39% / slope_proxy: 0.000799

## VZLA (Vizsla Silver)
- close: 3.1698 | RSI14: 33.594349 | ATR14%: 8.46%
- MA20 gap: -14.53% | MA50 gap: -29.13% | MA200 gap: -24.27%
- vol_ratio(Volume/Vol20): 0.194967 | gap_open: 4.63%
- RS vs SILJ gap: -19.02% / slope_proxy: -0.027303
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
- close: 7.66 | RSI14: 35.311498 | ATR14%: 11.39%
- MA20 gap: -18.30% | MA50 gap: -30.50% | MA200 gap: 6.24%
- vol_ratio(Volume/Vol20): 0.182207 | gap_open: 3.60%
- SilverMarginGate: SI=69.264999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.23% / slope_proxy: -0.01699
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
- close: 33.485001 | RSI14: 42.903975 | ATR14%: 13.47%
- MA20 gap: -16.20% | MA50 gap: -17.58% | MA200 gap: 102.81%
- vol_ratio(Volume/Vol20): 0.162018 | gap_open: 5.83%
- RS vs SILJ gap: 5.27% / slope_proxy: 0.216279
- RS vs GDXJ gap: 3.42% / slope_proxy: 0.056769
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
