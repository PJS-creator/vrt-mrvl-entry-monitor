# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-11**
- 실행시간(UTC): **2026-03-11 15:00:38**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.06 / 4주 변화 20.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 7.0 bp
- 10Y Real Yield (DFII10): 1.78 / 4주 변화 -9.0 bp
- VIX (VIXCLS): 24.93
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.390573
- MA60: 6.486455
- gap: 29.36%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.230513
- MA60: 0.211981
- gap: 8.74%
- MA60_slope_proxy: -0.016518
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-11**
- 실행시간(UTC): **2026-03-11 15:00:43**

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
- TERM_SPREAD_10Y_POLICY: 83.29 bp / 4주 변화 5.19 bp
- CURVE_10s5s: 49.01 bp / 4주 변화 -12.14 bp

## NWG Price
- close: 590.4
- MA50: 630.78 / gap50: -6.40%
- MA200: 569.735 / gap200: 3.63%

## Relative Strength
- RS vs FTSE gap: -7.78% / slope_proxy: -0.00214
- RS vs Peers gap: -5.40% / slope_proxy: -0.05797

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-11 15:00:49**

## Commodity Regime

- WTI ref (CL=F): 86.44 / 5D 15.78%
- Brent ref (BZ=F): 87.82 / 5D 7.89%
- Brent Tier: **80-90**
- Brent-WTI spread: 1.38
- Gas ref (NG=F): 3.12 / 5D 6.79%

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

- close: 54.41
- MA20 / MA60 / MA200: 51.11 / 45.39 / 43.79
- gap20 / gap60: 6.46% / 19.88%
- 5D return: 1.97%
- 20D high/low: 54.76 / 45.28

### Relative Strength

- ratio: 0.960120
- ratio_MA60: 0.903663
- ratio_gap: 6.25%
- ratio_slope_proxy(20d): -0.000350

### Volume (if available)

- volume: 6239685.00
- volume_MA20: 17384924.25
- volume_ratio: 0.36

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.91
- MA20 / MA60 / MA200: 16.56 / 14.22 / 12.85
- gap20 / gap60: 14.16% / 32.95%
- 5D return: 12.73%
- 20D high/low: 18.91 / 15.02

### Relative Strength

- ratio: 0.499340
- ratio_MA60: 0.399236
- ratio_gap: 25.07%
- ratio_slope_proxy(20d): 0.012301

### Volume (if available)

- volume: 13501995.00
- volume_MA20: 28123739.75
- volume_ratio: 0.48

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

- close: 6.33
- MA20 / MA60 / MA200: 6.27 / 5.08 / 3.82
- gap20 / gap60: 0.90% / 24.68%
- 5D return: -0.64%
- 20D high/low: 6.54 / 5.93

### Relative Strength

- ratio: 0.016357
- ratio_MA60: 0.014755
- ratio_gap: 10.86%
- ratio_slope_proxy(20d): 0.000521

### Volume (if available)

- volume: 8020273.00
- volume_MA20: 54409538.65
- volume_ratio: 0.15

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

- close: 11.85
- MA20 / MA60 / MA200: 10.35 / 8.77 / 11.32
- gap20 / gap60: 14.40% / 35.04%
- 5D return: 6.14%
- 20D high/low: 12.48 / 8.77

### Relative Strength

- ratio: 0.047312
- ratio_MA60: 0.041120
- ratio_gap: 15.06%
- ratio_slope_proxy(20d): 0.003260

### Volume (if available)

- volume: 6096836.00
- volume_MA20: 18463241.80
- volume_ratio: 0.33

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

- 데이터 기준일(주가): **2026-03-11**
- 실행시간(UTC): **2026-03-11 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.06
- IG OAS 4주 변화: 7.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -9.0 bp / latest 1.78
- VIX: 24.93
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: 0.92% / slope_proxy: -0.003035
- GDXJ/GLD gap: -3.46% / slope_proxy: 0.012308

## VZLA (Vizsla Silver)
- close: 4.0539 | RSI14: 43.199272 | ATR14%: 7.86%
- MA20 gap: 1.71% | MA50 gap: -18.63% | MA200 gap: -2.84%
- vol_ratio(Volume/Vol20): 0.120814 | gap_open: 2.17%
- RS vs SILJ gap: -24.81% / slope_proxy: -0.029069
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.09 | RSI14: 43.33006 | ATR14%: 10.32%
- MA20 gap: -7.12% | MA50 gap: -12.04% | MA200 gap: 46.45%
- vol_ratio(Volume/Vol20): 0.420448 | gap_open: 0.75%
- SilverMarginGate: SI=86.029999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.32% / slope_proxy: 0.004119
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
- close: 43.660099 | RSI14: 51.905141 | ATR14%: 13.13%
- MA20 gap: 1.44% | MA50 gap: 12.24% | MA200 gap: 195.68%
- vol_ratio(Volume/Vol20): 0.255455 | gap_open: 4.57%
- RS vs SILJ gap: 19.97% / slope_proxy: 0.249362
- RS vs GDXJ gap: 20.63% / slope_proxy: 0.065469
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
