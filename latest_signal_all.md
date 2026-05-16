# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-15**
- 실행시간(UTC): **2026-05-16 03:00:36**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.76 / 4주 변화 -10.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 2.0 / 4주 변화 7.0 bp
- VIX (VIXCLS): 17.26
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 11.007121
- MA60: 8.658024
- gap: 27.13%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.317953
- MA60: 0.265269
- gap: 19.86%
- MA60_slope_proxy: 0.039629
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-15**
- 실행시간(UTC): **2026-05-16 03:00:39**

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
- TERM_SPREAD_10Y_POLICY: 127.79 bp / 4주 변화 28.44 bp
- CURVE_10s5s: 46.22 bp / 4주 변화 0.15 bp

## NWG Price
- close: 561.2
- MA50: 576.4904 / gap50: -2.65%
- MA200: 584.4346 / gap200: -3.98%

## Relative Strength
- RS vs FTSE gap: -1.69% / slope_proxy: -0.002176
- RS vs Peers gap: -5.25% / slope_proxy: -0.036793

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-16 03:00:48**

## Commodity Regime

- WTI ref (CL=F): 101.16 / 5D 6.02%
- Brent ref (BZ=F): 109.24 / 5D 7.85%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.08
- Gas ref (NG=F): 2.96 / 5D 7.40%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 59.62
- MA20 / MA60 / MA200: 57.22 / 57.46 / 47.45
- gap20 / gap60: 4.19% / 3.77%
- 5D return: 12.43%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 1.003028
- ratio_MA60: 0.997290
- ratio_gap: 0.58%
- ratio_slope_proxy(20d): 0.038409

### Volume (if available)

- volume: 16671142.00
- volume_MA20: 12164222.10
- volume_ratio: 1.37

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.93
- MA20 / MA60 / MA200: 20.93 / 19.65 / 14.72
- gap20 / gap60: -4.79% / 1.42%
- 5D return: -1.97%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.550097
- ratio_MA60: 0.510363
- ratio_gap: 7.79%
- ratio_slope_proxy(20d): 0.045573

### Volume (if available)

- volume: 13672918.00
- volume_MA20: 17325345.90
- volume_ratio: 0.79

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 7.04
- MA20 / MA60 / MA200: 6.48 / 6.44 / 4.66
- gap20 / gap60: 8.57% / 9.28%
- 5D return: 10.00%
- 20D high/low: 7.04 / 5.89

### Relative Strength

- ratio: 0.015981
- ratio_MA60: 0.015827
- ratio_gap: 0.97%
- ratio_slope_proxy(20d): 0.000032

### Volume (if available)

- volume: 30417239.00
- volume_MA20: 35842616.95
- volume_ratio: 0.85

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.23
- MA20 / MA60 / MA200: 12.56 / 12.96 / 10.89
- gap20 / gap60: 13.25% / 9.81%
- 5D return: 24.28%
- 20D high/low: 14.23 / 11.45

### Relative Strength

- ratio: 0.058841
- ratio_MA60: 0.049805
- ratio_gap: 18.14%
- ratio_slope_proxy(20d): 0.001481

### Volume (if available)

- volume: 23154495.00
- volume_MA20: 21389984.75
- volume_ratio: 1.08

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-15**
- 실행시간(UTC): **2026-05-16 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.76
- IG OAS 4주 변화: -5.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 7.0 bp / latest 2.0
- VIX: 17.26
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -2.40% / slope_proxy: 0.000259
- GDXJ/GLD gap: -2.67% / slope_proxy: -0.00346

## VZLA (Vizsla Silver)
- close: 3.5 | RSI14: 49.078259 | ATR14%: 6.47%
- MA20 gap: 0.19% | MA50 gap: 1.43% | MA200 gap: -17.16%
- vol_ratio(Volume/Vol20): 1.747359 | gap_open: 5.59%
- RS vs SILJ gap: 4.03% / slope_proxy: -0.009575
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.7 | RSI14: 48.628584 | ATR14%: 8.17%
- MA20 gap: -0.01% | MA50 gap: 1.24% | MA200 gap: 7.23%
- vol_ratio(Volume/Vol20): 0.972927 | gap_open: 9.38%
- SilverMarginGate: SI=76.294998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.65% / slope_proxy: -0.023316
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
- close: 36.16 | RSI14: 45.028237 | ATR14%: 10.50%
- MA20 gap: -7.23% | MA50 gap: -4.61% | MA200 gap: 60.01%
- vol_ratio(Volume/Vol20): 1.85716 | gap_open: 6.76%
- RS vs SILJ gap: -2.80% / slope_proxy: 0.028319
- RS vs GDXJ gap: -0.03% / slope_proxy: 0.006483
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
