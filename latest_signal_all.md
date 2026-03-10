# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-09**
- 실행시간(UTC): **2026-03-10 03:00:42**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.13 / 4주 변화 26.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 8.0 bp
- 10Y Real Yield (DFII10): 1.8 / 4주 변화 -8.0 bp
- VIX (VIXCLS): 29.49
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.169036
- MA60: 6.41502
- gap: 27.34%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.234932
- MA60: 0.212383
- gap: 10.62%
- MA60_slope_proxy: -0.017812
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-09**
- 실행시간(UTC): **2026-03-10 03:00:49**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 74.8 bp / 4주 변화 -4.43 bp
- CURVE_10s5s: 55.53 bp / 4주 변화 -4.12 bp

## NWG Price
- close: 575.8
- MA50: 633.144 / gap50: -9.06%
- MA200: 569.043 / gap200: 1.19%

## Relative Strength
- RS vs FTSE gap: -9.38% / slope_proxy: -0.002058
- RS vs Peers gap: -5.72% / slope_proxy: -0.059005

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-10 03:00:56**

## Commodity Regime

- WTI ref (CL=F): 87.64 / 5D 23.04%
- Brent ref (BZ=F): 91.16 / 5D 17.26%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.52
- Gas ref (NG=F): 3.12 / 5D 5.27%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 55.02
- MA20 / MA60 / MA200: 50.60 / 45.19 / 43.86
- gap20 / gap60: 8.74% / 21.76%
- 5D return: 1.49%
- 20D high/low: 55.02 / 45.49

### Relative Strength

- ratio: 0.976918
- ratio_MA60: 0.906141
- ratio_gap: 7.81%
- ratio_slope_proxy(20d): -0.004084

### Volume (if available)

- volume: 32374239.00
- volume_MA20: 16572746.95
- volume_ratio: 1.95

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.16
- MA20 / MA60 / MA200: 16.25 / 14.01 / 12.77
- gap20 / gap60: 11.79% / 29.61%
- 5D return: 4.85%
- 20D high/low: 18.16 / 15.02

### Relative Strength

- ratio: 0.489488
- ratio_MA60: 0.395684
- ratio_gap: 23.71%
- ratio_slope_proxy(20d): 0.008361

### Volume (if available)

- volume: 71816397.00
- volume_MA20: 27138634.85
- volume_ratio: 2.65

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

- close: 6.17
- MA20 / MA60 / MA200: 6.21 / 5.01 / 3.78
- gap20 / gap60: -0.58% / 23.12%
- 5D return: -1.28%
- 20D high/low: 6.54 / 5.44

### Relative Strength

- ratio: 0.016275
- ratio_MA60: 0.014685
- ratio_gap: 10.82%
- ratio_slope_proxy(20d): 0.000462

### Volume (if available)

- volume: 41044256.00
- volume_MA20: 67307022.80
- volume_ratio: 0.61

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.51
- MA20 / MA60 / MA200: 10.21 / 8.59 / 11.31
- gap20 / gap60: 12.76% / 34.02%
- 5D return: 1.14%
- 20D high/low: 12.48 / 8.77

### Relative Strength

- ratio: 0.045893
- ratio_MA60: 0.040623
- ratio_gap: 12.97%
- ratio_slope_proxy(20d): 0.003099

### Volume (if available)

- volume: 30887640.00
- volume_MA20: 17772337.00
- volume_ratio: 1.74

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-09**
- 실행시간(UTC): **2026-03-10 03:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 26.0 bp / latest 3.13
- IG OAS 4주 변화: 8.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.8
- VIX: 29.49
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: -0.48% / slope_proxy: -0.002831
- GDXJ/GLD gap: -1.59% / slope_proxy: 0.013427

## VZLA (Vizsla Silver)
- close: 3.99 | RSI14: 41.082976 | ATR14%: 8.36%
- MA20 gap: 0.13% | MA50 gap: -20.99% | MA200 gap: -4.05%
- vol_ratio(Volume/Vol20): 0.405229 | gap_open: 3.00%
- RS vs SILJ gap: -27.00% / slope_proxy: -0.028919
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.1 | RSI14: 42.679789 | ATR14%: 10.57%
- MA20 gap: -8.13% | MA50 gap: -11.99% | MA200 gap: 48.46%
- vol_ratio(Volume/Vol20): 1.884312 | gap_open: 4.39%
- SilverMarginGate: SI=90.019997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.61% / slope_proxy: 0.009921
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 40.599998 | RSI14: 48.437988 | ATR14%: 14.50%
- MA20 gap: -4.21% | MA50 gap: 6.48% | MA200 gap: 182.88%
- vol_ratio(Volume/Vol20): 0.85391 | gap_open: 2.69%
- RS vs SILJ gap: 14.93% / slope_proxy: 0.246037
- RS vs GDXJ gap: 14.05% / slope_proxy: 0.064624
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
