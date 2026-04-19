# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-17**
- 실행시간(UTC): **2026-04-19 03:00:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.86 / 4주 변화 -41.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -9.0 bp
- 10Y Real Yield (DFII10): 1.93 / 4주 변화 5.0 bp
- VIX (VIXCLS): 17.94
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.704049
- MA60: 7.620691
- gap: 14.22%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.300952
- MA60: 0.22564
- gap: 33.38%
- MA60_slope_proxy: 0.015121
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-17**
- 실행시간(UTC): **2026-04-19 03:00:43**

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
- TERM_SPREAD_10Y_POLICY: 99.35 bp / 4주 변화 4.33 bp
- CURVE_10s5s: 46.07 bp / 4주 변화 -2.76 bp

## NWG Price
- close: 626.0
- MA50: 590.8008 / gap50: 5.96%
- MA200: 577.2308 / gap200: 8.45%

## Relative Strength
- RS vs FTSE gap: 1.04% / slope_proxy: -0.002873
- RS vs Peers gap: -2.20% / slope_proxy: -0.038956

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-19 03:00:50**

## Commodity Regime

- WTI ref (CL=F): 83.85 / 5D -13.17%
- Brent ref (BZ=F): 90.38 / 5D -5.06%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.53
- Gas ref (NG=F): 2.67 / 5D 0.98%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 53.79
- MA20 / MA60 / MA200: 60.62 / 53.56 / 46.10
- gap20 / gap60: -11.26% / 0.44%
- 5D return: -7.21%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 0.977645
- ratio_MA60: 0.958881
- ratio_gap: 1.96%
- ratio_slope_proxy(20d): 0.039139

### Volume (if available)

- volume: 24156200.00
- volume_MA20: 19089690.00
- volume_ratio: 1.27

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.45
- MA20 / MA60 / MA200: 20.51 / 17.78 / 13.94
- gap20 / gap60: -0.28% / 15.03%
- 5D return: -4.93%
- 20D high/low: 21.97 / 18.80

### Relative Strength

- ratio: 0.496842
- ratio_MA60: 0.467515
- ratio_gap: 6.27%
- ratio_slope_proxy(20d): 0.052733

### Volume (if available)

- volume: 42445000.00
- volume_MA20: 34652360.00
- volume_ratio: 1.22

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.94
- MA20 / MA60 / MA200: 6.53 / 6.08 / 4.30
- gap20 / gap60: -9.01% / -2.33%
- 5D return: -8.90%
- 20D high/low: 6.93 / 5.94

### Relative Strength

- ratio: 0.014824
- ratio_MA60: 0.015796
- ratio_gap: -6.15%
- ratio_slope_proxy(20d): 0.000767

### Volume (if available)

- volume: 48130100.00
- volume_MA20: 32569980.00
- volume_ratio: 1.48

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.46
- MA20 / MA60 / MA200: 14.76 / 11.95 / 11.20
- gap20 / gap60: -22.34% / -4.09%
- 5D return: -11.64%
- 20D high/low: 17.53 / 11.46

### Relative Strength

- ratio: 0.045645
- ratio_MA60: 0.048213
- ratio_gap: -5.33%
- ratio_slope_proxy(20d): 0.005093

### Volume (if available)

- volume: 39010000.00
- volume_MA20: 32922510.00
- volume_ratio: 1.18

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

- 데이터 기준일(주가): **2026-04-17**
- 실행시간(UTC): **2026-04-19 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -41.0 bp / latest 2.86
- IG OAS 4주 변화: -9.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 5.0 bp / latest 1.93
- VIX: 17.94
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 0.09% / slope_proxy: 0.009797
- GDXJ/GLD gap: 2.95% / slope_proxy: -0.004055

## VZLA (Vizsla Silver)
- close: 3.51 | RSI14: 51.530609 | ATR14%: 5.70%
- MA20 gap: 7.70% | MA50 gap: -4.23% | MA200 gap: -16.27%
- vol_ratio(Volume/Vol20): 0.793256 | gap_open: 3.21%
- RS vs SILJ gap: -12.11% / slope_proxy: -0.027432
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
- close: 9.2 | RSI14: 54.757177 | ATR14%: 8.11%
- MA20 gap: 13.16% | MA50 gap: -3.54% | MA200 gap: 20.81%
- vol_ratio(Volume/Vol20): 1.030216 | gap_open: 4.21%
- SilverMarginGate: SI=81.737999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -9.14% / slope_proxy: -0.025075
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
- close: 44.169998 | RSI14: 61.586344 | ATR14%: 8.70%
- MA20 gap: 22.13% | MA50 gap: 13.12% | MA200 gap: 131.73%
- vol_ratio(Volume/Vol20): 0.95801 | gap_open: 3.73%
- RS vs SILJ gap: 11.18% / slope_proxy: 0.081656
- RS vs GDXJ gap: 9.02% / slope_proxy: 0.019868
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
