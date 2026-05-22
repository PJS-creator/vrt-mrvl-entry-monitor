# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-22**
- 실행시간(UTC): **2026-05-22 15:00:51**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.78 / 4주 변화 -8.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 2.13 / 4주 변화 21.0 bp
- VIX (VIXCLS): 16.76
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.669294
- MA60: 8.821128
- gap: 9.62%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.339619
- MA60: 0.276782
- gap: 22.70%
- MA60_slope_proxy: 0.040699
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-22**
- 실행시간(UTC): **2026-05-22 15:00:54**

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
- TERM_SPREAD_10Y_POLICY: 120.54 bp / 4주 변화 11.72 bp
- CURVE_10s5s: 46.61 bp / 4주 변화 -0.06 bp

## NWG Price
- close: 587.8
- MA50: 575.7696 / gap50: 2.09%
- MA200: 585.7961 / gap200: 0.34%

## Relative Strength
- RS vs FTSE gap: 0.64% / slope_proxy: -0.001758
- RS vs Peers gap: -4.15% / slope_proxy: -0.033321

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-22 15:01:03**

## Commodity Regime

- WTI ref (CL=F): 97.55 / 5D -7.47%
- Brent ref (BZ=F): 104.17 / 5D -4.66%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.62
- Gas ref (NG=F): 3.06 / 5D 3.38%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 58.75
- MA20 / MA60 / MA200: 57.93 / 58.11 / 47.87
- gap20 / gap60: 1.42% / 1.09%
- 5D return: -1.46%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.991394
- ratio_MA60: 1.001249
- ratio_gap: -0.98%
- ratio_slope_proxy(20d): 0.033131

### Volume (if available)

- volume: 1861187.00
- volume_MA20: 12132139.35
- volume_ratio: 0.15

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.77
- MA20 / MA60 / MA200: 20.73 / 19.97 / 14.92
- gap20 / gap60: -4.62% / -1.00%
- 5D return: -0.78%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.546271
- ratio_MA60: 0.521830
- ratio_gap: 4.68%
- ratio_slope_proxy(20d): 0.046494

### Volume (if available)

- volume: 3231381.00
- volume_MA20: 17614979.05
- volume_ratio: 0.18

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.75
- MA20 / MA60 / MA200: 6.77 / 6.50 / 4.77
- gap20 / gap60: -0.27% / 3.86%
- 5D return: -4.05%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.015273
- ratio_MA60: 0.015803
- ratio_gap: -3.35%
- ratio_slope_proxy(20d): -0.000023

### Volume (if available)

- volume: 6818043.00
- volume_MA20: 37457822.15
- volume_ratio: 0.18

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.32
- MA20 / MA60 / MA200: 13.02 / 13.34 / 10.87
- gap20 / gap60: 2.29% / -0.13%
- 5D return: -6.39%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.056505
- ratio_MA60: 0.051091
- ratio_gap: 10.60%
- ratio_slope_proxy(20d): 0.002626

### Volume (if available)

- volume: 2975229.00
- volume_MA20: 20156956.45
- volume_ratio: 0.15

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-22**
- 실행시간(UTC): **2026-05-22 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.78
- IG OAS 4주 변화: -5.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.13
- VIX: 16.76
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -5.34% / slope_proxy: -0.00829
- GDXJ/GLD gap: -5.43% / slope_proxy: -0.004847

## VZLA (Vizsla Silver)
- close: 3.33 | RSI14: 44.546069 | ATR14%: 6.17%
- MA20 gap: -4.43% | MA50 gap: -1.60% | MA200 gap: -21.32%
- vol_ratio(Volume/Vol20): 0.347515 | gap_open: 0.00%
- RS vs SILJ gap: 3.60% / slope_proxy: -0.003415
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
- close: 8.01 | RSI14: 42.394916 | ATR14%: 7.92%
- MA20 gap: -6.68% | MA50 gap: -4.70% | MA200 gap: -2.63%
- vol_ratio(Volume/Vol20): 0.180961 | gap_open: 0.24%
- SilverMarginGate: SI=75.639999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.26% / slope_proxy: -0.016165
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
- close: 32.450001 | RSI14: 39.956111 | ATR14%: 10.10%
- MA20 gap: -13.18% | MA50 gap: -12.59% | MA200 gap: 38.98%
- vol_ratio(Volume/Vol20): 0.163518 | gap_open: 1.47%
- RS vs SILJ gap: -7.63% / slope_proxy: 0.026926
- RS vs GDXJ gap: -5.39% / slope_proxy: 0.007893
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
