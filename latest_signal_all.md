# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-20**
- 실행시간(UTC): **2026-04-21 03:00:37**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.83 / 4주 변화 -41.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 1.9 / 4주 변화 -11.0 bp
- VIX (VIXCLS): 17.48
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.92703
- MA60: 7.67012
- gap: 16.39%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.318648
- MA60: 0.227515
- gap: 40.06%
- MA60_slope_proxy: 0.017114
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-20**
- 실행시간(UTC): **2026-04-21 03:00:40**

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
- TERM_SPREAD_10Y_POLICY: 104.12 bp / 4주 변화 0.16 bp
- CURVE_10s5s: 48.22 bp / 4주 변화 9.47 bp

## NWG Price
- close: 607.2
- MA50: 589.95 / gap50: 2.92%
- MA200: 577.8522 / gap200: 5.08%

## Relative Strength
- RS vs FTSE gap: -1.26% / slope_proxy: -0.002785
- RS vs Peers gap: -3.70% / slope_proxy: -0.039333

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-21 03:00:47**

## Commodity Regime

- WTI ref (CL=F): 86.67 / 5D -12.53%
- Brent ref (BZ=F): 94.96 / 5D -4.43%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.29
- Gas ref (NG=F): 2.66 / 5D 1.26%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 54.48
- MA20 / MA60 / MA200: 60.31 / 53.75 / 46.15
- gap20 / gap60: -9.66% / 1.36%
- 5D return: -6.17%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 0.989286
- ratio_MA60: 0.960639
- ratio_gap: 2.98%
- ratio_slope_proxy(20d): 0.038934

### Volume (if available)

- volume: 10020467.00
- volume_MA20: 18317868.35
- volume_ratio: 0.55

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.76
- MA20 / MA60 / MA200: 20.61 / 17.89 / 13.99
- gap20 / gap60: 0.75% / 16.01%
- 5D return: -5.51%
- 20D high/low: 21.97 / 19.27

### Relative Strength

- ratio: 0.502663
- ratio_MA60: 0.469509
- ratio_gap: 7.06%
- ratio_slope_proxy(20d): 0.052118

### Volume (if available)

- volume: 18423035.00
- volume_MA20: 33525466.75
- volume_ratio: 0.55

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.89
- MA20 / MA60 / MA200: 6.51 / 6.10 / 4.31
- gap20 / gap60: -9.55% / -3.47%
- 5D return: -11.30%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.014762
- ratio_MA60: 0.015812
- ratio_gap: -6.64%
- ratio_slope_proxy(20d): 0.000750

### Volume (if available)

- volume: 27007801.00
- volume_MA20: 32104435.05
- volume_ratio: 0.84

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

- close: 11.45
- MA20 / MA60 / MA200: 14.54 / 11.98 / 11.18
- gap20 / gap60: -21.25% / -4.43%
- 5D return: -10.20%
- 20D high/low: 17.53 / 11.45

### Relative Strength

- ratio: 0.045373
- ratio_MA60: 0.048200
- ratio_gap: -5.86%
- ratio_slope_proxy(20d): 0.004724

### Volume (if available)

- volume: 15962311.00
- volume_MA20: 30320450.55
- volume_ratio: 0.53

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

- 데이터 기준일(주가): **2026-04-20**
- 실행시간(UTC): **2026-04-21 03:00:50**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -41.0 bp / latest 2.83
- IG OAS 4주 변화: -8.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -11.0 bp / latest 1.9
- VIX: 17.48
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 1.10% / slope_proxy: 0.010755
- GDXJ/GLD gap: 2.73% / slope_proxy: -0.003661

## VZLA (Vizsla Silver)
- close: 3.52 | RSI14: 51.943606 | ATR14%: 5.65%
- MA20 gap: 7.15% | MA50 gap: -3.56% | MA200 gap: -16.09%
- vol_ratio(Volume/Vol20): 1.063704 | gap_open: 1.99%
- RS vs SILJ gap: -10.27% / slope_proxy: -0.027031
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

## SCZM (Santacruz Silver)
- close: 9.1 | RSI14: 53.62529 | ATR14%: 7.96%
- MA20 gap: 10.60% | MA50 gap: -4.34% | MA200 gap: 19.04%
- vol_ratio(Volume/Vol20): 0.69699 | gap_open: 1.09%
- SilverMarginGate: SI=79.220001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.75% / slope_proxy: -0.026155
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
- close: 43.970001 | RSI14: 61.104805 | ATR14%: 8.51%
- MA20 gap: 19.27% | MA50 gap: 12.02% | MA200 gap: 128.24%
- vol_ratio(Volume/Vol20): 0.753145 | gap_open: 2.33%
- RS vs SILJ gap: 11.57% / slope_proxy: 0.078489
- RS vs GDXJ gap: 9.78% / slope_proxy: 0.018595
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trigger(Breakout/Retest)=FALSE
