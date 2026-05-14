# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-14**
- 실행시간(UTC): **2026-05-14 15:00:47**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.82 / 4주 변화 -3.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 1.99 / 4주 변화 10.0 bp
- VIX (VIXCLS): 17.87
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.637201
- MA60: 8.594895
- gap: 23.76%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.319541
- MA60: 0.263267
- gap: 21.38%
- MA60_slope_proxy: 0.039221
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-14**
- 실행시간(UTC): **2026-05-14 15:00:51**

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
- TERM_SPREAD_10Y_POLICY: 130.27 bp / 4주 변화 31.17 bp
- CURVE_10s5s: 45.52 bp / 4주 변화 -0.22 bp

## NWG Price
- close: 568.4
- MA50: 576.9458 / gap50: -1.48%
- MA200: 584.267 / gap200: -2.72%

## Relative Strength
- RS vs FTSE gap: -1.95% / slope_proxy: -0.002227
- RS vs Peers gap: -5.54% / slope_proxy: -0.036524

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-14 15:01:00**

## Commodity Regime

- WTI ref (CL=F): 100.84 / 5D 6.36%
- Brent ref (BZ=F): 105.29 / 5D 5.23%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.45
- Gas ref (NG=F): 2.86 / 5D 3.25%

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

- close: 56.81
- MA20 / MA60 / MA200: 56.93 / 57.32 / 47.37
- gap20 / gap60: -0.21% / -0.88%
- 5D return: 5.32%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.986970
- ratio_MA60: 0.996301
- ratio_gap: -0.94%
- ratio_slope_proxy(20d): 0.038812

### Volume (if available)

- volume: 3150469.00
- volume_MA20: 12258388.45
- volume_ratio: 0.26

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.77
- MA20 / MA60 / MA200: 20.95 / 19.58 / 14.69
- gap20 / gap60: -5.64% / 0.97%
- 5D return: -2.95%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.530455
- ratio_MA60: 0.507920
- ratio_gap: 4.44%
- ratio_slope_proxy(20d): 0.044971

### Volume (if available)

- volume: 3788787.00
- volume_MA20: 18246844.35
- volume_ratio: 0.21

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.70
- MA20 / MA60 / MA200: 6.42 / 6.43 / 4.64
- gap20 / gap60: 4.38% / 4.24%
- 5D return: 8.59%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015345
- ratio_MA60: 0.015827
- ratio_gap: -3.04%
- ratio_slope_proxy(20d): 0.000051

### Volume (if available)

- volume: 4290150.00
- volume_MA20: 35514327.50
- volume_ratio: 0.12

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

- close: 13.02
- MA20 / MA60 / MA200: 12.43 / 12.89 / 10.90
- gap20 / gap60: 4.73% / 1.00%
- 5D return: 11.33%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.054338
- ratio_MA60: 0.049560
- ratio_gap: 9.64%
- ratio_slope_proxy(20d): 0.001268

### Volume (if available)

- volume: 6538166.00
- volume_MA20: 21451323.30
- volume_ratio: 0.30

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

- 데이터 기준일(주가): **2026-05-14**
- 실행시간(UTC): **2026-05-14 15:01:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.82
- IG OAS 4주 변화: -4.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 10.0 bp / latest 1.99
- VIX: 17.87
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -4.13% / slope_proxy: 0.001531
- GDXJ/GLD gap: 1.65% / slope_proxy: -0.003236

## VZLA (Vizsla Silver)
- close: 3.65 | RSI14: 54.732431 | ATR14%: 5.94%
- MA20 gap: 4.63% | MA50 gap: 5.50% | MA200 gap: -13.54%
- vol_ratio(Volume/Vol20): 0.377661 | gap_open: 0.00%
- RS vs SILJ gap: -0.38% / slope_proxy: -0.010787
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
- close: 9.5 | RSI14: 57.261247 | ATR14%: 7.10%
- MA20 gap: 9.00% | MA50 gap: 10.28% | MA200 gap: 17.49%
- vol_ratio(Volume/Vol20): 0.348684 | gap_open: 0.80%
- SilverMarginGate: SI=85.404999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.83% / slope_proxy: -0.02456
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
- close: 40.389999 | RSI14: 51.975067 | ATR14%: 9.24%
- MA20 gap: 2.43% | MA50 gap: 6.22% | MA200 gap: 80.00%
- vol_ratio(Volume/Vol20): 0.462454 | gap_open: 1.44%
- RS vs SILJ gap: -0.45% / slope_proxy: 0.032624
- RS vs GDXJ gap: 3.71% / slope_proxy: 0.007187
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
