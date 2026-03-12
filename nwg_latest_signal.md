# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-11**
- 실행시간(UTC): **2026-03-12 03:02:21**

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
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 83.29 bp / 4주 변화 5.19 bp
- CURVE_10s5s: 49.01 bp / 4주 변화 -12.14 bp

## NWG Price
- close: 588.0
- MA50: 630.732 / gap50: -6.78%
- MA200: 569.723 / gap200: 3.21%

## Relative Strength
- RS vs FTSE gap: -8.05% / slope_proxy: -0.002143
- RS vs Peers gap: -5.37% / slope_proxy: -0.057965

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE
