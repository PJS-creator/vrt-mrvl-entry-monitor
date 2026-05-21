# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-20**
- 실행시간(UTC): **2026-05-21 03:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.86 / 4주 변화 1.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 2.18 / 4주 변화 26.0 bp
- VIX (VIXCLS): 18.06
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.278954
- MA60: 8.765195
- gap: 5.86%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.330819
- MA60: 0.271895
- gap: 21.67%
- MA60_slope_proxy: 0.04021
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-20**
- 실행시간(UTC): **2026-05-21 03:00:45**

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
- TERM_SPREAD_10Y_POLICY: 135.26 bp / 4주 변화 31.97 bp
- CURVE_10s5s: 47.3 bp / 4주 변화 -2.54 bp

## NWG Price
- close: 583.0
- MA50: 575.6964 / gap50: 1.27%
- MA200: 585.1871 / gap200: -0.37%

## Relative Strength
- RS vs FTSE gap: 0.07% / slope_proxy: -0.002011
- RS vs Peers gap: -4.23% / slope_proxy: -0.035257

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-21 03:00:56**

## Commodity Regime

- WTI ref (CL=F): 99.03 / 5D -1.97%
- Brent ref (BZ=F): 105.76 / 5D 0.12%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.73
- Gas ref (NG=F): 3.04 / 5D 6.11%

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

- close: 58.87
- MA20 / MA60 / MA200: 57.80 / 57.85 / 47.71
- gap20 / gap60: 1.86% / 1.76%
- 5D return: 4.79%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.984448
- ratio_MA60: 0.999242
- ratio_gap: -1.48%
- ratio_slope_proxy(20d): 0.034849

### Volume (if available)

- volume: 11253038.00
- volume_MA20: 12157156.90
- volume_ratio: 0.93

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.83
- MA20 / MA60 / MA200: 20.84 / 19.86 / 14.84
- gap20 / gap60: -4.86% / -0.17%
- 5D return: 1.23%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.539592
- ratio_MA60: 0.517738
- ratio_gap: 4.22%
- ratio_slope_proxy(20d): 0.046685

### Volume (if available)

- volume: 16613019.00
- volume_MA20: 17959555.95
- volume_ratio: 0.93

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 7.34
- MA20 / MA60 / MA200: 6.70 / 6.49 / 4.73
- gap20 / gap60: 9.50% / 13.08%
- 5D return: 10.88%
- 20D high/low: 7.58 / 6.06

### Relative Strength

- ratio: 0.016274
- ratio_MA60: 0.015830
- ratio_gap: 2.80%
- ratio_slope_proxy(20d): 0.000003

### Volume (if available)

- volume: 31350707.00
- volume_MA20: 38469220.35
- volume_ratio: 0.81

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

- close: 14.03
- MA20 / MA60 / MA200: 12.92 / 13.20 / 10.88
- gap20 / gap60: 8.59% / 6.28%
- 5D return: 7.92%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.057580
- ratio_MA60: 0.050592
- ratio_gap: 13.81%
- ratio_slope_proxy(20d): 0.002253

### Volume (if available)

- volume: 21369388.00
- volume_MA20: 21483014.40
- volume_ratio: 0.99

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-20**
- 실행시간(UTC): **2026-05-21 03:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.86
- IG OAS 4주 변화: -4.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.18
- VIX: 18.06
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -4.22% / slope_proxy: -0.003757
- GDXJ/GLD gap: -4.63% / slope_proxy: -0.003992

## VZLA (Vizsla Silver)
- close: 3.39 | RSI14: 46.495705 | ATR14%: 6.46%
- MA20 gap: -2.63% | MA50 gap: -0.57% | MA200 gap: -19.88%
- vol_ratio(Volume/Vol20): 0.698361 | gap_open: 1.84%
- RS vs SILJ gap: 3.18% / slope_proxy: -0.005987
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
- close: 8.38 | RSI14: 45.96304 | ATR14%: 8.20%
- MA20 gap: -2.88% | MA50 gap: -1.20% | MA200 gap: 2.37%
- vol_ratio(Volume/Vol20): 1.981009 | gap_open: 3.28%
- SilverMarginGate: SI=75.660004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.30% / slope_proxy: -0.019095
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
- close: 34.064999 | RSI14: 42.496214 | ATR14%: 10.47%
- MA20 gap: -10.09% | MA50 gap: -9.07% | MA200 gap: 47.75%
- vol_ratio(Volume/Vol20): 0.75778 | gap_open: 3.30%
- RS vs SILJ gap: -5.79% / slope_proxy: 0.026791
- RS vs GDXJ gap: -3.37% / slope_proxy: 0.007332
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
