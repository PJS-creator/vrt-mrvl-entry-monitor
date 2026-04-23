# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-22**
- 실행시간(UTC): **2026-04-23 03:00:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.85 / 4주 변화 -34.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 -14.0 bp
- VIX (VIXCLS): 19.5
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.723271
- MA60: 7.768644
- gap: 12.29%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.329929
- MA60: 0.231685
- gap: 42.40%
- MA60_slope_proxy: 0.02152
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-22**
- 실행시간(UTC): **2026-04-23 03:00:44**

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
- TERM_SPREAD_10Y_POLICY: 103.29 bp / 4주 변화 -8.74 bp
- CURVE_10s5s: 49.84 bp / 4주 변화 8.07 bp

## NWG Price
- close: 592.4
- MA50: 588.2521 / gap50: 0.71%
- MA200: 578.9311 / gap200: 2.33%

## Relative Strength
- RS vs FTSE gap: -2.05% / slope_proxy: -0.002599
- RS vs Peers gap: -4.75% / slope_proxy: -0.038429

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-23 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 94.32 / 5D 3.32%
- Brent ref (BZ=F): 103.26 / 5D 8.77%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.94
- Gas ref (NG=F): 2.72 / 5D 4.18%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 57.05
- MA20 / MA60 / MA200: 59.90 / 54.18 / 46.29
- gap20 / gap60: -4.75% / 5.30%
- 5D return: 2.19%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 1.009020
- ratio_MA60: 0.964393
- ratio_gap: 4.63%
- ratio_slope_proxy(20d): 0.039149

### Volume (if available)

- volume: 9382486.00
- volume_MA20: 17704369.30
- volume_ratio: 0.53

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.18
- MA20 / MA60 / MA200: 20.77 / 18.12 / 14.07
- gap20 / gap60: 1.97% / 16.87%
- 5D return: 3.12%
- 20D high/low: 21.97 / 19.82

### Relative Strength

- ratio: 0.521803
- ratio_MA60: 0.473815
- ratio_gap: 10.13%
- ratio_slope_proxy(20d): 0.051253

### Volume (if available)

- volume: 16439279.00
- volume_MA20: 30884658.95
- volume_ratio: 0.53

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

- close: 6.06
- MA20 / MA60 / MA200: 6.46 / 6.14 / 4.35
- gap20 / gap60: -6.24% / -1.32%
- 5D return: -1.46%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.014505
- ratio_MA60: 0.015827
- ratio_gap: -8.35%
- ratio_slope_proxy(20d): 0.000697

### Volume (if available)

- volume: 22532616.00
- volume_MA20: 30486555.80
- volume_ratio: 0.74

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

- close: 12.34
- MA20 / MA60 / MA200: 14.14 / 12.07 / 11.15
- gap20 / gap60: -12.74% / 2.26%
- 5D return: 1.31%
- 20D high/low: 17.53 / 11.45

### Relative Strength

- ratio: 0.047926
- ratio_MA60: 0.048227
- ratio_gap: -0.62%
- ratio_slope_proxy(20d): 0.004141

### Volume (if available)

- volume: 17745051.00
- volume_MA20: 27286817.55
- volume_ratio: 0.65

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-22**
- 실행시간(UTC): **2026-04-23 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.85
- IG OAS 4주 변화: -7.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -14.0 bp / latest 1.92
- VIX: 19.5
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.37% / slope_proxy: 0.012332
- GDXJ/GLD gap: 0.02% / slope_proxy: -0.003966

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 49.731008 | ATR14%: 5.75%
- MA20 gap: 4.44% | MA50 gap: -4.21% | MA200 gap: -17.59%
- vol_ratio(Volume/Vol20): 0.720422 | gap_open: 2.40%
- RS vs SILJ gap: -6.92% / slope_proxy: -0.026268
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 9.02 | RSI14: 52.524939 | ATR14%: 7.94%
- MA20 gap: 8.30% | MA50 gap: -4.06% | MA200 gap: 17.16%
- vol_ratio(Volume/Vol20): 0.8001 | gap_open: 4.00%
- SilverMarginGate: SI=76.224998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.91% / slope_proxy: -0.028476
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
- close: 40.544998 | RSI14: 53.280021 | ATR14%: 9.25%
- MA20 gap: 7.85% | MA50 gap: 2.94% | MA200 gap: 106.51%
- vol_ratio(Volume/Vol20): 0.655582 | gap_open: 4.34%
- RS vs SILJ gap: 6.73% / slope_proxy: 0.06871
- RS vs GDXJ gap: 6.21% / slope_proxy: 0.015134
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
