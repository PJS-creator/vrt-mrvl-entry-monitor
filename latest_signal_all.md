# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-19**
- 실행시간(UTC): **2026-03-20 03:00:36**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.2 / 4주 변화 34.0 bp
- IG OAS (BAMLC0A0CM): 0.91 / 4주 변화 13.0 bp
- 10Y Real Yield (DFII10): 1.86 / 4주 변화 6.0 bp
- VIX (VIXCLS): 25.09
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.387972
- MA60: 6.745983
- gap: 24.34%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.226704
- MA60: 0.210624
- gap: 7.63%
- MA60_slope_proxy: -0.012817
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-19**
- 실행시간(UTC): **2026-03-20 03:00:40**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 90.36 bp / 4주 변화 26.11 bp
- CURVE_10s5s: 50.54 bp / 4주 변화 -8.34 bp

## NWG Price
- close: 533.6
- MA50: 620.3821 / gap50: -13.99%
- MA200: 570.7095 / gap200: -6.50%

## Relative Strength
- RS vs FTSE gap: -12.71% / slope_proxy: -0.002791
- RS vs Peers gap: -6.04% / slope_proxy: -0.054858

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-20 03:00:47**

## Commodity Regime

- WTI ref (CL=F): 93.55 / 5D -2.28%
- Brent ref (BZ=F): 102.11 / 5D 1.64%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.56
- Gas ref (NG=F): 3.13 / 5D -3.12%

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

- close: 59.58
- MA20 / MA60 / MA200: 54.53 / 47.24 / 44.33
- gap20 / gap60: 9.27% / 26.11%
- 5D return: 2.00%
- 20D high/low: 59.58 / 50.70

### Relative Strength

- ratio: 1.003706
- ratio_MA60: 0.913772
- ratio_gap: 9.84%
- ratio_slope_proxy(20d): 0.016092

### Volume (if available)

- volume: 22364798.00
- volume_MA20: 19710994.90
- volume_ratio: 1.13

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.78
- MA20 / MA60 / MA200: 17.74 / 14.96 / 13.09
- gap20 / gap60: 11.53% / 32.21%
- 5D return: 4.27%
- 20D high/low: 19.78 / 15.79

### Relative Strength

- ratio: 0.541918
- ratio_MA60: 0.414783
- ratio_gap: 30.65%
- ratio_slope_proxy(20d): 0.029038

### Volume (if available)

- volume: 39872321.00
- volume_MA20: 33773936.05
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

- close: 6.46
- MA20 / MA60 / MA200: 6.31 / 5.31 / 3.93
- gap20 / gap60: 2.31% / 21.58%
- 5D return: 2.87%
- 20D high/low: 6.58 / 5.93

### Relative Strength

- ratio: 0.016454
- ratio_MA60: 0.015029
- ratio_gap: 9.48%
- ratio_slope_proxy(20d): 0.000619

### Volume (if available)

- volume: 34746566.00
- volume_MA20: 38862353.30
- volume_ratio: 0.89

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

- close: 14.29
- MA20 / MA60 / MA200: 11.55 / 9.50 / 11.35
- gap20 / gap60: 23.68% / 50.39%
- 5D return: 12.06%
- 20D high/low: 14.85 / 9.30

### Relative Strength

- ratio: 0.050697
- ratio_MA60: 0.043120
- ratio_gap: 17.57%
- ratio_slope_proxy(20d): 0.004621

### Volume (if available)

- volume: 98806243.00
- volume_MA20: 28425302.15
- volume_ratio: 3.48

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

- 데이터 기준일(주가): **2026-03-19**
- 실행시간(UTC): **2026-03-20 03:00:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 34.0 bp / latest 3.2
- IG OAS 4주 변화: 13.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.86
- VIX: 25.09
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -4.72% / slope_proxy: -0.006292
- GDXJ/GLD gap: -13.08% / slope_proxy: 0.006752

## VZLA (Vizsla Silver)
- close: 3.22 | RSI14: 29.615204 | ATR14%: 9.28%
- MA20 gap: -17.79% | MA50 gap: -32.00% | MA200 gap: -23.19%
- vol_ratio(Volume/Vol20): 1.425533 | gap_open: 8.63%
- RS vs SILJ gap: -20.87% / slope_proxy: -0.027522
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.57 | RSI14: 30.328072 | ATR14%: 12.37%
- MA20 gap: -27.67% | MA50 gap: -33.12% | MA200 gap: 6.76%
- vol_ratio(Volume/Vol20): 1.023969 | gap_open: 9.59%
- SilverMarginGate: SI=74.135002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.79% / slope_proxy: -0.006279
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
- close: 31.76 | RSI14: 38.724074 | ATR14%: 16.26%
- MA20 gap: -26.51% | MA50 gap: -21.30% | MA200 gap: 101.07%
- vol_ratio(Volume/Vol20): 1.617467 | gap_open: 8.47%
- RS vs SILJ gap: 3.25% / slope_proxy: 0.254046
- RS vs GDXJ gap: 2.45% / slope_proxy: 0.066679
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
