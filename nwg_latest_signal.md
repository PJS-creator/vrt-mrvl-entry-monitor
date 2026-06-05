# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-04**
- 실행시간(UTC): **2026-06-05 03:01:40**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **True**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 108.14 bp / 4주 변화 -18.87 bp
- CURVE_10s5s: 44.22 bp / 4주 변화 -1.41 bp

## NWG Price
- close: 601.4
- MA50: 580.7571 / gap50: 3.55%
- MA200: 588.1466 / gap200: 2.25%

## Relative Strength
- RS vs FTSE gap: 2.19% / slope_proxy: -0.000531
- RS vs Peers gap: -1.88% / slope_proxy: -0.020468

## Why not today?
- CurveGreen=FALSE
- RelativeTurn=FALSE
