# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-15**
- 실행시간(UTC): **2026-04-15 15:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.84 / 4주 변화 -38.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -11.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 5.0 bp
- VIX (VIXCLS): 18.36
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.916631
- MA60: 7.532964
- gap: 18.37%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.303009
- MA60: 0.222662
- gap: 36.09%
- MA60_slope_proxy: 0.011623
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-15**
- 실행시간(UTC): **2026-04-15 15:00:50**

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
- TERM_SPREAD_10Y_POLICY: 106.27 bp / 4주 변화 10.51 bp
- CURVE_10s5s: 45.05 bp / 4주 변화 -4.47 bp

## NWG Price
- close: 624.8
- MA50: 593.7058 / gap50: 5.24%
- MA200: 575.8421 / gap200: 8.50%

## Relative Strength
- RS vs FTSE gap: 1.35% / slope_proxy: -0.002981
- RS vs Peers gap: -0.74% / slope_proxy: -0.039229

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-15 15:00:56**

## Commodity Regime

- WTI ref (CL=F): 92.17 / 5D -2.37%
- Brent ref (BZ=F): 95.08 / 5D 0.35%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.91
- Gas ref (NG=F): 2.62 / 5D -3.93%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 56.10
- MA20 / MA60 / MA200: 61.00 / 53.14 / 45.96
- gap20 / gap60: -8.02% / 5.58%
- 5D return: -6.13%
- 20D high/low: 66.24 / 55.38

### Relative Strength

- ratio: 1.006007
- ratio_MA60: 0.955632
- ratio_gap: 5.27%
- ratio_slope_proxy(20d): 0.039211

### Volume (if available)

- volume: 3459327.00
- volume_MA20: 18983601.35
- volume_ratio: 0.18

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.87
- MA20 / MA60 / MA200: 20.40 / 17.52 / 13.86
- gap20 / gap60: 2.26% / 19.08%
- 5D return: 4.43%
- 20D high/low: 21.97 / 18.80

### Relative Strength

- ratio: 0.501888
- ratio_MA60: 0.463492
- ratio_gap: 8.28%
- ratio_slope_proxy(20d): 0.054236

### Volume (if available)

- volume: 3975869.00
- volume_MA20: 33614398.45
- volume_ratio: 0.12

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.17
- MA20 / MA60 / MA200: 6.55 / 6.03 / 4.26
- gap20 / gap60: -5.74% / 2.47%
- 5D return: -7.84%
- 20D high/low: 6.93 / 6.17

### Relative Strength

- ratio: 0.015235
- ratio_MA60: 0.015737
- ratio_gap: -3.19%
- ratio_slope_proxy(20d): 0.000783

### Volume (if available)

- volume: 7644820.00
- volume_MA20: 32012511.00
- volume_ratio: 0.24

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.45
- MA20 / MA60 / MA200: 15.02 / 11.84 / 11.23
- gap20 / gap60: -17.12% / 5.13%
- 5D return: -13.78%
- 20D high/low: 17.53 / 12.45

### Relative Strength

- ratio: 0.047846
- ratio_MA60: 0.048080
- ratio_gap: -0.49%
- ratio_slope_proxy(20d): 0.005643

### Volume (if available)

- volume: 3994926.00
- volume_MA20: 37370931.30
- volume_ratio: 0.11

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

- 데이터 기준일(주가): **2026-04-15**
- 실행시간(UTC): **2026-04-15 15:01:25**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -38.0 bp / latest 2.84
- IG OAS 4주 변화: -11.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 5.0 bp / latest 1.92
- VIX: 18.36
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.08% / slope_proxy: 0.007587
- GDXJ/GLD gap: 1.87% / slope_proxy: -0.004501

## VZLA (Vizsla Silver)
- close: 3.455 | RSI14: 49.084953 | ATR14%: 6.05%
- MA20 gap: 6.55% | MA50 gap: -7.39% | MA200 gap: -17.48%
- vol_ratio(Volume/Vol20): 0.376137 | gap_open: 0.29%
- RS vs SILJ gap: -13.29% / slope_proxy: -0.027509
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
- close: 9.125 | RSI14: 54.133479 | ATR14%: 8.26%
- MA20 gap: 14.02% | MA50 gap: -5.76% | MA200 gap: 20.77%
- vol_ratio(Volume/Vol20): 0.400401 | gap_open: 0.44%
- SilverMarginGate: SI=80.214996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.62% / slope_proxy: -0.023819
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
- close: 41.48 | RSI14: 57.796665 | ATR14%: 9.34%
- MA20 gap: 17.24% | MA50 gap: 6.36% | MA200 gap: 122.13%
- vol_ratio(Volume/Vol20): 0.17667 | gap_open: 0.96%
- RS vs SILJ gap: 7.11% / slope_proxy: 0.098099
- RS vs GDXJ gap: 4.37% / slope_proxy: 0.024694
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
