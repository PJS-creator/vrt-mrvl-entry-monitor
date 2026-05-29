# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-28**
- 실행시간(UTC): **2026-05-29 03:01:53**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (404 Client Error: Not Found for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS), using cached values if available.
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
- TERM_SPREAD_10Y_POLICY: 109.28 bp / 4주 변화 -10.65 bp
- CURVE_10s5s: 45.09 bp / 4주 변화 -1.62 bp

## NWG Price
- close: 590.2
- MA50: 576.9113 / gap50: 2.30%
- MA200: 586.8572 / gap200: 0.57%

## Relative Strength
- RS vs FTSE gap: 1.46% / slope_proxy: -0.001335
- RS vs Peers gap: -4.34% / slope_proxy: -0.028887

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE
