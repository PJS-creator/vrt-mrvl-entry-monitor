# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-17**
- 실행시간(UTC): **2026-04-17 15:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.86 / 4주 변화 -41.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -9.0 bp
- 10Y Real Yield (DFII10): 1.9 / 4주 변화 4.0 bp
- VIX (VIXCLS): 17.94
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.597705
- MA60: 7.618919
- gap: 12.85%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.296281
- MA60: 0.225563
- gap: 31.35%
- MA60_slope_proxy: 0.015044
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-17**
- 실행시간(UTC): **2026-04-17 15:00:45**

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
- TERM_SPREAD_10Y_POLICY: 99.35 bp / 4주 변화 4.33 bp
- CURVE_10s5s: 46.07 bp / 4주 변화 -2.76 bp

## NWG Price
- close: 629.4
- MA50: 590.8688 / gap50: 6.52%
- MA200: 577.2479 / gap200: 9.03%

## Relative Strength
- RS vs FTSE gap: 1.69% / slope_proxy: -0.002867
- RS vs Peers gap: -1.53% / slope_proxy: -0.038842

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-17 15:00:53**

## Commodity Regime

- WTI ref (CL=F): 79.38 / 5D -17.80%
- Brent ref (BZ=F): 86.50 / 5D -9.14%
- Brent Tier: **80-90**
- Brent-WTI spread: 7.12
- Gas ref (NG=F): 2.65 / 5D 0.23%

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

- close: 52.40
- MA20 / MA60 / MA200: 60.55 / 53.53 / 46.09
- gap20 / gap60: -13.46% / -2.12%
- 5D return: -9.61%
- 20D high/low: 66.24 / 52.40

### Relative Strength

- ratio: 0.975065
- ratio_MA60: 0.958838
- ratio_gap: 1.69%
- ratio_slope_proxy(20d): 0.039096

### Volume (if available)

- volume: 10048711.00
- volume_MA20: 18383795.55
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

- close: 19.96
- MA20 / MA60 / MA200: 20.48 / 17.77 / 13.94
- gap20 / gap60: -2.53% / 12.35%
- 5D return: -7.18%
- 20D high/low: 21.97 / 18.80

### Relative Strength

- ratio: 0.483356
- ratio_MA60: 0.467290
- ratio_gap: 3.44%
- ratio_slope_proxy(20d): 0.052508

### Volume (if available)

- volume: 17706516.00
- volume_MA20: 33414815.80
- volume_ratio: 0.53

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

- close: 5.89
- MA20 / MA60 / MA200: 6.53 / 6.08 / 4.30
- gap20 / gap60: -9.67% / -3.06%
- 5D return: -9.59%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.014930
- ratio_MA60: 0.015797
- ratio_gap: -5.49%
- ratio_slope_proxy(20d): 0.000769

### Volume (if available)

- volume: 14792700.00
- volume_MA20: 30902650.00
- volume_ratio: 0.48

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

- close: 11.33
- MA20 / MA60 / MA200: 14.75 / 11.95 / 11.20
- gap20 / gap60: -23.19% / -5.16%
- 5D return: -12.64%
- 20D high/low: 17.53 / 11.33

### Relative Strength

- ratio: 0.045500
- ratio_MA60: 0.048210
- ratio_gap: -5.62%
- ratio_slope_proxy(20d): 0.005090

### Volume (if available)

- volume: 16824504.00
- volume_MA20: 31811660.20
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

- 데이터 기준일(주가): **2026-04-17**
- 실행시간(UTC): **2026-04-17 15:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -41.0 bp / latest 2.86
- IG OAS 4주 변화: -9.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 1.9
- VIX: 17.94
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 0.97% / slope_proxy: 0.009864
- GDXJ/GLD gap: 4.43% / slope_proxy: -0.003982

## VZLA (Vizsla Silver)
- close: 3.58 | RSI14: 54.094913 | ATR14%: 5.59%
- MA20 gap: 9.73% | MA50 gap: -2.36% | MA200 gap: -14.61%
- vol_ratio(Volume/Vol20): 0.296109 | gap_open: 3.21%
- RS vs SILJ gap: -12.51% / slope_proxy: -0.027441
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
- close: 9.675 | RSI14: 58.610499 | ATR14%: 7.71%
- MA20 gap: 18.66% | MA50 gap: 1.34% | MA200 gap: 27.01%
- vol_ratio(Volume/Vol20): 0.356999 | gap_open: 4.21%
- SilverMarginGate: SI=82.964996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.79% / slope_proxy: -0.024953
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
- close: 44.887501 | RSI14: 62.569002 | ATR14%: 8.54%
- MA20 gap: 23.99% | MA50 gap: 14.91% | MA200 gap: 135.45%
- vol_ratio(Volume/Vol20): 0.423111 | gap_open: 3.73%
- RS vs SILJ gap: 10.28% / slope_proxy: 0.081472
- RS vs GDXJ gap: 8.85% / slope_proxy: 0.01986
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
