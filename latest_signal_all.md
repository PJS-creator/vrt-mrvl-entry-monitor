# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-14**
- 실행시간(UTC): **2026-04-15 03:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.95 / 4주 변화 -32.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 -12.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 5.0 bp
- VIX (VIXCLS): 19.12
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.092533
- MA60: 7.480608
- gap: 21.55%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.296084
- MA60: 0.220959
- gap: 34.00%
- MA60_slope_proxy: 0.00971
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-14**
- 실행시간(UTC): **2026-04-15 03:00:49**

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
- TERM_SPREAD_10Y_POLICY: 100.8 bp / 4주 변화 -0.21 bp
- CURVE_10s5s: 45.89 bp / 4주 변화 -3.89 bp

## NWG Price
- close: 627.8
- MA50: 594.8844 / gap50: 5.53%
- MA200: 575.2236 / gap200: 9.14%

## Relative Strength
- RS vs FTSE gap: 1.42% / slope_proxy: -0.003071
- RS vs Peers gap: -0.69% / slope_proxy: -0.039428

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-15 03:00:57**

## Commodity Regime

- WTI ref (CL=F): 91.00 / 5D -19.43%
- Brent ref (BZ=F): 95.13 / 5D -12.94%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.13
- Gas ref (NG=F): 2.59 / 5D -9.62%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 55.38
- MA20 / MA60 / MA200: 61.08 / 52.91 / 45.89
- gap20 / gap60: -9.33% / 4.66%
- 5D return: -12.01%
- 20D high/low: 66.24 / 55.38

### Relative Strength

- ratio: 0.989812
- ratio_MA60: 0.953815
- ratio_gap: 3.77%
- ratio_slope_proxy(20d): 0.038667

### Volume (if available)

- volume: 13745061.00
- volume_MA20: 19336833.05
- volume_ratio: 0.71

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.01
- MA20 / MA60 / MA200: 20.34 / 17.39 / 13.82
- gap20 / gap60: 3.31% / 20.84%
- 5D return: 1.45%
- 20D high/low: 21.97 / 18.80

### Relative Strength

- ratio: 0.503475
- ratio_MA60: 0.461503
- ratio_gap: 9.09%
- ratio_slope_proxy(20d): 0.054756

### Volume (if available)

- volume: 28977964.00
- volume_MA20: 34715598.20
- volume_ratio: 0.83

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

- close: 6.17
- MA20 / MA60 / MA200: 6.57 / 5.99 / 4.25
- gap20 / gap60: -6.10% / 2.94%
- 5D return: -7.63%
- 20D high/low: 6.93 / 6.17

### Relative Strength

- ratio: 0.015318
- ratio_MA60: 0.015699
- ratio_gap: -2.43%
- ratio_slope_proxy(20d): 0.000796

### Volume (if available)

- volume: 27316800.00
- volume_MA20: 34164225.00
- volume_ratio: 0.80

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.51
- MA20 / MA60 / MA200: 15.05 / 11.78 / 11.25
- gap20 / gap60: -16.86% / 6.18%
- 5D return: -21.76%
- 20D high/low: 17.53 / 12.51

### Relative Strength

- ratio: 0.048175
- ratio_MA60: 0.047993
- ratio_gap: 0.38%
- ratio_slope_proxy(20d): 0.005895

### Volume (if available)

- volume: 15400467.00
- volume_MA20: 37898923.35
- volume_ratio: 0.41

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-14**
- 실행시간(UTC): **2026-04-15 03:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -32.0 bp / latest 2.95
- IG OAS 4주 변화: -12.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 5.0 bp / latest 1.92
- VIX: 19.12
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 1.64% / slope_proxy: 0.006863
- GDXJ/GLD gap: 2.68% / slope_proxy: -0.0045

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 49.272339 | ATR14%: 6.16%
- MA20 gap: 6.49% | MA50 gap: -8.03% | MA200 gap: -17.30%
- vol_ratio(Volume/Vol20): 0.930576 | gap_open: 1.81%
- RS vs SILJ gap: -15.08% / slope_proxy: -0.027522
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
- close: 9.03 | RSI14: 53.308838 | ATR14%: 8.50%
- MA20 gap: 13.16% | MA50 gap: -7.18% | MA200 gap: 20.02%
- vol_ratio(Volume/Vol20): 1.221335 | gap_open: 1.63%
- SilverMarginGate: SI=80.275002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.95% / slope_proxy: -0.023594
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
- close: 41.700001 | RSI14: 58.287489 | ATR14%: 9.59%
- MA20 gap: 18.07% | MA50 gap: 7.27% | MA200 gap: 125.63%
- vol_ratio(Volume/Vol20): 0.717985 | gap_open: 4.40%
- RS vs SILJ gap: 6.77% / slope_proxy: 0.106609
- RS vs GDXJ gap: 3.65% / slope_proxy: 0.027199
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
