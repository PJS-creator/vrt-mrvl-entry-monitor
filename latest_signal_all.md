# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-29**
- 실행시간(UTC): **2026-04-30 03:00:36**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.85 / 4주 변화 -43.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -9.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 -8.0 bp
- VIX (VIXCLS): 17.83
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.923928
- MA60: 8.00905
- gap: 11.42%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.313403
- MA60: 0.241998
- gap: 29.51%
- MA60_slope_proxy: 0.030626
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-29**
- 실행시간(UTC): **2026-04-30 03:00:43**

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
- TERM_SPREAD_10Y_POLICY: 116.95 bp / 4주 변화 3.89 bp
- CURVE_10s5s: 47.02 bp / 4주 변화 5.21 bp

## NWG Price
- close: 569.0
- MA50: 585.9879 / gap50: -2.90%
- MA200: 580.9762 / gap200: -2.06%

## Relative Strength
- RS vs FTSE gap: -2.18% / slope_proxy: -0.002368
- RS vs Peers gap: -6.61% / slope_proxy: -0.036527

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-30 03:00:51**

## Commodity Regime

- WTI ref (CL=F): 108.71 / 5D 16.94%
- Brent ref (BZ=F): 112.28 / 5D 10.18%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.57
- Gas ref (NG=F): 2.64 / 5D -3.16%

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

- close: 60.76
- MA20 / MA60 / MA200: 58.34 / 55.32 / 46.62
- gap20 / gap60: 4.15% / 9.83%
- 5D return: 6.50%
- 20D high/low: 62.97 / 53.79

### Relative Strength

- ratio: 1.029307
- ratio_MA60: 0.974543
- ratio_gap: 5.62%
- ratio_slope_proxy(20d): 0.038367

### Volume (if available)

- volume: 13237286.00
- volume_MA20: 14623769.30
- volume_ratio: 0.91

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.85
- MA20 / MA60 / MA200: 20.86 / 18.52 / 14.21
- gap20 / gap60: 4.75% / 17.98%
- 5D return: 3.77%
- 20D high/low: 21.85 / 19.86

### Relative Strength

- ratio: 0.565330
- ratio_MA60: 0.482172
- ratio_gap: 17.25%
- ratio_slope_proxy(20d): 0.047084

### Volume (if available)

- volume: 19710295.00
- volume_MA20: 25699714.75
- volume_ratio: 0.77

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

- close: 6.96
- MA20 / MA60 / MA200: 6.39 / 6.27 / 4.44
- gap20 / gap60: 8.89% / 10.95%
- 5D return: 14.85%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015613
- ratio_MA60: 0.015887
- ratio_gap: -1.73%
- ratio_slope_proxy(20d): 0.000575

### Volume (if available)

- volume: 33846557.00
- volume_MA20: 31955297.85
- volume_ratio: 1.06

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.16
- MA20 / MA60 / MA200: 13.07 / 12.33 / 11.05
- gap20 / gap60: 0.66% / 6.77%
- 5D return: 6.65%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.048341
- ratio_MA60: 0.048451
- ratio_gap: -0.23%
- ratio_slope_proxy(20d): 0.002560

### Volume (if available)

- volume: 25448526.00
- volume_MA20: 24804296.30
- volume_ratio: 1.03

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

- 데이터 기준일(주가): **2026-04-29**
- 실행시간(UTC): **2026-04-30 03:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -43.0 bp / latest 2.85
- IG OAS 4주 변화: -9.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.92
- VIX: 17.83
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.69% / slope_proxy: 0.015199
- GDXJ/GLD gap: -5.43% / slope_proxy: -0.00371

## VZLA (Vizsla Silver)
- close: 3.4 | RSI14: 48.114754 | ATR14%: 5.74%
- MA20 gap: 0.94% | MA50 gap: -4.76% | MA200 gap: -19.18%
- vol_ratio(Volume/Vol20): 0.996473 | gap_open: 0.88%
- RS vs SILJ gap: 5.51% / slope_proxy: -0.023353
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
- close: 7.73 | RSI14: 40.224766 | ATR14%: 8.47%
- MA20 gap: -8.22% | MA50 gap: -15.87% | MA200 gap: -1.12%
- vol_ratio(Volume/Vol20): 1.403874 | gap_open: 1.65%
- SilverMarginGate: SI=72.745003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.56% / slope_proxy: -0.030942
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
- close: 34.209999 | RSI14: 41.406666 | ATR14%: 10.09%
- MA20 gap: -11.30% | MA50 gap: -13.54% | MA200 gap: 67.19%
- vol_ratio(Volume/Vol20): 1.00229 | gap_open: 1.32%
- RS vs SILJ gap: 0.29% / slope_proxy: 0.040123
- RS vs GDXJ gap: -0.31% / slope_proxy: 0.006665
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
