# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-30**
- 실행시간(UTC): **2026-05-01 03:00:38**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.82 / 4주 변화 -34.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -6.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 -6.0 bp
- VIX (VIXCLS): 18.81
- NFCI: -0.518

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.326802
- MA60: 8.060168
- gap: 15.71%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.32592
- MA60: 0.244266
- gap: 33.43%
- MA60_slope_proxy: 0.032337
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-30**
- 실행시간(UTC): **2026-05-01 03:00:42**

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
- TERM_SPREAD_10Y_POLICY: 119.93 bp / 4주 변화 8.78 bp
- CURVE_10s5s: 46.71 bp / 4주 변화 4.46 bp

## NWG Price
- close: 585.2
- MA50: 585.4128 / gap50: -0.04%
- MA200: 581.4586 / gap200: 0.64%

## Relative Strength
- RS vs FTSE gap: -0.68% / slope_proxy: -0.002368
- RS vs Peers gap: -4.80% / slope_proxy: -0.036415

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-01 03:00:50**

## Commodity Regime

- WTI ref (CL=F): 106.00 / 5D 10.59%
- Brent ref (BZ=F): 111.90 / 5D 6.50%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.90
- Gas ref (NG=F): 2.77 / 5D 6.04%

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

- close: 60.58
- MA20 / MA60 / MA200: 58.26 / 55.58 / 46.72
- gap20 / gap60: 3.99% / 8.99%
- 5D return: 4.76%
- 20D high/low: 62.97 / 53.79

### Relative Strength

- ratio: 1.015591
- ratio_MA60: 0.976845
- ratio_gap: 3.97%
- ratio_slope_proxy(20d): 0.037761

### Volume (if available)

- volume: 10367662.00
- volume_MA20: 13752403.10
- volume_ratio: 0.75

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 22.03
- MA20 / MA60 / MA200: 20.96 / 18.63 / 14.25
- gap20 / gap60: 5.09% / 18.22%
- 5D return: 4.18%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.554912
- ratio_MA60: 0.484765
- ratio_gap: 14.47%
- ratio_slope_proxy(20d): 0.046939

### Volume (if available)

- volume: 14058792.00
- volume_MA20: 23548644.60
- volume_ratio: 0.60

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

- close: 6.82
- MA20 / MA60 / MA200: 6.41 / 6.30 / 4.46
- gap20 / gap60: 6.44% / 8.19%
- 5D return: 12.54%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015215
- ratio_MA60: 0.015909
- ratio_gap: -4.36%
- ratio_slope_proxy(20d): 0.000553

### Volume (if available)

- volume: 38457287.00
- volume_MA20: 31787459.35
- volume_ratio: 1.21

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.27
- MA20 / MA60 / MA200: 13.00 / 12.39 / 11.03
- gap20 / gap60: 2.05% / 7.11%
- 5D return: 2.47%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.048263
- ratio_MA60: 0.048505
- ratio_gap: -0.50%
- ratio_slope_proxy(20d): 0.002301

### Volume (if available)

- volume: 17967428.00
- volume_MA20: 23788886.40
- volume_ratio: 0.76

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-30**
- 실행시간(UTC): **2026-05-01 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.82
- IG OAS 4주 변화: -6.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -6.0 bp / latest 1.96
- VIX: 18.81
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.12% / slope_proxy: 0.014608
- GDXJ/GLD gap: -4.45% / slope_proxy: -0.003881

## VZLA (Vizsla Silver)
- close: 3.38 | RSI14: 47.347175 | ATR14%: 5.86%
- MA20 gap: 0.27% | MA50 gap: -5.13% | MA200 gap: -19.66%
- vol_ratio(Volume/Vol20): 0.56215 | gap_open: 3.24%
- RS vs SILJ gap: 2.02% / slope_proxy: -0.022557
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
- close: 7.86 | RSI14: 41.936605 | ATR14%: 8.10%
- MA20 gap: -6.53% | MA50 gap: -14.14% | MA200 gap: 0.29%
- vol_ratio(Volume/Vol20): 1.176477 | gap_open: 2.85%
- SilverMarginGate: SI=74.629997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.56% / slope_proxy: -0.031417
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
- close: 36.459999 | RSI14: 46.607382 | ATR14%: 9.30%
- MA20 gap: -5.64% | MA50 gap: -7.65% | MA200 gap: 76.77%
- vol_ratio(Volume/Vol20): 0.71475 | gap_open: 5.99%
- RS vs SILJ gap: 3.36% / slope_proxy: 0.037459
- RS vs GDXJ gap: 3.73% / slope_proxy: 0.005823
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
