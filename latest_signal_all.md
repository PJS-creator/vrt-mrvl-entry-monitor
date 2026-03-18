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
- 실행시간(UTC): **2026-03-18 15:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.22 / 4주 변화 28.0 bp
- IG OAS (BAMLC0A0CM): 0.92 / 4주 변화 12.0 bp
- 10Y Real Yield (DFII10): 1.87 / 4주 변화 10.0 bp
- VIX (VIXCLS): 22.37
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.365127
- MA60: 6.703554
- gap: 24.79%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.223145
- MA60: 0.210799
- gap: 5.86%
- MA60_slope_proxy: -0.013349
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-18**
- 실행시간(UTC): **2026-03-18 15:00:51**

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
- close: 577.8
- MA50: 622.792 / gap50: -7.22%
- MA200: 570.8963 / gap200: 1.21%

## Relative Strength
- RS vs FTSE gap: -7.95% / slope_proxy: -0.002639
- RS vs Peers gap: -1.81% / slope_proxy: -0.054782

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-18 15:00:57**

## Commodity Regime

- WTI ref (CL=F): 98.48 / 5D 12.87%
- Brent ref (BZ=F): 109.79 / 5D 19.36%
- Brent Tier: **>=90**
- Brent-WTI spread: 11.31
- Gas ref (NG=F): 3.06 / 5D -4.49%

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

- close: 58.24
- MA20 / MA60 / MA200: 54.11 / 46.91 / 44.23
- gap20 / gap60: 7.63% / 24.15%
- 5D return: 4.78%
- 20D high/low: 58.41 / 50.70

### Relative Strength

- ratio: 0.994026
- ratio_MA60: 0.911978
- ratio_gap: 9.00%
- ratio_slope_proxy(20d): 0.014361

### Volume (if available)

- volume: 5826845.00
- volume_MA20: 19847157.25
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.80
- MA20 / MA60 / MA200: 17.54 / 14.83 / 13.05
- gap20 / gap60: 12.92% / 33.54%
- 5D return: 4.27%
- 20D high/low: 19.80 / 15.76

### Relative Strength

- ratio: 0.539393
- ratio_MA60: 0.411957
- ratio_gap: 30.93%
- ratio_slope_proxy(20d): 0.026105

### Volume (if available)

- volume: 7415523.00
- volume_MA20: 31720206.15
- volume_ratio: 0.23

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

- close: 6.42
- MA20 / MA60 / MA200: 6.32 / 5.27 / 3.92
- gap20 / gap60: 1.55% / 21.62%
- 5D return: 1.66%
- 20D high/low: 6.58 / 5.93

### Relative Strength

- ratio: 0.016714
- ratio_MA60: 0.014997
- ratio_gap: 11.45%
- ratio_slope_proxy(20d): 0.000621

### Volume (if available)

- volume: 8437878.00
- volume_MA20: 38964573.90
- volume_ratio: 0.22

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

- close: 13.43
- MA20 / MA60 / MA200: 11.26 / 9.35 / 11.33
- gap20 / gap60: 19.24% / 43.70%
- 5D return: 7.93%
- 20D high/low: 13.43 / 9.30

### Relative Strength

- ratio: 0.053290
- ratio_MA60: 0.042792
- ratio_gap: 24.53%
- ratio_slope_proxy(20d): 0.004449

### Volume (if available)

- volume: 5667499.00
- volume_MA20: 21587044.95
- volume_ratio: 0.26

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
- 실행시간(UTC): **2026-03-18 15:01:04**

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
- 10Y Real Yield 4주 변화: 10.0 bp / latest 1.87
- VIX: 22.37
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -1.63% / slope_proxy: -0.005055
- GDXJ/GLD gap: -9.35% / slope_proxy: 0.008328

## VZLA (Vizsla Silver)
- close: 3.4301 | RSI14: 32.704536 | ATR14%: 8.49%
- MA20 gap: -13.29% | MA50 gap: -28.40% | MA200 gap: -18.17%
- vol_ratio(Volume/Vol20): 0.361853 | gap_open: 3.07%
- RS vs SILJ gap: -23.92% / slope_proxy: -0.027558
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
- close: 8.33 | RSI14: 33.757327 | ATR14%: 11.07%
- MA20 gap: -21.58% | MA50 gap: -26.84% | MA200 gap: 17.88%
- vol_ratio(Volume/Vol20): 0.357819 | gap_open: 1.73%
- SilverMarginGate: SI=76.550003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.85% / slope_proxy: -0.004754
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
- close: 37.41 | RSI14: 44.780601 | ATR14%: 13.46%
- MA20 gap: -14.58% | MA50 gap: -7.21% | MA200 gap: 138.89%
- vol_ratio(Volume/Vol20): 0.40321 | gap_open: 6.33%
- RS vs SILJ gap: 11.62% / slope_proxy: 0.257158
- RS vs GDXJ gap: 10.90% / slope_proxy: 0.067532
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
