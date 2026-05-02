# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: OXY**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-01**
- 실행시간(UTC): **2026-05-02 15:00:37**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.83 / 4주 변화 -34.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.94 / 4주 변화 -3.0 bp
- VIX (VIXCLS): 16.89
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.313759
- MA60: 8.115138
- gap: 14.77%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.323546
- MA60: 0.246443
- gap: 31.29%
- MA60_slope_proxy: 0.033755
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-01**
- 실행시간(UTC): **2026-05-02 15:00:39**

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

- 실행시간(UTC): **2026-05-02 15:00:47**

## Commodity Regime

- WTI ref (CL=F): 101.94 / 5D 7.99%
- Brent ref (BZ=F): 108.17 / 5D 2.70%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.23
- Gas ref (NG=F): 2.78 / 5D 10.19%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **True**

### Trend

- close: 58.71
- MA20 / MA60 / MA200: 58.04 / 55.79 / 46.80
- gap20 / gap60: 1.15% / 5.24%
- 5D return: 2.78%
- 20D high/low: 62.96 / 53.79

### Relative Strength

- ratio: 0.997621
- ratio_MA60: 0.978716
- ratio_gap: 1.93%
- ratio_slope_proxy(20d): 0.037189

### Volume (if available)

- volume: 13810600.00
- volume_MA20: 13456230.00
- volume_ratio: 1.03

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.90
- MA20 / MA60 / MA200: 21.04 / 18.75 / 14.30
- gap20 / gap60: 4.11% / 16.81%
- 5D return: 4.94%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.555415
- ratio_MA60: 0.487238
- ratio_gap: 13.99%
- ratio_slope_proxy(20d): 0.046319

### Volume (if available)

- volume: 9250400.00
- volume_MA20: 22526780.00
- volume_ratio: 0.41

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

- close: 6.84
- MA20 / MA60 / MA200: 6.42 / 6.33 / 4.48
- gap20 / gap60: 6.54% / 8.08%
- 5D return: 11.95%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015380
- ratio_MA60: 0.015919
- ratio_gap: -3.39%
- ratio_slope_proxy(20d): 0.000521

### Volume (if available)

- volume: 31963800.00
- volume_MA20: 31412855.00
- volume_ratio: 1.02

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

- close: 12.73
- MA20 / MA60 / MA200: 12.91 / 12.44 / 11.01
- gap20 / gap60: -1.38% / 2.32%
- 5D return: 6.97%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.047138
- ratio_MA60: 0.048541
- ratio_gap: -2.89%
- ratio_slope_proxy(20d): 0.002066

### Volume (if available)

- volume: 19321200.00
- volume_MA20: 23140390.00
- volume_ratio: 0.83

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: OXY


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-01**
- 실행시간(UTC): **2026-05-02 15:00:55**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.83
- IG OAS 4주 변화: -5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -3.0 bp / latest 1.94
- VIX: 16.89
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -5.08% / slope_proxy: 0.013854
- GDXJ/GLD gap: -5.05% / slope_proxy: -0.003949

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 50.732864 | ATR14%: 5.71%
- MA20 gap: 2.34% | MA50 gap: -2.62% | MA200 gap: -17.79%
- vol_ratio(Volume/Vol20): 0.766698 | gap_open: 0.59%
- RS vs SILJ gap: 4.47% / slope_proxy: -0.021592
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
- close: 8.16 | RSI14: 45.794469 | ATR14%: 7.65%
- MA20 gap: -3.15% | MA50 gap: -10.46% | MA200 gap: 3.85%
- vol_ratio(Volume/Vol20): 1.030662 | gap_open: 0.64%
- SilverMarginGate: SI=75.950996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.90% / slope_proxy: -0.031519
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
- close: 38.73 | RSI14: 51.303517 | ATR14%: 8.62%
- MA20 gap: -0.12% | MA50 gap: -1.73% | MA200 gap: 86.20%
- vol_ratio(Volume/Vol20): 0.991 | gap_open: 0.00%
- RS vs SILJ gap: 9.13% / slope_proxy: 0.035898
- RS vs GDXJ gap: 10.90% / slope_proxy: 0.005386
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
