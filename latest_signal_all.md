# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-10**
- 실행시간(UTC): **2026-04-10 15:00:50**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.9 / 4주 변화 -27.0 bp
- IG OAS (BAMLC0A0CM): 0.83 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 11.0 bp
- VIX (VIXCLS): 19.49
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.806764
- MA60: 7.370693
- gap: 19.48%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.291691
- MA60: 0.218016
- gap: 33.79%
- MA60_slope_proxy: 0.006337
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-10**
- 실행시간(UTC): **2026-04-10 15:00:54**

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
- TERM_SPREAD_10Y_POLICY: 90.99 bp / 4주 변화 2.11 bp
- CURVE_10s5s: 44.14 bp / 4주 변화 -5.36 bp

## NWG Price
- close: 612.0
- MA50: 596.3899 / gap50: 2.62%
- MA200: 574.1147 / gap200: 6.60%

## Relative Strength
- RS vs FTSE gap: -1.37% / slope_proxy: -0.003247
- RS vs Peers gap: -3.03% / slope_proxy: -0.040961

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-10 15:01:03**

## Commodity Regime

- WTI ref (CL=F): 98.60 / 5D -11.60%
- Brent ref (BZ=F): 95.83 / 5D -12.11%
- Brent Tier: **>=90**
- Brent-WTI spread: -2.77
- Gas ref (NG=F): 2.68 / 5D -4.43%

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

- close: 57.96
- MA20 / MA60 / MA200: 61.16 / 52.47 / 45.75
- gap20 / gap60: -5.23% / 10.46%
- 5D return: -7.96%
- 20D high/low: 66.24 / 57.25

### Relative Strength

- ratio: 1.021620
- ratio_MA60: 0.950969
- ratio_gap: 7.43%
- ratio_slope_proxy(20d): 0.039302

### Volume (if available)

- volume: 2808247.00
- volume_MA20: 19112587.35
- volume_ratio: 0.15

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.99
- MA20 / MA60 / MA200: 20.05 / 17.08 / 13.72
- gap20 / gap60: 4.67% / 22.84%
- 5D return: 2.07%
- 20D high/low: 20.99 / 18.57

### Relative Strength

- ratio: 0.511455
- ratio_MA60: 0.456806
- ratio_gap: 11.96%
- ratio_slope_proxy(20d): 0.055029

### Volume (if available)

- volume: 5170835.00
- volume_MA20: 33914671.75
- volume_ratio: 0.15

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

- close: 6.50
- MA20 / MA60 / MA200: 6.56 / 5.93 / 4.21
- gap20 / gap60: -0.80% / 9.78%
- 5D return: -1.29%
- 20D high/low: 6.93 / 6.20

### Relative Strength

- ratio: 0.015834
- ratio_MA60: 0.015620
- ratio_gap: 1.37%
- ratio_slope_proxy(20d): 0.000817

### Volume (if available)

- volume: 3801341.00
- volume_MA20: 34395422.05
- volume_ratio: 0.11

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

- close: 12.80
- MA20 / MA60 / MA200: 15.04 / 11.62 / 11.29
- gap20 / gap60: -14.88% / 10.18%
- 5D return: -12.53%
- 20D high/low: 17.53 / 12.28

### Relative Strength

- ratio: 0.048203
- ratio_MA60: 0.047684
- ratio_gap: 1.09%
- ratio_slope_proxy(20d): 0.006219

### Volume (if available)

- volume: 8922355.00
- volume_MA20: 37580117.75
- volume_ratio: 0.24

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

- 데이터 기준일(주가): **2026-04-10**
- 실행시간(UTC): **2026-04-10 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -27.0 bp / latest 2.9
- IG OAS 4주 변화: -8.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 11.0 bp / latest 1.96
- VIX: 19.49
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 2.57% / slope_proxy: 0.003447
- GDXJ/GLD gap: 0.77% / slope_proxy: -0.004738

## VZLA (Vizsla Silver)
- close: 3.285 | RSI14: 41.834005 | ATR14%: 6.64%
- MA20 gap: 0.36% | MA50 gap: -14.58% | MA200 gap: -21.41%
- vol_ratio(Volume/Vol20): 0.173809 | gap_open: 1.53%
- RS vs SILJ gap: -17.96% / slope_proxy: -0.027483
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.05 | RSI14: 43.889521 | ATR14%: 9.59%
- MA20 gap: 0.47% | MA50 gap: -18.66% | MA200 gap: 7.85%
- vol_ratio(Volume/Vol20): 0.103115 | gap_open: 0.12%
- SilverMarginGate: SI=76.580002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.16% / slope_proxy: -0.022858
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
- close: 38.450001 | RSI14: 53.019312 | ATR14%: 10.69%
- MA20 gap: 9.34% | MA50 gap: -1.24% | MA200 gap: 112.28%
- vol_ratio(Volume/Vol20): 0.25409 | gap_open: 0.18%
- RS vs SILJ gap: 2.82% / slope_proxy: 0.124681
- RS vs GDXJ gap: -0.78% / slope_proxy: 0.032372
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
