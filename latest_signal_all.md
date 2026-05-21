# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-21**
- 실행시간(UTC): **2026-05-21 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.86 / 4주 변화 1.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 2.18 / 4주 변화 26.0 bp
- VIX (VIXCLS): 17.44
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.571659
- MA60: 8.793368
- gap: 8.85%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.340567
- MA60: 0.274408
- gap: 24.11%
- MA60_slope_proxy: 0.040388
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-21**
- 실행시간(UTC): **2026-05-21 15:00:53**

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
- TERM_SPREAD_10Y_POLICY: 133.33 bp / 4주 변화 25.91 bp
- CURVE_10s5s: 46.82 bp / 4주 변화 -1.38 bp

## NWG Price
- close: 581.4
- MA50: 575.8129 / gap50: 0.97%
- MA200: 585.4816 / gap200: -0.70%

## Relative Strength
- RS vs FTSE gap: -0.41% / slope_proxy: -0.001911
- RS vs Peers gap: -4.38% / slope_proxy: -0.034388

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-21 15:01:00**

## Commodity Regime

- WTI ref (CL=F): 101.24 / 5D 0.07%
- Brent ref (BZ=F): 107.48 / 5D 1.66%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.24
- Gas ref (NG=F): 3.16 / 5D 9.16%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 59.18
- MA20 / MA60 / MA200: 57.86 / 57.99 / 47.79
- gap20 / gap60: 2.28% / 2.04%
- 5D return: 4.12%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.990709
- ratio_MA60: 1.000254
- ratio_gap: -0.95%
- ratio_slope_proxy(20d): 0.033920

### Volume (if available)

- volume: 2889177.00
- volume_MA20: 11874833.85
- volume_ratio: 0.24

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.17
- MA20 / MA60 / MA200: 20.79 / 19.92 / 14.88
- gap20 / gap60: -3.03% / 1.22%
- 5D return: 1.95%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.550355
- ratio_MA60: 0.519917
- ratio_gap: 5.85%
- ratio_slope_proxy(20d): 0.046641

### Volume (if available)

- volume: 3798126.00
- volume_MA20: 17596491.30
- volume_ratio: 0.22

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 7.06
- MA20 / MA60 / MA200: 6.75 / 6.50 / 4.75
- gap20 / gap60: 4.55% / 8.58%
- 5D return: 2.17%
- 20D high/low: 7.58 / 6.11

### Relative Strength

- ratio: 0.015861
- ratio_MA60: 0.015826
- ratio_gap: 0.22%
- ratio_slope_proxy(20d): -0.000003

### Volume (if available)

- volume: 4780788.00
- volume_MA20: 37422449.40
- volume_ratio: 0.13

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.95
- MA20 / MA60 / MA200: 12.97 / 13.28 / 10.88
- gap20 / gap60: 7.52% / 5.02%
- 5D return: 7.19%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.057567
- ratio_MA60: 0.050848
- ratio_gap: 13.21%
- ratio_slope_proxy(20d): 0.002392

### Volume (if available)

- volume: 4223362.00
- volume_MA20: 20539663.10
- volume_ratio: 0.21

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-21**
- 실행시간(UTC): **2026-05-21 15:01:17**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.86
- IG OAS 4주 변화: -4.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.18
- VIX: 17.44
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -4.80% / slope_proxy: -0.005743
- GDXJ/GLD gap: -5.70% / slope_proxy: -0.004289

## VZLA (Vizsla Silver)
- close: 3.32 | RSI14: 44.366757 | ATR14%: 6.35%
- MA20 gap: -4.67% | MA50 gap: -2.18% | MA200 gap: -21.54%
- vol_ratio(Volume/Vol20): 0.105984 | gap_open: 2.36%
- RS vs SILJ gap: 2.90% / slope_proxy: -0.004707
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
- close: 8.02 | RSI14: 42.594111 | ATR14%: 8.30%
- MA20 gap: -6.73% | MA50 gap: -4.96% | MA200 gap: -2.27%
- vol_ratio(Volume/Vol20): 0.440132 | gap_open: 2.39%
- SilverMarginGate: SI=75.290001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.83% / slope_proxy: -0.01756
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
- close: 32.619999 | RSI14: 40.292521 | ATR14%: 10.55%
- MA20 gap: -13.30% | MA50 gap: -12.46% | MA200 gap: 40.60%
- vol_ratio(Volume/Vol20): 0.336457 | gap_open: 1.34%
- RS vs SILJ gap: -7.79% / slope_proxy: 0.027449
- RS vs GDXJ gap: -5.15% / slope_proxy: 0.007787
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
