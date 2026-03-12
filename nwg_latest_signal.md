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
