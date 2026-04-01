# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-01**
- 실행시간(UTC): **2026-04-01 15:00:40**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.28 / 4주 변화 20.0 bp
- IG OAS (BAMLC0A0CM): 0.9 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.04 / 4주 변화 28.0 bp
- VIX (VIXCLS): 25.25
- NFCI: -0.4337

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.324065
- MA60: 7.109741
- gap: 17.08%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.267228
- MA60: 0.211952
- gap: 26.08%
- MA60_slope_proxy: -0.002133
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-01**
- 실행시간(UTC): **2026-04-01 15:00:50**

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
- TERM_SPREAD_10Y_POLICY: 113.06 bp / 4주 변화 51.26 bp
- CURVE_10s5s: 41.81 bp / 4주 변화 -18.23 bp

## NWG Price
- close: 583.0
- MA50: 602.472 / gap50: -3.23%
- MA200: 571.8359 / gap200: 1.95%

## Relative Strength
- RS vs FTSE gap: -4.52% / slope_proxy: -0.003343
- RS vs Peers gap: -3.07% / slope_proxy: -0.045145

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-01 15:00:58**

## Commodity Regime

- WTI ref (CL=F): 99.01 / 5D 9.62%
- Brent ref (BZ=F): 101.29 / 5D -0.91%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.28
- Gas ref (NG=F): 2.83 / 5D -4.17%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 62.24
- MA20 / MA60 / MA200: 59.34 / 50.61 / 45.24
- gap20 / gap60: 4.88% / 22.97%
- 5D return: 0.63%
- 20D high/low: 66.24 / 52.99

### Relative Strength

- ratio: 1.052762
- ratio_MA60: 0.939042
- ratio_gap: 12.11%
- ratio_slope_proxy(20d): 0.033398

### Volume (if available)

- volume: 11860160.00
- volume_MA20: 22021523.00
- volume_ratio: 0.54

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.00
- MA20 / MA60 / MA200: 19.28 / 16.20 / 13.48
- gap20 / gap60: 3.78% / 23.48%
- 5D return: 0.93%
- 20D high/low: 20.81 / 16.73

### Relative Strength

- ratio: 0.517259
- ratio_MA60: 0.440293
- ratio_gap: 17.48%
- ratio_slope_proxy(20d): 0.049150

### Volume (if available)

- volume: 19776191.00
- volume_MA20: 38672804.55
- volume_ratio: 0.51

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

- close: 6.55
- MA20 / MA60 / MA200: 6.43 / 5.69 / 4.10
- gap20 / gap60: 1.90% / 15.05%
- 5D return: -3.25%
- 20D high/low: 6.93 / 5.93

### Relative Strength

- ratio: 0.016410
- ratio_MA60: 0.015356
- ratio_gap: 6.86%
- ratio_slope_proxy(20d): 0.000733

### Volume (if available)

- volume: 11313641.00
- volume_MA20: 36374597.05
- volume_ratio: 0.31

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

- close: 14.76
- MA20 / MA60 / MA200: 14.35 / 10.91 / 11.38
- gap20 / gap60: 2.84% / 35.30%
- 5D return: -11.70%
- 20D high/low: 17.53 / 11.38

### Relative Strength

- ratio: 0.053547
- ratio_MA60: 0.046209
- ratio_gap: 15.88%
- ratio_slope_proxy(20d): 0.006319

### Volume (if available)

- volume: 15095188.00
- volume_MA20: 36281584.40
- volume_ratio: 0.42

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-01**
- 실행시간(UTC): **2026-04-01 15:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.28
- IG OAS 4주 변화: 6.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.04
- VIX: 25.25
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 3.87% / slope_proxy: -0.003685
- GDXJ/GLD gap: -1.30% / slope_proxy: -0.002768

## VZLA (Vizsla Silver)
- close: 3.37 | RSI14: 42.604907 | ATR14%: 7.33%
- MA20 gap: -3.76% | MA50 gap: -20.46% | MA200 gap: -19.39%
- vol_ratio(Volume/Vol20): 0.294 | gap_open: 3.03%
- RS vs SILJ gap: -20.12% / slope_proxy: -0.027347
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
- close: 8.59 | RSI14: 46.022252 | ATR14%: 9.91%
- MA20 gap: -0.97% | MA50 gap: -19.97% | MA200 gap: 17.45%
- vol_ratio(Volume/Vol20): 0.414574 | gap_open: 3.62%
- SilverMarginGate: SI=75.410004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.18% / slope_proxy: -0.02002
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
- close: 36.02 | RSI14: 48.801555 | ATR14%: 12.02%
- MA20 gap: -1.22% | MA50 gap: -10.73% | MA200 gap: 110.67%
- vol_ratio(Volume/Vol20): 0.237223 | gap_open: 3.41%
- RS vs SILJ gap: -0.73% / slope_proxy: 0.176026
- RS vs GDXJ gap: -3.29% / slope_proxy: 0.046181
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
