# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-15**
- 실행시간(UTC): **2026-04-16 03:00:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.84 / 4주 변화 -38.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -11.0 bp
- 10Y Real Yield (DFII10): 1.89 / 4주 변화 6.0 bp
- VIX (VIXCLS): 18.36
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.808424
- MA60: 7.531161
- gap: 16.96%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.29713
- MA60: 0.222564
- gap: 33.50%
- MA60_slope_proxy: 0.011525
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-15**
- 실행시간(UTC): **2026-04-16 03:00:46**

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
- TERM_SPREAD_10Y_POLICY: 106.27 bp / 4주 변화 10.51 bp
- CURVE_10s5s: 45.05 bp / 4주 변화 -4.47 bp

## NWG Price
- close: 622.6
- MA50: 593.6618 / gap50: 4.87%
- MA200: 575.8311 / gap200: 8.12%

## Relative Strength
- RS vs FTSE gap: 1.18% / slope_proxy: -0.002983
- RS vs Peers gap: -1.01% / slope_proxy: -0.038874

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-16 03:00:55**

## Commodity Regime

- WTI ref (CL=F): 91.42 / 5D -3.17%
- Brent ref (BZ=F): 95.02 / 5D 0.29%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.60
- Gas ref (NG=F): 2.59 / 5D -4.85%

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

- close: 55.83
- MA20 / MA60 / MA200: 60.98 / 53.13 / 45.96
- gap20 / gap60: -8.45% / 5.07%
- 5D return: -6.59%
- 20D high/low: 66.24 / 55.38

### Relative Strength

- ratio: 1.001255
- ratio_MA60: 0.955553
- ratio_gap: 4.78%
- ratio_slope_proxy(20d): 0.039132

### Volume (if available)

- volume: 9540174.00
- volume_MA20: 19290653.70
- volume_ratio: 0.49

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.54
- MA20 / MA60 / MA200: 20.39 / 17.52 / 13.86
- gap20 / gap60: 0.75% / 17.25%
- 5D return: 2.80%
- 20D high/low: 21.97 / 18.80

### Relative Strength

- ratio: 0.495417
- ratio_MA60: 0.463384
- ratio_gap: 6.91%
- ratio_slope_proxy(20d): 0.054128

### Volume (if available)

- volume: 19876447.00
- volume_MA20: 34411137.35
- volume_ratio: 0.58

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

- close: 6.15
- MA20 / MA60 / MA200: 6.55 / 6.03 / 4.26
- gap20 / gap60: -6.10% / 2.06%
- 5D return: -8.21%
- 20D high/low: 6.93 / 6.15

### Relative Strength

- ratio: 0.015249
- ratio_MA60: 0.015737
- ratio_gap: -3.10%
- ratio_slope_proxy(20d): 0.000783

### Volume (if available)

- volume: 24970521.00
- volume_MA20: 32880581.05
- volume_ratio: 0.76

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

- close: 12.18
- MA20 / MA60 / MA200: 15.01 / 11.84 / 11.23
- gap20 / gap60: -18.84% / 2.89%
- 5D return: -15.65%
- 20D high/low: 17.53 / 12.18

### Relative Strength

- ratio: 0.047439
- ratio_MA60: 0.048073
- ratio_gap: -1.32%
- ratio_slope_proxy(20d): 0.005637

### Volume (if available)

- volume: 12408830.00
- volume_MA20: 37795436.50
- volume_ratio: 0.33

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

- 데이터 기준일(주가): **2026-04-15**
- 실행시간(UTC): **2026-04-16 03:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -38.0 bp / latest 2.84
- IG OAS 4주 변화: -11.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.89
- VIX: 18.36
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.63% / slope_proxy: 0.007546
- GDXJ/GLD gap: 1.17% / slope_proxy: -0.004536

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 47.812159 | ATR14%: 6.11%
- MA20 gap: 5.52% | MA50 gap: -8.31% | MA200 gap: -18.31%
- vol_ratio(Volume/Vol20): 1.395911 | gap_open: 0.29%
- RS vs SILJ gap: -13.12% / slope_proxy: -0.027505
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

## SCZM (Santacruz Silver)
- close: 8.82 | RSI14: 51.271154 | ATR14%: 8.55%
- MA20 gap: 10.42% | MA50 gap: -8.85% | MA200 gap: 16.75%
- vol_ratio(Volume/Vol20): 0.84955 | gap_open: 0.44%
- SilverMarginGate: SI=80.43 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.56% / slope_proxy: -0.023921
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
- close: 40.330002 | RSI14: 55.359877 | ATR14%: 9.61%
- MA20 gap: 14.18% | MA50 gap: 3.47% | MA200 gap: 116.04%
- vol_ratio(Volume/Vol20): 0.463381 | gap_open: 0.96%
- RS vs SILJ gap: 5.45% / slope_proxy: 0.09776
- RS vs GDXJ gap: 2.64% / slope_proxy: 0.024605
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
