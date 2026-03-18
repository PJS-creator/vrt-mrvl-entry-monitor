# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-17**
- 실행시간(UTC): **2026-03-18 03:00:37**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.27 / 4주 변화 33.0 bp
- IG OAS (BAMLC0A0CM): 0.94 / 4주 변화 15.0 bp
- 10Y Real Yield (DFII10): 1.87 / 4주 변화 10.0 bp
- VIX (VIXCLS): 23.51
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.235962
- MA60: 6.65785
- gap: 23.70%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.228759
- MA60: 0.211144
- gap: 8.34%
- MA60_slope_proxy: -0.013811
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-17**
- 실행시간(UTC): **2026-03-18 03:00:46**

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
- TERM_SPREAD_10Y_POLICY: 101.01 bp / 4주 변화 34.32 bp
- CURVE_10s5s: 49.78 bp / 4주 변화 -9.04 bp

## NWG Price
- close: 581.6
- MA50: 623.884 / gap50: -6.78%
- MA200: 570.6169 / gap200: 1.92%

## Relative Strength
- RS vs FTSE gap: -8.54% / slope_proxy: -0.002518
- RS vs Peers gap: -1.10% / slope_proxy: -0.055526

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-18 03:00:53**

## Commodity Regime

- WTI ref (CL=F): 93.65 / 5D 12.22%
- Brent ref (BZ=F): 102.08 / 5D 16.26%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.43
- Gas ref (NG=F): 2.98 / 5D -1.36%

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

- close: 57.73
- MA20 / MA60 / MA200: 53.54 / 46.60 / 44.14
- gap20 / gap60: 7.83% / 23.90%
- 5D return: 8.68%
- 20D high/low: 58.41 / 46.89

### Relative Strength

- ratio: 0.986669
- ratio_MA60: 0.910472
- ratio_gap: 8.37%
- ratio_slope_proxy(20d): 0.011780

### Volume (if available)

- volume: 12258511.00
- volume_MA20: 20217540.55
- volume_ratio: 0.61

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.51
- MA20 / MA60 / MA200: 17.31 / 14.69 / 13.00
- gap20 / gap60: 12.71% / 32.78%
- 5D return: 8.45%
- 20D high/low: 19.51 / 15.29

### Relative Strength

- ratio: 0.531463
- ratio_MA60: 0.409256
- ratio_gap: 29.86%
- ratio_slope_proxy(20d): 0.023191

### Volume (if available)

- volume: 26309343.00
- volume_MA20: 32221542.15
- volume_ratio: 0.82

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

- close: 6.58
- MA20 / MA60 / MA200: 6.31 / 5.23 / 3.90
- gap20 / gap60: 4.32% / 25.74%
- 5D return: 6.82%
- 20D high/low: 6.58 / 5.93

### Relative Strength

- ratio: 0.017063
- ratio_MA60: 0.014954
- ratio_gap: 14.10%
- ratio_slope_proxy(20d): 0.000601

### Volume (if available)

- volume: 50788661.00
- volume_MA20: 42067068.05
- volume_ratio: 1.21

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.97
- MA20 / MA60 / MA200: 11.07 / 9.22 / 11.32
- gap20 / gap60: 17.18% / 40.63%
- 5D return: 13.93%
- 20D high/low: 13.08 / 9.30

### Relative Strength

- ratio: 0.051571
- ratio_MA60: 0.042437
- ratio_gap: 21.52%
- ratio_slope_proxy(20d): 0.004187

### Volume (if available)

- volume: 13928283.00
- volume_MA20: 21781179.15
- volume_ratio: 0.64

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

- 데이터 기준일(주가): **2026-03-17**
- 실행시간(UTC): **2026-03-18 03:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.27
- IG OAS 4주 변화: 15.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: 10.0 bp / latest 1.87
- VIX: 23.51
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: 0.19% / slope_proxy: -0.004749
- GDXJ/GLD gap: -7.60% / slope_proxy: 0.00917

## VZLA (Vizsla Silver)
- close: 3.58 | RSI14: 35.19634 | ATR14%: 8.22%
- MA20 gap: -9.87% | MA50 gap: -25.94% | MA200 gap: -14.54%
- vol_ratio(Volume/Vol20): 0.565242 | gap_open: 1.10%
- RS vs SILJ gap: -24.78% / slope_proxy: -0.027914
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
- close: 8.65 | RSI14: 35.401153 | ATR14%: 10.88%
- MA20 gap: -19.04% | MA50 gap: -24.23% | MA200 gap: 22.96%
- vol_ratio(Volume/Vol20): 0.647437 | gap_open: 1.12%
- SilverMarginGate: SI=79.175003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.65% / slope_proxy: -0.003478
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
- close: 40.279999 | RSI14: 48.405155 | ATR14%: 12.67%
- MA20 gap: -8.37% | MA50 gap: 0.37% | MA200 gap: 160.07%
- vol_ratio(Volume/Vol20): 0.604856 | gap_open: 0.74%
- RS vs SILJ gap: 15.97% / slope_proxy: 0.258239
- RS vs GDXJ gap: 15.33% / slope_proxy: 0.067799
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
