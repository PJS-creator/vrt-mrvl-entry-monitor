# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-21**
- 실행시간(UTC): **2026-04-22 03:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.87 / 4주 변화 -32.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 1.91 / 4주 변화 -10.0 bp
- VIX (VIXCLS): 18.87
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.082558
- MA60: 7.721849
- gap: 17.62%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.325636
- MA60: 0.229601
- gap: 41.83%
- MA60_slope_proxy: 0.019382
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-21**
- 실행시간(UTC): **2026-04-22 03:00:47**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 94.73 bp / 4주 변화 -22.94 bp
- CURVE_10s5s: 49.51 bp / 4주 변화 11.12 bp

## NWG Price
- close: 601.6
- MA50: 588.7992 / gap50: 2.17%
- MA200: 578.4222 / gap200: 4.01%

## Relative Strength
- RS vs FTSE gap: -0.95% / slope_proxy: -0.002672
- RS vs Peers gap: -4.30% / slope_proxy: -0.038821

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-22 03:00:56**

## Commodity Regime

- WTI ref (CL=F): 89.40 / 5D -2.06%
- Brent ref (BZ=F): 92.85 / 5D -2.05%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.45
- Gas ref (NG=F): 2.69 / 5D 3.46%

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

- close: 56.33
- MA20 / MA60 / MA200: 60.11 / 53.96 / 46.22
- gap20 / gap60: -6.28% / 4.40%
- 5D return: 1.72%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 1.008233
- ratio_MA60: 0.962475
- ratio_gap: 4.75%
- ratio_slope_proxy(20d): 0.038958

### Volume (if available)

- volume: 15109530.00
- volume_MA20: 17957226.50
- volume_ratio: 0.84

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.15
- MA20 / MA60 / MA200: 20.70 / 18.01 / 14.03
- gap20 / gap60: 2.17% / 17.44%
- 5D return: 0.67%
- 20D high/low: 21.97 / 19.75

### Relative Strength

- ratio: 0.518509
- ratio_MA60: 0.471646
- ratio_gap: 9.94%
- ratio_slope_proxy(20d): 0.051790

### Volume (if available)

- volume: 12578123.00
- volume_MA20: 31512581.15
- volume_ratio: 0.40

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

- close: 6.05
- MA20 / MA60 / MA200: 6.49 / 6.12 / 4.33
- gap20 / gap60: -6.80% / -1.18%
- 5D return: -1.94%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.014807
- ratio_MA60: 0.015822
- ratio_gap: -6.42%
- ratio_slope_proxy(20d): 0.000727

### Volume (if available)

- volume: 27792216.00
- volume_MA20: 31135035.80
- volume_ratio: 0.89

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

- close: 12.09
- MA20 / MA60 / MA200: 14.35 / 12.02 / 11.16
- gap20 / gap60: -15.77% / 0.60%
- 5D return: -3.36%
- 20D high/low: 17.53 / 11.45

### Relative Strength

- ratio: 0.046900
- ratio_MA60: 0.048187
- ratio_gap: -2.67%
- ratio_slope_proxy(20d): 0.004406

### Volume (if available)

- volume: 23313932.00
- volume_MA20: 28863381.60
- volume_ratio: 0.81

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

- 데이터 기준일(주가): **2026-04-21**
- 실행시간(UTC): **2026-04-22 03:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -32.0 bp / latest 2.87
- IG OAS 4주 변화: -7.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -10.0 bp / latest 1.91
- VIX: 18.87
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.58% / slope_proxy: 0.011399
- GDXJ/GLD gap: -1.40% / slope_proxy: -0.003891

## VZLA (Vizsla Silver)
- close: 3.33 | RSI14: 44.231856 | ATR14%: 6.02%
- MA20 gap: 1.02% | MA50 gap: -8.12% | MA200 gap: -20.65%
- vol_ratio(Volume/Vol20): 1.251794 | gap_open: 1.14%
- RS vs SILJ gap: -8.37% / slope_proxy: -0.026656
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
- close: 8.49 | RSI14: 47.213938 | ATR14%: 8.56%
- MA20 gap: 2.62% | MA50 gap: -10.25% | MA200 gap: 10.68%
- vol_ratio(Volume/Vol20): 1.043203 | gap_open: 1.10%
- SilverMarginGate: SI=77.775002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.27% / slope_proxy: -0.027456
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
- close: 39.41 | RSI14: 51.262961 | ATR14%: 9.83%
- MA20 gap: 5.86% | MA50 gap: 0.15% | MA200 gap: 102.66%
- vol_ratio(Volume/Vol20): 1.484716 | gap_open: 1.30%
- RS vs SILJ gap: 7.03% / slope_proxy: 0.07421
- RS vs GDXJ gap: 5.85% / slope_proxy: 0.017034
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
