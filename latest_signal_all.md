# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-04**
- 실행시간(UTC): **2026-03-04 15:00:34**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.08 / 4주 변화 23.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 1.76 / 4주 변화 -18.0 bp
- VIX (VIXCLS): 23.57
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.679644
- MA60: 6.297862
- gap: 21.94%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.196961
- MA60: 0.214106
- gap: -8.01%
- MA60_slope_proxy: -0.019442
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-04**
- 실행시간(UTC): **2026-03-04 15:00:38**

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
- TERM_SPREAD_10Y_POLICY: 61.8 bp / 4주 변화 -13.74 bp
- CURVE_10s5s: 60.04 bp / 4주 변화 4.49 bp

## NWG Price
- close: 592.0
- MA50: 637.168 / gap50: -7.09%
- MA200: 568.1966 / gap200: 4.19%

## Relative Strength
- RS vs FTSE gap: -10.06% / slope_proxy: -0.001677
- RS vs Peers gap: -6.89% / slope_proxy: -0.056558

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-04 15:00:44**

## Commodity Regime

- WTI ref (CL=F): 74.54 / 5D 13.94%
- Brent ref (BZ=F): 81.64 / 5D 15.23%
- Brent Tier: **80-90**
- Brent-WTI spread: 7.10
- Gas ref (NG=F): 2.95 / 5D -0.74%

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

- close: 52.57
- MA20 / MA60 / MA200: 49.33 / 44.54 / 43.67
- gap20 / gap60: 6.58% / 18.03%
- 5D return: 3.20%
- 20D high/low: 54.21 / 45.09

### Relative Strength

- ratio: 0.948746
- ratio_MA60: 0.903948
- ratio_gap: 4.96%
- ratio_slope_proxy(20d): -0.008803

### Volume (if available)

- volume: 3553925.00
- volume_MA20: 13927031.25
- volume_ratio: 0.26

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.66
- MA20 / MA60 / MA200: 15.86 / 13.75 / 12.68
- gap20 / gap60: 5.04% / 21.20%
- 5D return: -0.30%
- 20D high/low: 17.32 / 14.87

### Relative Strength

- ratio: 0.445812
- ratio_MA60: 0.391118
- ratio_gap: 13.98%
- ratio_slope_proxy(20d): 0.003681

### Volume (if available)

- volume: 3627898.00
- volume_MA20: 22262789.90
- volume_ratio: 0.16

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

- close: 6.20
- MA20 / MA60 / MA200: 6.07 / 4.93 / 3.73
- gap20 / gap60: 2.15% / 25.85%
- 5D return: -3.28%
- 20D high/low: 6.54 / 4.94

### Relative Strength

- ratio: 0.016284
- ratio_MA60: 0.014617
- ratio_gap: 11.41%
- ratio_slope_proxy(20d): 0.000402

### Volume (if available)

- volume: 4156146.00
- volume_MA20: 66278127.30
- volume_ratio: 0.06

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 10.70
- MA20 / MA60 / MA200: 9.81 / 8.31 / 11.27
- gap20 / gap60: 9.04% / 28.77%
- 5D return: 14.93%
- 20D high/low: 11.46 / 8.77

### Relative Strength

- ratio: 0.044303
- ratio_MA60: 0.039937
- ratio_gap: 10.93%
- ratio_slope_proxy(20d): 0.002649

### Volume (if available)

- volume: 5526212.00
- volume_MA20: 12825010.60
- volume_ratio: 0.43

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-04**
- 실행시간(UTC): **2026-03-04 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.08
- IG OAS 4주 변화: 10.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -18.0 bp / latest 1.76
- VIX: 23.57
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 8.40% / slope_proxy: -0.003733
- GDXJ/GLD gap: 2.56% / slope_proxy: 0.014111

## VZLA (Vizsla Silver)
- close: 4.085 | RSI14: 42.393225 | ATR14%: 8.46%
- MA20 gap: 0.37% | MA50 gap: -20.62% | MA200 gap: -1.21%
- vol_ratio(Volume/Vol20): 0.029928 | gap_open: 2.97%
- RS vs SILJ gap: -31.11% / slope_proxy: -0.02686
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.68 | RSI14: 45.216917 | ATR14%: 10.30%
- MA20 gap: -4.66% | MA50 gap: -6.50% | MA200 gap: 59.95%
- vol_ratio(Volume/Vol20): 0.194812 | gap_open: 0.18%
- SilverMarginGate: SI=83.855003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.17% / slope_proxy: 0.017604
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
- close: 47.869999 | RSI14: 57.290051 | ATR14%: 12.05%
- MA20 gap: 14.65% | MA50 gap: 29.08% | MA200 gap: 247.05%
- vol_ratio(Volume/Vol20): 0.159422 | gap_open: 3.71%
- RS vs SILJ gap: 32.80% / slope_proxy: 0.248391
- RS vs GDXJ gap: 33.91% / slope_proxy: 0.065453
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
