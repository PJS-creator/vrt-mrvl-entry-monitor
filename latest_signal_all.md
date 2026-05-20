# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-19**
- 실행시간(UTC): **2026-05-20 03:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.83 / 4주 변화 -4.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -6.0 bp
- 10Y Real Yield (DFII10): 2.13 / 4주 변화 22.0 bp
- VIX (VIXCLS): 17.82
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.596372
- MA60: 8.737409
- gap: 9.83%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.32405
- MA60: 0.269496
- gap: 20.24%
- MA60_slope_proxy: 0.039895
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-19**
- 실행시간(UTC): **2026-05-20 03:00:47**

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
- TERM_SPREAD_10Y_POLICY: 137.63 bp / 4주 변화 42.9 bp
- CURVE_10s5s: 47.42 bp / 4주 변화 -2.09 bp

## NWG Price
- close: 567.0
- MA50: 575.5438 / gap50: -1.48%
- MA200: 584.9096 / gap200: -3.06%

## Relative Strength
- RS vs FTSE gap: -1.77% / slope_proxy: -0.002089
- RS vs Peers gap: -4.35% / slope_proxy: -0.035876

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-20 03:00:58**

## Commodity Regime

- WTI ref (CL=F): 104.16 / 5D 1.94%
- Brent ref (BZ=F): 111.24 / 5D 3.22%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.08
- Gas ref (NG=F): 3.10 / 5D 9.00%

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

- close: 60.70
- MA20 / MA60 / MA200: 57.70 / 57.73 / 47.62
- gap20 / gap60: 5.19% / 5.14%
- 5D return: 7.87%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.990374
- ratio_MA60: 0.998577
- ratio_gap: -0.82%
- ratio_slope_proxy(20d): 0.036102

### Volume (if available)

- volume: 12583159.00
- volume_MA20: 12063947.95
- volume_ratio: 1.04

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.41
- MA20 / MA60 / MA200: 20.90 / 19.81 / 14.81
- gap20 / gap60: -2.37% / 3.04%
- 5D return: -0.44%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.568682
- ratio_MA60: 0.515688
- ratio_gap: 10.28%
- ratio_slope_proxy(20d): 0.046791

### Volume (if available)

- volume: 21112629.00
- volume_MA20: 17897706.45
- volume_ratio: 1.18

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

- close: 7.45
- MA20 / MA60 / MA200: 6.64 / 6.48 / 4.71
- gap20 / gap60: 12.22% / 15.01%
- 5D return: 13.91%
- 20D high/low: 7.58 / 6.06

### Relative Strength

- ratio: 0.016518
- ratio_MA60: 0.015831
- ratio_gap: 4.34%
- ratio_slope_proxy(20d): 0.000009

### Volume (if available)

- volume: 37836962.00
- volume_MA20: 38049468.10
- volume_ratio: 0.99

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

- close: 14.78
- MA20 / MA60 / MA200: 12.84 / 13.12 / 10.88
- gap20 / gap60: 15.15% / 12.62%
- 5D return: 11.38%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.059894
- ratio_MA60: 0.050338
- ratio_gap: 18.98%
- ratio_slope_proxy(20d): 0.002040

### Volume (if available)

- volume: 17414834.00
- volume_MA20: 21294866.70
- volume_ratio: 0.82

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-19**
- 실행시간(UTC): **2026-05-20 03:01:23**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -4.0 bp / latest 2.83
- IG OAS 4주 변화: -6.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 22.0 bp / latest 2.13
- VIX: 17.82
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -5.73% / slope_proxy: -0.001975
- GDXJ/GLD gap: -6.10% / slope_proxy: -0.003715

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 41.668807 | ATR14%: 6.83%
- MA20 gap: -6.46% | MA50 gap: -4.80% | MA200 gap: -22.91%
- vol_ratio(Volume/Vol20): 1.259434 | gap_open: 0.00%
- RS vs SILJ gap: 3.56% / slope_proxy: -0.007211
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
- close: 8.23 | RSI14: 44.257204 | ATR14%: 8.33%
- MA20 gap: -4.97% | MA50 gap: -3.48% | MA200 gap: 0.81%
- vol_ratio(Volume/Vol20): 1.252094 | gap_open: 1.17%
- SilverMarginGate: SI=73.644997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.44% / slope_proxy: -0.020498
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
- close: 33.185001 | RSI14: 40.660961 | ATR14%: 11.11%
- MA20 gap: -13.15% | MA50 gap: -11.93% | MA200 gap: 44.89%
- vol_ratio(Volume/Vol20): 1.488131 | gap_open: 3.62%
- RS vs SILJ gap: -4.49% / slope_proxy: 0.028119
- RS vs GDXJ gap: -3.35% / slope_proxy: 0.00729
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
