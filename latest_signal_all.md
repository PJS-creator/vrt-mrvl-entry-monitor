# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-28**
- 실행시간(UTC): **2026-04-28 15:00:55**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.86 / 4주 변화 -56.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -11.0 bp
- 10Y Real Yield (DFII10): 1.89 / 4주 변화 -24.0 bp
- VIX (VIXCLS): 18.02
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.677616
- MA60: 7.962178
- gap: 8.99%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.312187
- MA60: 0.239991
- gap: 30.08%
- MA60_slope_proxy: 0.028936
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-28**
- 실행시간(UTC): **2026-04-28 15:00:58**

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
- TERM_SPREAD_10Y_POLICY: 112.9 bp / 4주 변화 -1.45 bp
- CURVE_10s5s: 46.01 bp / 4주 변화 6.26 bp

## NWG Price
- close: 575.6
- MA50: 586.7191 / gap50: -1.90%
- MA200: 580.5788 / gap200: -0.86%

## Relative Strength
- RS vs FTSE gap: -2.13% / slope_proxy: -0.002405
- RS vs Peers gap: -5.09% / slope_proxy: -0.036537

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-28 15:01:06**

## Commodity Regime

- WTI ref (CL=F): 100.27 / 5D 8.84%
- Brent ref (BZ=F): 104.71 / 5D 6.33%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.44
- Gas ref (NG=F): 2.73 / 5D 1.30%

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

- close: 58.22
- MA20 / MA60 / MA200: 58.53 / 55.03 / 46.54
- gap20 / gap60: -0.52% / 5.81%
- 5D return: 3.36%
- 20D high/low: 65.00 / 53.79

### Relative Strength

- ratio: 1.010500
- ratio_MA60: 0.971914
- ratio_gap: 3.97%
- ratio_slope_proxy(20d): 0.037922

### Volume (if available)

- volume: 3909944.00
- volume_MA20: 15268192.20
- volume_ratio: 0.26

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.00
- MA20 / MA60 / MA200: 20.79 / 18.40 / 14.16
- gap20 / gap60: 1.05% / 14.15%
- 5D return: -0.10%
- 20D high/low: 21.84 / 19.86

### Relative Strength

- ratio: 0.533799
- ratio_MA60: 0.479381
- ratio_gap: 11.35%
- ratio_slope_proxy(20d): 0.047116

### Volume (if available)

- volume: 4312727.00
- volume_MA20: 26615301.35
- volume_ratio: 0.16

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

- close: 6.58
- MA20 / MA60 / MA200: 6.36 / 6.23 / 4.42
- gap20 / gap60: 3.31% / 5.47%
- 5D return: 8.68%
- 20D high/low: 6.70 / 5.89

### Relative Strength

- ratio: 0.014882
- ratio_MA60: 0.015849
- ratio_gap: -6.10%
- ratio_slope_proxy(20d): 0.000571

### Volume (if available)

- volume: 7989999.00
- volume_MA20: 29619839.95
- volume_ratio: 0.27

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

- close: 12.20
- MA20 / MA60 / MA200: 13.21 / 12.26 / 11.06
- gap20 / gap60: -7.63% / -0.49%
- 5D return: 0.89%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.046410
- ratio_MA60: 0.048378
- ratio_gap: -4.07%
- ratio_slope_proxy(20d): 0.002820

### Volume (if available)

- volume: 3908617.00
- volume_MA20: 25244100.85
- volume_ratio: 0.15

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

- 데이터 기준일(주가): **2026-04-28**
- 실행시간(UTC): **2026-04-28 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -56.0 bp / latest 2.86
- IG OAS 4주 변화: -11.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -24.0 bp / latest 1.89
- VIX: 18.02
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -2.16% / slope_proxy: 0.015529
- GDXJ/GLD gap: -3.23% / slope_proxy: -0.003456

## VZLA (Vizsla Silver)
- close: 3.385 | RSI14: 47.666278 | ATR14%: 5.84%
- MA20 gap: 0.69% | MA50 gap: -5.29% | MA200 gap: -19.52%
- vol_ratio(Volume/Vol20): 0.330508 | gap_open: 3.41%
- RS vs SILJ gap: 0.88% / slope_proxy: -0.024219
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
- close: 7.825 | RSI14: 41.0806 | ATR14%: 8.58%
- MA20 gap: -7.52% | MA50 gap: -15.05% | MA200 gap: 0.34%
- vol_ratio(Volume/Vol20): 0.381073 | gap_open: 3.57%
- SilverMarginGate: SI=73.010002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -9.11% / slope_proxy: -0.030401
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
- close: 35.810001 | RSI14: 44.232584 | ATR14%: 9.86%
- MA20 gap: -7.29% | MA50 gap: -9.47% | MA200 gap: 76.31%
- vol_ratio(Volume/Vol20): 0.334133 | gap_open: 2.64%
- RS vs SILJ gap: 1.50% / slope_proxy: 0.043523
- RS vs GDXJ gap: 1.19% / slope_proxy: 0.007668
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
