# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-04**
- 실행시간(UTC): **2026-05-04 15:00:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.77 / 4주 변화 -36.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.94 / 4주 변화 -3.0 bp
- VIX (VIXCLS): 16.99
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.274868
- MA60: 8.170445
- gap: 13.52%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.323275
- MA60: 0.248587
- gap: 30.04%
- MA60_slope_proxy: 0.034951
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-01**
- 실행시간(UTC): **2026-05-04 15:00:44**

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
- TERM_SPREAD_10Y_POLICY: 125.53 bp / 4주 변화 22.51 bp
- CURVE_10s5s: 44.29 bp / 4주 변화 0.86 bp

## NWG Price
- close: 565.6
- MA50: 584.1298 / gap50: -3.17%
- MA200: 581.8056 / gap200: -2.79%

## Relative Strength
- RS vs FTSE gap: -3.54% / slope_proxy: -0.002456
- RS vs Peers gap: -8.24% / slope_proxy: -0.037537

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-04 15:00:52**

## ⚠️ DATA WARNING

- FRED DHHNGSP failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 102.51 / 5D 6.37%
- Brent ref (BZ=F): 111.44 / 5D 2.97%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.93
- Gas ref (NG=F): 2.87 / 5D 12.55%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 59.30
- MA20 / MA60 / MA200: 57.86 / 56.03 / 46.88
- gap20 / gap60: 2.49% / 5.84%
- 5D return: 3.54%
- 20D high/low: 62.94 / 53.79

### Relative Strength

- ratio: 1.005000
- ratio_MA60: 0.981046
- ratio_gap: 2.44%
- ratio_slope_proxy(20d): 0.037101

### Volume (if available)

- volume: 2365166.00
- volume_MA20: 12990668.30
- volume_ratio: 0.18

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.88
- MA20 / MA60 / MA200: 21.09 / 18.87 / 14.35
- gap20 / gap60: 3.71% / 15.95%
- 5D return: 4.37%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.554499
- ratio_MA60: 0.489791
- ratio_gap: 13.21%
- ratio_slope_proxy(20d): 0.045751

### Volume (if available)

- volume: 2785757.00
- volume_MA20: 21907432.85
- volume_ratio: 0.13

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.79
- MA20 / MA60 / MA200: 6.43 / 6.36 / 4.50
- gap20 / gap60: 5.60% / 6.77%
- 5D return: 4.14%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015346
- ratio_MA60: 0.015941
- ratio_gap: -3.73%
- ratio_slope_proxy(20d): 0.000498

### Volume (if available)

- volume: 5811177.00
- volume_MA20: 30631008.85
- volume_ratio: 0.19

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.10
- MA20 / MA60 / MA200: 12.77 / 12.50 / 11.00
- gap20 / gap60: 2.58% / 4.72%
- 5D return: 7.42%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.048180
- ratio_MA60: 0.048605
- ratio_gap: -0.88%
- ratio_slope_proxy(20d): 0.001776

### Volume (if available)

- volume: 4919106.00
- volume_MA20: 22137565.30
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-04**
- 실행시간(UTC): **2026-05-04 15:01:39**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -36.0 bp / latest 2.77
- IG OAS 4주 변화: -5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -3.0 bp / latest 1.94
- VIX: 16.99
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.75% / slope_proxy: 0.01281
- GDXJ/GLD gap: -4.60% / slope_proxy: -0.003782

## VZLA (Vizsla Silver)
- close: 3.465 | RSI14: 50.945169 | ATR14%: 5.51%
- MA20 gap: 2.23% | MA50 gap: -2.25% | MA200 gap: -17.68%
- vol_ratio(Volume/Vol20): 0.166961 | gap_open: 1.73%
- RS vs SILJ gap: 5.75% / slope_proxy: -0.020503
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
- close: 8.27 | RSI14: 47.180267 | ATR14%: 7.50%
- MA20 gap: -1.92% | MA50 gap: -8.65% | MA200 gap: 4.97%
- vol_ratio(Volume/Vol20): 0.377056 | gap_open: 1.59%
- SilverMarginGate: SI=74.690002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.55% / slope_proxy: -0.031207
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
- close: 37.209999 | RSI14: 48.243654 | ATR14%: 8.71%
- MA20 gap: -4.19% | MA50 gap: -5.41% | MA200 gap: 77.47%
- vol_ratio(Volume/Vol20): 0.218974 | gap_open: 4.47%
- RS vs SILJ gap: 5.39% / slope_proxy: 0.035681
- RS vs GDXJ gap: 6.89% / slope_proxy: 0.00533
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
