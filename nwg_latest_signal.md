# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-06**
- 실행시간(UTC): **2026-03-09 03:02:21**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (502 Server Error: Bad Gateway for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM), using cached values if available.
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
- TERM_SPREAD_10Y_POLICY: 68.12 bp / 4주 변화 -10.24 bp
- CURVE_10s5s: 58.29 bp / 4주 변화 2.0 bp

## NWG Price
- close: 575.6
- MA50: 634.564 / gap50: -9.29%
- MA200: 568.7835 / gap200: 1.20%

## Relative Strength
- RS vs FTSE gap: -9.92% / slope_proxy: -0.00198
- RS vs Peers gap: -6.02% / slope_proxy: -0.059417

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE
