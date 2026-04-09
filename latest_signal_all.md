# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-08**
- 실행시간(UTC): **2026-04-09 03:00:38**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.12 / 4주 변화 6.0 bp
- IG OAS (BAMLC0A0CM): 0.86 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 14.0 bp
- VIX (VIXCLS): 25.78
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.471291
- MA60: 7.272373
- gap: 16.49%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.270619
- MA60: 0.215581
- gap: 25.53%
- MA60_slope_proxy: 0.003413
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-07**
- 실행시간(UTC): **2026-04-09 03:00:45**

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
- TERM_SPREAD_10Y_POLICY: 102.8 bp / 4주 변화 28.0 bp
- CURVE_10s5s: 42.33 bp / 4주 변화 -13.2 bp

## NWG Price
- close: 569.0
- MA50: 599.3743 / gap50: -5.07%
- MA200: 572.5573 / gap200: -0.62%

## Relative Strength
- RS vs FTSE gap: -6.40% / slope_proxy: -0.003363
- RS vs Peers gap: -4.50% / slope_proxy: -0.043256

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-09 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 97.04 / 5D -4.28%
- Brent ref (BZ=F): 96.78 / 5D -18.23%
- Brent Tier: **>=90**
- Brent-WTI spread: -0.26
- Gas ref (NG=F): 2.73 / 5D -5.31%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 59.77
- MA20 / MA60 / MA200: 61.04 / 51.96 / 45.59
- gap20 / gap60: -2.07% / 15.03%
- 5D return: -8.05%
- 20D high/low: 66.24 / 55.58

### Relative Strength

- ratio: 1.029630
- ratio_MA60: 0.947704
- ratio_gap: 8.64%
- ratio_slope_proxy(20d): 0.039148

### Volume (if available)

- volume: 24340562.00
- volume_MA20: 21149103.10
- volume_ratio: 1.15

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.98
- MA20 / MA60 / MA200: 19.86 / 16.79 / 13.63
- gap20 / gap60: 0.59% / 18.99%
- 5D return: -3.71%
- 20D high/low: 20.86 / 18.57

### Relative Strength

- ratio: 0.505056
- ratio_MA60: 0.452066
- ratio_gap: 11.72%
- ratio_slope_proxy(20d): 0.054831

### Volume (if available)

- volume: 48638453.00
- volume_MA20: 36881672.65
- volume_ratio: 1.32

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.70
- MA20 / MA60 / MA200: 6.53 / 5.85 / 4.17
- gap20 / gap60: 2.54% / 14.52%
- 5D return: 1.06%
- 20D high/low: 6.93 / 6.20

### Relative Strength

- ratio: 0.016326
- ratio_MA60: 0.015540
- ratio_gap: 5.06%
- ratio_slope_proxy(20d): 0.000822

### Volume (if available)

- volume: 25246576.00
- volume_MA20: 36052818.80
- volume_ratio: 0.70

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.44
- MA20 / MA60 / MA200: 15.01 / 11.45 / 11.32
- gap20 / gap60: -3.82% / 26.15%
- 5D return: -8.38%
- 20D high/low: 17.53 / 12.28

### Relative Strength

- ratio: 0.052469
- ratio_MA60: 0.047382
- ratio_gap: 10.74%
- ratio_slope_proxy(20d): 0.006500

### Volume (if available)

- volume: 44642371.00
- volume_MA20: 37406063.55
- volume_ratio: 1.19

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-08**
- 실행시간(UTC): **2026-04-09 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 3.12
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 14.0 bp / latest 1.96
- VIX: 25.78
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 5.10% / slope_proxy: 0.000552
- GDXJ/GLD gap: 0.72% / slope_proxy: -0.004545

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 42.051045 | ATR14%: 7.10%
- MA20 gap: -1.32% | MA50 gap: -17.19% | MA200 gap: -20.99%
- vol_ratio(Volume/Vol20): 0.861257 | gap_open: 6.81%
- RS vs SILJ gap: -19.03% / slope_proxy: -0.02738
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.94 | RSI14: 42.643808 | ATR14%: 10.53%
- MA20 gap: -3.22% | MA50 gap: -22.15% | MA200 gap: 7.13%
- vol_ratio(Volume/Vol20): 0.681671 | gap_open: 9.92%
- SilverMarginGate: SI=74.059998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -19.88% / slope_proxy: -0.022296
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 37.0 | RSI14: 50.622776 | ATR14%: 11.39%
- MA20 gap: 4.43% | MA50 gap: -6.36% | MA200 gap: 108.36%
- vol_ratio(Volume/Vol20): 0.841846 | gap_open: 11.46%
- RS vs SILJ gap: -0.27% / slope_proxy: 0.143246
- RS vs GDXJ gap: -3.28% / slope_proxy: 0.037615
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
