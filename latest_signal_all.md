# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-06**
- 실행시간(UTC): **2026-05-07 03:00:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.77 / 4주 변화 -35.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 0.0 bp
- VIX (VIXCLS): 17.38
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.042529
- MA60: 8.290272
- gap: 21.14%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.313137
- MA60: 0.252478
- gap: 24.03%
- MA60_slope_proxy: 0.037005
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-06**
- 실행시간(UTC): **2026-05-07 03:00:44**

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
- TERM_SPREAD_10Y_POLICY: 117.41 bp / 4주 변화 14.61 bp
- CURVE_10s5s: 45.94 bp / 4주 변화 3.61 bp

## NWG Price
- close: 545.0
- MA50: 582.6907 / gap50: -6.47%
- MA200: 582.051 / gap200: -6.37%

## Relative Strength
- RS vs FTSE gap: -5.46% / slope_proxy: -0.002468
- RS vs Peers gap: -6.51% / slope_proxy: -0.03891

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-07 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 95.67 / 5D -10.49%
- Brent ref (BZ=F): 101.82 / 5D -13.73%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.15
- Gas ref (NG=F): 2.71 / 5D 2.57%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 55.12
- MA20 / MA60 / MA200: 57.49 / 56.41 / 47.03
- gap20 / gap60: -4.13% / -2.28%
- 5D return: -9.28%
- 20D high/low: 60.76 / 53.79

### Relative Strength

- ratio: 0.967018
- ratio_MA60: 0.984919
- ratio_gap: -1.82%
- ratio_slope_proxy(20d): 0.037215

### Volume (if available)

- volume: 20686046.00
- volume_MA20: 12936527.30
- volume_ratio: 1.60

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.91
- MA20 / MA60 / MA200: 21.21 / 19.08 / 14.45
- gap20 / gap60: -1.42% / 9.59%
- 5D return: -4.30%
- 20D high/low: 22.03 / 20.33

### Relative Strength

- ratio: 0.524060
- ratio_MA60: 0.494672
- ratio_gap: 5.94%
- ratio_slope_proxy(20d): 0.045241

### Volume (if available)

- volume: 28509332.00
- volume_MA20: 21155391.60
- volume_ratio: 1.35

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.23
- MA20 / MA60 / MA200: 6.39 / 6.38 / 4.54
- gap20 / gap60: -2.50% / -2.41%
- 5D return: -10.49%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.014402
- ratio_MA60: 0.015921
- ratio_gap: -9.54%
- ratio_slope_proxy(20d): 0.000381

### Volume (if available)

- volume: 46339791.00
- volume_MA20: 34844909.55
- volume_ratio: 1.33

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.00
- MA20 / MA60 / MA200: 12.53 / 12.60 / 10.97
- gap20 / gap60: -4.22% / -4.75%
- 5D return: -8.81%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.045903
- ratio_MA60: 0.048656
- ratio_gap: -5.66%
- ratio_slope_proxy(20d): 0.001274

### Volume (if available)

- volume: 18854217.00
- volume_MA20: 21389265.85
- volume_ratio: 0.88

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

- 데이터 기준일(주가): **2026-05-06**
- 실행시간(UTC): **2026-05-07 03:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.77
- IG OAS 4주 변화: -7.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 0.0 bp / latest 1.96
- VIX: 17.38
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -2.29% / slope_proxy: 0.010603
- GDXJ/GLD gap: -0.69% / slope_proxy: -0.003958

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 51.314031 | ATR14%: 5.92%
- MA20 gap: 2.00% | MA50 gap: -1.72% | MA200 gap: -17.81%
- vol_ratio(Volume/Vol20): 0.856952 | gap_open: 6.04%
- RS vs SILJ gap: -0.08% / slope_proxy: -0.018358
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
- close: 8.74 | RSI14: 53.275803 | ATR14%: 7.37%
- MA20 gap: 3.46% | MA50 gap: -1.69% | MA200 gap: 10.37%
- vol_ratio(Volume/Vol20): 1.292882 | gap_open: 4.50%
- SilverMarginGate: SI=78.415001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.27% / slope_proxy: -0.030699
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

## HYMC (Hycroft Mining)
- close: 39.759998 | RSI14: 53.542679 | ATR14%: 8.40%
- MA20 gap: 2.32% | MA50 gap: 1.85% | MA200 gap: 86.67%
- vol_ratio(Volume/Vol20): 1.025239 | gap_open: 6.70%
- RS vs SILJ gap: 5.53% / slope_proxy: 0.031207
- RS vs GDXJ gap: 6.28% / slope_proxy: 0.004157
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
