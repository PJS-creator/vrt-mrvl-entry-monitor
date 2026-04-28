# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-27**
- 실행시간(UTC): **2026-04-28 03:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.86 / 4주 변화 -56.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -11.0 bp
- 10Y Real Yield (DFII10): 1.89 / 4주 변화 -24.0 bp
- VIX (VIXCLS): 18.71
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.283904
- MA60: 7.918886
- gap: 17.24%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.312507
- MA60: 0.238046
- gap: 31.28%
- MA60_slope_proxy: 0.027098
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-27**
- 실행시간(UTC): **2026-04-28 03:00:44**

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
- TERM_SPREAD_10Y_POLICY: 112.1 bp / 4주 변화 -2.25 bp
- CURVE_10s5s: 46.59 bp / 4주 변화 6.84 bp

## NWG Price
- close: 579.4
- MA50: 587.2298 / gap50: -1.33%
- MA200: 579.7659 / gap200: -0.06%

## Relative Strength
- RS vs FTSE gap: -2.79% / slope_proxy: -0.002507
- RS vs Peers gap: -4.72% / slope_proxy: -0.037548

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-28 03:00:50**

## Commodity Regime

- WTI ref (CL=F): 97.27 / 5D 8.55%
- Brent ref (BZ=F): 102.43 / 5D 7.28%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.16
- Gas ref (NG=F): 2.72 / 5D 1.12%

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

- close: 57.27
- MA20 / MA60 / MA200: 58.93 / 54.81 / 46.48
- gap20 / gap60: -2.82% / 4.48%
- 5D return: 5.12%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 1.008807
- ratio_MA60: 0.969918
- ratio_gap: 4.01%
- ratio_slope_proxy(20d): 0.038387

### Volume (if available)

- volume: 6231828.00
- volume_MA20: 16158041.40
- volume_ratio: 0.39

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.96
- MA20 / MA60 / MA200: 20.77 / 18.31 / 14.11
- gap20 / gap60: 0.91% / 14.50%
- 5D return: 1.56%
- 20D high/low: 21.84 / 19.86

### Relative Strength

- ratio: 0.525445
- ratio_MA60: 0.477347
- ratio_gap: 10.08%
- ratio_slope_proxy(20d): 0.048279

### Volume (if available)

- volume: 18761193.00
- volume_MA20: 28879054.65
- volume_ratio: 0.65

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

- close: 6.52
- MA20 / MA60 / MA200: 6.37 / 6.21 / 4.40
- gap20 / gap60: 2.39% / 5.04%
- 5D return: 10.70%
- 20D high/low: 6.70 / 5.89

### Relative Strength

- ratio: 0.014838
- ratio_MA60: 0.015839
- ratio_gap: -6.32%
- ratio_slope_proxy(20d): 0.000595

### Volume (if available)

- volume: 62104580.00
- volume_MA20: 31324359.00
- volume_ratio: 1.98

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.19
- MA20 / MA60 / MA200: 13.44 / 12.22 / 11.09
- gap20 / gap60: -9.30% / -0.22%
- 5D return: 6.46%
- 20D high/low: 16.89 / 11.45

### Relative Strength

- ratio: 0.046993
- ratio_MA60: 0.048378
- ratio_gap: -2.86%
- ratio_slope_proxy(20d): 0.003192

### Volume (if available)

- volume: 10556324.00
- volume_MA20: 26122291.20
- volume_ratio: 0.40

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

- 데이터 기준일(주가): **2026-04-27**
- 실행시간(UTC): **2026-04-28 03:00:54**

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
- VIX: 18.71
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -1.18% / slope_proxy: 0.015158
- GDXJ/GLD gap: -1.86% / slope_proxy: -0.00379

## VZLA (Vizsla Silver)
- close: 3.52 | RSI14: 52.581336 | ATR14%: 5.70%
- MA20 gap: 5.11% | MA50 gap: -1.76% | MA200 gap: -16.30%
- vol_ratio(Volume/Vol20): 1.393612 | gap_open: 0.60%
- RS vs SILJ gap: -0.10% / slope_proxy: -0.024863
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
- close: 8.41 | RSI14: 46.514829 | ATR14%: 8.02%
- MA20 gap: -0.47% | MA50 gap: -9.11% | MA200 gap: 8.13%
- vol_ratio(Volume/Vol20): 0.697133 | gap_open: 0.12%
- SilverMarginGate: SI=74.345001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.97% / slope_proxy: -0.029698
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
- close: 38.119999 | RSI14: 48.720279 | ATR14%: 9.36%
- MA20 gap: -0.62% | MA50 gap: -3.62% | MA200 gap: 89.17%
- vol_ratio(Volume/Vol20): 0.478353 | gap_open: 1.41%
- RS vs SILJ gap: 3.63% / slope_proxy: 0.047047
- RS vs GDXJ gap: 3.93% / slope_proxy: 0.008701
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
