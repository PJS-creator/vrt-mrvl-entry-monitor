# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-07**
- 실행시간(UTC): **2026-04-08 03:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.05 / 4주 변화 -14.0 bp
- IG OAS (BAMLC0A0CM): 0.85 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 1.98 / 4주 변화 20.0 bp
- VIX (VIXCLS): 24.17
- NFCI: -0.4337

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.145962
- MA60: 7.223871
- gap: 12.76%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.273518
- MA60: 0.214634
- gap: 27.43%
- MA60_slope_proxy: 0.002251
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-07**
- 실행시간(UTC): **2026-04-08 03:00:45**

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
- TERM_SPREAD_10Y_POLICY: 103.02 bp / 4주 변화 34.9 bp
- CURVE_10s5s: 43.43 bp / 4주 변화 -14.86 bp

## NWG Price
- close: 569.0
- MA50: 599.3743 / gap50: -5.07%
- MA200: 572.5573 / gap200: -0.62%

## Relative Strength
- RS vs FTSE gap: -6.36% / slope_proxy: -0.003359
- RS vs Peers gap: -4.50% / slope_proxy: -0.043256

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-08 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 96.30 / 5D -6.40%
- Brent ref (BZ=F): 95.25 / 5D -15.54%
- Brent Tier: **>=90**
- Brent-WTI spread: -1.05
- Gas ref (NG=F): 2.75 / 5D -4.78%

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

- close: 62.94
- MA20 / MA60 / MA200: 60.70 / 51.67 / 45.51
- gap20 / gap60: 3.68% / 21.80%
- 5D return: -4.98%
- 20D high/low: 66.24 / 53.12

### Relative Strength

- ratio: 1.046210
- ratio_MA60: 0.945877
- ratio_gap: 10.61%
- ratio_slope_proxy(20d): 0.038125

### Volume (if available)

- volume: 12416188.00
- volume_MA20: 21109939.40
- volume_ratio: 0.59

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.71
- MA20 / MA60 / MA200: 19.76 / 16.66 / 13.60
- gap20 / gap60: 4.79% / 24.34%
- 5D return: -0.48%
- 20D high/low: 20.86 / 17.99

### Relative Strength

- ratio: 0.538482
- ratio_MA60: 0.449637
- ratio_gap: 19.76%
- ratio_slope_proxy(20d): 0.053954

### Volume (if available)

- volume: 13946872.00
- volume_MA20: 36101608.60
- volume_ratio: 0.39

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.68
- MA20 / MA60 / MA200: 6.51 / 5.81 / 4.15
- gap20 / gap60: 2.66% / 14.98%
- 5D return: 0.45%
- 20D high/low: 6.93 / 6.16

### Relative Strength

- ratio: 0.016381
- ratio_MA60: 0.015491
- ratio_gap: 5.75%
- ratio_slope_proxy(20d): 0.000805

### Volume (if available)

- volume: 24865047.00
- volume_MA20: 36445562.35
- volume_ratio: 0.68

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

- close: 15.99
- MA20 / MA60 / MA200: 14.86 / 11.33 / 11.34
- gap20 / gap60: 7.60% / 41.18%
- 5D return: -5.33%
- 20D high/low: 17.53 / 11.38

### Relative Strength

- ratio: 0.056249
- ratio_MA60: 0.047129
- ratio_gap: 19.35%
- ratio_slope_proxy(20d): 0.006495

### Volume (if available)

- volume: 22285963.00
- volume_MA20: 36299603.15
- volume_ratio: 0.61

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

- 데이터 기준일(주가): **2026-04-07**
- 실행시간(UTC): **2026-04-08 03:01:13**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -14.0 bp / latest 3.05
- IG OAS 4주 변화: 0.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: 20.0 bp / latest 1.98
- VIX: 24.17
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 5.07% / slope_proxy: -0.000546
- GDXJ/GLD gap: -2.11% / slope_proxy: -0.00432

## VZLA (Vizsla Silver)
- close: 3.23 | RSI14: 39.337736 | ATR14%: 7.27%
- MA20 gap: -4.61% | MA50 gap: -20.26% | MA200 gap: -22.67%
- vol_ratio(Volume/Vol20): 0.9876 | gap_open: 1.21%
- RS vs SILJ gap: -19.57% / slope_proxy: -0.02747
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
- close: 7.86 | RSI14: 41.861799 | ATR14%: 10.39%
- MA20 gap: -5.74% | MA50 gap: -24.07% | MA200 gap: 6.42%
- vol_ratio(Volume/Vol20): 0.585287 | gap_open: 0.61%
- SilverMarginGate: SI=76.589996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -19.08% / slope_proxy: -0.02205
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
- close: 36.57 | RSI14: 49.859513 | ATR14%: 11.34%
- MA20 gap: 2.09% | MA50 gap: -8.04% | MA200 gap: 107.91%
- vol_ratio(Volume/Vol20): 0.492675 | gap_open: 2.64%
- RS vs SILJ gap: 1.47% / slope_proxy: 0.152045
- RS vs GDXJ gap: -0.65% / slope_proxy: 0.040064
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
