# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-14**
- 실행시간(UTC): **2026-04-14 15:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.95 / 4주 변화 -32.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 -12.0 bp
- 10Y Real Yield (DFII10): 1.95 / 4주 변화 3.0 bp
- VIX (VIXCLS): 19.12
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.098327
- MA60: 7.480704
- gap: 21.62%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.299539
- MA60: 0.221017
- gap: 35.53%
- MA60_slope_proxy: 0.009767
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-14**
- 실행시간(UTC): **2026-04-14 15:00:45**

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
- TERM_SPREAD_10Y_POLICY: 100.8 bp / 4주 변화 -0.21 bp
- CURVE_10s5s: 45.89 bp / 4주 변화 -3.89 bp

## NWG Price
- close: 624.4
- MA50: 594.8164 / gap50: 4.97%
- MA200: 575.2066 / gap200: 8.55%

## Relative Strength
- RS vs FTSE gap: 1.05% / slope_proxy: -0.003075
- RS vs Peers gap: -0.92% / slope_proxy: -0.040041

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-14 15:00:52**

## Commodity Regime

- WTI ref (CL=F): 93.57 / 5D -17.16%
- Brent ref (BZ=F): 95.79 / 5D -12.34%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.22
- Gas ref (NG=F): 2.62 / 5D -8.88%

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

- close: 55.29
- MA20 / MA60 / MA200: 61.07 / 52.91 / 45.89
- gap20 / gap60: -9.47% / 4.50%
- 5D return: -12.15%
- 20D high/low: 66.24 / 55.29

### Relative Strength

- ratio: 0.991838
- ratio_MA60: 0.953848
- ratio_gap: 3.98%
- ratio_slope_proxy(20d): 0.038701

### Volume (if available)

- volume: 6080245.00
- volume_MA20: 18951137.25
- volume_ratio: 0.32

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.09
- MA20 / MA60 / MA200: 20.34 / 17.39 / 13.82
- gap20 / gap60: 3.71% / 21.32%
- 5D return: 1.86%
- 20D high/low: 21.97 / 18.80

### Relative Strength

- ratio: 0.504243
- ratio_MA60: 0.461516
- ratio_gap: 9.26%
- ratio_slope_proxy(20d): 0.054769

### Volume (if available)

- volume: 8208688.00
- volume_MA20: 33676294.40
- volume_ratio: 0.24

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

- close: 6.39
- MA20 / MA60 / MA200: 6.58 / 6.00 / 4.25
- gap20 / gap60: -2.84% / 6.62%
- 5D return: -4.27%
- 20D high/low: 6.93 / 6.22

### Relative Strength

- ratio: 0.015661
- ratio_MA60: 0.015705
- ratio_gap: -0.28%
- ratio_slope_proxy(20d): 0.000802

### Volume (if available)

- volume: 6473914.00
- volume_MA20: 33121600.70
- volume_ratio: 0.20

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

- close: 12.49
- MA20 / MA60 / MA200: 15.05 / 11.78 / 11.25
- gap20 / gap60: -16.96% / 6.06%
- 5D return: -21.86%
- 20D high/low: 17.53 / 12.49

### Relative Strength

- ratio: 0.048462
- ratio_MA60: 0.047998
- ratio_gap: 0.97%
- ratio_slope_proxy(20d): 0.005900

### Volume (if available)

- volume: 4690691.00
- volume_MA20: 37358899.55
- volume_ratio: 0.13

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

- 데이터 기준일(주가): **2026-04-14**
- 실행시간(UTC): **2026-04-14 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -32.0 bp / latest 2.95
- IG OAS 4주 변화: -12.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 3.0 bp / latest 1.95
- VIX: 19.12
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 1.97% / slope_proxy: 0.006888
- GDXJ/GLD gap: 2.74% / slope_proxy: -0.004497

## VZLA (Vizsla Silver)
- close: 3.395 | RSI14: 46.821744 | ATR14%: 6.26%
- MA20 gap: 4.60% | MA50 gap: -9.73% | MA200 gap: -18.85%
- vol_ratio(Volume/Vol20): 0.280921 | gap_open: 1.81%
- RS vs SILJ gap: -16.27% / slope_proxy: -0.027547
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 9.05 | RSI14: 53.472373 | ATR14%: 8.48%
- MA20 gap: 13.40% | MA50 gap: -6.98% | MA200 gap: 20.28%
- vol_ratio(Volume/Vol20): 0.604349 | gap_open: 1.63%
- SilverMarginGate: SI=79.195 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.35% / slope_proxy: -0.023563
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 41.759998 | RSI14: 58.377001 | ATR14%: 9.58%
- MA20 gap: 18.22% | MA50 gap: 7.42% | MA200 gap: 125.95%
- vol_ratio(Volume/Vol20): 0.362318 | gap_open: 4.40%
- RS vs SILJ gap: 7.40% / slope_proxy: 0.106738
- RS vs GDXJ gap: 4.71% / slope_proxy: 0.027254
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trigger(Breakout/Retest)=FALSE
