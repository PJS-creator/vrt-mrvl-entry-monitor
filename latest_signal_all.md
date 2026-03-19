# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-18**
- 실행시간(UTC): **2026-03-19 03:00:36**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.22 / 4주 변화 28.0 bp
- IG OAS (BAMLC0A0CM): 0.92 / 4주 변화 12.0 bp
- 10Y Real Yield (DFII10): 1.83 / 4주 변화 4.0 bp
- VIX (VIXCLS): 22.37
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.218255
- MA60: 6.701106
- gap: 22.64%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.222572
- MA60: 0.21079
- gap: 5.59%
- MA60_slope_proxy: -0.013358
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-18**
- 실행시간(UTC): **2026-03-19 03:00:45**

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
- TERM_SPREAD_10Y_POLICY: 95.76 bp / 4주 변화 29.66 bp
- CURVE_10s5s: 49.52 bp / 4주 변화 -9.72 bp

## NWG Price
- close: 580.0
- MA50: 622.836 / gap50: -6.88%
- MA200: 570.9073 / gap200: 1.59%

## Relative Strength
- RS vs FTSE gap: -7.70% / slope_proxy: -0.002636
- RS vs Peers gap: -1.66% / slope_proxy: -0.054756

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-19 03:00:53**

## Commodity Regime

- WTI ref (CL=F): 96.55 / 5D 10.66%
- Brent ref (BZ=F): 107.01 / 5D 16.34%
- Brent Tier: **>=90**
- Brent-WTI spread: 10.46
- Gas ref (NG=F): 3.24 / 5D 1.06%

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

- close: 58.38
- MA20 / MA60 / MA200: 54.11 / 46.91 / 44.24
- gap20 / gap60: 7.89% / 24.45%
- 5D return: 5.04%
- 20D high/low: 58.41 / 50.70

### Relative Strength

- ratio: 0.999144
- ratio_MA60: 0.912063
- ratio_gap: 9.55%
- ratio_slope_proxy(20d): 0.014446

### Volume (if available)

- volume: 15999502.00
- volume_MA20: 20356680.10
- volume_ratio: 0.79

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.77
- MA20 / MA60 / MA200: 17.53 / 14.83 / 13.05
- gap20 / gap60: 12.75% / 33.33%
- 5D return: 4.11%
- 20D high/low: 19.77 / 15.76

### Relative Strength

- ratio: 0.545229
- ratio_MA60: 0.412055
- ratio_gap: 32.32%
- ratio_slope_proxy(20d): 0.026202

### Volume (if available)

- volume: 27070707.00
- volume_MA20: 32703975.35
- volume_ratio: 0.83

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

- close: 6.25
- MA20 / MA60 / MA200: 6.31 / 5.27 / 3.91
- gap20 / gap60: -0.94% / 18.55%
- 5D return: -0.95%
- 20D high/low: 6.58 / 5.93

### Relative Strength

- ratio: 0.016302
- ratio_MA60: 0.014990
- ratio_gap: 8.75%
- ratio_slope_proxy(20d): 0.000614

### Volume (if available)

- volume: 38858508.00
- volume_MA20: 40487085.40
- volume_ratio: 0.96

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.85
- MA20 / MA60 / MA200: 11.33 / 9.37 / 11.34
- gap20 / gap60: 31.03% / 58.50%
- 5D return: 19.35%
- 20D high/low: 14.85 / 9.30

### Relative Strength

- ratio: 0.055781
- ratio_MA60: 0.042834
- ratio_gap: 30.23%
- ratio_slope_proxy(20d): 0.004491

### Volume (if available)

- volume: 52992111.00
- volume_MA20: 23955215.55
- volume_ratio: 2.21

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

- 데이터 기준일(주가): **2026-03-18**
- 실행시간(UTC): **2026-03-19 03:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 28.0 bp / latest 3.22
- IG OAS 4주 변화: 12.0 bp / latest 0.92
- 10Y Real Yield 4주 변화: 4.0 bp / latest 1.83
- VIX: 22.37
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -2.91% / slope_proxy: -0.00515
- GDXJ/GLD gap: -11.17% / slope_proxy: 0.008237

## VZLA (Vizsla Silver)
- close: 3.36 | RSI14: 31.656454 | ATR14%: 8.66%
- MA20 gap: -14.99% | MA50 gap: -29.84% | MA200 gap: -19.84%
- vol_ratio(Volume/Vol20): 0.935711 | gap_open: 3.07%
- RS vs SILJ gap: -23.29% / slope_proxy: -0.027542
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
- close: 7.82 | RSI14: 31.431267 | ATR14%: 11.99%
- MA20 gap: -26.21% | MA50 gap: -31.26% | MA200 gap: 10.71%
- vol_ratio(Volume/Vol20): 1.233198 | gap_open: 1.73%
- SilverMarginGate: SI=76.305 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -19.61% / slope_proxy: -0.004909
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
- close: 36.240002 | RSI14: 43.45413 | ATR14%: 13.99%
- MA20 gap: -17.14% | MA50 gap: -10.06% | MA200 gap: 131.50%
- vol_ratio(Volume/Vol20): 1.039052 | gap_open: 6.33%
- RS vs SILJ gap: 11.31% / slope_proxy: 0.2571
- RS vs GDXJ gap: 10.43% / slope_proxy: 0.06751
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
