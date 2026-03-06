# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-06**
- 실행시간(UTC): **2026-03-06 15:00:39**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.0 / 4주 변화 3.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 1.8 / 4주 변화 -14.0 bp
- VIX (VIXCLS): 23.75
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.638261
- MA60: 6.382983
- gap: 19.67%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.223989
- MA60: 0.212303
- gap: 5.50%
- MA60_slope_proxy: -0.018902
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-06**
- 실행시간(UTC): **2026-03-06 15:00:49**

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
- TERM_SPREAD_10Y_POLICY: 68.12 bp / 4주 변화 -10.24 bp
- CURVE_10s5s: 58.29 bp / 4주 변화 2.0 bp

## NWG Price
- close: 569.6
- MA50: 634.444 / gap50: -10.22%
- MA200: 568.7535 / gap200: 0.15%

## Relative Strength
- RS vs FTSE gap: -10.55% / slope_proxy: -0.001986
- RS vs Peers gap: -6.63% / slope_proxy: -0.059526

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-06 15:00:56**

## Commodity Regime

- WTI ref (CL=F): 88.71 / 5D 32.36%
- Brent ref (BZ=F): 91.39 / 5D 26.09%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.68
- Gas ref (NG=F): 3.09 / 5D 7.97%

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

- close: 53.68
- MA20 / MA60 / MA200: 50.14 / 44.95 / 43.79
- gap20 / gap60: 7.07% / 19.42%
- 5D return: 1.13%
- 20D high/low: 54.21 / 45.49

### Relative Strength

- ratio: 0.954142
- ratio_MA60: 0.904990
- ratio_gap: 5.43%
- ratio_slope_proxy(20d): -0.006204

### Volume (if available)

- volume: 6560105.00
- volume_MA20: 14194465.25
- volume_ratio: 0.46

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.20
- MA20 / MA60 / MA200: 16.06 / 13.91 / 12.74
- gap20 / gap60: 7.10% / 23.68%
- 5D return: 3.43%
- 20D high/low: 17.32 / 14.87

### Relative Strength

- ratio: 0.479136
- ratio_MA60: 0.393917
- ratio_gap: 21.63%
- ratio_slope_proxy(20d): 0.006334

### Volume (if available)

- volume: 9773173.00
- volume_MA20: 22749273.65
- volume_ratio: 0.43

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

- close: 6.01
- MA20 / MA60 / MA200: 6.17 / 4.98 / 3.76
- gap20 / gap60: -2.53% / 20.69%
- 5D return: -7.18%
- 20D high/low: 6.54 / 5.39

### Relative Strength

- ratio: 0.016079
- ratio_MA60: 0.014665
- ratio_gap: 9.64%
- ratio_slope_proxy(20d): 0.000441

### Volume (if available)

- volume: 4626122.00
- volume_MA20: 65557446.10
- volume_ratio: 0.07

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.46
- MA20 / MA60 / MA200: 10.13 / 8.51 / 11.30
- gap20 / gap60: 23.05% / 46.48%
- 5D return: 28.59%
- 20D high/low: 12.46 / 8.77

### Relative Strength

- ratio: 0.049501
- ratio_MA60: 0.040490
- ratio_gap: 22.26%
- ratio_slope_proxy(20d): 0.002975

### Volume (if available)

- volume: 6620206.00
- volume_MA20: 15714060.30
- volume_ratio: 0.42

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-06**
- 실행시간(UTC): **2026-03-06 15:01:28**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 3.0 bp / latest 3.0
- IG OAS 4주 변화: 6.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -14.0 bp / latest 1.8
- VIX: 23.75
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 0.26% / slope_proxy: -0.002859
- GDXJ/GLD gap: -3.54% / slope_proxy: 0.013611

## VZLA (Vizsla Silver)
- close: 3.904 | RSI14: 39.714795 | ATR14%: 8.55%
- MA20 gap: -2.66% | MA50 gap: -23.21% | MA200 gap: -5.95%
- vol_ratio(Volume/Vol20): 0.122725 | gap_open: 3.69%
- RS vs SILJ gap: -27.82% / slope_proxy: -0.028313
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
- close: 9.69 | RSI14: 40.385957 | ATR14%: 10.81%
- MA20 gap: -12.13% | MA50 gap: -15.42% | MA200 gap: 43.36%
- vol_ratio(Volume/Vol20): 0.123337 | gap_open: 3.31%
- SilverMarginGate: SI=82.945 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.68% / slope_proxy: 0.012238
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
- close: 41.650002 | RSI14: 49.376207 | ATR14%: 13.93%
- MA20 gap: -1.37% | MA50 gap: 9.85% | MA200 gap: 193.77%
- vol_ratio(Volume/Vol20): 0.185638 | gap_open: 0.80%
- RS vs SILJ gap: 21.45% / slope_proxy: 0.247246
- RS vs GDXJ gap: 21.01% / slope_proxy: 0.065061
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
