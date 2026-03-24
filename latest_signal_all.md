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
- 실행시간(UTC): **2026-03-24 03:00:38**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.24 / 4주 변화 38.0 bp
- IG OAS (BAMLC0A0CM): 0.88 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.01 / 4주 변화 21.0 bp
- VIX (VIXCLS): 26.78
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.171082
- MA60: 6.824107
- gap: 19.74%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.230376
- MA60: 0.210325
- gap: 9.53%
- MA60_slope_proxy: -0.011354
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-23**
- 실행시간(UTC): **2026-03-24 03:00:41**

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
- close: 530.2
- MA50: 615.7323 / gap50: -13.89%
- MA200: 570.7595 / gap200: -7.11%

## Relative Strength
- RS vs FTSE gap: -11.17% / slope_proxy: -0.003009
- RS vs Peers gap: -6.86% / slope_proxy: -0.053712

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-24 03:00:48**

## Commodity Regime

- WTI ref (CL=F): 91.34 / 5D -2.31%
- Brent ref (BZ=F): 103.63 / 5D 3.41%
- Brent Tier: **>=90**
- Brent-WTI spread: 12.29
- Gas ref (NG=F): 2.92 / 5D -3.41%

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

- close: 60.31
- MA20 / MA60 / MA200: 55.39 / 47.93 / 44.52
- gap20 / gap60: 8.88% / 25.83%
- 5D return: 5.34%
- 20D high/low: 60.71 / 50.70

### Relative Strength

- ratio: 1.011404
- ratio_MA60: 0.917632
- ratio_gap: 10.22%
- ratio_slope_proxy(20d): 0.019384

### Volume (if available)

- volume: 22284047.00
- volume_MA20: 20704742.35
- volume_ratio: 1.08

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.27
- MA20 / MA60 / MA200: 18.04 / 15.20 / 13.17
- gap20 / gap60: 6.80% / 26.75%
- 5D return: 0.52%
- 20D high/low: 19.78 / 16.54

### Relative Strength

- ratio: 0.522931
- ratio_MA60: 0.419856
- ratio_gap: 24.55%
- ratio_slope_proxy(20d): 0.034192

### Volume (if available)

- volume: 51229960.00
- volume_MA20: 36435673.00
- volume_ratio: 1.41

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
- gap20 / gap60: 2.50% / 19.84%
- 5D return: 4.19%
- 20D high/low: 6.58 / 5.93

### Relative Strength

- ratio: 0.016197
- ratio_MA60: 0.015095
- ratio_gap: 7.30%
- ratio_slope_proxy(20d): 0.000611

### Volume (if available)

- volume: 47481274.00
- volume_MA20: 37821578.70
- volume_ratio: 1.26

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 15.80
- MA20 / MA60 / MA200: 12.18 / 9.80 / 11.37
- gap20 / gap60: 29.72% / 61.20%
- 5D return: 28.66%
- 20D high/low: 15.81 / 9.30

### Relative Strength

- ratio: 0.055014
- ratio_MA60: 0.043781
- ratio_gap: 25.66%
- ratio_slope_proxy(20d): 0.005027

### Volume (if available)

- volume: 52899606.00
- volume_MA20: 33931875.30
- volume_ratio: 1.56

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
- 실행시간(UTC): **2026-03-24 03:00:53**

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
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.01
- VIX: 26.78
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: 0.61% / slope_proxy: -0.0067
- GDXJ/GLD gap: -7.07% / slope_proxy: 0.004021

## VZLA (Vizsla Silver)
- close: 3.1 | RSI14: 30.069406 | ATR14%: 9.38%
- MA20 gap: -19.12% | MA50 gap: -33.03% | MA200 gap: -26.02%
- vol_ratio(Volume/Vol20): 1.161385 | gap_open: 1.33%
- RS vs SILJ gap: -22.53% / slope_proxy: -0.027568
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
- close: 7.59 | RSI14: 33.080636 | ATR14%: 12.31%
- MA20 gap: -24.31% | MA50 gap: -32.30% | MA200 gap: 6.35%
- vol_ratio(Volume/Vol20): 1.139147 | gap_open: 1.96%
- SilverMarginGate: SI=67.635002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.41% / slope_proxy: -0.010324
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
- close: 32.169998 | RSI14: 40.497542 | ATR14%: 15.16%
- MA20 gap: -23.71% | MA50 gap: -20.54% | MA200 gap: 100.20%
- vol_ratio(Volume/Vol20): 0.877223 | gap_open: 1.70%
- RS vs SILJ gap: 3.50% / slope_proxy: 0.239704
- RS vs GDXJ gap: 1.89% / slope_proxy: 0.062953
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
