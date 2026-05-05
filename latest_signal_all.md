# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-05**
- 실행시간(UTC): **2026-05-05 15:01:13**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.78 / 4주 변화 -27.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.91 / 4주 변화 -8.0 bp
- VIX (VIXCLS): 18.29
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.574871
- MA60: 8.227415
- gap: 16.38%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.318394
- MA60: 0.250559
- gap: 27.07%
- MA60_slope_proxy: 0.036032
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-05**
- 실행시간(UTC): **2026-05-05 15:01:15**

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
- TERM_SPREAD_10Y_POLICY: 121.09 bp / 4주 변화 18.29 bp
- CURVE_10s5s: 46.73 bp / 4주 변화 4.4 bp

## NWG Price
- close: 544.6
- MA50: 582.6827 / gap50: -6.54%
- MA200: 582.049 / gap200: -6.43%

## Relative Strength
- RS vs FTSE gap: -5.18% / slope_proxy: -0.002465
- RS vs Peers gap: -5.85% / slope_proxy: -0.0388

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-05 15:01:26**

## Commodity Regime

- WTI ref (CL=F): 102.22 / 5D 2.29%
- Brent ref (BZ=F): 111.14 / 5D -0.11%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.92
- Gas ref (NG=F): 2.79 / 5D 8.91%

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

- close: 59.36
- MA20 / MA60 / MA200: 57.73 / 56.26 / 46.97
- gap20 / gap60: 2.83% / 5.50%
- 5D return: 1.28%
- 20D high/low: 60.76 / 53.79

### Relative Strength

- ratio: 1.002872
- ratio_MA60: 0.983404
- ratio_gap: 1.98%
- ratio_slope_proxy(20d): 0.037528

### Volume (if available)

- volume: 2618923.00
- volume_MA20: 12849891.15
- volume_ratio: 0.20

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.80
- MA20 / MA60 / MA200: 21.16 / 18.99 / 14.40
- gap20 / gap60: 3.00% / 14.80%
- 5D return: 2.66%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.550032
- ratio_MA60: 0.492553
- ratio_gap: 11.67%
- ratio_slope_proxy(20d): 0.045537

### Volume (if available)

- volume: 3658419.00
- volume_MA20: 21806075.95
- volume_ratio: 0.17

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

- close: 6.39
- MA20 / MA60 / MA200: 6.42 / 6.38 / 4.52
- gap20 / gap60: -0.39% / 0.27%
- 5D return: -5.82%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.014547
- ratio_MA60: 0.015941
- ratio_gap: -8.75%
- ratio_slope_proxy(20d): 0.000451

### Volume (if available)

- volume: 26369093.00
- volume_MA20: 31951094.65
- volume_ratio: 0.83

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

- close: 13.05
- MA20 / MA60 / MA200: 12.65 / 12.57 / 10.99
- gap20 / gap60: 3.18% / 3.87%
- 5D return: 7.36%
- 20D high/low: 14.44 / 11.45

### Relative Strength

- ratio: 0.048551
- ratio_MA60: 0.048679
- ratio_gap: -0.26%
- ratio_slope_proxy(20d): 0.001551

### Volume (if available)

- volume: 4669209.00
- volume_MA20: 22153075.45
- volume_ratio: 0.21

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-05**
- 실행시간(UTC): **2026-05-05 15:01:36**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -27.0 bp / latest 2.78
- IG OAS 4주 변화: -5.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.91
- VIX: 18.29
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -4.26% / slope_proxy: 0.011571
- GDXJ/GLD gap: -5.17% / slope_proxy: -0.003816

## VZLA (Vizsla Silver)
- close: 3.315 | RSI14: 44.955647 | ATR14%: 5.94%
- MA20 gap: -2.16% | MA50 gap: -6.12% | MA200 gap: -21.24%
- vol_ratio(Volume/Vol20): 0.252217 | gap_open: 1.49%
- RS vs SILJ gap: 2.75% / slope_proxy: -0.019561
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
- close: 8.09 | RSI14: 45.674515 | ATR14%: 7.48%
- MA20 gap: -3.96% | MA50 gap: -9.74% | MA200 gap: 2.44%
- vol_ratio(Volume/Vol20): 0.231127 | gap_open: 1.90%
- SilverMarginGate: SI=74.114998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.21% / slope_proxy: -0.031064
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
- close: 36.060001 | RSI14: 46.156697 | ATR14%: 8.80%
- MA20 gap: -6.95% | MA50 gap: -8.00% | MA200 gap: 70.71%
- vol_ratio(Volume/Vol20): 0.153098 | gap_open: 1.91%
- RS vs SILJ gap: 3.05% / slope_proxy: 0.03345
- RS vs GDXJ gap: 3.64% / slope_proxy: 0.004659
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
