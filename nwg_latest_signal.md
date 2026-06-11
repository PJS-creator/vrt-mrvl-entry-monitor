# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-11**
- 실행시간(UTC): **2026-06-11 15:01:54**

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
- TERM_SPREAD_10Y_POLICY: 113.73 bp / 4주 변화 -16.54 bp
- CURVE_10s5s: 45.0 bp / 4주 변화 -0.52 bp

## NWG Price
- close: 589.3
- MA50: 586.3511 / gap50: 0.50%
- MA200: 589.0367 / gap200: 0.04%

## Relative Strength
- RS vs FTSE gap: 1.70% / slope_proxy: -6.4e-05
- RS vs Peers gap: -0.24% / slope_proxy: -0.019815

## Why not today?
- CurveGreen=FALSE
- RelativeTurn=FALSE
