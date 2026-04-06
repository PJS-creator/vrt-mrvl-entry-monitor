# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-06**
- 실행시간(UTC): **2026-04-06 15:00:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.13 / 4주 변화 0.0 bp
- IG OAS (BAMLC0A0CM): 0.86 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 1.97 / 4주 변화 15.0 bp
- VIX (VIXCLS): 23.87
- NFCI: -0.4337

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.114339
- MA60: 7.182076
- gap: 12.98%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.274794
- MA60: 0.213713
- gap: 28.58%
- MA60_slope_proxy: 0.001221
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-02**
- 실행시간(UTC): **2026-04-06 15:00:45**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 111.15 bp / 4주 변화 38.03 bp
- CURVE_10s5s: 42.25 bp / 4주 변화 -14.4 bp

## NWG Price
- close: 575.4
- MA50: 600.9212 / gap50: -4.25%
- MA200: 572.1824 / gap200: 0.56%

## Relative Strength
- RS vs FTSE gap: -6.36% / slope_proxy: -0.003359
- RS vs Peers gap: -4.12% / slope_proxy: -0.044092

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-06 15:00:54**

## Commodity Regime

- WTI ref (CL=F): 111.05 / 5D 11.45%
- Brent ref (BZ=F): 108.71 / 5D -3.43%
- Brent Tier: **>=90**
- Brent-WTI spread: -2.34
- Gas ref (NG=F): 2.81 / 5D -9.21%

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

- close: 62.59
- MA20 / MA60 / MA200: 60.28 / 51.33 / 45.42
- gap20 / gap60: 3.84% / 21.92%
- 5D return: -4.18%
- 20D high/low: 66.24 / 53.12

### Relative Strength

- ratio: 1.058513
- ratio_MA60: 0.944004
- ratio_gap: 12.13%
- ratio_slope_proxy(20d): 0.037343

### Volume (if available)

- volume: 3964668.00
- volume_MA20: 21760593.40
- volume_ratio: 0.18

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.62
- MA20 / MA60 / MA200: 19.62 / 16.50 / 13.56
- gap20 / gap60: 5.06% / 24.92%
- 5D return: -0.74%
- 20D high/low: 20.81 / 17.99

### Relative Strength

- ratio: 0.535849
- ratio_MA60: 0.446554
- ratio_gap: 20.00%
- ratio_slope_proxy(20d): 0.052537

### Volume (if available)

- volume: 4164666.00
- volume_MA20: 38713133.30
- volume_ratio: 0.11

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

- close: 6.52
- MA20 / MA60 / MA200: 6.48 / 5.77 / 4.13
- gap20 / gap60: 0.65% / 13.03%
- 5D return: -5.92%
- 20D high/low: 6.93 / 6.16

### Relative Strength

- ratio: 0.016362
- ratio_MA60: 0.015441
- ratio_gap: 5.97%
- ratio_slope_proxy(20d): 0.000779

### Volume (if available)

- volume: 5828339.00
- volume_MA20: 36475856.95
- volume_ratio: 0.16

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

- close: 15.16
- MA20 / MA60 / MA200: 14.60 / 11.17 / 11.35
- gap20 / gap60: 3.89% / 35.75%
- 5D return: -13.49%
- 20D high/low: 17.53 / 11.38

### Relative Strength

- ratio: 0.053693
- ratio_MA60: 0.046789
- ratio_gap: 14.75%
- ratio_slope_proxy(20d): 0.006365

### Volume (if available)

- volume: 5377050.00
- volume_MA20: 35759032.50
- volume_ratio: 0.15

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-06**
- 실행시간(UTC): **2026-04-06 15:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 3.13
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 15.0 bp / latest 1.97
- VIX: 23.87
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 5.22% / slope_proxy: -0.001611
- GDXJ/GLD gap: -2.28% / slope_proxy: -0.003889

## VZLA (Vizsla Silver)
- close: 3.325 | RSI14: 42.000101 | ATR14%: 7.18%
- MA20 gap: -2.93% | MA50 gap: -19.29% | MA200 gap: -20.41%
- vol_ratio(Volume/Vol20): 0.257458 | gap_open: 0.00%
- RS vs SILJ gap: -17.95% / slope_proxy: -0.027494
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
- close: 8.14 | RSI14: 43.788841 | ATR14%: 10.22%
- MA20 gap: -3.67% | MA50 gap: -22.54% | MA200 gap: 10.57%
- vol_ratio(Volume/Vol20): 0.276517 | gap_open: 0.89%
- SilverMarginGate: SI=72.660004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.39% / slope_proxy: -0.021648
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
- close: 35.84 | RSI14: 48.638983 | ATR14%: 11.83%
- MA20 gap: -0.49% | MA50 gap: -10.50% | MA200 gap: 105.73%
- vol_ratio(Volume/Vol20): 0.190429 | gap_open: 0.58%
- RS vs SILJ gap: 0.05% / slope_proxy: 0.158842
- RS vs GDXJ gap: -1.60% / slope_proxy: 0.041754
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
