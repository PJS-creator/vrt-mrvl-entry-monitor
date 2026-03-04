# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-04**
- 실행시간(UTC): **2026-03-04 23:00:38**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.08 / 4주 변화 23.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 1.76 / 4주 변화 -18.0 bp
- VIX (VIXCLS): 23.57
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.60763
- MA60: 6.296661
- gap: 20.82%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.195665
- MA60: 0.214084
- gap: -8.60%
- MA60_slope_proxy: -0.019463
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-04**
- 실행시간(UTC): **2026-03-04 23:01:00**

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
- TERM_SPREAD_10Y_POLICY: 61.8 bp / 4주 변화 -13.74 bp
- CURVE_10s5s: 60.04 bp / 4주 변화 4.49 bp

## NWG Price
- close: 594.8
- MA50: 637.224 / gap50: -6.66%
- MA200: 568.2106 / gap200: 4.68%

## Relative Strength
- RS vs FTSE gap: -9.80% / slope_proxy: -0.001674
- RS vs Peers gap: -7.44% / slope_proxy: -0.056656

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-04 23:01:07**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED OVXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 76.11 / 5D 16.34%
- Brent ref (BZ=F): 82.54 / 5D 16.50%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.43
- Gas ref (NG=F): 2.93 / 5D -1.21%

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

- close: 53.61
- MA20 / MA60 / MA200: 49.38 / 44.56 / 43.68
- gap20 / gap60: 8.57% / 20.32%
- 5D return: 5.24%
- 20D high/low: 54.21 / 45.09

### Relative Strength

- ratio: 0.954084
- ratio_MA60: 0.904037
- ratio_gap: 5.54%
- ratio_slope_proxy(20d): -0.008714

### Volume (if available)

- volume: 14757937.00
- volume_MA20: 14489941.85
- volume_ratio: 1.02

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.77
- MA20 / MA60 / MA200: 15.87 / 13.75 / 12.68
- gap20 / gap60: 5.70% / 21.98%
- 5D return: 0.36%
- 20D high/low: 17.32 / 14.87

### Relative Strength

- ratio: 0.447319
- ratio_MA60: 0.391143
- ratio_gap: 14.36%
- ratio_slope_proxy(20d): 0.003706

### Volume (if available)

- volume: 19676993.00
- volume_MA20: 23065634.65
- volume_ratio: 0.85

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

- close: 6.37
- MA20 / MA60 / MA200: 6.08 / 4.93 / 3.73
- gap20 / gap60: 4.80% / 29.22%
- 5D return: -0.62%
- 20D high/low: 6.54 / 4.94

### Relative Strength

- ratio: 0.016622
- ratio_MA60: 0.014622
- ratio_gap: 13.67%
- ratio_slope_proxy(20d): 0.000408

### Volume (if available)

- volume: 33959341.00
- volume_MA20: 67768852.05
- volume_ratio: 0.50

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

- close: 11.16
- MA20 / MA60 / MA200: 9.84 / 8.32 / 11.28
- gap20 / gap60: 13.47% / 34.18%
- 5D return: 19.87%
- 20D high/low: 11.46 / 8.77

### Relative Strength

- ratio: 0.044823
- ratio_MA60: 0.039945
- ratio_gap: 12.21%
- ratio_slope_proxy(20d): 0.002658

### Volume (if available)

- volume: 36778033.00
- volume_MA20: 14393586.65
- volume_ratio: 2.56

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

- 데이터 기준일(주가): **2026-03-04**
- 실행시간(UTC): **2026-03-04 23:01:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.08
- IG OAS 4주 변화: 10.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -15.0 bp / latest 1.77
- VIX: 23.57
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 9.35% / slope_proxy: -0.003661
- GDXJ/GLD gap: 2.70% / slope_proxy: 0.014118

## VZLA (Vizsla Silver)
- close: 4.16 | RSI14: 44.006136 | ATR14%: 8.36%
- MA20 gap: 2.12% | MA50 gap: -19.18% | MA200 gap: 0.60%
- vol_ratio(Volume/Vol20): 0.225491 | gap_open: 2.97%
- RS vs SILJ gap: -30.06% / slope_proxy: -0.026831
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.36 | RSI14: 43.647732 | ATR14%: 10.85%
- MA20 gap: -7.38% | MA50 gap: -9.25% | MA200 gap: 55.20%
- vol_ratio(Volume/Vol20): 0.872536 | gap_open: 0.18%
- SilverMarginGate: SI=83.764999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.94% / slope_proxy: 0.017444
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
- close: 47.665001 | RSI14: 57.006966 | ATR14%: 12.41%
- MA20 gap: 14.18% | MA50 gap: 28.54% | MA200 gap: 245.59%
- vol_ratio(Volume/Vol20): 0.76693 | gap_open: 3.71%
- RS vs SILJ gap: 31.87% / slope_proxy: 0.248235
- RS vs GDXJ gap: 33.69% / slope_proxy: 0.065444
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
