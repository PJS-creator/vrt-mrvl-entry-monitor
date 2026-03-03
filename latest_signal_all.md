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
- 실행시간(UTC): **2026-03-03 16:12:00**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.03 / 4주 변화 22.0 bp
- IG OAS (BAMLC0A0CM): 0.85 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 1.72 / 4주 변화 -18.0 bp
- VIX (VIXCLS): 21.44
- NFCI: -0.5629

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.445315
- MA60: 6.276489
- gap: 18.62%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.199288
- MA60: 0.215378
- gap: -7.47%
- MA60_slope_proxy: -0.019321
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-03**
- 실행시간(UTC): **2026-03-03 16:12:06**

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
- close: 584.8
- MA50: 638.196 / gap50: -8.37%
- MA200: 567.8261 / gap200: 2.99%

## Relative Strength
- RS vs FTSE gap: -10.39% / slope_proxy: -0.001468
- RS vs Peers gap: -6.53% / slope_proxy: -0.05444

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-03 16:12:14**

## Commodity Regime

- WTI ref (CL=F): 77.03 / 5D 17.37%
- Brent ref (BZ=F): 83.76 / 5D 18.36%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.73
- Gas ref (NG=F): 3.12 / 5D 6.96%

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

- close: 54.89
- MA20 / MA60 / MA200: 49.02 / 44.39 / 43.63
- gap20 / gap60: 11.97% / 23.66%
- 5D return: 5.66%
- 20D high/low: 54.89 / 45.09

### Relative Strength

- ratio: 0.963219
- ratio_MA60: 0.903825
- ratio_gap: 6.57%
- ratio_slope_proxy(20d): -0.009524

### Volume (if available)

- volume: 11029480.00
- volume_MA20: 13658009.00
- volume_ratio: 0.81

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.16
- MA20 / MA60 / MA200: 15.80 / 13.69 / 12.66
- gap20 / gap60: 8.59% / 25.37%
- 5D return: 3.74%
- 20D high/low: 17.32 / 14.87

### Relative Strength

- ratio: 0.471466
- ratio_MA60: 0.390268
- ratio_gap: 20.81%
- ratio_slope_proxy(20d): 0.003002

### Volume (if available)

- volume: 21596779.00
- volume_MA20: 22447458.95
- volume_ratio: 0.96

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

- close: 6.14
- MA20 / MA60 / MA200: 6.01 / 4.90 / 3.71
- gap20 / gap60: 2.10% / 25.29%
- 5D return: -6.17%
- 20D high/low: 6.54 / 4.94

### Relative Strength

- ratio: 0.015806
- ratio_MA60: 0.014588
- ratio_gap: 8.34%
- ratio_slope_proxy(20d): 0.000373

### Volume (if available)

- volume: 17574319.00
- volume_MA20: 66539740.95
- volume_ratio: 0.26

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

- close: 12.34
- MA20 / MA60 / MA200: 9.80 / 8.26 / 11.27
- gap20 / gap60: 25.93% / 49.29%
- 5D return: 31.93%
- 20D high/low: 12.34 / 8.77

### Relative Strength

- ratio: 0.048557
- ratio_MA60: 0.039794
- ratio_gap: 22.02%
- ratio_slope_proxy(20d): 0.002628

### Volume (if available)

- volume: 22473126.00
- volume_MA20: 11725321.30
- volume_ratio: 1.92

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
- 실행시간(UTC): **2026-03-03 16:12:24**

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
- 10Y Real Yield 4주 변화: -18.0 bp / latest 1.72
- VIX: 21.44
- NFCI: -0.56294

### Leadership ratios
- SILJ/SLV gap: 7.84% / slope_proxy: -0.004186
- GDXJ/GLD gap: 3.15% / slope_proxy: 0.014369

## VZLA (Vizsla Silver)
- close: 4.0 | RSI14: 40.787996 | ATR14%: 9.00%
- MA20 gap: -3.03% | MA50 gap: -22.56% | MA200 gap: -3.06%
- vol_ratio(Volume/Vol20): 0.241604 | gap_open: 7.73%
- RS vs SILJ gap: -32.21% / slope_proxy: -0.026007
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
- close: 11.06 | RSI14: 47.241321 | ATR14%: 10.34%
- MA20 gap: -2.14% | MA50 gap: -2.78% | MA200 gap: 66.80%
- vol_ratio(Volume/Vol20): 0.47987 | gap_open: 9.46%
- SilverMarginGate: SI=82.855003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.03% / slope_proxy: 0.020188
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
- close: 48.100101 | RSI14: 57.65229 | ATR14%: 12.45%
- MA20 gap: 16.06% | MA50 gap: 32.04% | MA200 gap: 254.53%
- vol_ratio(Volume/Vol20): 0.660337 | gap_open: 10.66%
- RS vs SILJ gap: 37.19% / slope_proxy: 0.249048
- RS vs GDXJ gap: 37.45% / slope_proxy: 0.065699
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
