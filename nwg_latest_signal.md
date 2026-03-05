# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-04**
- 실행시간(UTC): **2026-03-05 07:01:26**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
