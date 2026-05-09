# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-08**
- 실행시간(UTC): **2026-05-09 03:00:35**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.79 / 4주 변화 -11.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 1.0 bp
- VIX (VIXCLS): 17.08
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.721761
- MA60: 8.377773
- gap: 16.04%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.300297
- MA60: 0.255779
- gap: 17.40%
- MA60_slope_proxy: 0.037829
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-08**
- 실행시간(UTC): **2026-05-09 03:00:38**

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
- TERM_SPREAD_10Y_POLICY: 114.32 bp / 4주 변화 23.33 bp
- CURVE_10s5s: 45.95 bp / 4주 변화 1.81 bp

## NWG Price
- close: 579.8
- MA50: 580.6582 / gap50: -0.15%
- MA200: 583.1801 / gap200: -0.58%

## Relative Strength
- RS vs FTSE gap: 0.86% / slope_proxy: -0.002383
- RS vs Peers gap: -2.97% / slope_proxy: -0.038193

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-09 03:00:45**

## Commodity Regime

- WTI ref (CL=F): 94.68 / 5D -7.12%
- Brent ref (BZ=F): 100.49 / 5D -7.10%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.81
- Gas ref (NG=F): 2.75 / 5D -1.08%

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

- close: 53.03
- MA20 / MA60 / MA200: 57.02 / 56.64 / 47.14
- gap20 / gap60: -7.00% / -6.37%
- 5D return: -9.67%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.952065
- ratio_MA60: 0.988090
- ratio_gap: -3.65%
- ratio_slope_proxy(20d): 0.037180

### Volume (if available)

- volume: 10914705.00
- volume_MA20: 13095120.25
- volume_ratio: 0.83

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.33
- MA20 / MA60 / MA200: 21.15 / 19.24 / 14.53
- gap20 / gap60: -3.87% / 5.65%
- 5D return: -7.17%
- 20D high/low: 22.03 / 20.33

### Relative Strength

- ratio: 0.519683
- ratio_MA60: 0.498756
- ratio_gap: 4.20%
- ratio_slope_proxy(20d): 0.044464

### Volume (if available)

- volume: 13257945.00
- volume_MA20: 20312372.25
- volume_ratio: 0.65

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

- close: 6.40
- MA20 / MA60 / MA200: 6.36 / 6.40 / 4.57
- gap20 / gap60: 0.57% / -0.04%
- 5D return: -6.43%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015208
- ratio_MA60: 0.015912
- ratio_gap: -4.43%
- ratio_slope_proxy(20d): 0.000292

### Volume (if available)

- volume: 31205305.00
- volume_MA20: 36008725.25
- volume_ratio: 0.87

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.45
- MA20 / MA60 / MA200: 12.39 / 12.65 / 10.94
- gap20 / gap60: -7.57% / -9.51%
- 5D return: -10.05%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.047686
- ratio_MA60: 0.048725
- ratio_gap: -2.13%
- ratio_slope_proxy(20d): 0.001030

### Volume (if available)

- volume: 17426991.00
- volume_MA20: 19995354.55
- volume_ratio: 0.87

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

- 데이터 기준일(주가): **2026-05-08**
- 실행시간(UTC): **2026-05-09 03:00:50**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.79
- IG OAS 4주 변화: -4.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 1.0 bp / latest 1.96
- VIX: 17.08
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -3.78% / slope_proxy: 0.008104
- GDXJ/GLD gap: 1.29% / slope_proxy: -0.004148

## VZLA (Vizsla Silver)
- close: 3.56 | RSI14: 54.830144 | ATR14%: 5.82%
- MA20 gap: 4.23% | MA50 gap: 1.78% | MA200 gap: -15.46%
- vol_ratio(Volume/Vol20): 0.735669 | gap_open: 1.75%
- RS vs SILJ gap: 0.61% / slope_proxy: -0.015845
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 9.03 | RSI14: 56.209296 | ATR14%: 7.18%
- MA20 gap: 5.80% | MA50 gap: 3.14% | MA200 gap: 13.35%
- vol_ratio(Volume/Vol20): 0.82349 | gap_open: 1.93%
- SilverMarginGate: SI=80.834999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 0.26% / slope_proxy: -0.029057
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
- close: 38.439999 | RSI14: 50.892541 | ATR14%: 8.90%
- MA20 gap: -1.19% | MA50 gap: -0.45% | MA200 gap: 77.59%
- vol_ratio(Volume/Vol20): 0.796327 | gap_open: 1.93%
- RS vs SILJ gap: -0.78% / slope_proxy: 0.031637
- RS vs GDXJ gap: -0.31% / slope_proxy: 0.004714
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
