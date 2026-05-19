# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-19**
- 실행시간(UTC): **2026-05-19 15:00:46**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.83 / 4주 변화 -4.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -6.0 bp
- 10Y Real Yield (DFII10): 2.1 / 4주 변화 20.0 bp
- VIX (VIXCLS): 17.82
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.463375
- MA60: 8.735192
- gap: 8.34%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.316252
- MA60: 0.269366
- gap: 17.41%
- MA60_slope_proxy: 0.039765
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-19**
- 실행시간(UTC): **2026-05-19 15:00:50**

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
- TERM_SPREAD_10Y_POLICY: 137.63 bp / 4주 변화 42.9 bp
- CURVE_10s5s: 47.42 bp / 4주 변화 -2.09 bp

## NWG Price
- close: 567.6
- MA50: 575.5558 / gap50: -1.38%
- MA200: 584.9126 / gap200: -2.96%

## Relative Strength
- RS vs FTSE gap: -1.63% / slope_proxy: -0.002088
- RS vs Peers gap: -4.27% / slope_proxy: -0.035863

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-19 15:00:59**

## Commodity Regime

- WTI ref (CL=F): 103.65 / 5D 1.44%
- Brent ref (BZ=F): 110.80 / 5D 2.81%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.15
- Gas ref (NG=F): 3.09 / 5D 8.55%

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

- close: 59.81
- MA20 / MA60 / MA200: 57.66 / 57.72 / 47.62
- gap20 / gap60: 3.73% / 3.62%
- 5D return: 6.29%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.987779
- ratio_MA60: 0.998533
- ratio_gap: -1.08%
- ratio_slope_proxy(20d): 0.036059

### Volume (if available)

- volume: 4096701.00
- volume_MA20: 11638585.05
- volume_ratio: 0.35

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.14
- MA20 / MA60 / MA200: 20.89 / 19.80 / 14.81
- gap20 / gap60: -3.57% / 1.73%
- 5D return: -1.73%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.561455
- ratio_MA60: 0.515568
- ratio_gap: 8.90%
- ratio_slope_proxy(20d): 0.046671

### Volume (if available)

- volume: 5747731.00
- volume_MA20: 17128526.55
- volume_ratio: 0.34

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 7.39
- MA20 / MA60 / MA200: 6.64 / 6.48 / 4.71
- gap20 / gap60: 11.43% / 14.18%
- 5D return: 13.07%
- 20D high/low: 7.58 / 6.06

### Relative Strength

- ratio: 0.016503
- ratio_MA60: 0.015831
- ratio_gap: 4.25%
- ratio_slope_proxy(20d): 0.000008

### Volume (if available)

- volume: 10332828.00
- volume_MA20: 36670796.40
- volume_ratio: 0.28

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

- close: 14.16
- MA20 / MA60 / MA200: 12.80 / 13.11 / 10.88
- gap20 / gap60: 10.62% / 8.02%
- 5D return: 6.74%
- 20D high/low: 14.23 / 11.45

### Relative Strength

- ratio: 0.057613
- ratio_MA60: 0.050300
- ratio_gap: 14.54%
- ratio_slope_proxy(20d): 0.002002

### Volume (if available)

- volume: 3798491.00
- volume_MA20: 20611834.55
- volume_ratio: 0.18

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

- 데이터 기준일(주가): **2026-05-19**
- 실행시간(UTC): **2026-05-19 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -4.0 bp / latest 2.83
- IG OAS 4주 변화: -6.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 20.0 bp / latest 2.1
- VIX: 17.82
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -6.36% / slope_proxy: -0.002024
- GDXJ/GLD gap: -6.68% / slope_proxy: -0.003743

## VZLA (Vizsla Silver)
- close: 3.24 | RSI14: 41.138618 | ATR14%: 6.88%
- MA20 gap: -7.00% | MA50 gap: -5.37% | MA200 gap: -23.39%
- vol_ratio(Volume/Vol20): 0.69001 | gap_open: 0.00%
- RS vs SILJ gap: 3.32% / slope_proxy: -0.007215
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
- close: 8.205 | RSI14: 44.042041 | ATR14%: 8.36%
- MA20 gap: -5.25% | MA50 gap: -3.76% | MA200 gap: 0.50%
- vol_ratio(Volume/Vol20): 0.556564 | gap_open: 1.17%
- SilverMarginGate: SI=74.300003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.51% / slope_proxy: -0.020495
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
- close: 31.725 | RSI14: 38.755417 | ATR14%: 11.59%
- MA20 gap: -16.81% | MA50 gap: -15.74% | MA200 gap: 38.55%
- vol_ratio(Volume/Vol20): 0.532195 | gap_open: 3.62%
- RS vs SILJ gap: -8.29% / slope_proxy: 0.027326
- RS vs GDXJ gap: -7.24% / slope_proxy: 0.007084
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
