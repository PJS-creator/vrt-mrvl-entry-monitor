# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-03**
- 실행시간(UTC): **2026-03-03 23:00:37**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.03 / 4주 변화 22.0 bp
- IG OAS (BAMLC0A0CM): 0.85 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 1.76 / 4주 변화 -18.0 bp
- VIX (VIXCLS): 21.44
- NFCI: -0.5629

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.438831
- MA60: 6.276381
- gap: 18.52%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.198205
- MA60: 0.21536
- gap: -7.97%
- MA60_slope_proxy: -0.019339
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-03**
- 실행시간(UTC): **2026-03-03 23:01:04**

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
- TERM_SPREAD_10Y_POLICY: 54.35 bp / 4주 변화 -22.45 bp
- CURVE_10s5s: 59.63 bp / 4주 변화 3.87 bp

## NWG Price
- close: 586.2
- MA50: 638.224 / gap50: -8.15%
- MA200: 567.8331 / gap200: 3.23%

## Relative Strength
- RS vs FTSE gap: -10.58% / slope_proxy: -0.00147
- RS vs Peers gap: -7.10% / slope_proxy: -0.054544

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-03 23:01:11**

## Commodity Regime

- WTI ref (CL=F): 74.80 / 5D 13.97%
- Brent ref (BZ=F): 81.87 / 5D 15.68%
- Brent Tier: **80-90**
- Brent-WTI spread: 7.07
- Gas ref (NG=F): 3.04 / 5D 4.25%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 53.68
- MA20 / MA60 / MA200: 48.96 / 44.37 / 43.62
- gap20 / gap60: 9.64% / 20.99%
- 5D return: 3.33%
- 20D high/low: 54.21 / 45.09

### Relative Strength

- ratio: 0.949752
- ratio_MA60: 0.903600
- ratio_gap: 5.11%
- ratio_slope_proxy(20d): -0.009749

### Volume (if available)

- volume: 22400288.00
- volume_MA20: 14230404.40
- volume_ratio: 1.57

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.96
- MA20 / MA60 / MA200: 15.79 / 13.68 / 12.66
- gap20 / gap60: 7.40% / 23.95%
- 5D return: 2.54%
- 20D high/low: 17.32 / 14.87

### Relative Strength

- ratio: 0.460619
- ratio_MA60: 0.390087
- ratio_gap: 18.08%
- ratio_slope_proxy(20d): 0.002821

### Volume (if available)

- volume: 46516709.00
- volume_MA20: 23694700.45
- volume_ratio: 1.96

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

- close: 6.11
- MA20 / MA60 / MA200: 6.01 / 4.90 / 3.71
- gap20 / gap60: 1.69% / 24.77%
- 5D return: -6.57%
- 20D high/low: 6.54 / 4.94

### Relative Strength

- ratio: 0.015888
- ratio_MA60: 0.014590
- ratio_gap: 8.90%
- ratio_slope_proxy(20d): 0.000374

### Volume (if available)

- volume: 41390936.00
- volume_MA20: 67735936.80
- volume_ratio: 0.61

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

- close: 11.46
- MA20 / MA60 / MA200: 9.75 / 8.25 / 11.27
- gap20 / gap60: 17.52% / 38.94%
- 5D return: 22.57%
- 20D high/low: 11.46 / 8.77

### Relative Strength

- ratio: 0.046572
- ratio_MA60: 0.039761
- ratio_gap: 17.13%
- ratio_slope_proxy(20d): 0.002595

### Volume (if available)

- volume: 50596067.00
- volume_MA20: 13137588.35
- volume_ratio: 3.85

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-03**
- 실행시간(UTC): **2026-03-03 23:01:28**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 22.0 bp / latest 3.03
- IG OAS 4주 변화: 11.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: -18.0 bp / latest 1.76
- VIX: 21.44
- NFCI: -0.56294

### Leadership ratios
- SILJ/SLV gap: 8.98% / slope_proxy: -0.0041
- GDXJ/GLD gap: 2.77% / slope_proxy: 0.01435

## VZLA (Vizsla Silver)
- close: 4.04 | RSI14: 41.380088 | ATR14%: 8.91%
- MA20 gap: -2.11% | MA50 gap: -21.80% | MA200 gap: -2.09%
- vol_ratio(Volume/Vol20): 0.535912 | gap_open: 7.73%
- RS vs SILJ gap: -31.82% / slope_proxy: -0.025996
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 11.08 | RSI14: 47.344522 | ATR14%: 10.32%
- MA20 gap: -1.97% | MA50 gap: -2.61% | MA200 gap: 67.10%
- vol_ratio(Volume/Vol20): 0.838259 | gap_open: 9.46%
- SilverMarginGate: SI=82.300003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.24% / slope_proxy: 0.020175
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 48.509998 | RSI14: 58.192213 | ATR14%: 12.35%
- MA20 gap: 16.99% | MA50 gap: 33.14% | MA200 gap: 257.50%
- vol_ratio(Volume/Vol20): 1.252609 | gap_open: 10.66%
- RS vs SILJ gap: 37.77% / slope_proxy: 0.249145
- RS vs GDXJ gap: 39.32% / slope_proxy: 0.065778
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
