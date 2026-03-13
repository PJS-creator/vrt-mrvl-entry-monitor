# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-12**
- 실행시간(UTC): **2026-03-13 03:00:39**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.09 / 4주 변화 25.0 bp
- IG OAS (BAMLC0A0CM): 0.88 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 1.85 / 4주 변화 -1.0 bp
- VIX (VIXCLS): 24.23
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.246737
- MA60: 6.528368
- gap: 26.32%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.225878
- MA60: 0.211679
- gap: 6.71%
- MA60_slope_proxy: -0.015848
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-12**
- 실행시간(UTC): **2026-03-13 03:00:58**

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
- TERM_SPREAD_10Y_POLICY: 75.1 bp / 4주 변화 0.31 bp
- CURVE_10s5s: 50.8 bp / 4주 변화 -8.84 bp

## NWG Price
- close: 573.0
- MA50: 629.156 / gap50: -8.93%
- MA200: 569.9654 / gap200: 0.53%

## Relative Strength
- RS vs FTSE gap: -9.75% / slope_proxy: -0.002216
- RS vs Peers gap: -2.12% / slope_proxy: -0.057236

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-13 03:01:07**

## Commodity Regime

- WTI ref (CL=F): 96.18 / 5D 18.73%
- Brent ref (BZ=F): 97.42 / 5D 14.06%
- Brent Tier: **>=90**
- Brent-WTI spread: 1.24
- Gas ref (NG=F): 3.25 / 5D 8.26%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 58.41
- MA20 / MA60 / MA200: 51.74 / 45.70 / 43.89
- gap20 / gap60: 12.90% / 27.81%
- 5D return: 10.23%
- 20D high/low: 58.41 / 45.28

### Relative Strength

- ratio: 1.015649
- ratio_MA60: 0.905749
- ratio_gap: 12.13%
- ratio_slope_proxy(20d): 0.002931

### Volume (if available)

- volume: 39201062.00
- volume_MA20: 19491403.10
- volume_ratio: 2.01

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.97
- MA20 / MA60 / MA200: 16.72 / 14.33 / 12.89
- gap20 / gap60: 13.45% / 32.34%
- 5D return: 13.39%
- 20D high/low: 18.99 / 15.02

### Relative Strength

- ratio: 0.525194
- ratio_MA60: 0.401777
- ratio_gap: 30.72%
- ratio_slope_proxy(20d): 0.014919

### Volume (if available)

- volume: 49198711.00
- volume_MA20: 30419385.55
- volume_ratio: 1.62

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

- close: 6.28
- MA20 / MA60 / MA200: 6.29 / 5.11 / 3.84
- gap20 / gap60: -0.10% / 22.85%
- 5D return: 2.45%
- 20D high/low: 6.54 / 5.93

### Relative Strength

- ratio: 0.016860
- ratio_MA60: 0.014803
- ratio_gap: 13.90%
- ratio_slope_proxy(20d): 0.000547

### Volume (if available)

- volume: 28859022.00
- volume_MA20: 50349976.10
- volume_ratio: 0.57

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.77
- MA20 / MA60 / MA200: 10.53 / 8.89 / 11.33
- gap20 / gap60: 21.22% / 43.61%
- 5D return: 3.99%
- 20D high/low: 12.77 / 8.77

### Relative Strength

- ratio: 0.050307
- ratio_MA60: 0.041522
- ratio_gap: 21.16%
- ratio_slope_proxy(20d): 0.003439

### Volume (if available)

- volume: 23760424.00
- volume_MA20: 20033111.20
- volume_ratio: 1.19

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

- 데이터 기준일(주가): **2026-03-12**
- 실행시간(UTC): **2026-03-13 03:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 25.0 bp / latest 3.09
- IG OAS 4주 변화: 11.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: -1.0 bp / latest 1.85
- VIX: 24.23
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -0.93% / slope_proxy: -0.003551
- GDXJ/GLD gap: -4.54% / slope_proxy: 0.011446

## VZLA (Vizsla Silver)
- close: 3.88 | RSI14: 39.773066 | ATR14%: 8.03%
- MA20 gap: -2.70% | MA50 gap: -21.63% | MA200 gap: -7.13%
- vol_ratio(Volume/Vol20): 0.482277 | gap_open: 0.98%
- RS vs SILJ gap: -24.89% / slope_proxy: -0.028697
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
- close: 9.86 | RSI14: 41.960445 | ATR14%: 10.09%
- MA20 gap: -8.53% | MA50 gap: -14.00% | MA200 gap: 42.27%
- vol_ratio(Volume/Vol20): 0.663391 | gap_open: 0.00%
- SilverMarginGate: SI=84.82 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.96% / slope_proxy: 0.001441
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
- close: 40.119999 | RSI14: 47.679065 | ATR14%: 13.81%
- MA20 gap: -7.12% | MA50 gap: 2.31% | MA200 gap: 168.44%
- vol_ratio(Volume/Vol20): 0.480076 | gap_open: 0.40%
- RS vs SILJ gap: 12.95% / slope_proxy: 0.250437
- RS vs GDXJ gap: 13.14% / slope_proxy: 0.065774
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
