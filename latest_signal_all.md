# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-19**
- 실행시간(UTC): **2026-03-19 15:00:38**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.2 / 4주 변화 34.0 bp
- IG OAS (BAMLC0A0CM): 0.91 / 4주 변화 13.0 bp
- 10Y Real Yield (DFII10): 1.83 / 4주 변화 4.0 bp
- VIX (VIXCLS): 25.09
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.381252
- MA60: 6.745871
- gap: 24.24%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.222866
- MA60: 0.21056
- gap: 5.84%
- MA60_slope_proxy: -0.012881
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-19**
- 실행시간(UTC): **2026-03-19 15:00:41**

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
- TERM_SPREAD_10Y_POLICY: 90.36 bp / 4주 변화 26.11 bp
- CURVE_10s5s: 50.54 bp / 4주 변화 -8.34 bp

## NWG Price
- close: 530.8
- MA50: 620.3261 / gap50: -14.43%
- MA200: 570.6955 / gap200: -6.99%

## Relative Strength
- RS vs FTSE gap: -13.17% / slope_proxy: -0.002796
- RS vs Peers gap: -6.21% / slope_proxy: -0.054889

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-19 15:00:47**

## Commodity Regime

- WTI ref (CL=F): 96.49 / 5D 0.79%
- Brent ref (BZ=F): 105.98 / 5D 5.49%
- Brent Tier: **>=90**
- Brent-WTI spread: 9.49
- Gas ref (NG=F): 3.20 / 5D -1.14%

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

- close: 60.40
- MA20 / MA60 / MA200: 54.57 / 47.26 / 44.33
- gap20 / gap60: 10.70% / 27.82%
- 5D return: 3.42%
- 20D high/low: 60.40 / 50.70

### Relative Strength

- ratio: 1.015295
- ratio_MA60: 0.913965
- ratio_gap: 11.09%
- ratio_slope_proxy(20d): 0.016285

### Volume (if available)

- volume: 8990420.00
- volume_MA20: 19039701.00
- volume_ratio: 0.47

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.20
- MA20 / MA60 / MA200: 17.76 / 14.97 / 13.09
- gap20 / gap60: 13.79% / 34.99%
- 5D return: 6.51%
- 20D high/low: 20.20 / 15.79

### Relative Strength

- ratio: 0.559540
- ratio_MA60: 0.415076
- ratio_gap: 34.80%
- ratio_slope_proxy(20d): 0.029332

### Volume (if available)

- volume: 15275573.00
- volume_MA20: 32543513.65
- volume_ratio: 0.47

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

- close: 6.54
- MA20 / MA60 / MA200: 6.32 / 5.31 / 3.93
- gap20 / gap60: 3.44% / 22.96%
- 5D return: 4.06%
- 20D high/low: 6.58 / 5.93

### Relative Strength

- ratio: 0.016609
- ratio_MA60: 0.015031
- ratio_gap: 10.50%
- ratio_slope_proxy(20d): 0.000622

### Volume (if available)

- volume: 7093621.00
- volume_MA20: 37478796.05
- volume_ratio: 0.19

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 16.05
- MA20 / MA60 / MA200: 11.64 / 9.53 / 11.36
- gap20 / gap60: 37.82% / 68.34%
- 5D return: 25.82%
- 20D high/low: 16.05 / 9.30

### Relative Strength

- ratio: 0.054497
- ratio_MA60: 0.043183
- ratio_gap: 26.20%
- ratio_slope_proxy(20d): 0.004684

### Volume (if available)

- volume: 52165690.00
- volume_MA20: 26076199.50
- volume_ratio: 2.00

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

- 데이터 기준일(주가): **2026-03-19**
- 실행시간(UTC): **2026-03-19 15:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 34.0 bp / latest 3.2
- IG OAS 4주 변화: 13.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 4.0 bp / latest 1.83
- VIX: 25.09
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -2.15% / slope_proxy: -0.006101
- GDXJ/GLD gap: -12.79% / slope_proxy: 0.006766

## VZLA (Vizsla Silver)
- close: 3.145 | RSI14: 28.626347 | ATR14%: 9.50%
- MA20 gap: -19.63% | MA50 gap: -33.56% | MA200 gap: -24.97%
- vol_ratio(Volume/Vol20): 0.691789 | gap_open: 8.63%
- RS vs SILJ gap: -22.10% / slope_proxy: -0.027553
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.33 | RSI14: 29.339486 | ATR14%: 12.78%
- MA20 gap: -29.88% | MA50 gap: -35.21% | MA200 gap: 3.39%
- vol_ratio(Volume/Vol20): 0.545018 | gap_open: 9.59%
- SilverMarginGate: SI=70.25 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.78% / slope_proxy: -0.006391
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
- close: 30.565001 | RSI14: 37.631438 | ATR14%: 16.77%
- MA20 gap: -29.18% | MA50 gap: -24.22% | MA200 gap: 93.58%
- vol_ratio(Volume/Vol20): 0.800377 | gap_open: 8.47%
- RS vs SILJ gap: 0.18% / slope_proxy: 0.253463
- RS vs GDXJ gap: -0.79% / slope_proxy: 0.066523
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
