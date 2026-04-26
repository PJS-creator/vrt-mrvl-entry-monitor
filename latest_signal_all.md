# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-24**
- 실행시간(UTC): **2026-04-26 03:00:39**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.86 / 4주 변화 -35.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 -16.0 bp
- VIX (VIXCLS): 19.31
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.202275
- MA60: 7.868269
- gap: 16.95%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.324441
- MA60: 0.236083
- gap: 37.43%
- MA60_slope_proxy: 0.025383
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-24**
- 실행시간(UTC): **2026-04-26 03:00:42**

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
- TERM_SPREAD_10Y_POLICY: 108.82 bp / 4주 변화 6.61 bp
- CURVE_10s5s: 46.67 bp / 4주 변화 6.92 bp

## NWG Price
- close: 579.4
- MA50: 587.2298 / gap50: -1.33%
- MA200: 579.7659 / gap200: -0.06%

## Relative Strength
- RS vs FTSE gap: -2.79% / slope_proxy: -0.002507
- RS vs Peers gap: -4.72% / slope_proxy: -0.037548

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-26 03:00:49**

## Commodity Regime

- WTI ref (CL=F): 94.40 / 5D 12.58%
- Brent ref (BZ=F): 105.33 / 5D 16.54%
- Brent Tier: **>=90**
- Brent-WTI spread: 10.93
- Gas ref (NG=F): 2.52 / 5D -5.65%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 57.12
- MA20 / MA60 / MA200: 59.33 / 54.61 / 46.42
- gap20 / gap60: -3.73% / 4.59%
- 5D return: 6.19%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 1.004396
- ratio_MA60: 0.968118
- ratio_gap: 3.75%
- ratio_slope_proxy(20d): 0.038593

### Volume (if available)

- volume: 7835700.00
- volume_MA20: 16854220.00
- volume_ratio: 0.46

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.87
- MA20 / MA60 / MA200: 20.76 / 18.21 / 14.07
- gap20 / gap60: 0.55% / 14.58%
- 5D return: 2.65%
- 20D high/low: 21.84 / 19.86

### Relative Strength

- ratio: 0.522534
- ratio_MA60: 0.475336
- ratio_gap: 9.93%
- ratio_slope_proxy(20d): 0.049520

### Volume (if available)

- volume: 15320700.00
- volume_MA20: 29431055.00
- volume_ratio: 0.52

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.11
- MA20 / MA60 / MA200: 6.39 / 6.18 / 4.38
- gap20 / gap60: -4.36% / -1.14%
- 5D return: 2.86%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.013974
- ratio_MA60: 0.015826
- ratio_gap: -11.70%
- ratio_slope_proxy(20d): 0.000620

### Volume (if available)

- volume: 32674500.00
- volume_MA20: 30117960.00
- volume_ratio: 1.08

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

- close: 11.90
- MA20 / MA60 / MA200: 13.71 / 12.18 / 11.12
- gap20 / gap60: -13.18% / -2.26%
- 5D return: 3.84%
- 20D high/low: 17.53 / 11.45

### Relative Strength

- ratio: 0.046287
- ratio_MA60: 0.048352
- ratio_gap: -4.27%
- ratio_slope_proxy(20d): 0.003546

### Volume (if available)

- volume: 24200400.00
- volume_MA20: 26952470.00
- volume_ratio: 0.90

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

- 데이터 기준일(주가): **2026-04-24**
- 실행시간(UTC): **2026-04-26 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.86
- IG OAS 4주 변화: -8.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -16.0 bp / latest 1.92
- VIX: 19.31
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.64% / slope_proxy: 0.014115
- GDXJ/GLD gap: -0.84% / slope_proxy: -0.004037

## VZLA (Vizsla Silver)
- close: 3.35 | RSI14: 46.080078 | ATR14%: 5.87%
- MA20 gap: 0.59% | MA50 gap: -6.57% | MA200 gap: -20.29%
- vol_ratio(Volume/Vol20): 0.565505 | gap_open: 1.21%
- RS vs SILJ gap: -6.32% / slope_proxy: -0.025634
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
- close: 8.49 | RSI14: 47.309521 | ATR14%: 8.14%
- MA20 gap: 0.88% | MA50 gap: -8.54% | MA200 gap: 9.51%
- vol_ratio(Volume/Vol20): 0.63151 | gap_open: 1.63%
- SilverMarginGate: SI=76.383003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.42% / slope_proxy: -0.029529
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
- close: 38.040001 | RSI14: 48.552426 | ATR14%: 9.71%
- MA20 gap: -0.17% | MA50 gap: -3.58% | MA200 gap: 90.40%
- vol_ratio(Volume/Vol20): 0.606351 | gap_open: 1.48%
- RS vs SILJ gap: 2.54% / slope_proxy: 0.052539
- RS vs GDXJ gap: 1.79% / slope_proxy: 0.010358
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
