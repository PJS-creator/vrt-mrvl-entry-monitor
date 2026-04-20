# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-20**
- 실행시간(UTC): **2026-04-20 15:01:04**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.83 / 4주 변화 -41.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 1.93 / 4주 변화 5.0 bp
- VIX (VIXCLS): 17.48
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.817603
- MA60: 7.668297
- gap: 14.99%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.314426
- MA60: 0.227444
- gap: 38.24%
- MA60_slope_proxy: 0.017043
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-20**
- 실행시간(UTC): **2026-04-20 15:01:12**

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
- TERM_SPREAD_10Y_POLICY: 104.12 bp / 4주 변화 0.16 bp
- CURVE_10s5s: 48.22 bp / 4주 변화 9.47 bp

## NWG Price
- close: 610.2
- MA50: 590.01 / gap50: 3.42%
- MA200: 577.8672 / gap200: 5.60%

## Relative Strength
- RS vs FTSE gap: -0.80% / slope_proxy: -0.00278
- RS vs Peers gap: -3.27% / slope_proxy: -0.038287

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-20 15:01:29**

## Commodity Regime

- WTI ref (CL=F): 87.36 / 5D -11.83%
- Brent ref (BZ=F): 95.70 / 5D -3.68%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.34
- Gas ref (NG=F): 2.69 / 5D 2.40%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 54.71
- MA20 / MA60 / MA200: 60.32 / 53.75 / 46.15
- gap20 / gap60: -9.30% / 1.78%
- 5D return: -5.77%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 0.983993
- ratio_MA60: 0.960551
- ratio_gap: 2.44%
- ratio_slope_proxy(20d): 0.038845

### Volume (if available)

- volume: 3953024.00
- volume_MA20: 18013116.20
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.75
- MA20 / MA60 / MA200: 20.61 / 17.89 / 13.99
- gap20 / gap60: 0.68% / 15.93%
- 5D return: -5.58%
- 20D high/low: 21.97 / 19.27

### Relative Strength

- ratio: 0.503642
- ratio_MA60: 0.469525
- ratio_gap: 7.27%
- ratio_slope_proxy(20d): 0.052134

### Volume (if available)

- volume: 4805304.00
- volume_MA20: 32843045.20
- volume_ratio: 0.15

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.94
- MA20 / MA60 / MA200: 6.51 / 6.10 / 4.32
- gap20 / gap60: -8.82% / -2.67%
- 5D return: -10.54%
- 20D high/low: 6.93 / 5.94

### Relative Strength

- ratio: 0.014703
- ratio_MA60: 0.015811
- ratio_gap: -7.01%
- ratio_slope_proxy(20d): 0.000750

### Volume (if available)

- volume: 6599933.00
- volume_MA20: 31081326.65
- volume_ratio: 0.21

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.40
- MA20 / MA60 / MA200: 14.54 / 11.98 / 11.18
- gap20 / gap60: -21.55% / -4.80%
- 5D return: -10.55%
- 20D high/low: 17.53 / 11.40

### Relative Strength

- ratio: 0.045019
- ratio_MA60: 0.048194
- ratio_gap: -6.59%
- ratio_slope_proxy(20d): 0.004718

### Volume (if available)

- volume: 6962543.00
- volume_MA20: 29864327.15
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-20**
- 실행시간(UTC): **2026-04-20 15:01:40**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -41.0 bp / latest 2.83
- IG OAS 4주 변화: -8.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 5.0 bp / latest 1.93
- VIX: 17.48
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.14% / slope_proxy: 0.010662
- GDXJ/GLD gap: 2.27% / slope_proxy: -0.003684

## VZLA (Vizsla Silver)
- close: 3.455 | RSI14: 49.204839 | ATR14%: 5.67%
- MA20 gap: 5.28% | MA50 gap: -5.30% | MA200 gap: -17.63%
- vol_ratio(Volume/Vol20): 0.451096 | gap_open: 1.99%
- RS vs SILJ gap: -10.82% / slope_proxy: -0.027043
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
- close: 8.8699 | RSI14: 51.190446 | ATR14%: 8.16%
- MA20 gap: 7.95% | MA50 gap: -6.71% | MA200 gap: 16.05%
- vol_ratio(Volume/Vol20): 0.403266 | gap_open: 1.09%
- SilverMarginGate: SI=79.714996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -9.94% / slope_proxy: -0.026216
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
- close: 43.375 | RSI14: 59.715718 | ATR14%: 8.62%
- MA20 gap: 17.75% | MA50 gap: 10.53% | MA200 gap: 125.18%
- vol_ratio(Volume/Vol20): 0.346653 | gap_open: 2.33%
- RS vs SILJ gap: 11.42% / slope_proxy: 0.07846
- RS vs GDXJ gap: 8.99% / slope_proxy: 0.018555
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
