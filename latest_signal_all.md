# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-16**
- 실행시간(UTC): **2026-03-17 03:00:37**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.28 / 4주 변화 33.0 bp
- IG OAS (BAMLC0A0CM): 0.93 / 4주 변화 14.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 15.0 bp
- VIX (VIXCLS): 27.19
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.128339
- MA60: 6.609455
- gap: 22.98%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.232484
- MA60: 0.211355
- gap: 10.00%
- MA60_slope_proxy: -0.014313
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-16**
- 실행시간(UTC): **2026-03-17 03:00:43**

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
- TERM_SPREAD_10Y_POLICY: 97.58 bp / 4주 변화 27.32 bp
- CURVE_10s5s: 49.64 bp / 4주 변화 -8.79 bp

## NWG Price
- close: 573.4
- MA50: 625.464 / gap50: -8.32%
- MA200: 570.3574 / gap200: 0.53%

## Relative Strength
- RS vs FTSE gap: -9.31% / slope_proxy: -0.002404
- RS vs Peers gap: -1.58% / slope_proxy: -0.056154

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-17 03:00:51**

## Commodity Regime

- WTI ref (CL=F): 96.04 / 5D 1.34%
- Brent ref (BZ=F): 103.09 / 5D 4.17%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.05
- Gas ref (NG=F): 3.03 / 5D -2.95%

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

- close: 57.25
- MA20 / MA60 / MA200: 52.94 / 46.31 / 44.06
- gap20 / gap60: 8.15% / 23.63%
- 5D return: 4.55%
- 20D high/low: 58.41 / 45.72

### Relative Strength

- ratio: 0.988774
- ratio_MA60: 0.909207
- ratio_gap: 8.75%
- ratio_slope_proxy(20d): 0.009159

### Volume (if available)

- volume: 14937613.00
- volume_MA20: 20007080.65
- volume_ratio: 0.75

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.17
- MA20 / MA60 / MA200: 17.09 / 14.56 / 12.96
- gap20 / gap60: 12.20% / 31.62%
- 5D return: 5.56%
- 20D high/low: 19.17 / 15.02

### Relative Strength

- ratio: 0.524774
- ratio_MA60: 0.406747
- ratio_gap: 29.02%
- ratio_slope_proxy(20d): 0.020391

### Volume (if available)

- volume: 26308756.00
- volume_MA20: 31442727.80
- volume_ratio: 0.84

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

- close: 6.20
- MA20 / MA60 / MA200: 6.29 / 5.19 / 3.88
- gap20 / gap60: -1.36% / 19.48%
- 5D return: 0.49%
- 20D high/low: 6.54 / 5.93

### Relative Strength

- ratio: 0.016641
- ratio_MA60: 0.014903
- ratio_gap: 11.66%
- ratio_slope_proxy(20d): 0.000575

### Volume (if available)

- volume: 33305894.00
- volume_MA20: 43688484.70
- volume_ratio: 0.76

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.28
- MA20 / MA60 / MA200: 10.87 / 9.12 / 11.33
- gap20 / gap60: 12.96% / 34.68%
- 5D return: 6.69%
- 20D high/low: 13.10 / 8.77

### Relative Strength

- ratio: 0.048868
- ratio_MA60: 0.042155
- ratio_gap: 15.93%
- ratio_slope_proxy(20d): 0.003900

### Volume (if available)

- volume: 17508248.00
- volume_MA20: 21579452.40
- volume_ratio: 0.81

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

- 데이터 기준일(주가): **2026-03-16**
- 실행시간(UTC): **2026-03-17 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.28
- IG OAS 4주 변화: 14.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 15.0 bp / latest 1.92
- VIX: 27.19
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -1.27% / slope_proxy: -0.004418
- GDXJ/GLD gap: -7.36% / slope_proxy: 0.009953

## VZLA (Vizsla Silver)
- close: 3.63 | RSI14: 36.047009 | ATR14%: 8.31%
- MA20 gap: -8.68% | MA50 gap: -25.50% | MA200 gap: -13.27%
- vol_ratio(Volume/Vol20): 0.670841 | gap_open: 0.00%
- RS vs SILJ gap: -24.92% / slope_proxy: -0.028184
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
- close: 8.9 | RSI14: 36.697527 | ATR14%: 10.91%
- MA20 gap: -16.81% | MA50 gap: -22.15% | MA200 gap: 27.11%
- vol_ratio(Volume/Vol20): 2.909234 | gap_open: 3.54%
- SilverMarginGate: SI=81.455002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.10% / slope_proxy: -0.002139
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
- close: 39.32 | RSI14: 47.074599 | ATR14%: 13.39%
- MA20 gap: -9.87% | MA50 gap: -1.24% | MA200 gap: 156.96%
- vol_ratio(Volume/Vol20): 0.781548 | gap_open: 2.87%
- RS vs SILJ gap: 13.70% / slope_proxy: 0.254893
- RS vs GDXJ gap: 13.28% / slope_proxy: 0.066938
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
