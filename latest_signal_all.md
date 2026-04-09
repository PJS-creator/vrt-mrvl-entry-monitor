# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-09**
- 실행시간(UTC): **2026-04-09 15:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.94 / 4주 변화 -15.0 bp
- IG OAS (BAMLC0A0CM): 0.83 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 14.0 bp
- VIX (VIXCLS): 21.04
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.617903
- MA60: 7.320586
- gap: 17.72%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.284805
- MA60: 0.216791
- gap: 31.37%
- MA60_slope_proxy: 0.004894
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-09**
- 실행시간(UTC): **2026-04-09 15:00:45**

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
- TERM_SPREAD_10Y_POLICY: 112.4 bp / 4주 변화 37.3 bp
- CURVE_10s5s: 41.7 bp / 4주 변화 -9.1 bp

## NWG Price
- close: 602.8
- MA50: 597.2407 / gap50: 0.93%
- MA200: 573.5422 / gap200: 5.10%

## Relative Strength
- RS vs FTSE gap: -2.56% / slope_proxy: -0.003288
- RS vs Peers gap: -3.38% / slope_proxy: -0.041685

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-09 15:00:52**

## Commodity Regime

- WTI ref (CL=F): 102.00 / 5D 1.88%
- Brent ref (BZ=F): 99.03 / 5D -2.11%
- Brent Tier: **>=90**
- Brent-WTI spread: -2.97
- Gas ref (NG=F): 2.71 / 5D -3.83%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 60.52
- MA20 / MA60 / MA200: 61.28 / 52.26 / 45.68
- gap20 / gap60: -1.24% / 15.81%
- 5D return: -2.75%
- 20D high/low: 66.24 / 57.25

### Relative Strength

- ratio: 1.030830
- ratio_MA60: 0.949492
- ratio_gap: 8.57%
- ratio_slope_proxy(20d): 0.039668

### Volume (if available)

- volume: 4612710.00
- volume_MA20: 20397330.50
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.89
- MA20 / MA60 / MA200: 19.96 / 16.94 / 13.68
- gap20 / gap60: 4.65% / 23.28%
- 5D return: 4.01%
- 20D high/low: 20.89 / 18.57

### Relative Strength

- ratio: 0.521018
- ratio_MA60: 0.454742
- ratio_gap: 14.57%
- ratio_slope_proxy(20d): 0.055412

### Volume (if available)

- volume: 9763897.00
- volume_MA20: 35322789.85
- volume_ratio: 0.28

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

- close: 6.80
- MA20 / MA60 / MA200: 6.56 / 5.89 / 4.19
- gap20 / gap60: 3.68% / 15.40%
- 5D return: 4.62%
- 20D high/low: 6.93 / 6.20

### Relative Strength

- ratio: 0.016279
- ratio_MA60: 0.015584
- ratio_gap: 4.46%
- ratio_slope_proxy(20d): 0.000829

### Volume (if available)

- volume: 5759844.00
- volume_MA20: 35002587.20
- volume_ratio: 0.16

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.78
- MA20 / MA60 / MA200: 15.08 / 11.55 / 11.31
- gap20 / gap60: -8.63% / 19.28%
- 5D return: -6.13%
- 20D high/low: 17.53 / 12.28

### Relative Strength

- ratio: 0.050234
- ratio_MA60: 0.047582
- ratio_gap: 5.57%
- ratio_slope_proxy(20d): 0.006414

### Volume (if available)

- volume: 8199190.00
- volume_MA20: 36771449.50
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-09**
- 실행시간(UTC): **2026-04-09 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -15.0 bp / latest 2.94
- IG OAS 4주 변화: -5.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 14.0 bp / latest 1.96
- VIX: 21.04
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 3.08% / slope_proxy: 0.001848
- GDXJ/GLD gap: -0.62% / slope_proxy: -0.004696

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 40.924596 | ATR14%: 7.01%
- MA20 gap: -1.29% | MA50 gap: -16.78% | MA200 gap: -21.98%
- vol_ratio(Volume/Vol20): 0.226276 | gap_open: 0.61%
- RS vs SILJ gap: -18.10% / slope_proxy: -0.02741
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
- close: 7.9515 | RSI14: 42.762991 | ATR14%: 10.13%
- MA20 gap: -1.76% | MA50 gap: -20.77% | MA200 gap: 6.92%
- vol_ratio(Volume/Vol20): 0.124829 | gap_open: 0.50%
- SilverMarginGate: SI=74.870003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.24% / slope_proxy: -0.022615
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
- close: 36.470001 | RSI14: 49.62016 | ATR14%: 11.35%
- MA20 gap: 3.83% | MA50 gap: -6.84% | MA200 gap: 103.47%
- vol_ratio(Volume/Vol20): 0.186495 | gap_open: 0.49%
- RS vs SILJ gap: -0.56% / slope_proxy: 0.132621
- RS vs GDXJ gap: -4.19% / slope_proxy: 0.034661
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
