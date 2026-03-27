# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-27**
- 실행시간(UTC): **2026-03-27 15:00:38**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.21 / 4주 변화 23.0 bp
- IG OAS (BAMLC0A0CM): 0.88 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.02 / 4주 변화 25.0 bp
- VIX (VIXCLS): 27.44
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.245302
- MA60: 7.004535
- gap: 17.71%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.252651
- MA60: 0.211039
- gap: 19.72%
- MA60_slope_proxy: -0.006613
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-27**
- 실행시간(UTC): **2026-03-27 15:00:41**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 102.21 bp / 4주 변화 40.77 bp
- CURVE_10s5s: 39.75 bp / 4주 변화 -19.39 bp

## NWG Price
- close: 539.8
- MA50: 607.7725 / gap50: -11.18%
- MA200: 571.1814 / gap200: -5.49%

## Relative Strength
- RS vs FTSE gap: -8.85% / slope_proxy: -0.003249
- RS vs Peers gap: -4.85% / slope_proxy: -0.04858

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-27 15:00:47**

## Commodity Regime

- WTI ref (CL=F): 98.06 / 5D -0.26%
- Brent ref (BZ=F): 103.93 / 5D -7.36%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.87
- Gas ref (NG=F): 3.02 / 5D -2.52%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 65.57
- MA20 / MA60 / MA200: 57.72 / 49.46 / 44.95
- gap20 / gap60: 13.60% / 32.56%
- 5D return: 8.01%
- 20D high/low: 65.57 / 52.99

### Relative Strength

- ratio: 1.048285
- ratio_MA60: 0.926108
- ratio_gap: 13.19%
- ratio_slope_proxy(20d): 0.027427

### Volume (if available)

- volume: 6504055.00
- volume_MA20: 21442472.75
- volume_ratio: 0.30

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.66
- MA20 / MA60 / MA200: 18.75 / 15.77 / 13.35
- gap20 / gap60: 10.21% / 31.05%
- 5D return: 9.89%
- 20D high/low: 20.66 / 16.73

### Relative Strength

- ratio: 0.559740
- ratio_MA60: 0.431463
- ratio_gap: 29.73%
- ratio_slope_proxy(20d): 0.043675

### Volume (if available)

- volume: 7279199.00
- volume_MA20: 37072504.95
- volume_ratio: 0.20

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

- close: 6.96
- MA20 / MA60 / MA200: 6.37 / 5.57 / 4.05
- gap20 / gap60: 9.11% / 24.77%
- 5D return: 11.82%
- 20D high/low: 6.96 / 5.93

### Relative Strength

- ratio: 0.016752
- ratio_MA60: 0.015246
- ratio_gap: 9.88%
- ratio_slope_proxy(20d): 0.000686

### Volume (if available)

- volume: 10827923.00
- volume_MA20: 37065071.15
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 17.23
- MA20 / MA60 / MA200: 13.66 / 10.45 / 11.39
- gap20 / gap60: 26.10% / 64.76%
- 5D return: 8.95%
- 20D high/low: 17.23 / 11.14

### Relative Strength

- ratio: 0.057847
- ratio_MA60: 0.045166
- ratio_gap: 28.08%
- ratio_slope_proxy(20d): 0.005918

### Volume (if available)

- volume: 8905312.00
- volume_MA20: 37985320.60
- volume_ratio: 0.23

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

- 데이터 기준일(주가): **2026-03-27**
- 실행시간(UTC): **2026-03-27 15:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.21
- IG OAS 4주 변화: 6.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 25.0 bp / latest 2.02
- VIX: 27.44
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -0.23% / slope_proxy: -0.004519
- GDXJ/GLD gap: -8.13% / slope_proxy: -0.000503

## VZLA (Vizsla Silver)
- close: 3.19 | RSI14: 36.154522 | ATR14%: 8.25%
- MA20 gap: -12.45% | MA50 gap: -27.76% | MA200 gap: -23.75%
- vol_ratio(Volume/Vol20): 0.174739 | gap_open: 0.00%
- RS vs SILJ gap: -18.26% / slope_proxy: -0.027233
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.5899 | RSI14: 36.37069 | ATR14%: 11.31%
- MA20 gap: -16.68% | MA50 gap: -30.65% | MA200 gap: 4.95%
- vol_ratio(Volume/Vol20): 0.139226 | gap_open: 0.14%
- SilverMarginGate: SI=69.75 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.20% / slope_proxy: -0.018338
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 33.209999 | RSI14: 43.568746 | ATR14%: 13.41%
- MA20 gap: -14.81% | MA50 gap: -18.12% | MA200 gap: 99.53%
- vol_ratio(Volume/Vol20): 0.185473 | gap_open: 1.51%
- RS vs SILJ gap: 3.19% / slope_proxy: 0.208387
- RS vs GDXJ gap: 2.08% / slope_proxy: 0.054721
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
