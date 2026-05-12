# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-11**
- 실행시간(UTC): **2026-05-12 03:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.81 / 4주 변화 -13.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 -3.0 bp
- 10Y Real Yield (DFII10): 1.93 / 4주 변화 -2.0 bp
- VIX (VIXCLS): 17.19
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.404978
- MA60: 8.43065
- gap: 23.42%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.296438
- MA60: 0.257511
- gap: 15.12%
- MA60_slope_proxy: 0.038109
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-11**
- 실행시간(UTC): **2026-05-12 03:00:43**

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
- TERM_SPREAD_10Y_POLICY: 113.01 bp / 4주 변화 13.29 bp
- CURVE_10s5s: 46.15 bp / 4주 변화 0.77 bp

## NWG Price
- close: 581.4
- MA50: 579.9831 / gap50: 0.24%
- MA200: 583.5805 / gap200: -0.37%

## Relative Strength
- RS vs FTSE gap: 0.83% / slope_proxy: -0.002347
- RS vs Peers gap: -3.15% / slope_proxy: -0.037262

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-12 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 99.07 / 5D -6.91%
- Brent ref (BZ=F): 105.16 / 5D -8.11%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.09
- Gas ref (NG=F): 2.92 / 5D 1.78%

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

- close: 55.14
- MA20 / MA60 / MA200: 56.87 / 56.80 / 47.19
- gap20 / gap60: -3.05% / -2.93%
- 5D return: -8.51%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.964492
- ratio_MA60: 0.990095
- ratio_gap: -2.59%
- ratio_slope_proxy(20d): 0.037638

### Volume (if available)

- volume: 13678653.00
- volume_MA20: 13157257.65
- volume_ratio: 1.04

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.75
- MA20 / MA60 / MA200: 21.09 / 19.34 / 14.57
- gap20 / gap60: -1.63% / 7.31%
- 5D return: -5.72%
- 20D high/low: 22.03 / 20.33

### Relative Strength

- ratio: 0.536730
- ratio_MA60: 0.501137
- ratio_gap: 7.10%
- ratio_slope_proxy(20d): 0.044403

### Volume (if available)

- volume: 20504680.00
- volume_MA20: 20022524.00
- volume_ratio: 1.02

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.55
- MA20 / MA60 / MA200: 6.36 / 6.41 / 4.59
- gap20 / gap60: 3.00% / 2.16%
- 5D return: -4.80%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015192
- ratio_MA60: 0.015897
- ratio_gap: -4.43%
- ratio_slope_proxy(20d): 0.000232

### Volume (if available)

- volume: 32581029.00
- volume_MA20: 36611031.45
- volume_ratio: 0.89

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

- close: 11.62
- MA20 / MA60 / MA200: 12.33 / 12.69 / 10.93
- gap20 / gap60: -5.77% / -8.45%
- 5D return: -15.61%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.048276
- ratio_MA60: 0.048820
- ratio_gap: -1.11%
- ratio_slope_proxy(20d): 0.000975

### Volume (if available)

- volume: 18147952.00
- volume_MA20: 19749132.60
- volume_ratio: 0.92

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

- 데이터 기준일(주가): **2026-05-11**
- 실행시간(UTC): **2026-05-12 03:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -13.0 bp / latest 2.81
- IG OAS 4주 변화: -3.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -2.0 bp / latest 1.93
- VIX: 17.19
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -4.04% / slope_proxy: 0.006082
- GDXJ/GLD gap: 3.95% / slope_proxy: -0.003923

## VZLA (Vizsla Silver)
- close: 3.73 | RSI14: 60.075402 | ATR14%: 5.58%
- MA20 gap: 8.54% | MA50 gap: 7.04% | MA200 gap: -11.46%
- vol_ratio(Volume/Vol20): 1.012948 | gap_open: 1.97%
- RS vs SILJ gap: -0.88% / slope_proxy: -0.014581
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
- close: 9.43 | RSI14: 60.022114 | ATR14%: 6.93%
- MA20 gap: 9.96% | MA50 gap: 8.48% | MA200 gap: 17.97%
- vol_ratio(Volume/Vol20): 1.255076 | gap_open: 1.77%
- SilverMarginGate: SI=86.900002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.42% / slope_proxy: -0.028372
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
- close: 43.709999 | RSI14: 59.861471 | ATR14%: 8.44%
- MA20 gap: 11.77% | MA50 gap: 13.59% | MA200 gap: 100.08%
- vol_ratio(Volume/Vol20): 1.993135 | gap_open: 3.90%
- RS vs SILJ gap: 5.67% / slope_proxy: 0.032815
- RS vs GDXJ gap: 9.67% / slope_proxy: 0.005453
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
