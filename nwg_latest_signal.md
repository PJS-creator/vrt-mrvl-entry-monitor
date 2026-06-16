# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-16**
- 실행시간(UTC): **2026-06-16 15:02:22**

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
- TERM_SPREAD_10Y_POLICY: 106.56 bp / 4주 변화 -31.07 bp
- CURVE_10s5s: 46.07 bp / 4주 변화 -1.35 bp

## NWG Price
- close: 627.7002
- MA50: 589.8151 / gap50: 6.42%
- MA200: 590.3568 / gap200: 6.33%

## Relative Strength
- RS vs FTSE gap: 6.55% / slope_proxy: 0.000156
- RS vs Peers gap: -0.38% / slope_proxy: -0.020064

## Why not today?
- CurveGreen=FALSE
- PullbackZone=FALSE
- RelativeTurn=FALSE
