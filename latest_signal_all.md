# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-21**
- 실행시간(UTC): **2026-05-22 03:00:38**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.8 / 4주 변화 -4.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 2.13 / 4주 변화 21.0 bp
- VIX (VIXCLS): 17.44
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.409369
- MA60: 8.790664
- gap: 7.04%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.335793
- MA60: 0.274328
- gap: 22.41%
- MA60_slope_proxy: 0.040309
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-21**
- 실행시간(UTC): **2026-05-22 03:00:40**

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
- TERM_SPREAD_10Y_POLICY: 133.33 bp / 4주 변화 25.91 bp
- CURVE_10s5s: 46.82 bp / 4주 변화 -1.38 bp

## NWG Price
- close: 581.8
- MA50: 575.8209 / gap50: 1.04%
- MA200: 585.4836 / gap200: -0.63%

## Relative Strength
- RS vs FTSE gap: -0.20% / slope_proxy: -0.001909
- RS vs Peers gap: -4.19% / slope_proxy: -0.034358

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-22 03:00:47**

## Commodity Regime

- WTI ref (CL=F): 97.39 / 5D -3.74%
- Brent ref (BZ=F): 104.18 / 5D -1.46%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.79
- Gas ref (NG=F): 3.13 / 5D 8.26%

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

- close: 58.83
- MA20 / MA60 / MA200: 57.84 / 57.99 / 47.79
- gap20 / gap60: 1.70% / 1.45%
- 5D return: 3.50%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.994926
- ratio_MA60: 1.000324
- ratio_gap: -0.54%
- ratio_slope_proxy(20d): 0.033991

### Volume (if available)

- volume: 13933153.00
- volume_MA20: 12428417.65
- volume_ratio: 1.12

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.03
- MA20 / MA60 / MA200: 20.79 / 19.92 / 14.88
- gap20 / gap60: -3.64% / 0.55%
- 5D return: 1.26%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.541205
- ratio_MA60: 0.519764
- ratio_gap: 4.13%
- ratio_slope_proxy(20d): 0.046489

### Volume (if available)

- volume: 15488366.00
- volume_MA20: 18183218.30
- volume_ratio: 0.85

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.82
- MA20 / MA60 / MA200: 6.74 / 6.50 / 4.75
- gap20 / gap60: 1.17% / 4.96%
- 5D return: -1.30%
- 20D high/low: 7.58 / 6.11

### Relative Strength

- ratio: 0.015321
- ratio_MA60: 0.015817
- ratio_gap: -3.13%
- ratio_slope_proxy(20d): -0.000012

### Volume (if available)

- volume: 27516133.00
- volume_MA20: 38559391.65
- volume_ratio: 0.71

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

- close: 13.56
- MA20 / MA60 / MA200: 12.95 / 13.27 / 10.87
- gap20 / gap60: 4.71% / 2.17%
- 5D return: 4.23%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.056394
- ratio_MA60: 0.050828
- ratio_gap: 10.95%
- ratio_slope_proxy(20d): 0.002373

### Volume (if available)

- volume: 17748793.00
- volume_MA20: 21218094.65
- volume_ratio: 0.84

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

- 데이터 기준일(주가): **2026-05-21**
- 실행시간(UTC): **2026-05-22 03:00:50**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -4.0 bp / latest 2.8
- IG OAS 4주 변화: -4.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.13
- VIX: 17.44
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -5.50% / slope_proxy: -0.005797
- GDXJ/GLD gap: -5.28% / slope_proxy: -0.004269

## VZLA (Vizsla Silver)
- close: 3.38 | RSI14: 46.179147 | ATR14%: 6.35%
- MA20 gap: -3.03% | MA50 gap: -0.45% | MA200 gap: -20.13%
- vol_ratio(Volume/Vol20): 0.55507 | gap_open: 2.36%
- RS vs SILJ gap: 3.22% / slope_proxy: -0.004701
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
- close: 8.18 | RSI14: 44.028389 | ATR14%: 8.14%
- MA20 gap: -4.96% | MA50 gap: -3.10% | MA200 gap: -0.33%
- vol_ratio(Volume/Vol20): 1.307821 | gap_open: 2.39%
- SilverMarginGate: SI=76.589996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.35% / slope_proxy: -0.017537
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
- close: 33.290001 | RSI14: 41.285188 | ATR14%: 10.37%
- MA20 gap: -11.60% | MA50 gap: -10.70% | MA200 gap: 43.46%
- vol_ratio(Volume/Vol20): 0.962224 | gap_open: 1.34%
- RS vs SILJ gap: -7.29% / slope_proxy: 0.027553
- RS vs GDXJ gap: -4.43% / slope_proxy: 0.007825
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
