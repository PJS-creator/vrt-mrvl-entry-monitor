# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-23**
- 실행시간(UTC): **2026-03-23 15:00:38**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.24 / 4주 변화 38.0 bp
- IG OAS (BAMLC0A0CM): 0.88 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 1.88 / 4주 변화 9.0 bp
- VIX (VIXCLS): 26.78
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.592557
- MA60: 6.831131
- gap: 25.79%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.228516
- MA60: 0.210294
- gap: 8.67%
- MA60_slope_proxy: -0.011385
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-23**
- 실행시간(UTC): **2026-03-23 15:00:49**

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
- TERM_SPREAD_10Y_POLICY: 103.96 bp / 4주 변화 40.28 bp
- CURVE_10s5s: 38.75 bp / 4주 변화 -20.04 bp

## NWG Price
- close: 533.2
- MA50: 615.7923 / gap50: -13.41%
- MA200: 570.7745 / gap200: -6.58%

## Relative Strength
- RS vs FTSE gap: -11.51% / slope_proxy: -0.003013
- RS vs Peers gap: -6.96% / slope_proxy: -0.05373

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-23 15:00:58**

## Commodity Regime

- WTI ref (CL=F): 89.70 / 5D -4.06%
- Brent ref (BZ=F): 101.68 / 5D 1.47%
- Brent Tier: **>=90**
- Brent-WTI spread: 11.98
- Gas ref (NG=F): 2.92 / 5D -3.34%

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

- close: 60.15
- MA20 / MA60 / MA200: 55.38 / 47.93 / 44.52
- gap20 / gap60: 8.62% / 25.52%
- 5D return: 5.07%
- 20D high/low: 60.71 / 50.70

### Relative Strength

- ratio: 1.008128
- ratio_MA60: 0.917577
- ratio_gap: 9.87%
- ratio_slope_proxy(20d): 0.019330

### Volume (if available)

- volume: 10843820.00
- volume_MA20: 20129111.00
- volume_ratio: 0.54

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.30
- MA20 / MA60 / MA200: 18.04 / 15.20 / 13.17
- gap20 / gap60: 6.96% / 26.94%
- 5D return: 0.68%
- 20D high/low: 19.78 / 16.54

### Relative Strength

- ratio: 0.521343
- ratio_MA60: 0.419830
- ratio_gap: 24.18%
- ratio_slope_proxy(20d): 0.034165

### Volume (if available)

- volume: 19171615.00
- volume_MA20: 34828915.75
- volume_ratio: 0.55

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

- close: 6.46
- MA20 / MA60 / MA200: 6.30 / 5.39 / 3.97
- gap20 / gap60: 2.51% / 19.85%
- 5D return: 4.21%
- 20D high/low: 6.58 / 5.93

### Relative Strength

- ratio: 0.016089
- ratio_MA60: 0.015093
- ratio_gap: 6.60%
- ratio_slope_proxy(20d): 0.000609

### Volume (if available)

- volume: 12182013.00
- volume_MA20: 36056510.65
- volume_ratio: 0.34

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

- close: 15.61
- MA20 / MA60 / MA200: 12.17 / 9.80 / 11.36
- gap20 / gap60: 28.26% / 59.31%
- 5D return: 27.12%
- 20D high/low: 15.81 / 9.30

### Relative Strength

- ratio: 0.055479
- ratio_MA60: 0.043788
- ratio_gap: 26.70%
- ratio_slope_proxy(20d): 0.005034

### Volume (if available)

- volume: 19811554.00
- volume_MA20: 32265367.70
- volume_ratio: 0.61

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

- 데이터 기준일(주가): **2026-03-23**
- 실행시간(UTC): **2026-03-23 15:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 38.0 bp / latest 3.24
- IG OAS 4주 변화: 10.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.88
- VIX: 26.78
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: 0.32% / slope_proxy: -0.006721
- GDXJ/GLD gap: -7.17% / slope_proxy: 0.004016

## VZLA (Vizsla Silver)
- close: 3.175 | RSI14: 32.399013 | ATR14%: 9.15%
- MA20 gap: -17.25% | MA50 gap: -31.44% | MA200 gap: -24.24%
- vol_ratio(Volume/Vol20): 0.458199 | gap_open: 1.33%
- RS vs SILJ gap: -21.95% / slope_proxy: -0.027554
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
- close: 7.74 | RSI14: 34.486331 | ATR14%: 12.01%
- MA20 gap: -22.87% | MA50 gap: -30.98% | MA200 gap: 8.45%
- vol_ratio(Volume/Vol20): 0.595917 | gap_open: 1.96%
- SilverMarginGate: SI=70.050003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.15% / slope_proxy: -0.01031
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
- close: 32.259998 | RSI14: 40.633525 | ATR14%: 15.05%
- MA20 gap: -23.51% | MA50 gap: -20.32% | MA200 gap: 100.75%
- vol_ratio(Volume/Vol20): 0.41163 | gap_open: 1.70%
- RS vs SILJ gap: 2.12% / slope_proxy: 0.23944
- RS vs GDXJ gap: 0.57% / slope_proxy: 0.062889
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
