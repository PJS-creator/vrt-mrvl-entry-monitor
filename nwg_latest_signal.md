# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-30 15:01:38**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

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
- TERM_SPREAD_10Y_POLICY: 107.59 bp / 4주 변화 -17.94 bp
- CURVE_10s5s: 45.99 bp / 4주 변화 1.7 bp

## NWG Price
- close: 599.4
- MA50: 577.4358 / gap50: 3.80%
- MA200: 587.1723 / gap200: 2.08%

## Relative Strength
- RS vs FTSE gap: 3.15% / slope_proxy: -0.001131
- RS vs Peers gap: -3.73% / slope_proxy: -0.027043

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE
