# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-18**
- 실행시간(UTC): **2026-05-18 15:00:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.8 / 4주 변화 -3.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 2.0 / 4주 변화 7.0 bp
- VIX (VIXCLS): 18.43
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.13677
- MA60: 8.703341
- gap: 16.47%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.31391
- MA60: 0.267311
- gap: 17.43%
- MA60_slope_proxy: 0.039796
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-18**
- 실행시간(UTC): **2026-05-18 15:00:47**

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
- TERM_SPREAD_10Y_POLICY: 121.61 bp / 4주 변화 17.49 bp
- CURVE_10s5s: 45.34 bp / 4주 변화 -2.88 bp

## NWG Price
- close: 566.4
- MA50: 575.9271 / gap50: -1.65%
- MA200: 584.6331 / gap200: -3.12%

## Relative Strength
- RS vs FTSE gap: -1.89% / slope_proxy: -0.002154
- RS vs Peers gap: -5.26% / slope_proxy: -0.036487

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-18 15:00:56**

## Commodity Regime

- WTI ref (CL=F): 102.03 / 5D 4.04%
- Brent ref (BZ=F): 110.02 / 5D 5.58%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.99
- Gas ref (NG=F): 3.02 / 5D 3.71%

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

- close: 59.62
- MA20 / MA60 / MA200: 57.48 / 57.59 / 47.53
- gap20 / gap60: 3.72% / 3.52%
- 5D return: 8.12%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.991848
- ratio_MA60: 0.998049
- ratio_gap: -0.62%
- ratio_slope_proxy(20d): 0.037410

### Volume (if available)

- volume: 3521461.00
- volume_MA20: 11765973.05
- volume_ratio: 0.30

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.18
- MA20 / MA60 / MA200: 20.91 / 19.73 / 14.76
- gap20 / gap60: -3.49% / 2.30%
- 5D return: -2.75%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.552574
- ratio_MA60: 0.512927
- ratio_gap: 7.73%
- ratio_slope_proxy(20d): 0.046155

### Volume (if available)

- volume: 4944816.00
- volume_MA20: 16643525.80
- volume_ratio: 0.30

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 7.42
- MA20 / MA60 / MA200: 6.56 / 6.46 / 4.69
- gap20 / gap60: 13.09% / 14.91%
- 5D return: 13.28%
- 20D high/low: 7.42 / 6.05

### Relative Strength

- ratio: 0.016345
- ratio_MA60: 0.015821
- ratio_gap: 3.31%
- ratio_slope_proxy(20d): 0.000009

### Volume (if available)

- volume: 13135055.00
- volume_MA20: 35126637.75
- volume_ratio: 0.37

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

- close: 14.28
- MA20 / MA60 / MA200: 12.71 / 13.04 / 10.89
- gap20 / gap60: 12.35% / 9.51%
- 5D return: 22.85%
- 20D high/low: 14.28 / 11.45

### Relative Strength

- ratio: 0.057749
- ratio_MA60: 0.050054
- ratio_gap: 15.37%
- ratio_slope_proxy(20d): 0.001742

### Volume (if available)

- volume: 7984881.00
- volume_MA20: 20956194.05
- volume_ratio: 0.38

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

- 데이터 기준일(주가): **2026-05-18**
- 실행시간(UTC): **2026-05-18 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.8
- IG OAS 4주 변화: -5.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 7.0 bp / latest 2.0
- VIX: 18.43
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -3.86% / slope_proxy: -0.000787
- GDXJ/GLD gap: -2.87% / slope_proxy: -0.003597

## VZLA (Vizsla Silver)
- close: 3.395 | RSI14: 45.696687 | ATR14%: 6.56%
- MA20 gap: -2.65% | MA50 gap: -1.27% | MA200 gap: -19.69%
- vol_ratio(Volume/Vol20): 0.245945 | gap_open: 1.14%
- RS vs SILJ gap: 2.02% / slope_proxy: -0.008445
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
- close: 8.6 | RSI14: 47.677964 | ATR14%: 8.06%
- MA20 gap: -0.87% | MA50 gap: 0.41% | MA200 gap: 5.65%
- vol_ratio(Volume/Vol20): 0.310428 | gap_open: 1.21%
- SilverMarginGate: SI=76.910004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.84% / slope_proxy: -0.021962
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
- close: 34.82 | RSI14: 43.031383 | ATR14%: 10.53%
- MA20 gap: -9.61% | MA50 gap: -7.95% | MA200 gap: 53.02%
- vol_ratio(Volume/Vol20): 0.389088 | gap_open: 0.95%
- RS vs SILJ gap: -5.31% / slope_proxy: 0.027095
- RS vs GDXJ gap: -3.45% / slope_proxy: 0.006574
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
