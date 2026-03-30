# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-30**
- 실행시간(UTC): **2026-03-30 15:00:37**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.42 / 4주 변화 32.0 bp
- IG OAS (BAMLC0A0CM): 0.91 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.08 / 4주 변화 34.0 bp
- VIX (VIXCLS): 31.05
- NFCI: -0.475

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.788205
- MA60: 7.039184
- gap: 10.64%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.245185
- MA60: 0.21121
- gap: 16.09%
- MA60_slope_proxy: -0.005441
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-30**
- 실행시간(UTC): **2026-03-30 15:00:41**

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
- TERM_SPREAD_10Y_POLICY: 114.35 bp / 4주 변화 55.85 bp
- CURVE_10s5s: 39.75 bp / 4주 변화 -21.48 bp

## NWG Price
- close: 542.6
- MA50: 605.7096 / gap50: -10.42%
- MA200: 571.3059 / gap200: -5.02%

## Relative Strength
- RS vs FTSE gap: -9.35% / slope_proxy: -0.003322
- RS vs Peers gap: -4.49% / slope_proxy: -0.047603

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-30 15:00:49**

## Commodity Regime

- WTI ref (CL=F): 101.75 / 5D 15.45%
- Brent ref (BZ=F): 107.65 / 5D 7.71%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.90
- Gas ref (NG=F): 2.87 / 5D -0.83%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **False**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 66.82
- MA20 / MA60 / MA200: 58.35 / 49.89 / 45.06
- gap20 / gap60: 14.51% / 33.93%
- 5D return: 10.79%
- 20D high/low: 66.82 / 52.99

### Relative Strength

- ratio: 1.058619
- ratio_MA60: 0.928426
- ratio_gap: 14.02%
- ratio_slope_proxy(20d): 0.029473

### Volume (if available)

- volume: 6488093.00
- volume_MA20: 20821919.65
- volume_ratio: 0.31

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.36
- MA20 / MA60 / MA200: 18.95 / 15.93 / 13.40
- gap20 / gap60: 12.70% / 34.12%
- 5D return: 10.85%
- 20D high/low: 21.36 / 16.73

### Relative Strength

- ratio: 0.574039
- ratio_MA60: 0.434935
- ratio_gap: 31.98%
- ratio_slope_proxy(20d): 0.046069

### Volume (if available)

- volume: 13863097.00
- volume_MA20: 36679234.85
- volume_ratio: 0.38

### Checks

- RISK_OK_SOFT: **False**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.87
- MA20 / MA60 / MA200: 6.40 / 5.62 / 4.07
- gap20 / gap60: 7.20% / 22.17%
- 5D return: 6.27%
- 20D high/low: 6.93 / 5.93

### Relative Strength

- ratio: 0.016470
- ratio_MA60: 0.015277
- ratio_gap: 7.81%
- ratio_slope_proxy(20d): 0.000704

### Volume (if available)

- volume: 12232550.00
- volume_MA20: 36385712.50
- volume_ratio: 0.34

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

- close: 17.00
- MA20 / MA60 / MA200: 13.96 / 10.63 / 11.40
- gap20 / gap60: 21.77% / 59.88%
- 5D return: 7.56%
- 20D high/low: 17.53 / 11.14

### Relative Strength

- ratio: 0.057107
- ratio_MA60: 0.045552
- ratio_gap: 25.37%
- ratio_slope_proxy(20d): 0.006071

### Volume (if available)

- volume: 8362226.00
- volume_MA20: 36997611.30
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

- 데이터 기준일(주가): **2026-03-30**
- 실행시간(UTC): **2026-03-30 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 32.0 bp / latest 3.42
- IG OAS 4주 변화: 6.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 34.0 bp / latest 2.08
- VIX: 31.05
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -1.07% / slope_proxy: -0.004565
- GDXJ/GLD gap: -7.54% / slope_proxy: -0.00158

## VZLA (Vizsla Silver)
- close: 3.155 | RSI14: 35.049196 | ATR14%: 8.15%
- MA20 gap: -11.85% | MA50 gap: -27.61% | MA200 gap: -24.56%
- vol_ratio(Volume/Vol20): 0.178992 | gap_open: 1.90%
- RS vs SILJ gap: -18.38% / slope_proxy: -0.027188
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.66 | RSI14: 37.281622 | ATR14%: 10.98%
- MA20 gap: -13.86% | MA50 gap: -29.55% | MA200 gap: 5.56%
- vol_ratio(Volume/Vol20): 0.240069 | gap_open: 3.75%
- SilverMarginGate: SI=70.919998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.19% / slope_proxy: -0.01924
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 31.889999 | RSI14: 41.867718 | ATR14%: 13.78%
- MA20 gap: -15.60% | MA50 gap: -21.27% | MA200 gap: 90.03%
- vol_ratio(Volume/Vol20): 0.18939 | gap_open: 1.19%
- RS vs SILJ gap: -1.38% / slope_proxy: 0.197349
- RS vs GDXJ gap: -3.68% / slope_proxy: 0.051809
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
