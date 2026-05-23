# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-22**
- 실행시간(UTC): **2026-05-23 03:00:37**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.78 / 4주 변화 -8.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 2.18 / 4주 변화 26.0 bp
- VIX (VIXCLS): 16.76
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.533042
- MA60: 8.818857
- gap: 8.10%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.340661
- MA60: 0.2768
- gap: 23.07%
- MA60_slope_proxy: 0.040717
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-22**
- 실행시간(UTC): **2026-05-23 03:00:39**

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
- TERM_SPREAD_10Y_POLICY: 120.54 bp / 4주 변화 11.72 bp
- CURVE_10s5s: 46.61 bp / 4주 변화 -0.06 bp

## NWG Price
- close: 581.8
- MA50: 575.8209 / gap50: 1.04%
- MA200: 585.4836 / gap200: -0.63%

## Relative Strength
- RS vs FTSE gap: -0.20% / slope_proxy: -0.001909
- RS vs Peers gap: -4.19% / slope_proxy: -0.034358

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-23 03:00:46**

## Commodity Regime

- WTI ref (CL=F): 97.00 / 5D -7.99%
- Brent ref (BZ=F): 103.94 / 5D -4.87%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.94
- Gas ref (NG=F): 3.03 / 5D 2.50%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 58.81
- MA20 / MA60 / MA200: 57.93 / 58.12 / 47.87
- gap20 / gap60: 1.52% / 1.20%
- 5D return: -1.36%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.988570
- ratio_MA60: 1.001202
- ratio_gap: -1.26%
- ratio_slope_proxy(20d): 0.033083

### Volume (if available)

- volume: 6390743.00
- volume_MA20: 12359812.15
- volume_ratio: 0.52

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.90
- MA20 / MA60 / MA200: 20.74 / 19.98 / 14.92
- gap20 / gap60: -4.05% / -0.39%
- 5D return: -0.15%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.547154
- ratio_MA60: 0.521845
- ratio_gap: 4.85%
- ratio_slope_proxy(20d): 0.046509

### Volume (if available)

- volume: 10230599.00
- volume_MA20: 17965264.95
- volume_ratio: 0.57

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.81
- MA20 / MA60 / MA200: 6.78 / 6.50 / 4.77
- gap20 / gap60: 0.50% / 4.69%
- 5D return: -3.27%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.015339
- ratio_MA60: 0.015804
- ratio_gap: -2.94%
- ratio_slope_proxy(20d): -0.000022

### Volume (if available)

- volume: 25434553.00
- volume_MA20: 38389847.65
- volume_ratio: 0.66

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.83
- MA20 / MA60 / MA200: 13.05 / 13.35 / 10.87
- gap20 / gap60: 6.00% / 3.63%
- 5D return: -2.81%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.057422
- ratio_MA60: 0.051106
- ratio_gap: 12.36%
- ratio_slope_proxy(20d): 0.002642

### Volume (if available)

- volume: 10322811.00
- volume_MA20: 20525805.55
- volume_ratio: 0.50

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-22**
- 실행시간(UTC): **2026-05-23 03:00:52**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.78
- IG OAS 4주 변화: -5.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.18
- VIX: 16.76
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -4.97% / slope_proxy: -0.008262
- GDXJ/GLD gap: -4.77% / slope_proxy: -0.004815

## VZLA (Vizsla Silver)
- close: 3.37 | RSI14: 45.843016 | ATR14%: 6.20%
- MA20 gap: -3.34% | MA50 gap: -0.44% | MA200 gap: -20.38%
- vol_ratio(Volume/Vol20): 0.572248 | gap_open: 0.00%
- RS vs SILJ gap: 4.07% / slope_proxy: -0.003406
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
- close: 8.03 | RSI14: 42.580766 | ATR14%: 7.94%
- MA20 gap: -6.45% | MA50 gap: -4.46% | MA200 gap: -2.39%
- vol_ratio(Volume/Vol20): 0.709626 | gap_open: 0.24%
- SilverMarginGate: SI=75.915001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.73% / slope_proxy: -0.016187
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
- close: 32.32 | RSI14: 39.758028 | ATR14%: 10.16%
- MA20 gap: -13.52% | MA50 gap: -12.94% | MA200 gap: 38.42%
- vol_ratio(Volume/Vol20): 0.60996 | gap_open: 1.47%
- RS vs SILJ gap: -8.65% / slope_proxy: 0.026713
- RS vs GDXJ gap: -6.54% / slope_proxy: 0.007832
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
