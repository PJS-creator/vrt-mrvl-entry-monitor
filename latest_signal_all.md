# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-13**
- 실행시간(UTC): **2026-04-14 03:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.94 / 4주 변화 -34.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 -11.0 bp
- 10Y Real Yield (DFII10): 1.95 / 4주 변화 3.0 bp
- VIX (VIXCLS): 19.23
- NFCI: -0.433

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.848377
- MA60: 7.423744
- gap: 19.19%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.296161
- MA60: 0.219402
- gap: 34.99%
- MA60_slope_proxy: 0.008037
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-13**
- 실행시간(UTC): **2026-04-14 03:00:44**

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
- TERM_SPREAD_10Y_POLICY: 99.72 bp / 4주 변화 2.14 bp
- CURVE_10s5s: 45.38 bp / 4주 변화 -4.26 bp

## NWG Price
- close: 612.6
- MA50: 595.6271 / gap50: 2.85%
- MA200: 574.6401 / gap200: 6.61%

## Relative Strength
- RS vs FTSE gap: -0.92% / slope_proxy: -0.003167
- RS vs Peers gap: -2.59% / slope_proxy: -0.040886

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-14 03:00:51**

## Commodity Regime

- WTI ref (CL=F): 97.20 / 5D -13.53%
- Brent ref (BZ=F): 98.17 / 5D -10.57%
- Brent Tier: **>=90**
- Brent-WTI spread: 0.97
- Gas ref (NG=F): 2.61 / 5D -7.01%

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

- close: 58.06
- MA20 / MA60 / MA200: 61.17 / 52.71 / 45.83
- gap20 / gap60: -5.08% / 10.16%
- 5D return: -7.78%
- 20D high/low: 66.24 / 57.25

### Relative Strength

- ratio: 1.016635
- ratio_MA60: 0.952457
- ratio_gap: 6.74%
- ratio_slope_proxy(20d): 0.038938

### Volume (if available)

- volume: 11207437.00
- volume_MA20: 19242446.85
- volume_ratio: 0.58

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.97
- MA20 / MA60 / MA200: 20.24 / 17.25 / 13.77
- gap20 / gap60: 8.52% / 27.38%
- 5D return: 5.32%
- 20D high/low: 21.97 / 18.80

### Relative Strength

- ratio: 0.529143
- ratio_MA60: 0.459412
- ratio_gap: 15.18%
- ratio_slope_proxy(20d): 0.055171

### Volume (if available)

- volume: 25878813.00
- volume_MA20: 34614320.65
- volume_ratio: 0.75

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

- close: 6.64
- MA20 / MA60 / MA200: 6.57 / 5.96 / 4.23
- gap20 / gap60: 1.03% / 11.34%
- 5D return: 0.76%
- 20D high/low: 6.93 / 6.20

### Relative Strength

- ratio: 0.016074
- ratio_MA60: 0.015665
- ratio_gap: 2.61%
- ratio_slope_proxy(20d): 0.000810

### Volume (if available)

- volume: 19099575.00
- volume_MA20: 34394223.75
- volume_ratio: 0.56

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.75
- MA20 / MA60 / MA200: 15.04 / 11.71 / 11.27
- gap20 / gap60: -15.20% / 8.92%
- 5D return: -20.01%
- 20D high/low: 17.53 / 12.28

### Relative Strength

- ratio: 0.048739
- ratio_MA60: 0.047845
- ratio_gap: 1.87%
- ratio_slope_proxy(20d): 0.006040

### Volume (if available)

- volume: 21124687.00
- volume_MA20: 37964364.35
- volume_ratio: 0.56

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

- 데이터 기준일(주가): **2026-04-13**
- 실행시간(UTC): **2026-04-14 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.94
- IG OAS 4주 변화: -11.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 3.0 bp / latest 1.95
- VIX: 19.23
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 4.08% / slope_proxy: 0.005304
- GDXJ/GLD gap: 2.02% / slope_proxy: -0.00457

## VZLA (Vizsla Silver)
- close: 3.31 | RSI14: 43.235775 | ATR14%: 6.56%
- MA20 gap: 1.61% | MA50 gap: -12.77% | MA200 gap: -20.84%
- vol_ratio(Volume/Vol20): 0.856958 | gap_open: 1.54%
- RS vs SILJ gap: -16.96% / slope_proxy: -0.027524
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.61 | RSI14: 49.587979 | ATR14%: 9.06%
- MA20 gap: 7.99% | MA50 gap: -12.05% | MA200 gap: 14.91%
- vol_ratio(Volume/Vol20): 0.704672 | gap_open: 1.00%
- SilverMarginGate: SI=76.739998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -12.65% / slope_proxy: -0.023173
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 39.560001 | RSI14: 54.82209 | ATR14%: 10.27%
- MA20 gap: 12.38% | MA50 gap: 1.99% | MA200 gap: 116.30%
- vol_ratio(Volume/Vol20): 0.476893 | gap_open: 0.83%
- RS vs SILJ gap: 4.91% / slope_proxy: 0.115359
- RS vs GDXJ gap: 1.40% / slope_proxy: 0.029714
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
