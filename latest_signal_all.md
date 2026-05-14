# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: PBR**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-13**
- 실행시간(UTC): **2026-05-14 03:00:38**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.82 / 4주 변화 -2.0 bp
- IG OAS (BAMLC0A0CM): 0.77 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 1.99 / 4주 변화 10.0 bp
- VIX (VIXCLS): 17.99
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.656393
- MA60: 8.54213
- gap: 24.75%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.310851
- MA60: 0.261135
- gap: 19.04%
- MA60_slope_proxy: 0.038571
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-13**
- 실행시간(UTC): **2026-05-14 03:00:42**

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
- TERM_SPREAD_10Y_POLICY: 120.89 bp / 4주 변화 14.62 bp
- CURVE_10s5s: 44.61 bp / 4주 변화 -0.44 bp

## NWG Price
- close: 564.0
- MA50: 577.593 / gap50: -2.35%
- MA200: 584.0485 / gap200: -3.43%

## Relative Strength
- RS vs FTSE gap: -2.63% / slope_proxy: -0.002249
- RS vs Peers gap: -5.80% / slope_proxy: -0.036938

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-14 03:00:49**

## Commodity Regime

- WTI ref (CL=F): 101.45 / 5D 6.70%
- Brent ref (BZ=F): 105.99 / 5D 4.66%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.54
- Gas ref (NG=F): 2.87 / 5D 4.95%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 56.18
- MA20 / MA60 / MA200: 56.93 / 57.15 / 47.31
- gap20 / gap60: -1.33% / -1.70%
- 5D return: 1.92%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.974839
- ratio_MA60: 0.994210
- ratio_gap: -1.95%
- ratio_slope_proxy(20d): 0.038657

### Volume (if available)

- volume: 5737686.00
- volume_MA20: 12543169.30
- volume_ratio: 0.46

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **True**

### Trend

- close: 19.59
- MA20 / MA60 / MA200: 21.03 / 19.50 / 14.65
- gap20 / gap60: -6.86% / 0.44%
- 5D return: -6.31%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.532626
- ratio_MA60: 0.505741
- ratio_gap: 5.32%
- ratio_slope_proxy(20d): 0.045059

### Volume (if available)

- volume: 18217044.00
- volume_MA20: 19574917.20
- volume_ratio: 0.93

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.62
- MA20 / MA60 / MA200: 6.40 / 6.42 / 4.62
- gap20 / gap60: 3.41% / 3.12%
- 5D return: 6.26%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015133
- ratio_MA60: 0.015840
- ratio_gap: -4.46%
- ratio_slope_proxy(20d): 0.000103

### Volume (if available)

- volume: 26429388.00
- volume_MA20: 36397374.40
- volume_ratio: 0.73

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

- close: 13.00
- MA20 / MA60 / MA200: 12.41 / 12.83 / 10.91
- gap20 / gap60: 4.75% / 1.34%
- 5D return: 8.33%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.054307
- ratio_MA60: 0.049367
- ratio_gap: 10.01%
- ratio_slope_proxy(20d): 0.001182

### Volume (if available)

- volume: 31434489.00
- volume_MA20: 22031774.45
- volume_ratio: 1.43

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: PBR


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-13**
- 실행시간(UTC): **2026-05-14 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.82
- IG OAS 4주 변화: -4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 10.0 bp / latest 1.99
- VIX: 17.99
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -3.93% / slope_proxy: 0.002867
- GDXJ/GLD gap: 4.42% / slope_proxy: -0.003502

## VZLA (Vizsla Silver)
- close: 3.85 | RSI14: 63.313849 | ATR14%: 5.60%
- MA20 gap: 10.71% | MA50 gap: 10.95% | MA200 gap: -8.75%
- vol_ratio(Volume/Vol20): 0.884021 | gap_open: 1.56%
- RS vs SILJ gap: 0.87% / slope_proxy: -0.012062
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
- close: 10.02 | RSI14: 63.998191 | ATR14%: 6.76%
- MA20 gap: 15.28% | MA50 gap: 16.08% | MA200 gap: 24.37%
- vol_ratio(Volume/Vol20): 0.881012 | gap_open: 1.97%
- SilverMarginGate: SI=87.455002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.14% / slope_proxy: -0.025767
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
- close: 43.630001 | RSI14: 58.508831 | ATR14%: 8.59%
- MA20 gap: 10.60% | MA50 gap: 14.30% | MA200 gap: 96.05%
- vol_ratio(Volume/Vol20): 0.972715 | gap_open: 1.17%
- RS vs SILJ gap: 3.26% / slope_proxy: 0.033571
- RS vs GDXJ gap: 8.95% / slope_proxy: 0.006872
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
