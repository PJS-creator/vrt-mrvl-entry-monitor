# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-06**
- 실행시간(UTC): **2026-05-06 15:00:46**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.77 / 4주 변화 -35.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 1.95 / 4주 변화 -3.0 bp
- VIX (VIXCLS): 17.38
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.91787
- MA60: 8.288194
- gap: 19.66%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.30977
- MA60: 0.252422
- gap: 22.72%
- MA60_slope_proxy: 0.036949
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-06**
- 실행시간(UTC): **2026-05-06 15:00:49**

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
- TERM_SPREAD_10Y_POLICY: 117.41 bp / 4주 변화 14.61 bp
- CURVE_10s5s: 45.94 bp / 4주 변화 3.61 bp

## NWG Price
- close: 572.6
- MA50: 581.8355 / gap50: -1.59%
- MA200: 582.3994 / gap200: -1.68%

## Relative Strength
- RS vs FTSE gap: -2.53% / slope_proxy: -0.002472
- RS vs Peers gap: -6.37% / slope_proxy: -0.039379

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-06 15:00:58**

## Commodity Regime

- WTI ref (CL=F): 95.40 / 5D -10.74%
- Brent ref (BZ=F): 102.20 / 5D -13.41%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.80
- Gas ref (NG=F): 2.73 / 5D 2.95%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 55.69
- MA20 / MA60 / MA200: 57.52 / 56.42 / 47.04
- gap20 / gap60: -3.19% / -1.29%
- 5D return: -8.34%
- 20D high/low: 60.76 / 53.79

### Relative Strength

- ratio: 0.972921
- ratio_MA60: 0.985017
- ratio_gap: -1.23%
- ratio_slope_proxy(20d): 0.037314

### Volume (if available)

- volume: 7207444.00
- volume_MA20: 12256787.20
- volume_ratio: 0.59

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.94
- MA20 / MA60 / MA200: 21.21 / 19.08 / 14.45
- gap20 / gap60: -1.28% / 9.74%
- 5D return: -4.16%
- 20D high/low: 22.03 / 20.33

### Relative Strength

- ratio: 0.526395
- ratio_MA60: 0.494710
- ratio_gap: 6.40%
- ratio_slope_proxy(20d): 0.045280

### Volume (if available)

- volume: 7679110.00
- volume_MA20: 20112265.50
- volume_ratio: 0.38

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

- close: 6.29
- MA20 / MA60 / MA200: 6.39 / 6.39 / 4.54
- gap20 / gap60: -1.53% / -1.41%
- 5D return: -9.55%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.014503
- ratio_MA60: 0.015923
- ratio_gap: -8.92%
- ratio_slope_proxy(20d): 0.000383

### Volume (if available)

- volume: 12790534.00
- volume_MA20: 33165291.70
- volume_ratio: 0.39

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.01
- MA20 / MA60 / MA200: 12.53 / 12.60 / 10.97
- gap20 / gap60: -4.18% / -4.72%
- 5D return: -8.78%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.045639
- ratio_MA60: 0.048651
- ratio_gap: -6.19%
- ratio_slope_proxy(20d): 0.001269

### Volume (if available)

- volume: 6329505.00
- volume_MA20: 20756620.25
- volume_ratio: 0.30

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-06**
- 실행시간(UTC): **2026-05-06 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.77
- IG OAS 4주 변화: -7.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -3.0 bp / latest 1.95
- VIX: 17.38
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -2.39% / slope_proxy: 0.010595
- GDXJ/GLD gap: -0.58% / slope_proxy: -0.003952

## VZLA (Vizsla Silver)
- close: 3.45 | RSI14: 50.971909 | ATR14%: 5.94%
- MA20 gap: 1.72% | MA50 gap: -2.00% | MA200 gap: -18.04%
- vol_ratio(Volume/Vol20): 0.431704 | gap_open: 6.04%
- RS vs SILJ gap: -0.23% / slope_proxy: -0.018361
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
- close: 8.44 | RSI14: 50.234785 | ATR14%: 7.43%
- MA20 gap: 0.08% | MA50 gap: -5.00% | MA200 gap: 6.60%
- vol_ratio(Volume/Vol20): 0.459474 | gap_open: 4.50%
- SilverMarginGate: SI=78.080002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.49% / slope_proxy: -0.030855
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
- close: 39.080002 | RSI14: 52.386303 | ATR14%: 8.49%
- MA20 gap: 0.66% | MA50 gap: 0.14% | MA200 gap: 83.51%
- vol_ratio(Volume/Vol20): 0.458525 | gap_open: 6.70%
- RS vs SILJ gap: 3.88% / slope_proxy: 0.030869
- RS vs GDXJ gap: 4.19% / slope_proxy: 0.004049
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
