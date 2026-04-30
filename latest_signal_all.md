# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-30**
- 실행시간(UTC): **2026-04-30 15:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.82 / 4주 변화 -34.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -6.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 -8.0 bp
- VIX (VIXCLS): 18.81
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.15139
- MA60: 8.057245
- gap: 13.58%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.323807
- MA60: 0.244231
- gap: 32.58%
- MA60_slope_proxy: 0.032302
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-30**
- 실행시간(UTC): **2026-04-30 15:00:55**

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
- TERM_SPREAD_10Y_POLICY: 119.93 bp / 4주 변화 8.78 bp
- CURVE_10s5s: 46.71 bp / 4주 변화 4.46 bp

## NWG Price
- close: 581.4
- MA50: 585.3368 / gap50: -0.67%
- MA200: 581.4396 / gap200: -0.01%

## Relative Strength
- RS vs FTSE gap: -1.27% / slope_proxy: -0.002374
- RS vs Peers gap: -5.35% / slope_proxy: -0.036505

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-30 15:01:05**

## Commodity Regime

- WTI ref (CL=F): 105.78 / 5D 10.36%
- Brent ref (BZ=F): 110.52 / 5D 5.19%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.74
- Gas ref (NG=F): 2.69 / 5D 2.87%

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

- close: 59.96
- MA20 / MA60 / MA200: 58.22 / 55.57 / 46.71
- gap20 / gap60: 2.98% / 7.90%
- 5D return: 3.68%
- 20D high/low: 62.97 / 53.79

### Relative Strength

- ratio: 1.010959
- ratio_MA60: 0.976767
- ratio_gap: 3.50%
- ratio_slope_proxy(20d): 0.037684

### Volume (if available)

- volume: 3514787.00
- volume_MA20: 13408699.35
- volume_ratio: 0.26

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.88
- MA20 / MA60 / MA200: 20.95 / 18.63 / 14.25
- gap20 / gap60: 4.39% / 17.40%
- 5D return: 3.45%
- 20D high/low: 21.88 / 19.86

### Relative Strength

- ratio: 0.556616
- ratio_MA60: 0.484793
- ratio_gap: 14.82%
- ratio_slope_proxy(20d): 0.046967

### Volume (if available)

- volume: 2975001.00
- volume_MA20: 22992905.05
- volume_ratio: 0.13

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

- close: 6.93
- MA20 / MA60 / MA200: 6.41 / 6.31 / 4.46
- gap20 / gap60: 8.14% / 9.98%
- 5D return: 14.44%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015484
- ratio_MA60: 0.015913
- ratio_gap: -2.69%
- ratio_slope_proxy(20d): 0.000558

### Volume (if available)

- volume: 10647094.00
- volume_MA20: 30396249.70
- volume_ratio: 0.35

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.22
- MA20 / MA60 / MA200: 13.00 / 12.39 / 11.03
- gap20 / gap60: 1.72% / 6.75%
- 5D return: 2.12%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.048295
- ratio_MA60: 0.048506
- ratio_gap: -0.44%
- ratio_slope_proxy(20d): 0.002302

### Volume (if available)

- volume: 6820929.00
- volume_MA20: 23228991.45
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-30**
- 실행시간(UTC): **2026-04-30 15:01:20**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.82
- IG OAS 4주 변화: -6.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.92
- VIX: 18.81
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -2.65% / slope_proxy: 0.014644
- GDXJ/GLD gap: -4.29% / slope_proxy: -0.003873

## VZLA (Vizsla Silver)
- close: 3.455 | RSI14: 50.329186 | ATR14%: 5.67%
- MA20 gap: 2.38% | MA50 gap: -3.06% | MA200 gap: -17.89%
- vol_ratio(Volume/Vol20): 0.200341 | gap_open: 3.24%
- RS vs SILJ gap: 4.42% / slope_proxy: -0.022511
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
- close: 7.885 | RSI14: 42.254626 | ATR14%: 8.08%
- MA20 gap: -6.25% | MA50 gap: -13.87% | MA200 gap: 0.61%
- vol_ratio(Volume/Vol20): 0.242071 | gap_open: 2.85%
- SilverMarginGate: SI=73.684998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.12% / slope_proxy: -0.031395
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
- close: 36.064999 | RSI14: 45.762236 | ATR14%: 9.40%
- MA20 gap: -6.62% | MA50 gap: -8.64% | MA200 gap: 74.88%
- vol_ratio(Volume/Vol20): 0.204034 | gap_open: 5.99%
- RS vs SILJ gap: 2.43% / slope_proxy: 0.03727
- RS vs GDXJ gap: 2.33% / slope_proxy: 0.005751
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
