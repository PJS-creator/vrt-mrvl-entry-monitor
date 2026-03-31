# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-30**
- 실행시간(UTC): **2026-03-31 03:00:37**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.42 / 4주 변화 32.0 bp
- IG OAS (BAMLC0A0CM): 0.91 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.13 / 4주 변화 41.0 bp
- VIX (VIXCLS): 31.05
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.724934
- MA60: 7.03813
- gap: 9.76%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.242214
- MA60: 0.21116
- gap: 14.71%
- MA60_slope_proxy: -0.00549
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-30**
- 실행시간(UTC): **2026-03-31 03:00:48**

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
- TERM_SPREAD_10Y_POLICY: 114.35 bp / 4주 변화 55.85 bp
- CURVE_10s5s: 39.75 bp / 4주 변화 -21.48 bp

## NWG Price
- close: 545.4
- MA50: 605.7656 / gap50: -9.97%
- MA200: 571.3199 / gap200: -4.54%

## Relative Strength
- RS vs FTSE gap: -9.22% / slope_proxy: -0.003321
- RS vs Peers gap: -4.73% / slope_proxy: -0.047645

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-31 03:00:55**

## Commodity Regime

- WTI ref (CL=F): 102.06 / 5D 15.81%
- Brent ref (BZ=F): 106.20 / 5D 6.26%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.14
- Gas ref (NG=F): 2.85 / 5D -1.56%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **False**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 66.24
- MA20 / MA60 / MA200: 58.32 / 49.88 / 45.06
- gap20 / gap60: 13.58% / 32.80%
- 5D return: 9.83%
- 20D high/low: 66.24 / 52.99

### Relative Strength

- ratio: 1.069077
- ratio_MA60: 0.933993
- ratio_gap: 14.46%
- ratio_slope_proxy(20d): 0.029166

### Volume (if available)

- volume: 22158470.00
- volume_MA20: 21607293.50
- volume_ratio: 1.03

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.81
- MA20 / MA60 / MA200: 18.93 / 15.92 / 13.40
- gap20 / gap60: 9.95% / 30.74%
- 5D return: 7.99%
- 20D high/low: 20.81 / 16.73

### Relative Strength

- ratio: 0.565950
- ratio_MA60: 0.434800
- ratio_gap: 30.16%
- ratio_slope_proxy(20d): 0.045934

### Volume (if available)

- volume: 48947585.00
- volume_MA20: 38434449.25
- volume_ratio: 1.27

### Checks

- RISK_OK_SOFT: **False**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.65
- MA20 / MA60 / MA200: 6.39 / 5.62 / 4.07
- gap20 / gap60: 4.02% / 18.42%
- 5D return: 2.94%
- 20D high/low: 6.93 / 5.93

### Relative Strength

- ratio: 0.016546
- ratio_MA60: 0.015278
- ratio_gap: 8.30%
- ratio_slope_proxy(20d): 0.000705

### Volume (if available)

- volume: 39002292.00
- volume_MA20: 37724844.60
- volume_ratio: 1.03

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

- close: 16.89
- MA20 / MA60 / MA200: 13.95 / 10.63 / 11.40
- gap20 / gap60: 21.07% / 58.92%
- 5D return: 6.90%
- 20D high/low: 17.53 / 11.14

### Relative Strength

- ratio: 0.057519
- ratio_MA60: 0.045559
- ratio_gap: 26.25%
- ratio_slope_proxy(20d): 0.006078

### Volume (if available)

- volume: 22102742.00
- volume_MA20: 37692622.10
- volume_ratio: 0.59

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

- 데이터 기준일(주가): **2026-03-30**
- 실행시간(UTC): **2026-03-31 03:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 32.0 bp / latest 3.42
- IG OAS 4주 변화: 6.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 41.0 bp / latest 2.13
- VIX: 31.05
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -1.95% / slope_proxy: -0.004631
- GDXJ/GLD gap: -8.44% / slope_proxy: -0.001624

## VZLA (Vizsla Silver)
- close: 3.13 | RSI14: 34.501156 | ATR14%: 8.33%
- MA20 gap: -12.52% | MA50 gap: -28.17% | MA200 gap: -25.16%
- vol_ratio(Volume/Vol20): 0.828038 | gap_open: 1.90%
- RS vs SILJ gap: -17.26% / slope_proxy: -0.027162
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.59 | RSI14: 36.871433 | ATR14%: 11.23%
- MA20 gap: -14.61% | MA50 gap: -30.19% | MA200 gap: 4.60%
- vol_ratio(Volume/Vol20): 0.675197 | gap_open: 3.75%
- SilverMarginGate: SI=72.364998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.13% / slope_proxy: -0.019182
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 30.469999 | RSI14: 40.219022 | ATR14%: 14.72%
- MA20 gap: -19.20% | MA50 gap: -24.72% | MA200 gap: 81.65%
- vol_ratio(Volume/Vol20): 0.681857 | gap_open: 1.19%
- RS vs SILJ gap: -3.67% / slope_proxy: 0.196901
- RS vs GDXJ gap: -6.41% / slope_proxy: 0.051673
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
