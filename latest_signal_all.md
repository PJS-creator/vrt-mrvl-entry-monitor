# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-12**
- 실행시간(UTC): **2026-05-12 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.79 / 4주 변화 -16.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 1.93 / 4주 변화 -2.0 bp
- VIX (VIXCLS): 18.38
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.196868
- MA60: 8.48236
- gap: 20.21%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.294573
- MA60: 0.259208
- gap: 13.64%
- MA60_slope_proxy: 0.038249
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-12**
- 실행시간(UTC): **2026-05-12 15:01:11**

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
- TERM_SPREAD_10Y_POLICY: 111.95 bp / 4주 변화 11.15 bp
- CURVE_10s5s: 44.44 bp / 4주 변화 -1.45 bp

## NWG Price
- close: 560.4
- MA50: 578.6401 / gap50: -3.15%
- MA200: 583.788 / gap200: -4.01%

## Relative Strength
- RS vs FTSE gap: -2.53% / slope_proxy: -0.002313
- RS vs Peers gap: -4.84% / slope_proxy: -0.036851

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-12 15:01:20**

## ⚠️ DATA WARNING

- FRED DCOILBRENTEU failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DHHNGSP failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DTWEXBGS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VXEWZCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 101.83 / 5D -0.43%
- Brent ref (BZ=F): 107.84 / 5D -1.85%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.01
- Gas ref (NG=F): 2.83 / 5D 1.51%

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

- close: 55.90
- MA20 / MA60 / MA200: 56.90 / 56.97 / 47.25
- gap20 / gap60: -1.75% / -1.88%
- 5D return: -5.80%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.973868
- ratio_MA60: 0.992173
- ratio_gap: -1.85%
- ratio_slope_proxy(20d): 0.038359

### Volume (if available)

- volume: 3172861.00
- volume_MA20: 12494088.05
- volume_ratio: 0.25

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.61
- MA20 / MA60 / MA200: 21.08 / 19.43 / 14.62
- gap20 / gap60: -2.25% / 6.06%
- 5D return: -5.35%
- 20D high/low: 22.03 / 20.33

### Relative Strength

- ratio: 0.538975
- ratio_MA60: 0.503507
- ratio_gap: 7.04%
- ratio_slope_proxy(20d): 0.044694

### Volume (if available)

- volume: 9249220.00
- volume_MA20: 18971856.00
- volume_ratio: 0.49

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

- close: 6.54
- MA20 / MA60 / MA200: 6.38 / 6.41 / 4.61
- gap20 / gap60: 2.61% / 2.08%
- 5D return: 4.72%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015218
- ratio_MA60: 0.015865
- ratio_gap: -4.08%
- ratio_slope_proxy(20d): 0.000166

### Volume (if available)

- volume: 7541141.00
- volume_MA20: 35470422.05
- volume_ratio: 0.21

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

- close: 12.95
- MA20 / MA60 / MA200: 12.35 / 12.75 / 10.92
- gap20 / gap60: 4.79% / 1.51%
- 5D return: -0.58%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.052853
- ratio_MA60: 0.049105
- ratio_gap: 7.63%
- ratio_slope_proxy(20d): 0.001001

### Volume (if available)

- volume: 12891065.00
- volume_MA20: 19688603.25
- volume_ratio: 0.65

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-12**
- 실행시간(UTC): **2026-05-12 15:02:44**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -16.0 bp / latest 2.79
- IG OAS 4주 변화: -4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: -2.0 bp / latest 1.93
- VIX: 18.38
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -3.82% / slope_proxy: 0.004238
- GDXJ/GLD gap: 3.03% / slope_proxy: -0.003879

## VZLA (Vizsla Silver)
- close: 3.665 | RSI14: 57.333958 | ATR14%: 5.55%
- MA20 gap: 6.33% | MA50 gap: 5.62% | MA200 gap: -13.05%
- vol_ratio(Volume/Vol20): 0.28099 | gap_open: 2.41%
- RS vs SILJ gap: -0.41% / slope_proxy: -0.013358
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
- close: 9.312 | RSI14: 58.406522 | ATR14%: 6.83%
- MA20 gap: 8.40% | MA50 gap: 7.82% | MA200 gap: 16.10%
- vol_ratio(Volume/Vol20): 0.368386 | gap_open: 2.12%
- SilverMarginGate: SI=85.309998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.42% / slope_proxy: -0.027432
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
- close: 42.18 | RSI14: 56.627855 | ATR14%: 8.47%
- MA20 gap: 7.79% | MA50 gap: 10.39% | MA200 gap: 91.39%
- vol_ratio(Volume/Vol20): 0.351466 | gap_open: 3.80%
- RS vs SILJ gap: 3.90% / slope_proxy: 0.032827
- RS vs GDXJ gap: 7.80% / slope_proxy: 0.005959
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
