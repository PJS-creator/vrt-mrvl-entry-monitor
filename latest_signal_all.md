# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-13**
- 실행시간(UTC): **2026-05-13 15:00:48**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.82 / 4주 변화 -2.0 bp
- IG OAS (BAMLC0A0CM): 0.77 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 1.95 / 4주 변화 3.0 bp
- VIX (VIXCLS): 17.99
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.64037
- MA60: 8.541863
- gap: 24.57%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.314437
- MA60: 0.261195
- gap: 20.38%
- MA60_slope_proxy: 0.038631
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-13**
- 실행시간(UTC): **2026-05-13 15:00:51**

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
- TERM_SPREAD_10Y_POLICY: 120.89 bp / 4주 변화 14.62 bp
- CURVE_10s5s: 44.61 bp / 4주 변화 -0.44 bp

## NWG Price
- close: 561.7013
- MA50: 577.547 / gap50: -2.74%
- MA200: 584.037 / gap200: -3.82%

## Relative Strength
- RS vs FTSE gap: -2.93% / slope_proxy: -0.002252
- RS vs Peers gap: -5.82% / slope_proxy: -0.036941

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-13 15:01:02**

## Commodity Regime

- WTI ref (CL=F): 102.99 / 5D 8.32%
- Brent ref (BZ=F): 107.45 / 5D 6.10%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.46
- Gas ref (NG=F): 2.88 / 5D 5.38%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 55.92
- MA20 / MA60 / MA200: 56.92 / 57.15 / 47.31
- gap20 / gap60: -1.76% / -2.15%
- 5D return: 1.45%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.977793
- ratio_MA60: 0.994259
- ratio_gap: -1.66%
- ratio_slope_proxy(20d): 0.038706

### Volume (if available)

- volume: 1878365.00
- volume_MA20: 12349318.25
- volume_ratio: 0.15

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.27
- MA20 / MA60 / MA200: 21.07 / 19.51 / 14.66
- gap20 / gap60: -3.77% / 3.87%
- 5D return: -3.06%
- 20D high/low: 22.03 / 20.27

### Relative Strength

- ratio: 0.532746
- ratio_MA60: 0.505743
- ratio_gap: 5.34%
- ratio_slope_proxy(20d): 0.045061

### Volume (if available)

- volume: 2140156.00
- volume_MA20: 18770907.80
- volume_ratio: 0.11

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.58
- MA20 / MA60 / MA200: 6.40 / 6.42 / 4.62
- gap20 / gap60: 2.75% / 2.43%
- 5D return: 5.54%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015099
- ratio_MA60: 0.015839
- ratio_gap: -4.67%
- ratio_slope_proxy(20d): 0.000102

### Volume (if available)

- volume: 4051298.00
- volume_MA20: 35278379.90
- volume_ratio: 0.11

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

- close: 13.66
- MA20 / MA60 / MA200: 12.44 / 12.84 / 10.91
- gap20 / gap60: 9.82% / 6.43%
- 5D return: 13.88%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.056945
- ratio_MA60: 0.049411
- ratio_gap: 15.25%
- ratio_slope_proxy(20d): 0.001226

### Volume (if available)

- volume: 12402644.00
- volume_MA20: 21073802.20
- volume_ratio: 0.59

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

- 데이터 기준일(주가): **2026-05-13**
- 실행시간(UTC): **2026-05-13 15:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.82
- IG OAS 4주 변화: -4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 3.0 bp / latest 1.95
- VIX: 17.99
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -4.60% / slope_proxy: 0.002816
- GDXJ/GLD gap: 4.32% / slope_proxy: -0.003507

## VZLA (Vizsla Silver)
- close: 3.84 | RSI14: 62.856288 | ATR14%: 5.46%
- MA20 gap: 10.44% | MA50 gap: 10.67% | MA200 gap: -8.99%
- vol_ratio(Volume/Vol20): 0.275008 | gap_open: 1.56%
- RS vs SILJ gap: 0.96% / slope_proxy: -0.01206
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
- close: 10.11 | RSI14: 65.23161 | ATR14%: 6.56%
- MA20 gap: 16.25% | MA50 gap: 17.10% | MA200 gap: 25.48%
- vol_ratio(Volume/Vol20): 0.262028 | gap_open: 1.97%
- SilverMarginGate: SI=88.764999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.41% / slope_proxy: -0.025706
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
- close: 44.060001 | RSI14: 59.429512 | ATR14%: 8.32%
- MA20 gap: 11.63% | MA50 gap: 15.40% | MA200 gap: 97.96%
- vol_ratio(Volume/Vol20): 0.370868 | gap_open: 1.17%
- RS vs SILJ gap: 4.62% / slope_proxy: 0.033856
- RS vs GDXJ gap: 10.30% / slope_proxy: 0.006943
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
