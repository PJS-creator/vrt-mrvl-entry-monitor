# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-02**
- 실행시간(UTC): **2026-04-04 15:00:38**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.17 / 4주 변화 17.0 bp
- IG OAS (BAMLC0A0CM): 0.86 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 1.97 / 4주 변화 15.0 bp
- VIX (VIXCLS): 24.54
- NFCI: -0.4337

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.178091
- MA60: 7.145365
- gap: 14.45%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.273017
- MA60: 0.212795
- gap: 28.30%
- MA60_slope_proxy: 5.4e-05
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-02**
- 실행시간(UTC): **2026-04-04 15:00:42**

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
- TERM_SPREAD_10Y_POLICY: 111.15 bp / 4주 변화 38.03 bp
- CURVE_10s5s: 42.25 bp / 4주 변화 -14.4 bp

## NWG Price
- close: 575.4
- MA50: 600.9212 / gap50: -4.25%
- MA200: 572.1824 / gap200: 0.56%

## Relative Strength
- RS vs FTSE gap: -6.36% / slope_proxy: -0.003359
- RS vs Peers gap: -4.12% / slope_proxy: -0.044092

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-04 15:00:52**

## Commodity Regime

- WTI ref (CL=F): 111.54 / 5D 18.06%
- Brent ref (BZ=F): 109.03 / 5D 0.94%
- Brent Tier: **>=90**
- Brent-WTI spread: -2.51
- Gas ref (NG=F): 2.80 / 5D -6.64%

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

- close: 62.97
- MA20 / MA60 / MA200: 59.84 / 50.97 / 45.33
- gap20 / gap60: 5.22% / 23.54%
- 5D return: -2.16%
- 20D high/low: 66.24 / 53.12

### Relative Strength

- ratio: 1.062785
- ratio_MA60: 0.941527
- ratio_gap: 12.88%
- ratio_slope_proxy(20d): 0.035614

### Volume (if available)

- volume: 22356800.00
- volume_MA20: 23085145.00
- volume_ratio: 0.97

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.56
- MA20 / MA60 / MA200: 19.47 / 16.35 / 13.52
- gap20 / gap60: 5.58% / 25.73%
- 5D return: 1.13%
- 20D high/low: 20.81 / 17.60

### Relative Strength

- ratio: 0.536115
- ratio_MA60: 0.443505
- ratio_gap: 20.88%
- ratio_slope_proxy(20d): 0.051126

### Volume (if available)

- volume: 30490100.00
- volume_MA20: 40611435.00
- volume_ratio: 0.75

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

- close: 6.59
- MA20 / MA60 / MA200: 6.45 / 5.73 / 4.12
- gap20 / gap60: 2.19% / 15.01%
- 5D return: -4.35%
- 20D high/low: 6.93 / 5.93

### Relative Strength

- ratio: 0.016514
- ratio_MA60: 0.015398
- ratio_gap: 7.25%
- ratio_slope_proxy(20d): 0.000752

### Volume (if available)

- volume: 39485100.00
- volume_MA20: 38109895.00
- volume_ratio: 1.04

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

- close: 14.64
- MA20 / MA60 / MA200: 14.46 / 11.03 / 11.36
- gap20 / gap60: 1.23% / 32.70%
- 5D return: -12.96%
- 20D high/low: 17.53 / 11.38

### Relative Strength

- ratio: 0.052070
- ratio_MA60: 0.046475
- ratio_gap: 12.04%
- ratio_slope_proxy(20d): 0.006317

### Volume (if available)

- volume: 32333700.00
- volume_MA20: 36927740.00
- volume_ratio: 0.88

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-02**
- 실행시간(UTC): **2026-04-04 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 17.0 bp / latest 3.17
- IG OAS 4주 변화: 4.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 15.0 bp / latest 1.97
- VIX: 24.54
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 5.67% / slope_proxy: -0.00266
- GDXJ/GLD gap: -2.25% / slope_proxy: -0.003356

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 39.670747 | ATR14%: 7.55%
- MA20 gap: -5.75% | MA50 gap: -22.01% | MA200 gap: -21.99%
- vol_ratio(Volume/Vol20): 1.009887 | gap_open: 6.01%
- RS vs SILJ gap: -20.58% / slope_proxy: -0.027472
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
- close: 7.83 | RSI14: 40.96584 | ATR14%: 10.99%
- MA20 gap: -8.36% | MA50 gap: -26.37% | MA200 gap: 6.73%
- vol_ratio(Volume/Vol20): 0.984015 | gap_open: 7.44%
- SilverMarginGate: SI=72.735001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -20.05% / slope_proxy: -0.021007
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
- close: 36.009998 | RSI14: 48.900502 | ATR14%: 12.21%
- MA20 gap: -0.43% | MA50 gap: -10.56% | MA200 gap: 108.66%
- vol_ratio(Volume/Vol20): 0.678884 | gap_open: 7.36%
- RS vs SILJ gap: 0.58% / slope_proxy: 0.167303
- RS vs GDXJ gap: -0.87% / slope_proxy: 0.043897
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
