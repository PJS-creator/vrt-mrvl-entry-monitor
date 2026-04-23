# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-23**
- 실행시간(UTC): **2026-04-23 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.84 / 4주 변화 -33.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 -14.0 bp
- VIX (VIXCLS): 18.92
- NFCI: -0.497

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.154106
- MA60: 7.819233
- gap: 17.07%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.336744
- MA60: 0.233905
- gap: 43.97%
- MA60_slope_proxy: 0.023558
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-23**
- 실행시간(UTC): **2026-04-23 15:00:51**

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
- TERM_SPREAD_10Y_POLICY: 107.42 bp / 4주 변화 -4.57 bp
- CURVE_10s5s: 48.2 bp / 4주 변화 6.16 bp

## NWG Price
- close: 583.2
- MA50: 587.8209 / gap50: -0.79%
- MA200: 579.3605 / gap200: 0.66%

## Relative Strength
- RS vs FTSE gap: -3.20% / slope_proxy: -0.002561
- RS vs Peers gap: -5.41% / slope_proxy: -0.038029

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-23 15:00:58**

## Commodity Regime

- WTI ref (CL=F): 93.31 / 5D -1.46%
- Brent ref (BZ=F): 102.70 / 5D 3.33%
- Brent Tier: **>=90**
- Brent-WTI spread: 9.39
- Gas ref (NG=F): 2.75 / 5D 3.78%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 57.03
- MA20 / MA60 / MA200: 59.66 / 54.39 / 46.35
- gap20 / gap60: -4.40% / 4.85%
- 5D return: 0.28%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 1.007241
- ratio_MA60: 0.966205
- ratio_gap: 4.25%
- ratio_slope_proxy(20d): 0.038995

### Volume (if available)

- volume: 2672319.00
- volume_MA20: 17141450.95
- volume_ratio: 0.16

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.20
- MA20 / MA60 / MA200: 20.84 / 18.23 / 14.11
- gap20 / gap60: 1.70% / 16.29%
- 5D return: -1.42%
- 20D high/low: 21.97 / 19.98

### Relative Strength

- ratio: 0.521787
- ratio_MA60: 0.475904
- ratio_gap: 9.64%
- ratio_slope_proxy(20d): 0.050630

### Volume (if available)

- volume: 3594651.00
- volume_MA20: 29917372.55
- volume_ratio: 0.12

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

- close: 6.07
- MA20 / MA60 / MA200: 6.43 / 6.16 / 4.36
- gap20 / gap60: -5.64% / -1.54%
- 5D return: -4.49%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.014234
- ratio_MA60: 0.015829
- ratio_gap: -10.07%
- ratio_slope_proxy(20d): 0.000661

### Volume (if available)

- volume: 5830323.00
- volume_MA20: 29066656.15
- volume_ratio: 0.20

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

- close: 12.53
- MA20 / MA60 / MA200: 13.93 / 12.13 / 11.14
- gap20 / gap60: -10.10% / 3.27%
- 5D return: -1.22%
- 20D high/low: 17.53 / 11.45

### Relative Strength

- ratio: 0.048735
- ratio_MA60: 0.048317
- ratio_gap: 0.87%
- ratio_slope_proxy(20d): 0.003864

### Volume (if available)

- volume: 3700821.00
- volume_MA20: 26067531.05
- volume_ratio: 0.14

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

- 데이터 기준일(주가): **2026-04-23**
- 실행시간(UTC): **2026-04-23 15:01:14**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -33.0 bp / latest 2.84
- IG OAS 4주 변화: -8.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -14.0 bp / latest 1.92
- VIX: 18.92
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.39% / slope_proxy: 0.01308
- GDXJ/GLD gap: -0.96% / slope_proxy: -0.004038

## VZLA (Vizsla Silver)
- close: 3.4132 | RSI14: 47.899826 | ATR14%: 5.59%
- MA20 gap: 2.76% | MA50 gap: -5.14% | MA200 gap: -18.75%
- vol_ratio(Volume/Vol20): 0.248159 | gap_open: 2.31%
- RS vs SILJ gap: -5.76% / slope_proxy: -0.025846
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
- close: 8.7 | RSI14: 49.29971 | ATR14%: 8.01%
- MA20 gap: 4.05% | MA50 gap: -6.93% | MA200 gap: 12.60%
- vol_ratio(Volume/Vol20): 0.291484 | gap_open: 2.11%
- SilverMarginGate: SI=76.165001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.99% / slope_proxy: -0.029191
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
- close: 38.369999 | RSI14: 49.087466 | ATR14%: 9.58%
- MA20 gap: 1.54% | MA50 gap: -2.66% | MA200 gap: 93.70%
- vol_ratio(Volume/Vol20): 0.386563 | gap_open: 2.71%
- RS vs SILJ gap: 3.01% / slope_proxy: 0.059719
- RS vs GDXJ gap: 2.19% / slope_proxy: 0.012443
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
