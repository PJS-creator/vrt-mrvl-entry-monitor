# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-08**
- 실행시간(UTC): **2026-10-08 15:00:45**

## Verdict
🟡 ENTRY (LOOSE): Risk+Curve + PriceConfirm (Demand monthly not confirmed)

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **True**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **True**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 158.68 bp / 4주 변화 23.89 bp
- CURVE_10s5s: 43.69 bp / 4주 변화 -2.26 bp

## NWG Price
- close: 644.8
- MA50: 691.5362 / gap50: -6.76%
- MA200: 635.2733 / gap200: 1.50%

## Relative Strength
- RS vs FTSE gap: -3.96% / slope_proxy: 0.000438
- RS vs Peers gap: 3.52% / slope_proxy: 0.012444

## Why not today?
- DemandGreen=FALSE (monthly)
