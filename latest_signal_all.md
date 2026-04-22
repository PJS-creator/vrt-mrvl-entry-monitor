# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-22**
- 실행시간(UTC): **2026-04-22 15:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.85 / 4주 변화 -34.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 1.91 / 4주 변화 -10.0 bp
- VIX (VIXCLS): 19.5
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.726713
- MA60: 7.768701
- gap: 12.33%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.328264
- MA60: 0.231657
- gap: 41.70%
- MA60_slope_proxy: 0.021492
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-22**
- 실행시간(UTC): **2026-04-22 15:00:46**

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
- TERM_SPREAD_10Y_POLICY: 103.29 bp / 4주 변화 -8.74 bp
- CURVE_10s5s: 49.84 bp / 4주 변화 8.07 bp

## NWG Price
- close: 593.8
- MA50: 588.2801 / gap50: 0.94%
- MA200: 578.9381 / gap200: 2.57%

## Relative Strength
- RS vs FTSE gap: -1.89% / slope_proxy: -0.002597
- RS vs Peers gap: -4.56% / slope_proxy: -0.037259

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-22 15:00:54**

## Commodity Regime

- WTI ref (CL=F): 91.65 / 5D 0.39%
- Brent ref (BZ=F): 95.43 / 5D 0.53%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.78
- Gas ref (NG=F): 2.74 / 5D 4.98%

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

- close: 56.44
- MA20 / MA60 / MA200: 59.87 / 54.17 / 46.29
- gap20 / gap60: -5.72% / 4.20%
- 5D return: 1.09%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 1.000372
- ratio_MA60: 0.964249
- ratio_gap: 3.75%
- ratio_slope_proxy(20d): 0.039005

### Volume (if available)

- volume: 3204465.00
- volume_MA20: 17393643.25
- volume_ratio: 0.18

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.00
- MA20 / MA60 / MA200: 20.76 / 18.12 / 14.07
- gap20 / gap60: 1.14% / 15.89%
- 5D return: 2.24%
- 20D high/low: 21.97 / 19.82

### Relative Strength

- ratio: 0.514643
- ratio_MA60: 0.473695
- ratio_gap: 8.64%
- ratio_slope_proxy(20d): 0.051133

### Volume (if available)

- volume: 4276096.00
- volume_MA20: 30274949.80
- volume_ratio: 0.14

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

- close: 5.99
- MA20 / MA60 / MA200: 6.46 / 6.14 / 4.35
- gap20 / gap60: -7.27% / -2.45%
- 5D return: -2.60%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.014333
- ratio_MA60: 0.015824
- ratio_gap: -9.42%
- ratio_slope_proxy(20d): 0.000694

### Volume (if available)

- volume: 4448040.00
- volume_MA20: 29580897.00
- volume_ratio: 0.15

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

- close: 12.35
- MA20 / MA60 / MA200: 14.14 / 12.07 / 11.15
- gap20 / gap60: -12.67% / 2.34%
- 5D return: 1.40%
- 20D high/low: 17.53 / 11.45

### Relative Strength

- ratio: 0.048196
- ratio_MA60: 0.048232
- ratio_gap: -0.07%
- ratio_slope_proxy(20d): 0.004146

### Volume (if available)

- volume: 5678823.00
- volume_MA20: 26681961.15
- volume_ratio: 0.21

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-22**
- 실행시간(UTC): **2026-04-22 15:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.85
- IG OAS 4주 변화: -7.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -10.0 bp / latest 1.91
- VIX: 19.5
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.19% / slope_proxy: 0.012346
- GDXJ/GLD gap: 0.80% / slope_proxy: -0.003928

## VZLA (Vizsla Silver)
- close: 3.465 | RSI14: 49.920932 | ATR14%: 5.75%
- MA20 gap: 4.58% | MA50 gap: -4.07% | MA200 gap: -17.47%
- vol_ratio(Volume/Vol20): 0.282954 | gap_open: 2.40%
- RS vs SILJ gap: -6.99% / slope_proxy: -0.02627
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
- close: 8.95 | RSI14: 51.88556 | ATR14%: 7.95%
- MA20 gap: 7.51% | MA50 gap: -4.79% | MA200 gap: 16.25%
- vol_ratio(Volume/Vol20): 0.187707 | gap_open: 4.00%
- SilverMarginGate: SI=77.989998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.85% / slope_proxy: -0.028523
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
- close: 41.029999 | RSI14: 54.091908 | ATR14%: 9.14%
- MA20 gap: 9.07% | MA50 gap: 4.15% | MA200 gap: 108.96%
- vol_ratio(Volume/Vol20): 0.206281 | gap_open: 4.34%
- RS vs SILJ gap: 7.75% / slope_proxy: 0.068918
- RS vs GDXJ gap: 6.70% / slope_proxy: 0.01516
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
