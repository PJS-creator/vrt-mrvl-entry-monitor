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
- 실행시간(UTC): **2026-04-08 15:01:00**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.12 / 4주 변화 6.0 bp
- IG OAS (BAMLC0A0CM): 0.86 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 1.98 / 4주 변화 20.0 bp
- VIX (VIXCLS): 25.78
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.343575
- MA60: 7.270244
- gap: 14.76%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.270492
- MA60: 0.215579
- gap: 25.47%
- MA60_slope_proxy: 0.003411
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-08**
- 실행시간(UTC): **2026-04-08 15:01:03**

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
- close: 609.6
- MA50: 598.5634 / gap50: 1.84%
- MA200: 573.0578 / gap200: 6.38%

## Relative Strength
- RS vs FTSE gap: -2.09% / slope_proxy: -0.003325
- RS vs Peers gap: -3.51% / slope_proxy: -0.042683

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-08 15:01:11**

## Commodity Regime

- WTI ref (CL=F): 95.32 / 5D -5.98%
- Brent ref (BZ=F): 94.44 / 5D -20.20%
- Brent Tier: **>=90**
- Brent-WTI spread: -0.88
- Gas ref (NG=F): 2.75 / 5D -4.51%

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

- close: 58.77
- MA20 / MA60 / MA200: 60.99 / 51.94 / 45.58
- gap20 / gap60: -3.63% / 13.15%
- 5D return: -9.58%
- 20D high/low: 66.24 / 55.58

### Relative Strength

- ratio: 1.019958
- ratio_MA60: 0.947543
- ratio_gap: 7.64%
- ratio_slope_proxy(20d): 0.038987

### Volume (if available)

- volume: 13353353.00
- volume_MA20: 20559927.65
- volume_ratio: 0.65

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.62
- MA20 / MA60 / MA200: 19.84 / 16.79 / 13.63
- gap20 / gap60: -1.11% / 16.92%
- 5D return: -5.42%
- 20D high/low: 20.86 / 18.57

### Relative Strength

- ratio: 0.497591
- ratio_MA60: 0.451941
- ratio_gap: 10.10%
- ratio_slope_proxy(20d): 0.054707

### Volume (if available)

- volume: 27513419.00
- volume_MA20: 35794485.95
- volume_ratio: 0.77

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

- close: 6.54
- MA20 / MA60 / MA200: 6.53 / 5.85 / 4.17
- gap20 / gap60: 0.14% / 11.75%
- 5D return: -1.43%
- 20D high/low: 6.93 / 6.20

### Relative Strength

- ratio: 0.016130
- ratio_MA60: 0.015537
- ratio_gap: 3.82%
- ratio_slope_proxy(20d): 0.000819

### Volume (if available)

- volume: 9014974.00
- volume_MA20: 35224798.70
- volume_ratio: 0.26

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

- close: 14.19
- MA20 / MA60 / MA200: 15.00 / 11.44 / 11.32
- gap20 / gap60: -5.44% / 23.97%
- 5D return: -9.99%
- 20D high/low: 17.53 / 12.28

### Relative Strength

- ratio: 0.052635
- ratio_MA60: 0.047384
- ratio_gap: 11.08%
- ratio_slope_proxy(20d): 0.006503

### Volume (if available)

- volume: 23076299.00
- volume_MA20: 36258484.95
- volume_ratio: 0.64

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
- 실행시간(UTC): **2026-04-08 15:01:18**

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
- 10Y Real Yield 4주 변화: 20.0 bp / latest 1.98
- VIX: 25.78
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 4.47% / slope_proxy: 0.000504
- GDXJ/GLD gap: 0.14% / slope_proxy: -0.004574

## VZLA (Vizsla Silver)
- close: 3.27 | RSI14: 40.9185 | ATR14%: 7.17%
- MA20 gap: -2.17% | MA50 gap: -17.93% | MA200 gap: -21.71%
- vol_ratio(Volume/Vol20): 0.354543 | gap_open: 6.81%
- RS vs SILJ gap: -19.93% / slope_proxy: -0.0274
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
- close: 8.19 | RSI14: 44.957462 | ATR14%: 10.07%
- MA20 gap: -0.33% | MA50 gap: -19.74% | MA200 gap: 10.49%
- vol_ratio(Volume/Vol20): 0.347448 | gap_open: 9.92%
- SilverMarginGate: SI=75.455002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.57% / slope_proxy: -0.022173
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
- close: 37.380001 | RSI14: 51.278204 | ATR14%: 11.28%
- MA20 gap: 5.45% | MA50 gap: -5.42% | MA200 gap: 110.48%
- vol_ratio(Volume/Vol20): 0.358438 | gap_open: 11.46%
- RS vs SILJ gap: 0.52% / slope_proxy: 0.143404
- RS vs GDXJ gap: -2.03% / slope_proxy: 0.037679
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trigger(Breakout/Retest)=FALSE
