# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-10**
- 실행시간(UTC): **2026-03-11 03:00:40**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.19 / 4주 변화 35.0 bp
- IG OAS (BAMLC0A0CM): 0.85 / 4주 변화 9.0 bp
- 10Y Real Yield (DFII10): 1.78 / 4주 변화 -9.0 bp
- VIX (VIXCLS): 25.5
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.314655
- MA60: 6.448692
- gap: 28.94%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.234817
- MA60: 0.212167
- gap: 10.68%
- MA60_slope_proxy: -0.017152
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-10**
- 실행시간(UTC): **2026-03-11 03:00:50**

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
- TERM_SPREAD_10Y_POLICY: 85.89 bp / 4주 변화 8.69 bp
- CURVE_10s5s: 53.01 bp / 4주 변화 -7.14 bp

## NWG Price
- close: 590.6
- MA50: 632.036 / gap50: -6.56%
- MA200: 569.3975 / gap200: 3.72%

## Relative Strength
- RS vs FTSE gap: -8.33% / slope_proxy: -0.002093
- RS vs Peers gap: -5.95% / slope_proxy: -0.058398

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-11 03:00:58**

## Commodity Regime

- WTI ref (CL=F): 84.52 / 5D 13.36%
- Brent ref (BZ=F): 86.15 / 5D 5.84%
- Brent Tier: **80-90**
- Brent-WTI spread: 1.63
- Gas ref (NG=F): 3.03 / 5D -0.82%

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

- close: 53.12
- MA20 / MA60 / MA200: 50.92 / 45.38 / 43.93
- gap20 / gap60: 4.32% / 17.07%
- 5D return: -1.04%
- 20D high/low: 55.02 / 45.49

### Relative Strength

- ratio: 0.955396
- ratio_MA60: 0.906868
- ratio_gap: 5.35%
- ratio_slope_proxy(20d): -0.002573

### Volume (if available)

- volume: 23022072.00
- volume_MA20: 17420798.60
- volume_ratio: 1.32

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.99
- MA20 / MA60 / MA200: 16.38 / 14.11 / 12.81
- gap20 / gap60: 9.82% / 27.52%
- 5D return: 6.07%
- 20D high/low: 18.16 / 15.02

### Relative Strength

- ratio: 0.479350
- ratio_MA60: 0.397235
- ratio_gap: 20.67%
- ratio_slope_proxy(20d): 0.010226

### Volume (if available)

- volume: 32932818.00
- volume_MA20: 28181390.90
- volume_ratio: 1.17

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

- close: 6.16
- MA20 / MA60 / MA200: 6.23 / 5.04 / 3.80
- gap20 / gap60: -1.10% / 22.17%
- 5D return: 0.82%
- 20D high/low: 6.54 / 5.44

### Relative Strength

- ratio: 0.016115
- ratio_MA60: 0.014717
- ratio_gap: 9.49%
- ratio_slope_proxy(20d): 0.000483

### Volume (if available)

- volume: 36575263.00
- volume_MA20: 59975003.15
- volume_ratio: 0.61

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

- close: 11.40
- MA20 / MA60 / MA200: 10.27 / 8.68 / 11.31
- gap20 / gap60: 11.01% / 31.37%
- 5D return: -0.52%
- 20D high/low: 12.48 / 8.77

### Relative Strength

- ratio: 0.046387
- ratio_MA60: 0.040873
- ratio_gap: 13.49%
- ratio_slope_proxy(20d): 0.003154

### Volume (if available)

- volume: 23902108.00
- volume_MA20: 18511690.40
- volume_ratio: 1.29

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

- 데이터 기준일(주가): **2026-03-10**
- 실행시간(UTC): **2026-03-11 03:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 35.0 bp / latest 3.19
- IG OAS 4주 변화: 9.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: -9.0 bp / latest 1.78
- VIX: 25.5
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 0.07% / slope_proxy: -0.002749
- GDXJ/GLD gap: -1.54% / slope_proxy: 0.012948

## VZLA (Vizsla Silver)
- close: 4.14 | RSI14: 44.953624 | ATR14%: 7.91%
- MA20 gap: 3.81% | MA50 gap: -17.52% | MA200 gap: -0.62%
- vol_ratio(Volume/Vol20): 0.474055 | gap_open: 2.26%
- RS vs SILJ gap: -25.67% / slope_proxy: -0.029171
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.62 | RSI14: 46.498937 | ATR14%: 10.00%
- MA20 gap: -2.83% | MA50 gap: -7.58% | MA200 gap: 55.09%
- vol_ratio(Volume/Vol20): 0.675004 | gap_open: 4.75%
- SilverMarginGate: SI=89.144997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.32% / slope_proxy: 0.006867
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
- close: 44.849998 | RSI14: 53.416092 | ATR14%: 13.16%
- MA20 gap: 5.06% | MA50 gap: 16.41% | MA200 gap: 207.98%
- vol_ratio(Volume/Vol20): 1.075242 | gap_open: 3.10%
- RS vs SILJ gap: 21.86% / slope_proxy: 0.247085
- RS vs GDXJ gap: 22.74% / slope_proxy: 0.064901
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
