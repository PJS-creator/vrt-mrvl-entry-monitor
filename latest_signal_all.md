# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-16**
- 실행시간(UTC): **2026-04-16 15:00:48**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.85 / 4주 변화 -35.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -11.0 bp
- 10Y Real Yield (DFII10): 1.89 / 4주 변화 6.0 bp
- VIX (VIXCLS): 18.17
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.690856
- MA60: 7.578973
- gap: 14.67%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.29143
- MA60: 0.224016
- gap: 30.09%
- MA60_slope_proxy: 0.013331
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-16**
- 실행시간(UTC): **2026-04-16 15:01:06**

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
- TERM_SPREAD_10Y_POLICY: 99.1 bp / 4주 변화 8.74 bp
- CURVE_10s5s: 45.74 bp / 4주 변화 -4.8 bp

## NWG Price
- close: 620.2
- MA50: 592.1873 / gap50: 4.73%
- MA200: 576.5644 / gap200: 7.57%

## Relative Strength
- RS vs FTSE gap: 0.67% / slope_proxy: -0.002925
- RS vs Peers gap: -1.20% / slope_proxy: -0.038772

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-16 15:01:13**

## Commodity Regime

- WTI ref (CL=F): 90.34 / 5D -7.69%
- Brent ref (BZ=F): 98.01 / 5D 2.18%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.67
- Gas ref (NG=F): 2.66 / 5D -0.41%

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

- close: 56.64
- MA20 / MA60 / MA200: 60.90 / 53.38 / 46.04
- gap20 / gap60: -6.99% / 6.11%
- 5D return: -3.23%
- 20D high/low: 66.24 / 55.38

### Relative Strength

- ratio: 1.000707
- ratio_MA60: 0.957415
- ratio_gap: 4.52%
- ratio_slope_proxy(20d): 0.039393

### Volume (if available)

- volume: 3257420.00
- volume_MA20: 18782051.00
- volume_ratio: 0.17

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.30
- MA20 / MA60 / MA200: 20.46 / 17.66 / 13.90
- gap20 / gap60: 4.06% / 20.59%
- 5D return: 2.92%
- 20D high/low: 21.97 / 18.80

### Relative Strength

- ratio: 0.516242
- ratio_MA60: 0.465627
- ratio_gap: 10.87%
- ratio_slope_proxy(20d): 0.053573

### Volume (if available)

- volume: 9174114.00
- volume_MA20: 33429075.70
- volume_ratio: 0.27

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

- close: 6.29
- MA20 / MA60 / MA200: 6.55 / 6.06 / 4.28
- gap20 / gap60: -3.92% / 3.89%
- 5D return: -4.04%
- 20D high/low: 6.93 / 6.15

### Relative Strength

- ratio: 0.015440
- ratio_MA60: 0.015774
- ratio_gap: -2.12%
- ratio_slope_proxy(20d): 0.000783

### Volume (if available)

- volume: 6635301.00
- volume_MA20: 31269480.05
- volume_ratio: 0.21

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

- close: 12.74
- MA20 / MA60 / MA200: 14.90 / 11.91 / 11.22
- gap20 / gap60: -14.51% / 6.97%
- 5D return: -1.92%
- 20D high/low: 17.53 / 12.18

### Relative Strength

- ratio: 0.048418
- ratio_MA60: 0.048183
- ratio_gap: 0.49%
- ratio_slope_proxy(20d): 0.005350

### Volume (if available)

- volume: 5565146.00
- volume_MA20: 35360332.30
- volume_ratio: 0.16

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

- 데이터 기준일(주가): **2026-04-16**
- 실행시간(UTC): **2026-04-16 15:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.85
- IG OAS 4주 변화: -11.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.89
- VIX: 18.17
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 0.60% / slope_proxy: 0.008622
- GDXJ/GLD gap: 1.76% / slope_proxy: -0.004493

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 47.812159 | ATR14%: 5.88%
- MA20 gap: 5.43% | MA50 gap: -7.41% | MA200 gap: -18.36%
- vol_ratio(Volume/Vol20): 0.352524 | gap_open: 0.88%
- RS vs SILJ gap: -12.60% / slope_proxy: -0.027575
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
- close: 8.81 | RSI14: 51.170856 | ATR14%: 8.37%
- MA20 gap: 9.61% | MA50 gap: -8.21% | MA200 gap: 16.17%
- vol_ratio(Volume/Vol20): 0.279954 | gap_open: 0.91%
- SilverMarginGate: SI=78.510002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.70% / slope_proxy: -0.024511
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
- close: 40.169998 | RSI14: 55.012347 | ATR14%: 9.33%
- MA20 gap: 13.10% | MA50 gap: 3.16% | MA200 gap: 113.07%
- vol_ratio(Volume/Vol20): 0.212702 | gap_open: 2.50%
- RS vs SILJ gap: 4.47% / slope_proxy: 0.087341
- RS vs GDXJ gap: 1.85% / slope_proxy: 0.021621
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
