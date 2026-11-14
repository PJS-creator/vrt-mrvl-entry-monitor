# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-13**
- 실행시간(UTC): **2026-11-14 03:00:48**

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
- CURVE_10s5s: 31.92 bp / 4주 변화 -9.46 bp

## NWG Price
- close: 597.2
- MA50: 655.564 / gap50: -8.90%
- MA200: 632.513 / gap200: -5.58%

## Relative Strength
- RS vs FTSE gap: -10.84% / slope_proxy: -0.002351
- RS vs Peers gap: -3.91% / slope_proxy: 0.010865

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE
