# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-09**
- 실행시간(UTC): **2026-03-09 15:00:43**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.13 / 4주 변화 26.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 8.0 bp
- 10Y Real Yield (DFII10): 1.82 / 4주 변화 -7.0 bp
- VIX (VIXCLS): 29.49
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.190693
- MA60: 6.415381
- gap: 27.67%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.228056
- MA60: 0.212269
- gap: 7.44%
- MA60_slope_proxy: -0.017927
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-09**
- 실행시간(UTC): **2026-03-09 15:00:54**

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
- TERM_SPREAD_10Y_POLICY: 74.8 bp / 4주 변화 -4.43 bp
- CURVE_10s5s: 55.53 bp / 4주 변화 -4.12 bp

## NWG Price
- close: 571.4
- MA50: 633.056 / gap50: -9.74%
- MA200: 569.021 / gap200: 0.42%

## Relative Strength
- RS vs FTSE gap: -9.64% / slope_proxy: -0.00206
- RS vs Peers gap: -5.92% / slope_proxy: -0.05904

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-09 15:01:00**

## ⚠️ DATA WARNING

- FRED OVXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VXEWZCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 100.29 / 5D 40.80%
- Brent ref (BZ=F): 102.46 / 5D 31.80%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.17
- Gas ref (NG=F): 3.24 / 5D 9.32%

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

- close: 55.97
- MA20 / MA60 / MA200: 50.64 / 45.20 / 43.87
- gap20 / gap60: 10.53% / 23.83%
- 5D return: 3.26%
- 20D high/low: 55.97 / 45.49

### Relative Strength

- ratio: 0.982018
- ratio_MA60: 0.906226
- ratio_gap: 8.36%
- ratio_slope_proxy(20d): -0.003999

### Volume (if available)

- volume: 11230305.00
- volume_MA20: 15512580.25
- volume_ratio: 0.72

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.42
- MA20 / MA60 / MA200: 16.26 / 14.02 / 12.78
- gap20 / gap60: 13.33% / 31.46%
- 5D return: 6.38%
- 20D high/low: 18.42 / 15.02

### Relative Strength

- ratio: 0.506599
- ratio_MA60: 0.395969
- ratio_gap: 27.94%
- ratio_slope_proxy(20d): 0.008646

### Volume (if available)

- volume: 22254433.00
- volume_MA20: 24659711.65
- volume_ratio: 0.90

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

- close: 6.08
- MA20 / MA60 / MA200: 6.20 / 5.01 / 3.78
- gap20 / gap60: -1.96% / 21.37%
- 5D return: -2.72%
- 20D high/low: 6.54 / 5.44

### Relative Strength

- ratio: 0.016286
- ratio_MA60: 0.014686
- ratio_gap: 10.90%
- ratio_slope_proxy(20d): 0.000462

### Volume (if available)

- volume: 12425777.00
- volume_MA20: 65875343.85
- volume_ratio: 0.19

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

- close: 12.73
- MA20 / MA60 / MA200: 10.27 / 8.61 / 11.31
- gap20 / gap60: 24.02% / 47.93%
- 5D return: 11.91%
- 20D high/low: 12.73 / 8.77

### Relative Strength

- ratio: 0.049476
- ratio_MA60: 0.040682
- ratio_gap: 21.61%
- ratio_slope_proxy(20d): 0.003159

### Volume (if available)

- volume: 8061464.00
- volume_MA20: 16627918.20
- volume_ratio: 0.48

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

- 데이터 기준일(주가): **2026-03-09**
- 실행시간(UTC): **2026-03-09 15:01:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 26.0 bp / latest 3.13
- IG OAS 4주 변화: 8.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -7.0 bp / latest 1.82
- VIX: 29.49
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: -2.64% / slope_proxy: -0.002992
- GDXJ/GLD gap: -4.70% / slope_proxy: 0.013271

## VZLA (Vizsla Silver)
- close: 3.825 | RSI14: 38.330001 | ATR14%: 8.72%
- MA20 gap: -3.82% | MA50 gap: -24.21% | MA200 gap: -8.00%
- vol_ratio(Volume/Vol20): 0.162263 | gap_open: 3.00%
- RS vs SILJ gap: -26.69% / slope_proxy: -0.028911
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
- close: 9.72 | RSI14: 40.547008 | ATR14%: 10.76%
- MA20 gap: -11.44% | MA50 gap: -15.24% | MA200 gap: 42.92%
- vol_ratio(Volume/Vol20): 0.513277 | gap_open: 4.39%
- SilverMarginGate: SI=84.754997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -12.91% / slope_proxy: 0.009961
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
- close: 37.560001 | RSI14: 44.818894 | ATR14%: 15.17%
- MA20 gap: -11.07% | MA50 gap: -1.33% | MA200 gap: 161.97%
- vol_ratio(Volume/Vol20): 0.26776 | gap_open: 2.69%
- RS vs SILJ gap: 11.45% / slope_proxy: 0.245432
- RS vs GDXJ gap: 10.17% / slope_proxy: 0.064453
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
