# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-13**
- 실행시간(UTC): **2026-03-15 03:00:36**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.17 / 4주 변화 25.0 bp
- IG OAS (BAMLC0A0CM): 0.91 / 4주 변화 13.0 bp
- 10Y Real Yield (DFII10): 1.89 / 4주 변화 9.0 bp
- VIX (VIXCLS): 27.29
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.0301
- MA60: 6.56831
- gap: 22.26%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.226835
- MA60: 0.211471
- gap: 7.27%
- MA60_slope_proxy: -0.01508
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-13**
- 실행시간(UTC): **2026-03-15 03:00:42**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 88.88 bp / 4주 변화 14.99 bp
- CURVE_10s5s: 49.5 bp / 4주 변화 -9.46 bp

## NWG Price
- close: 565.2
- MA50: 627.308 / gap50: -9.90%
- MA200: 570.1539 / gap200: -0.87%

## Relative Strength
- RS vs FTSE gap: -10.35% / slope_proxy: -0.002294
- RS vs Peers gap: -2.10% / slope_proxy: -0.056606

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-15 03:00:50**

## Commodity Regime

- WTI ref (CL=F): 98.71 / 5D 8.59%
- Brent ref (BZ=F): 98.91 / 5D 6.71%
- Brent Tier: **>=90**
- Brent-WTI spread: 0.20
- Gas ref (NG=F): 3.13 / 5D -1.73%

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

- close: 57.88
- MA20 / MA60 / MA200: 52.37 / 46.00 / 43.97
- gap20 / gap60: 10.53% / 25.83%
- 5D return: 7.32%
- 20D high/low: 58.41 / 45.72

### Relative Strength

- ratio: 1.003120
- ratio_MA60: 0.907589
- ratio_gap: 10.53%
- ratio_slope_proxy(20d): 0.006251

### Volume (if available)

- volume: 15137186.00
- volume_MA20: 19636504.30
- volume_ratio: 0.77

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.57
- MA20 / MA60 / MA200: 16.89 / 14.44 / 12.92
- gap20 / gap60: 9.97% / 28.59%
- 5D return: 5.51%
- 20D high/low: 18.99 / 15.02

### Relative Strength

- ratio: 0.523246
- ratio_MA60: 0.404240
- ratio_gap: 29.44%
- ratio_slope_proxy(20d): 0.017632

### Volume (if available)

- volume: 32885060.00
- volume_MA20: 30932568.00
- volume_ratio: 1.06

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

- close: 6.36
- MA20 / MA60 / MA200: 6.30 / 5.15 / 3.86
- gap20 / gap60: 0.91% / 23.50%
- 5D return: 7.25%
- 20D high/low: 6.54 / 5.93

### Relative Strength

- ratio: 0.017137
- ratio_MA60: 0.014855
- ratio_gap: 15.36%
- ratio_slope_proxy(20d): 0.000568

### Volume (if available)

- volume: 36500454.00
- volume_MA20: 46930882.70
- volume_ratio: 0.78

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.10
- MA20 / MA60 / MA200: 10.73 / 9.01 / 11.33
- gap20 / gap60: 22.14% / 45.37%
- 5D return: 4.97%
- 20D high/low: 13.10 / 8.77

### Relative Strength

- ratio: 0.051928
- ratio_MA60: 0.041863
- ratio_gap: 24.04%
- ratio_slope_proxy(20d): 0.003687

### Volume (if available)

- volume: 27597176.00
- volume_MA20: 20918363.80
- volume_ratio: 1.32

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

- 데이터 기준일(주가): **2026-03-13**
- 실행시간(UTC): **2026-03-15 03:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 25.0 bp / latest 3.17
- IG OAS 4주 변화: 13.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.89
- VIX: 27.29
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -1.65% / slope_proxy: -0.003792
- GDXJ/GLD gap: -8.88% / slope_proxy: 0.010759

## VZLA (Vizsla Silver)
- close: 3.59 | RSI14: 34.877784 | ATR14%: 8.71%
- MA20 gap: -9.92% | MA50 gap: -26.88% | MA200 gap: -14.15%
- vol_ratio(Volume/Vol20): 0.591721 | gap_open: 0.77%
- RS vs SILJ gap: -25.64% / slope_proxy: -0.02846
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
- close: 9.33 | RSI14: 38.977173 | ATR14%: 10.52%
- MA20 gap: -13.21% | MA50 gap: -18.49% | MA200 gap: 33.91%
- vol_ratio(Volume/Vol20): 2.618266 | gap_open: 1.62%
- SilverMarginGate: SI=81.343002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.37% / slope_proxy: -0.000536
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
- close: 37.93 | RSI14: 45.173627 | ATR14%: 14.26%
- MA20 gap: -12.68% | MA50 gap: -3.98% | MA200 gap: 150.85%
- vol_ratio(Volume/Vol20): 0.72567 | gap_open: 0.09%
- RS vs SILJ gap: 12.04% / slope_proxy: 0.251936
- RS vs GDXJ gap: 12.27% / slope_proxy: 0.066199
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
