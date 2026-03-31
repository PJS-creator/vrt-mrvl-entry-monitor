# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-31**
- 실행시간(UTC): **2026-03-31 15:00:42**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.46 / 4주 변화 43.0 bp
- IG OAS (BAMLC0A0CM): 0.93 / 4주 변화 8.0 bp
- 10Y Real Yield (DFII10): 2.13 / 4주 변화 41.0 bp
- VIX (VIXCLS): 30.61
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.879778
- MA60: 7.067899
- gap: 11.49%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.252709
- MA60: 0.211384
- gap: 19.55%
- MA60_slope_proxy: -0.003976
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-31**
- 실행시간(UTC): **2026-03-31 15:00:54**

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
- TERM_SPREAD_10Y_POLICY: 114.35 bp / 4주 변화 60.0 bp
- CURVE_10s5s: 39.75 bp / 4주 변화 -19.88 bp

## NWG Price
- close: 551.4
- MA50: 603.7628 / gap50: -8.67%
- MA200: 571.4704 / gap200: -3.51%

## Relative Strength
- RS vs FTSE gap: -8.51% / slope_proxy: -0.003365
- RS vs Peers gap: -4.58% / slope_proxy: -0.046803

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-31 15:01:01**

## Commodity Regime

- WTI ref (CL=F): 104.00 / 5D 12.62%
- Brent ref (BZ=F): 107.87 / 5D 3.23%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.87
- Gas ref (NG=F): 2.93 / 5D -0.51%

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

- close: 67.33
- MA20 / MA60 / MA200: 59.02 / 50.30 / 45.17
- gap20 / gap60: 14.09% / 33.86%
- 5D return: 9.93%
- 20D high/low: 67.33 / 52.99

### Relative Strength

- ratio: 1.072646
- ratio_MA60: 0.936370
- ratio_gap: 14.55%
- ratio_slope_proxy(20d): 0.031164

### Volume (if available)

- volume: 7310563.00
- volume_MA20: 20803028.15
- volume_ratio: 0.35

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.29
- MA20 / MA60 / MA200: 19.14 / 16.07 / 13.44
- gap20 / gap60: 11.19% / 32.43%
- 5D return: 7.77%
- 20D high/low: 21.29 / 16.73

### Relative Strength

- ratio: 0.568889
- ratio_MA60: 0.438112
- ratio_gap: 29.85%
- ratio_slope_proxy(20d): 0.048025

### Volume (if available)

- volume: 11377624.00
- volume_MA20: 36672031.20
- volume_ratio: 0.31

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

- close: 6.78
- MA20 / MA60 / MA200: 6.43 / 5.66 / 4.08
- gap20 / gap60: 5.43% / 19.74%
- 5D return: 2.19%
- 20D high/low: 6.93 / 5.93

### Relative Strength

- ratio: 0.016509
- ratio_MA60: 0.015314
- ratio_gap: 7.80%
- ratio_slope_proxy(20d): 0.000724

### Volume (if available)

- volume: 7055418.00
- volume_MA20: 36041495.90
- volume_ratio: 0.20

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

- close: 16.38
- MA20 / MA60 / MA200: 14.20 / 10.78 / 11.39
- gap20 / gap60: 15.37% / 51.90%
- 5D return: -1.33%
- 20D high/low: 17.53 / 11.14

### Relative Strength

- ratio: 0.056279
- ratio_MA60: 0.045903
- ratio_gap: 22.60%
- ratio_slope_proxy(20d): 0.006197

### Volume (if available)

- volume: 14122856.00
- volume_MA20: 35911857.80
- volume_ratio: 0.39

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

- 데이터 기준일(주가): **2026-03-31**
- 실행시간(UTC): **2026-03-31 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 43.0 bp / latest 3.46
- IG OAS 4주 변화: 8.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 41.0 bp / latest 2.13
- VIX: 30.61
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -1.81% / slope_proxy: -0.0045
- GDXJ/GLD gap: -6.19% / slope_proxy: -0.00234

## VZLA (Vizsla Silver)
- close: 3.255 | RSI14: 38.896006 | ATR14%: 7.85%
- MA20 gap: -8.02% | MA50 gap: -24.30% | MA200 gap: -22.14%
- vol_ratio(Volume/Vol20): 0.223595 | gap_open: 2.24%
- RS vs SILJ gap: -16.94% / slope_proxy: -0.027221
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
- close: 8.17 | RSI14: 42.515075 | ATR14%: 10.47%
- MA20 gap: -6.55% | MA50 gap: -24.38% | MA200 gap: 12.19%
- vol_ratio(Volume/Vol20): 0.337916 | gap_open: 2.50%
- SilverMarginGate: SI=73.650002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.45% / slope_proxy: -0.019512
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
- close: 33.580002 | RSI14: 45.299554 | ATR14%: 13.30%
- MA20 gap: -9.16% | MA50 gap: -16.99% | MA200 gap: 98.40%
- vol_ratio(Volume/Vol20): 0.296586 | gap_open: 3.45%
- RS vs SILJ gap: 1.00% / slope_proxy: 0.18677
- RS vs GDXJ gap: -1.69% / slope_proxy: 0.049025
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
