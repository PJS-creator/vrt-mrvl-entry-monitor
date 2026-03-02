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
- 실행시간(UTC): **2026-03-02 18:47:22**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.12 / 4주 변화 24.0 bp
- IG OAS (BAMLC0A0CM): 0.86 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 1.74 / 4주 변화 -15.0 bp
- VIX (VIXCLS): 19.86
- NFCI: -0.5629

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.602664
- MA60: 6.256143
- gap: 21.52%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.200811
- MA60: 0.216681
- gap: -7.32%
- MA60_slope_proxy: -0.018952
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-02**
- 실행시간(UTC): **2026-03-02 18:47:26**

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

- 실행시간(UTC): **2026-03-02 18:47:32**

## Commodity Regime

- WTI ref (CL=F): 71.17 / 5D 7.33%
- Brent ref (BZ=F): 77.64 / 5D 8.60%
- Brent Tier: **70-80**
- Brent-WTI spread: 6.47
- Gas ref (NG=F): 2.97 / 5D -0.54%

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

- close: 53.70
- MA20 / MA60 / MA200: 48.44 / 44.17 / 43.57
- gap20 / gap60: 10.86% / 21.58%
- 5D return: 2.42%
- 20D high/low: 53.70 / 43.80

### Relative Strength

- ratio: 0.946589
- ratio_MA60: 0.903158
- ratio_gap: 4.81%
- ratio_slope_proxy(20d): -0.010969

### Volume (if available)

- volume: 23538329.00
- volume_MA20: 13264286.45
- volume_ratio: 1.77

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.06
- MA20 / MA60 / MA200: 15.68 / 13.61 / 12.63
- gap20 / gap60: 8.79% / 25.35%
- 5D return: 5.70%
- 20D high/low: 17.06 / 14.87

### Relative Strength

- ratio: 0.442485
- ratio_MA60: 0.388770
- ratio_gap: 13.82%
- ratio_slope_proxy(20d): 0.001648

### Volume (if available)

- volume: 30758080.00
- volume_MA20: 22653559.00
- volume_ratio: 1.36

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

- close: 6.16
- MA20 / MA60 / MA200: 5.94 / 4.87 / 3.69
- gap20 / gap60: 3.71% / 26.54%
- 5D return: -3.60%
- 20D high/low: 6.54 / 4.82

### Relative Strength

- ratio: 0.015666
- ratio_MA60: 0.014570
- ratio_gap: 7.52%
- ratio_slope_proxy(20d): 0.000350

### Volume (if available)

- volume: 32130634.00
- volume_MA20: 66949401.70
- volume_ratio: 0.48

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

- close: 11.02
- MA20 / MA60 / MA200: 9.61 / 8.17 / 11.26
- gap20 / gap60: 14.63% / 34.92%
- 5D return: 16.83%
- 20D high/low: 11.02 / 8.77

### Relative Strength

- ratio: 0.044454
- ratio_MA60: 0.039514
- ratio_gap: 12.50%
- ratio_slope_proxy(20d): 0.002430

### Volume (if available)

- volume: 34327636.00
- volume_MA20: 10540541.80
- volume_ratio: 3.26

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
- 실행시간(UTC): **2026-03-02 18:47:38**

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
- 10Y Real Yield 4주 변화: -15.0 bp / latest 1.74
- VIX: 19.86
- NFCI: -0.56294

### Leadership ratios
- SILJ/SLV gap: 10.10% / slope_proxy: -0.004936
- GDXJ/GLD gap: 6.56% / slope_proxy: 0.014651

## VZLA (Vizsla Silver)
- close: 4.31 | RSI14: 45.933206 | ATR14%: 8.08%
- MA20 gap: 3.30% | MA50 gap: -16.91% | MA200 gap: 4.69%
- vol_ratio(Volume/Vol20): 0.458875 | gap_open: 1.37%
- RS vs SILJ gap: -33.54% / slope_proxy: -0.025045
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 11.9921 | RSI14: 52.65543 | ATR14%: 9.12%
- MA20 gap: 6.01% | MA50 gap: 5.87% | MA200 gap: 82.20%
- vol_ratio(Volume/Vol20): 0.690239 | gap_open: 0.32%
- SilverMarginGate: SI=88.315002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.64% / slope_proxy: 0.022857
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
- close: 52.9575 | RSI14: 67.401862 | ATR14%: 10.63%
- MA20 gap: 30.25% | MA50 gap: 48.38% | MA200 gap: 297.35%
- vol_ratio(Volume/Vol20): 0.929328 | gap_open: 0.54%
- RS vs SILJ gap: 40.86% / slope_proxy: 0.245917
- RS vs GDXJ gap: 43.48% / slope_proxy: 0.064923
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
