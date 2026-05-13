# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-12**
- 실행시간(UTC): **2026-05-13 03:00:39**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.79 / 4주 변화 -16.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 1.95 / 4주 변화 3.0 bp
- VIX (VIXCLS): 18.38
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.495426
- MA60: 8.487336
- gap: 23.66%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.293096
- MA60: 0.259184
- gap: 13.08%
- MA60_slope_proxy: 0.038225
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-12**
- 실행시간(UTC): **2026-05-13 03:00:41**

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
- TERM_SPREAD_10Y_POLICY: 111.95 bp / 4주 변화 11.15 bp
- CURVE_10s5s: 44.44 bp / 4주 변화 -1.45 bp

## NWG Price
- close: 562.8
- MA50: 578.6881 / gap50: -2.75%
- MA200: 583.8 / gap200: -3.60%

## Relative Strength
- RS vs FTSE gap: -2.29% / slope_proxy: -0.002311
- RS vs Peers gap: -4.61% / slope_proxy: -0.036814

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-13 03:00:49**

## Commodity Regime

- WTI ref (CL=F): 101.33 / 5D -0.92%
- Brent ref (BZ=F): 106.79 / 5D -2.80%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.46
- Gas ref (NG=F): 2.82 / 5D 1.26%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 56.27
- MA20 / MA60 / MA200: 56.92 / 56.98 / 47.25
- gap20 / gap60: -1.14% / -1.24%
- 5D return: -5.17%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.977419
- ratio_MA60: 0.992233
- ratio_gap: -1.49%
- ratio_slope_proxy(20d): 0.038418

### Volume (if available)

- volume: 10314525.00
- volume_MA20: 12851951.25
- volume_ratio: 0.80

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.50
- MA20 / MA60 / MA200: 21.07 / 19.43 / 14.62
- gap20 / gap60: -2.72% / 5.53%
- 5D return: -5.83%
- 20D high/low: 22.03 / 20.33

### Relative Strength

- ratio: 0.536088
- ratio_MA60: 0.503459
- ratio_gap: 6.48%
- ratio_slope_proxy(20d): 0.044646

### Volume (if available)

- volume: 21396670.00
- volume_MA20: 19600848.50
- volume_ratio: 1.09

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.54
- MA20 / MA60 / MA200: 6.38 / 6.41 / 4.61
- gap20 / gap60: 2.54% / 2.00%
- 5D return: 4.64%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.014957
- ratio_MA60: 0.015860
- ratio_gap: -5.69%
- ratio_slope_proxy(20d): 0.000161

### Volume (if available)

- volume: 21672004.00
- volume_MA20: 36177125.20
- volume_ratio: 0.60

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

- close: 13.27
- MA20 / MA60 / MA200: 12.37 / 12.76 / 10.92
- gap20 / gap60: 7.28% / 4.01%
- 5D return: 1.92%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.054316
- ratio_MA60: 0.049129
- ratio_gap: 10.56%
- ratio_slope_proxy(20d): 0.001025

### Volume (if available)

- volume: 41653155.00
- volume_MA20: 21128297.75
- volume_ratio: 1.97

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-12**
- 실행시간(UTC): **2026-05-13 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -16.0 bp / latest 2.79
- IG OAS 4주 변화: -4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 3.0 bp / latest 1.95
- VIX: 18.38
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -3.40% / slope_proxy: 0.00427
- GDXJ/GLD gap: 4.63% / slope_proxy: -0.003801

## VZLA (Vizsla Silver)
- close: 3.85 | RSI14: 63.313849 | ATR14%: 5.57%
- MA20 gap: 11.40% | MA50 gap: 10.83% | MA200 gap: -8.68%
- vol_ratio(Volume/Vol20): 0.923153 | gap_open: 2.41%
- RS vs SILJ gap: 1.13% / slope_proxy: -0.013329
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
- close: 10.15 | RSI14: 65.795193 | ATR14%: 6.72%
- MA20 gap: 17.59% | MA50 gap: 17.30% | MA200 gap: 26.48%
- vol_ratio(Volume/Vol20): 1.236259 | gap_open: 2.12%
- SilverMarginGate: SI=87.120003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.85% / slope_proxy: -0.027179
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
- close: 45.16 | RSI14: 61.922139 | ATR14%: 8.33%
- MA20 gap: 14.96% | MA50 gap: 18.01% | MA200 gap: 104.77%
- vol_ratio(Volume/Vol20): 1.0548 | gap_open: 3.80%
- RS vs SILJ gap: 7.50% / slope_proxy: 0.033577
- RS vs GDXJ gap: 12.45% / slope_proxy: 0.006202
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
