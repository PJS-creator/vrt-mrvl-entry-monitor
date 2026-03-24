# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-24**
- 실행시간(UTC): **2026-03-24 15:00:40**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.19 / 4주 변화 24.0 bp
- IG OAS (BAMLC0A0CM): 0.88 / 4주 변화 8.0 bp
- 10Y Real Yield (DFII10): 2.01 / 4주 변화 21.0 bp
- VIX (VIXCLS): 26.15
- NFCI: -0.4857

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.376437
- MA60: 6.866118
- gap: 22.00%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.23502
- MA60: 0.210286
- gap: 11.76%
- MA60_slope_proxy: -0.01041
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-24**
- 실행시간(UTC): **2026-03-24 15:00:50**

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
- TERM_SPREAD_10Y_POLICY: 117.67 bp / 4주 변화 55.35 bp
- CURVE_10s5s: 38.39 bp / 4주 변화 -20.27 bp

## NWG Price
- close: 527.2
- MA50: 613.7053 / gap50: -14.10%
- MA200: 570.825 / gap200: -7.64%

## Relative Strength
- RS vs FTSE gap: -11.53% / slope_proxy: -0.003069
- RS vs Peers gap: -6.33% / slope_proxy: -0.052746

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-24 15:00:57**

## Commodity Regime

- WTI ref (CL=F): 91.96 / 5D -4.42%
- Brent ref (BZ=F): 103.42 / 5D 0.00%
- Brent Tier: **>=90**
- Brent-WTI spread: 11.46
- Gas ref (NG=F): 2.90 / 5D -4.35%

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

- close: 61.44
- MA20 / MA60 / MA200: 55.88 / 48.29 / 44.62
- gap20 / gap60: 9.95% / 27.22%
- 5D return: 6.42%
- 20D high/low: 61.44 / 50.70

### Relative Strength

- ratio: 1.006224
- ratio_MA60: 0.925235
- ratio_gap: 8.75%
- ratio_slope_proxy(20d): 0.021025

### Volume (if available)

- volume: 5953180.00
- volume_MA20: 20603724.00
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.85
- MA20 / MA60 / MA200: 18.21 / 15.34 / 13.22
- gap20 / gap60: 8.99% / 29.40%
- 5D return: 1.72%
- 20D high/low: 19.85 / 16.61

### Relative Strength

- ratio: 0.541772
- ratio_MA60: 0.422615
- ratio_gap: 28.20%
- ratio_slope_proxy(20d): 0.036655

### Volume (if available)

- volume: 8795140.00
- volume_MA20: 35629082.00
- volume_ratio: 0.25

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

- close: 6.62
- MA20 / MA60 / MA200: 6.31 / 5.43 / 3.99
- gap20 / gap60: 4.97% / 21.82%
- 5D return: 0.61%
- 20D high/low: 6.62 / 5.93

### Relative Strength

- ratio: 0.016226
- ratio_MA60: 0.015129
- ratio_gap: 7.25%
- ratio_slope_proxy(20d): 0.000614

### Volume (if available)

- volume: 10268185.00
- volume_MA20: 36539564.25
- volume_ratio: 0.28

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

- close: 17.20
- MA20 / MA60 / MA200: 12.57 / 9.97 / 11.38
- gap20 / gap60: 36.80% / 72.55%
- 5D return: 32.61%
- 20D high/low: 17.20 / 9.30

### Relative Strength

- ratio: 0.058797
- ratio_MA60: 0.044127
- ratio_gap: 33.25%
- ratio_slope_proxy(20d): 0.005228

### Volume (if available)

- volume: 18276093.00
- volume_MA20: 34495614.65
- volume_ratio: 0.53

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

- 데이터 기준일(주가): **2026-03-24**
- 실행시간(UTC): **2026-03-24 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 24.0 bp / latest 3.19
- IG OAS 4주 변화: 8.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.01
- VIX: 26.15
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: 0.11% / slope_proxy: -0.00657
- GDXJ/GLD gap: -8.11% / slope_proxy: 0.002818

## VZLA (Vizsla Silver)
- close: 3.11 | RSI14: 30.413737 | ATR14%: 9.00%
- MA20 gap: -18.02% | MA50 gap: -32.07% | MA200 gap: -25.75%
- vol_ratio(Volume/Vol20): 0.189915 | gap_open: 2.26%
- RS vs SILJ gap: -22.00% / slope_proxy: -0.027451
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
- close: 7.89 | RSI14: 36.036645 | ATR14%: 11.49%
- MA20 gap: -19.64% | MA50 gap: -29.30% | MA200 gap: 10.17%
- vol_ratio(Volume/Vol20): 0.175089 | gap_open: 1.19%
- SilverMarginGate: SI=69.610001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.39% / slope_proxy: -0.012395
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
- close: 33.330002 | RSI14: 42.331063 | ATR14%: 14.14%
- MA20 gap: -19.67% | MA50 gap: -17.92% | MA200 gap: 105.55%
- vol_ratio(Volume/Vol20): 0.177511 | gap_open: 2.77%
- RS vs SILJ gap: 6.04% / slope_proxy: 0.231871
- RS vs GDXJ gap: 5.91% / slope_proxy: 0.06093
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
