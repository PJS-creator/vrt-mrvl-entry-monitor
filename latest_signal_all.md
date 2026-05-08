# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-08**
- 실행시간(UTC): **2026-05-08 15:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.79 / 4주 변화 -11.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 1.94 / 4주 변화 -2.0 bp
- VIX (VIXCLS): 17.08
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.816443
- MA60: 8.379352
- gap: 17.15%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.295549
- MA60: 0.2557
- gap: 15.58%
- MA60_slope_proxy: 0.03775
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-08**
- 실행시간(UTC): **2026-05-08 15:00:49**

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
- TERM_SPREAD_10Y_POLICY: 114.32 bp / 4주 변화 23.33 bp
- CURVE_10s5s: 45.95 bp / 4주 변화 1.81 bp

## NWG Price
- close: 579.8
- MA50: 580.6582 / gap50: -0.15%
- MA200: 583.1801 / gap200: -0.58%

## Relative Strength
- RS vs FTSE gap: 0.72% / slope_proxy: -0.002385
- RS vs Peers gap: -3.32% / slope_proxy: -0.03825

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-08 15:00:57**

## Commodity Regime

- WTI ref (CL=F): 95.20 / 5D -6.61%
- Brent ref (BZ=F): 101.31 / 5D -6.34%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.11
- Gas ref (NG=F): 2.82 / 5D 1.47%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 54.01
- MA20 / MA60 / MA200: 57.07 / 56.66 / 47.14
- gap20 / gap60: -5.35% / -4.66%
- 5D return: -8.00%
- 20D high/low: 60.76 / 53.79

### Relative Strength

- ratio: 0.964726
- ratio_MA60: 0.988301
- ratio_gap: -2.39%
- ratio_slope_proxy(20d): 0.037391

### Volume (if available)

- volume: 2502350.00
- volume_MA20: 12672237.50
- volume_ratio: 0.20

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.55
- MA20 / MA60 / MA200: 21.16 / 19.25 / 14.53
- gap20 / gap60: -2.85% / 6.80%
- 5D return: -6.14%
- 20D high/low: 22.03 / 20.33

### Relative Strength

- ratio: 0.522032
- ratio_MA60: 0.498795
- ratio_gap: 4.66%
- ratio_slope_proxy(20d): 0.044504

### Volume (if available)

- volume: 4451002.00
- volume_MA20: 19871770.10
- volume_ratio: 0.22

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

- close: 6.28
- MA20 / MA60 / MA200: 6.36 / 6.40 / 4.57
- gap20 / gap60: -1.30% / -1.96%
- 5D return: -8.26%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.014842
- ratio_MA60: 0.015906
- ratio_gap: -6.69%
- ratio_slope_proxy(20d): 0.000286

### Volume (if available)

- volume: 4699011.00
- volume_MA20: 34681525.55
- volume_ratio: 0.14

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.64
- MA20 / MA60 / MA200: 12.40 / 12.66 / 10.94
- gap20 / gap60: -6.07% / -7.99%
- 5D return: -8.52%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.047737
- ratio_MA60: 0.048726
- ratio_gap: -2.03%
- ratio_slope_proxy(20d): 0.001031

### Volume (if available)

- volume: 3420697.00
- volume_MA20: 19290604.85
- volume_ratio: 0.18

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-08**
- 실행시간(UTC): **2026-05-08 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.79
- IG OAS 4주 변화: -4.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -2.0 bp / latest 1.94
- VIX: 17.08
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -4.36% / slope_proxy: 0.00806
- GDXJ/GLD gap: 0.83% / slope_proxy: -0.00417

## VZLA (Vizsla Silver)
- close: 3.525 | RSI14: 53.666408 | ATR14%: 5.88%
- MA20 gap: 3.26% | MA50 gap: 0.80% | MA200 gap: -16.29%
- vol_ratio(Volume/Vol20): 0.293367 | gap_open: 1.75%
- RS vs SILJ gap: 0.29% / slope_proxy: -0.015851
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
- close: 9.06 | RSI14: 56.498244 | ATR14%: 7.16%
- MA20 gap: 6.13% | MA50 gap: 3.47% | MA200 gap: 13.72%
- vol_ratio(Volume/Vol20): 0.402245 | gap_open: 1.93%
- SilverMarginGate: SI=81.220001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.25% / slope_proxy: -0.02901
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
- close: 38.689999 | RSI14: 51.398452 | ATR14%: 8.80%
- MA20 gap: -0.57% | MA50 gap: 0.18% | MA200 gap: 78.73%
- vol_ratio(Volume/Vol20): 0.398341 | gap_open: 1.93%
- RS vs SILJ gap: 0.51% / slope_proxy: 0.031904
- RS vs GDXJ gap: 0.95% / slope_proxy: 0.004779
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
