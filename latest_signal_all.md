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
- 실행시간(UTC): **2026-03-25 15:00:42**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.19 / 4주 변화 22.0 bp
- IG OAS (BAMLC0A0CM): 0.87 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.01 / 4주 변화 24.0 bp
- VIX (VIXCLS): 26.95
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.954923
- MA60: 6.923456
- gap: 29.34%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.242651
- MA60: 0.210384
- gap: 15.34%
- MA60_slope_proxy: -0.009262
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-25**
- 실행시간(UTC): **2026-03-25 15:00:47**

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
- close: 542.8
- MA50: 612.0983 / gap50: -11.32%
- MA200: 570.9874 / gap200: -4.94%

## Relative Strength
- RS vs FTSE gap: -10.39% / slope_proxy: -0.003128
- RS vs Peers gap: -6.65% / slope_proxy: -0.051234

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-25 15:00:55**

## Commodity Regime

- WTI ref (CL=F): 88.60 / 5D -8.02%
- Brent ref (BZ=F): 96.08 / 5D -10.52%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.48
- Gas ref (NG=F): 2.88 / 5D -6.20%

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

- close: 61.46
- MA20 / MA60 / MA200: 56.40 / 48.65 / 44.72
- gap20 / gap60: 8.96% / 26.33%
- 5D return: 5.28%
- 20D high/low: 61.46 / 51.19

### Relative Strength

- ratio: 1.012354
- ratio_MA60: 0.927064
- ratio_gap: 9.20%
- ratio_slope_proxy(20d): 0.022886

### Volume (if available)

- volume: 5124305.00
- volume_MA20: 20862075.25
- volume_ratio: 0.25

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.89
- MA20 / MA60 / MA200: 18.36 / 15.47 / 13.26
- gap20 / gap60: 8.30% / 28.51%
- 5D return: 0.58%
- 20D high/low: 19.89 / 16.61

### Relative Strength

- ratio: 0.527874
- ratio_MA60: 0.425273
- ratio_gap: 24.13%
- ratio_slope_proxy(20d): 0.038803

### Volume (if available)

- volume: 5947008.00
- volume_MA20: 36036995.40
- volume_ratio: 0.17

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

- close: 6.80
- MA20 / MA60 / MA200: 6.33 / 5.48 / 4.01
- gap20 / gap60: 7.48% / 24.07%
- 5D return: 8.80%
- 20D high/low: 6.80 / 5.93

### Relative Strength

- ratio: 0.016598
- ratio_MA60: 0.015169
- ratio_gap: 9.42%
- ratio_slope_proxy(20d): 0.000641

### Volume (if available)

- volume: 8973422.00
- volume_MA20: 37051901.10
- volume_ratio: 0.24

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
- MA20 / MA60 / MA200: 12.92 / 10.12 / 11.39
- gap20 / gap60: 30.19% / 66.16%
- 5D return: 13.27%
- 20D high/low: 16.82 / 9.46

### Relative Strength

- ratio: 0.058350
- ratio_MA60: 0.044446
- ratio_gap: 31.28%
- ratio_slope_proxy(20d): 0.005421

### Volume (if available)

- volume: 9145176.00
- volume_MA20: 36252108.80
- volume_ratio: 0.25

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
- 실행시간(UTC): **2026-03-25 15:01:05**

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
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.01
- VIX: 26.95
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.30% / slope_proxy: -0.00567
- GDXJ/GLD gap: -6.39% / slope_proxy: 0.001837

## VZLA (Vizsla Silver)
- close: 3.255 | RSI14: 35.336634 | ATR14%: 8.49%
- MA20 gap: -13.45% | MA50 gap: -28.09% | MA200 gap: -22.27%
- vol_ratio(Volume/Vol20): 0.156698 | gap_open: 5.43%
- RS vs SILJ gap: -21.33% / slope_proxy: -0.027465
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
- close: 8.085 | RSI14: 37.941494 | ATR14%: 11.13%
- MA20 gap: -15.84% | MA50 gap: -27.12% | MA200 gap: 12.48%
- vol_ratio(Volume/Vol20): 0.297507 | gap_open: 7.46%
- SilverMarginGate: SI=73.440002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.92% / slope_proxy: -0.014805
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
- close: 36.130001 | RSI14: 46.618904 | ATR14%: 12.95%
- MA20 gap: -11.58% | MA50 gap: -11.16% | MA200 gap: 120.66%
- vol_ratio(Volume/Vol20): 0.290713 | gap_open: 9.45%
- RS vs SILJ gap: 9.03% / slope_proxy: 0.224167
- RS vs GDXJ gap: 8.40% / slope_proxy: 0.058917
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
