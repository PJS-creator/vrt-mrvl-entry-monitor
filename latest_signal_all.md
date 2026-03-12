# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-12**
- 실행시간(UTC): **2026-03-12 15:00:41**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.06 / 4주 변화 20.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 7.0 bp
- 10Y Real Yield (DFII10): 1.78 / 4주 변화 -9.0 bp
- VIX (VIXCLS): 24.93
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.067227
- MA60: 6.525376
- gap: 23.63%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.228338
- MA60: 0.21172
- gap: 7.85%
- MA60_slope_proxy: -0.015807
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-12**
- 실행시간(UTC): **2026-03-12 15:02:25**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: 75.1 bp / 4주 변화 0.31 bp
- CURVE_10s5s: 50.8 bp / 4주 변화 -8.84 bp

## NWG Price
- close: 568.2
- MA50: 629.06 / gap50: -9.67%
- MA200: 569.9414 / gap200: -0.31%

## Relative Strength
- RS vs FTSE gap: -10.44% / slope_proxy: -0.002223
- RS vs Peers gap: -2.43% / slope_proxy: -0.057292

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-12 15:03:53**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DCOILBRENTEU failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DHHNGSP failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED OVXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DTWEXBGS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VXEWZCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 95.65 / 5D 18.07%
- Brent ref (BZ=F): 96.21 / 5D 12.64%
- Brent Tier: **>=90**
- Brent-WTI spread: 0.56
- Gas ref (NG=F): 3.22 / 5D 7.09%

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

- close: 58.60
- MA20 / MA60 / MA200: 51.75 / 45.70 / 43.89
- gap20 / gap60: 13.25% / 28.23%
- 5D return: 10.60%
- 20D high/low: 58.60 / 45.28

### Relative Strength

- ratio: 1.015333
- ratio_MA60: 0.905743
- ratio_gap: 12.10%
- ratio_slope_proxy(20d): 0.002926

### Volume (if available)

- volume: 17459286.00
- volume_MA20: 18393264.30
- volume_ratio: 0.95

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.70
- MA20 / MA60 / MA200: 16.71 / 14.33 / 12.88
- gap20 / gap60: 11.90% / 30.46%
- 5D return: 11.75%
- 20D high/low: 18.99 / 15.02

### Relative Strength

- ratio: 0.517652
- ratio_MA60: 0.401651
- ratio_gap: 28.88%
- ratio_slope_proxy(20d): 0.014793

### Volume (if available)

- volume: 16178678.00
- volume_MA20: 28759203.90
- volume_ratio: 0.56

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

- close: 6.24
- MA20 / MA60 / MA200: 6.28 / 5.11 / 3.84
- gap20 / gap60: -0.70% / 22.09%
- 5D return: 1.80%
- 20D high/low: 6.54 / 5.93

### Relative Strength

- ratio: 0.016818
- ratio_MA60: 0.014802
- ratio_gap: 13.62%
- ratio_slope_proxy(20d): 0.000547

### Volume (if available)

- volume: 7783908.00
- volume_MA20: 49295270.40
- volume_ratio: 0.16

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

- close: 12.96
- MA20 / MA60 / MA200: 10.54 / 8.90 / 11.33
- gap20 / gap60: 22.91% / 45.69%
- 5D return: 5.54%
- 20D high/low: 12.96 / 8.77

### Relative Strength

- ratio: 0.050714
- ratio_MA60: 0.041529
- ratio_gap: 22.12%
- ratio_slope_proxy(20d): 0.003446

### Volume (if available)

- volume: 9291124.00
- volume_MA20: 19305586.20
- volume_ratio: 0.48

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

- 데이터 기준일(주가): **2026-03-12**
- 실행시간(UTC): **2026-03-12 15:07:25**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.06
- IG OAS 4주 변화: 7.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -9.0 bp / latest 1.78
- VIX: 24.93
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -2.36% / slope_proxy: -0.003658
- GDXJ/GLD gap: -5.76% / slope_proxy: 0.011386

## VZLA (Vizsla Silver)
- close: 3.915 | RSI14: 40.40867 | ATR14%: 7.90%
- MA20 gap: -1.86% | MA50 gap: -20.93% | MA200 gap: -6.30%
- vol_ratio(Volume/Vol20): 0.161519 | gap_open: 0.98%
- RS vs SILJ gap: -23.64% / slope_proxy: -0.028664
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 9.9918 | RSI14: 42.715406 | ATR14%: 9.96%
- MA20 gap: -7.36% | MA50 gap: -12.88% | MA200 gap: 44.16%
- vol_ratio(Volume/Vol20): 0.340474 | gap_open: 0.00%
- SilverMarginGate: SI=85.699997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.12% / slope_proxy: 0.001545
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
- close: 40.195 | RSI14: 47.763308 | ATR14%: 13.74%
- MA20 gap: -6.95% | MA50 gap: 2.49% | MA200 gap: 168.93%
- vol_ratio(Volume/Vol20): 0.194128 | gap_open: 0.40%
- RS vs SILJ gap: 14.02% / slope_proxy: 0.250629
- RS vs GDXJ gap: 13.75% / slope_proxy: 0.065802
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
