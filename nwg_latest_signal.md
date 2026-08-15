# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-14**
- 실행시간(UTC): **2026-08-15 03:00:48**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- BoE IUDBEDR failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.
- BoE IUDSOIA failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.
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
- close: 705.6
- MA50: 664.2588 / gap50: 6.22%
- MA200: 620.574 / gap200: 13.70%

## Relative Strength
- RS vs FTSE gap: 6.19% / slope_proxy: 0.002923
- RS vs Peers gap: 3.34% / slope_proxy: 0.011331

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE
