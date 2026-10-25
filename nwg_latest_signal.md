# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-23**
- 실행시간(UTC): **2026-10-25 00:30:16**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- BoE IUDMNPY failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.
- BoE IUDSNPY failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: None bp / 4주 변화 None bp
- CURVE_10s5s: None bp / 4주 변화 None bp

## NWG Price
- close: 627.4
- MA50: 678.736 / gap50: -7.56%
- MA200: 635.3695 / gap200: -1.25%

## Relative Strength
- RS vs FTSE gap: -7.96% / slope_proxy: -0.000336
- RS vs Peers gap: 2.54% / slope_proxy: 0.020721

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE
