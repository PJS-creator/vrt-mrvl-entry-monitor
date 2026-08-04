# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-03**
- 실행시간(UTC): **2026-08-04 23:39:00**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- BoE IUDBEDR failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- CURVE_10s5s: 46.88 bp / 4주 변화 -1.83 bp

## NWG Price
- close: 722.8
- MA50: 645.82 / gap50: 11.92%
- MA200: 614.3698 / gap200: 17.65%

## Relative Strength
- RS vs FTSE gap: 10.38% / slope_proxy: 0.002156
- RS vs Peers gap: 3.54% / slope_proxy: -0.001687

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE
