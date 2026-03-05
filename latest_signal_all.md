# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-05**
- 실행시간(UTC): **2026-03-05 15:00:39**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.08 / 4주 변화 23.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 1.77 / 4주 변화 -15.0 bp
- VIX (VIXCLS): 21.15
- NFCI: -0.5236

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.946897
- MA60: 6.320905
- gap: 25.72%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.197505
- MA60: 0.212842
- gap: -7.21%
- MA60_slope_proxy: -0.019481
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-05**
- 실행시간(UTC): **2026-03-05 15:01:22**

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
- TERM_SPREAD_10Y_POLICY: 73.12 bp / 4주 변화 -2.92 bp
- CURVE_10s5s: 56.65 bp / 4주 변화 1.42 bp

## NWG Price
- close: 593.4
- MA50: 636.172 / gap50: -6.72%
- MA200: 568.5581 / gap200: 4.37%

## Relative Strength
- RS vs FTSE gap: -9.09% / slope_proxy: -0.001817
- RS vs Peers gap: -6.85% / slope_proxy: -0.058223

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-05 15:01:37**

## Commodity Regime

- WTI ref (CL=F): 78.00 / 5D 19.61%
- Brent ref (BZ=F): 84.00 / 5D 18.73%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.00
- Gas ref (NG=F): 2.95 / 5D 4.21%

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

- close: 54.26
- MA20 / MA60 / MA200: 49.76 / 44.76 / 43.74
- gap20 / gap60: 9.05% / 21.23%
- 5D return: 5.50%
- 20D high/low: 54.26 / 45.09

### Relative Strength

- ratio: 0.956292
- ratio_MA60: 0.904533
- ratio_gap: 5.72%
- ratio_slope_proxy(20d): -0.007687

### Volume (if available)

- volume: 2465912.00
- volume_MA20: 13704060.60
- volume_ratio: 0.18

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.76
- MA20 / MA60 / MA200: 15.95 / 13.83 / 12.71
- gap20 / gap60: 5.10% / 21.23%
- 5D return: 0.90%
- 20D high/low: 17.32 / 14.87

### Relative Strength

- ratio: 0.452728
- ratio_MA60: 0.392256
- ratio_gap: 15.42%
- ratio_slope_proxy(20d): 0.004532

### Volume (if available)

- volume: 4510235.00
- volume_MA20: 22055881.75
- volume_ratio: 0.20

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

- close: 6.38
- MA20 / MA60 / MA200: 6.13 / 4.96 / 3.75
- gap20 / gap60: 4.00% / 28.48%
- 5D return: -0.08%
- 20D high/low: 6.54 / 4.94

### Relative Strength

- ratio: 0.016806
- ratio_MA60: 0.014657
- ratio_gap: 14.67%
- ratio_slope_proxy(20d): 0.000430

### Volume (if available)

- volume: 2792480.00
- volume_MA20: 65526494.00
- volume_ratio: 0.04

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

- close: 12.18
- MA20 / MA60 / MA200: 9.96 / 8.41 / 11.29
- gap20 / gap60: 22.19% / 44.82%
- 5D return: 28.56%
- 20D high/low: 12.18 / 8.77

### Relative Strength

- ratio: 0.048483
- ratio_MA60: 0.040201
- ratio_gap: 20.60%
- ratio_slope_proxy(20d): 0.002785

### Volume (if available)

- volume: 7296065.00
- volume_MA20: 14230033.25
- volume_ratio: 0.51

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

- 데이터 기준일(주가): **2026-03-05**
- 실행시간(UTC): **2026-03-05 15:01:46**

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
- VIX: 21.15
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 5.94% / slope_proxy: -0.002848
- GDXJ/GLD gap: 0.43% / slope_proxy: 0.013786

## VZLA (Vizsla Silver)
- close: 4.11 | RSI14: 43.138977 | ATR14%: 8.12%
- MA20 gap: 1.93% | MA50 gap: -19.76% | MA200 gap: -0.81%
- vol_ratio(Volume/Vol20): 0.044493 | gap_open: 2.40%
- RS vs SILJ gap: -28.08% / slope_proxy: -0.027611
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
- close: 10.008 | RSI14: 41.924221 | ATR14%: 10.82%
- MA20 gap: -9.54% | MA50 gap: -12.55% | MA200 gap: 48.97%
- vol_ratio(Volume/Vol20): 0.184106 | gap_open: 2.12%
- SilverMarginGate: SI=82.540001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.00% / slope_proxy: 0.014401
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
- close: 45.654999 | RSI14: 54.180073 | ATR14%: 12.54%
- MA20 gap: 8.54% | MA50 gap: 21.21% | MA200 gap: 225.96%
- vol_ratio(Volume/Vol20): 0.149284 | gap_open: 2.17%
- RS vs SILJ gap: 28.54% / slope_proxy: 0.248389
- RS vs GDXJ gap: 29.42% / slope_proxy: 0.06543
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
