# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-14**
- 실행시간(UTC): **2026-05-15 03:01:14**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.82 / 4주 변화 -3.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 1.99 / 4주 변화 9.0 bp
- VIX (VIXCLS): 17.87
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.879988
- MA60: 8.598941
- gap: 26.53%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.315697
- MA60: 0.263203
- gap: 19.94%
- MA60_slope_proxy: 0.039157
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-14**
- 실행시간(UTC): **2026-05-15 03:01:16**

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
- TERM_SPREAD_10Y_POLICY: 130.27 bp / 4주 변화 31.17 bp
- CURVE_10s5s: 45.52 bp / 4주 변화 -0.22 bp

## NWG Price
- close: 570.4
- MA50: 576.9858 / gap50: -1.14%
- MA200: 584.277 / gap200: -2.38%

## Relative Strength
- RS vs FTSE gap: -1.88% / slope_proxy: -0.002227
- RS vs Peers gap: -5.89% / slope_proxy: -0.036582

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-15 03:01:24**

## Commodity Regime

- WTI ref (CL=F): 102.43 / 5D 8.04%
- Brent ref (BZ=F): 107.05 / 5D 6.99%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.62
- Gas ref (NG=F): 2.93 / 5D 5.85%

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

- close: 56.84
- MA20 / MA60 / MA200: 56.93 / 57.32 / 47.37
- gap20 / gap60: -0.16% / -0.83%
- 5D return: 5.38%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.978819
- ratio_MA60: 0.996165
- ratio_gap: -1.74%
- ratio_slope_proxy(20d): 0.038676

### Volume (if available)

- volume: 8747381.00
- volume_MA20: 12538804.05
- volume_ratio: 0.70

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.78
- MA20 / MA60 / MA200: 20.95 / 19.58 / 14.69
- gap20 / gap60: -5.60% / 1.02%
- 5D return: -2.90%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.532723
- ratio_MA60: 0.507958
- ratio_gap: 4.88%
- ratio_slope_proxy(20d): 0.045009

### Volume (if available)

- volume: 14142629.00
- volume_MA20: 18764951.45
- volume_ratio: 0.75

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.91
- MA20 / MA60 / MA200: 6.43 / 6.43 / 4.64
- gap20 / gap60: 7.47% / 7.45%
- 5D return: 11.99%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015654
- ratio_MA60: 0.015832
- ratio_gap: -1.12%
- ratio_slope_proxy(20d): 0.000056

### Volume (if available)

- volume: 28586806.00
- volume_MA20: 36730295.30
- volume_ratio: 0.78

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.01
- MA20 / MA60 / MA200: 12.43 / 12.89 / 10.90
- gap20 / gap60: 4.70% / 0.96%
- 5D return: 11.29%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.053965
- ratio_MA60: 0.049554
- ratio_gap: 8.90%
- ratio_slope_proxy(20d): 0.001262

### Volume (if available)

- volume: 21044137.00
- volume_MA20: 22179256.85
- volume_ratio: 0.95

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-14**
- 실행시간(UTC): **2026-05-15 03:01:31**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.82
- IG OAS 4주 변화: -4.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.99
- VIX: 17.87
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -2.91% / slope_proxy: 0.001623
- GDXJ/GLD gap: 2.54% / slope_proxy: -0.003193

## VZLA (Vizsla Silver)
- close: 3.76 | RSI14: 59.141154 | ATR14%: 5.77%
- MA20 gap: 7.61% | MA50 gap: 8.61% | MA200 gap: -10.95%
- vol_ratio(Volume/Vol20): 1.205507 | gap_open: 0.00%
- RS vs SILJ gap: 2.55% / slope_proxy: -0.010732
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
- close: 9.7 | RSI14: 59.677438 | ATR14%: 6.95%
- MA20 gap: 11.17% | MA50 gap: 12.55% | MA200 gap: 19.95%
- vol_ratio(Volume/Vol20): 0.60382 | gap_open: 0.80%
- SilverMarginGate: SI=81.779999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.92% / slope_proxy: -0.024459
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
- close: 39.360001 | RSI14: 50.193188 | ATR14%: 9.64%
- MA20 gap: -0.05% | MA50 gap: 3.56% | MA200 gap: 75.45%
- vol_ratio(Volume/Vol20): 1.195524 | gap_open: 1.44%
- RS vs SILJ gap: -2.97% / slope_proxy: 0.032099
- RS vs GDXJ gap: 0.79% / slope_proxy: 0.007033
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
