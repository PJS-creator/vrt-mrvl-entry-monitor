# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-02**
- 실행시간(UTC): **2026-03-03 00:45:30**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.12 / 4주 변화 24.0 bp
- IG OAS (BAMLC0A0CM): 0.86 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 1.72 / 4주 변화 -18.0 bp
- VIX (VIXCLS): 19.86
- NFCI: -0.5629

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.671131
- MA60: 6.257284
- gap: 22.60%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.198971
- MA60: 0.216651
- gap: -8.16%
- MA60_slope_proxy: -0.018983
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-02**
- 실행시간(UTC): **2026-03-03 00:45:38**

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
- TERM_SPREAD_10Y_POLICY: 58.5 bp / 4주 변화 -16.33 bp
- CURVE_10s5s: 61.23 bp / 4주 변화 6.06 bp

## NWG Price
- close: 601.0
- MA50: 639.316 / gap50: -5.99%
- MA200: 567.4807 / gap200: 5.91%

## Relative Strength
- RS vs FTSE gap: -11.04% / slope_proxy: -0.001235
- RS vs Peers gap: -9.44% / slope_proxy: -0.052333

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-03 00:45:44**

## Commodity Regime

- WTI ref (CL=F): 71.42 / 5D 7.71%
- Brent ref (BZ=F): 78.33 / 5D 9.57%
- Brent Tier: **70-80**
- Brent-WTI spread: 6.91
- Gas ref (NG=F): 2.99 / 5D 0.27%

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

- close: 54.21
- MA20 / MA60 / MA200: 48.47 / 44.18 / 43.57
- gap20 / gap60: 11.85% / 22.71%
- 5D return: 3.40%
- 20D high/low: 54.21 / 43.80

### Relative Strength

- ratio: 0.950386
- ratio_MA60: 0.903221
- ratio_gap: 5.22%
- ratio_slope_proxy(20d): -0.010906

### Volume (if available)

- volume: 32448678.00
- volume_MA20: 13709803.90
- volume_ratio: 2.37

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.32
- MA20 / MA60 / MA200: 15.70 / 13.61 / 12.63
- gap20 / gap60: 10.35% / 27.22%
- 5D return: 7.31%
- 20D high/low: 17.32 / 14.87

### Relative Strength

- ratio: 0.448240
- ratio_MA60: 0.388866
- ratio_gap: 15.27%
- ratio_slope_proxy(20d): 0.001744

### Volume (if available)

- volume: 43976869.00
- volume_MA20: 23314498.45
- volume_ratio: 1.89

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

- close: 6.25
- MA20 / MA60 / MA200: 5.94 / 4.87 / 3.69
- gap20 / gap60: 5.15% / 28.35%
- 5D return: -2.19%
- 20D high/low: 6.54 / 4.82

### Relative Strength

- ratio: 0.015806
- ratio_MA60: 0.014572
- ratio_gap: 8.46%
- ratio_slope_proxy(20d): 0.000353

### Volume (if available)

- volume: 51921521.00
- volume_MA20: 67938946.05
- volume_ratio: 0.76

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

- close: 11.38
- MA20 / MA60 / MA200: 9.63 / 8.17 / 11.26
- gap20 / gap60: 18.18% / 39.27%
- 5D return: 20.68%
- 20D high/low: 11.38 / 8.77

### Relative Strength

- ratio: 0.045716
- ratio_MA60: 0.039535
- ratio_gap: 15.63%
- ratio_slope_proxy(20d): 0.002451

### Volume (if available)

- volume: 46157149.00
- volume_MA20: 11132017.45
- volume_ratio: 4.15

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-02**
- 실행시간(UTC): **2026-03-03 00:45:52**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 24.0 bp / latest 3.12
- IG OAS 4주 변화: 11.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: -18.0 bp / latest 1.72
- VIX: 19.86
- NFCI: -0.56294

### Leadership ratios
- SILJ/SLV gap: 10.53% / slope_proxy: -0.004904
- GDXJ/GLD gap: 7.98% / slope_proxy: 0.014722

## VZLA (Vizsla Silver)
- close: 4.4 | RSI14: 47.598718 | ATR14%: 7.92%
- MA20 gap: 5.34% | MA50 gap: -15.21% | MA200 gap: 6.86%
- vol_ratio(Volume/Vol20): 0.656293 | gap_open: 1.37%
- RS vs SILJ gap: -33.52% / slope_proxy: -0.025045
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

## SCZM (Santacruz Silver)
- close: 12.15 | RSI14: 53.610345 | ATR14%: 9.00%
- MA20 gap: 7.33% | MA50 gap: 7.23% | MA200 gap: 84.58%
- vol_ratio(Volume/Vol20): 0.921471 | gap_open: 0.32%
- SilverMarginGate: SI=91.139999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.29% / slope_proxy: 0.022819
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
- close: 55.740002 | RSI14: 69.706994 | ATR14%: 10.13%
- MA20 gap: 36.62% | MA50 gap: 55.94% | MA200 gap: 317.79%
- vol_ratio(Volume/Vol20): 1.299853 | gap_open: 0.54%
- RS vs SILJ gap: 45.15% / slope_proxy: 0.246621
- RS vs GDXJ gap: 48.17% / slope_proxy: 0.065118
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
