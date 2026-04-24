# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-24**
- 실행시간(UTC): **2026-04-24 15:00:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.86 / 4주 변화 -35.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 -10.0 bp
- VIX (VIXCLS): 19.31
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.084819
- MA60: 7.866311
- gap: 15.49%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.322436
- MA60: 0.23605
- gap: 36.60%
- MA60_slope_proxy: 0.02535
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-24**
- 실행시간(UTC): **2026-04-24 15:00:43**

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
- TERM_SPREAD_10Y_POLICY: 108.82 bp / 4주 변화 6.61 bp
- CURVE_10s5s: 46.67 bp / 4주 변화 6.92 bp

## NWG Price
- close: 580.4
- MA50: 587.2498 / gap50: -1.17%
- MA200: 579.7709 / gap200: 0.11%

## Relative Strength
- RS vs FTSE gap: -2.82% / slope_proxy: -0.002507
- RS vs Peers gap: -4.68% / slope_proxy: -0.037542

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-24 15:00:51**

## Commodity Regime

- WTI ref (CL=F): 94.91 / 5D 13.19%
- Brent ref (BZ=F): 98.87 / 5D 9.39%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.96
- Gas ref (NG=F): 2.67 / 5D -0.15%

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

- close: 57.25
- MA20 / MA60 / MA200: 59.34 / 54.61 / 46.42
- gap20 / gap60: -3.52% / 4.83%
- 5D return: 6.43%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 1.008901
- ratio_MA60: 0.968193
- ratio_gap: 4.20%
- ratio_slope_proxy(20d): 0.038668

### Volume (if available)

- volume: 2045673.00
- volume_MA20: 16563913.65
- volume_ratio: 0.12

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.70
- MA20 / MA60 / MA200: 20.86 / 18.32 / 14.15
- gap20 / gap60: -0.76% / 13.04%
- 5D return: 1.25%
- 20D high/low: 21.97 / 19.98

### Relative Strength

- ratio: 0.521602
- ratio_MA60: 0.478056
- ratio_gap: 9.11%
- ratio_slope_proxy(20d): 0.049744

### Volume (if available)

- volume: 2998704.00
- volume_MA20: 28813940.20
- volume_ratio: 0.10

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.08
- MA20 / MA60 / MA200: 6.39 / 6.18 / 4.38
- gap20 / gap60: -4.81% / -1.62%
- 5D return: 2.36%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.014015
- ratio_MA60: 0.015827
- ratio_gap: -11.45%
- ratio_slope_proxy(20d): 0.000620

### Volume (if available)

- volume: 5079379.00
- volume_MA20: 28737438.95
- volume_ratio: 0.18

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

- close: 12.27
- MA20 / MA60 / MA200: 13.73 / 12.18 / 11.12
- gap20 / gap60: -10.64% / 0.69%
- 5D return: 7.02%
- 20D high/low: 17.53 / 11.45

### Relative Strength

- ratio: 0.047911
- ratio_MA60: 0.048379
- ratio_gap: -0.97%
- ratio_slope_proxy(20d): 0.003573

### Volume (if available)

- volume: 7898579.00
- volume_MA20: 26135548.95
- volume_ratio: 0.30

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-24**
- 실행시간(UTC): **2026-04-24 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.86
- IG OAS 4주 변화: -8.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -10.0 bp / latest 1.92
- VIX: 19.31
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.57% / slope_proxy: 0.014119
- GDXJ/GLD gap: -1.63% / slope_proxy: -0.004076

## VZLA (Vizsla Silver)
- close: 3.375 | RSI14: 47.071023 | ATR14%: 5.82%
- MA20 gap: 1.30% | MA50 gap: -5.88% | MA200 gap: -19.70%
- vol_ratio(Volume/Vol20): 0.193905 | gap_open: 1.21%
- RS vs SILJ gap: -5.49% / slope_proxy: -0.025617
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
- close: 8.66 | RSI14: 48.980966 | ATR14%: 7.96%
- MA20 gap: 2.80% | MA50 gap: -6.75% | MA200 gap: 11.69%
- vol_ratio(Volume/Vol20): 0.290081 | gap_open: 1.63%
- SilverMarginGate: SI=75.910004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.46% / slope_proxy: -0.02943
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
- close: 38.310001 | RSI14: 49.074842 | ATR14%: 9.52%
- MA20 gap: 0.50% | MA50 gap: -2.91% | MA200 gap: 91.74%
- vol_ratio(Volume/Vol20): 0.282035 | gap_open: 1.48%
- RS vs SILJ gap: 3.40% / slope_proxy: 0.052715
- RS vs GDXJ gap: 3.17% / slope_proxy: 0.010429
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
