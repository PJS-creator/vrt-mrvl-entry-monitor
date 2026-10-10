# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-09**
- 실행시간(UTC): **2026-10-10 15:00:44**

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
- TERM_SPREAD_10Y_POLICY: 163.52 bp / 4주 변화 19.3 bp
- CURVE_10s5s: 44.24 bp / 4주 변화 -1.48 bp

## NWG Price
- close: 642.6
- MA50: 690.6145 / gap50: -6.95%
- MA200: 635.2201 / gap200: 1.16%

## Relative Strength
- RS vs FTSE gap: -5.01% / slope_proxy: 0.000336
- RS vs Peers gap: 2.73% / slope_proxy: 0.012989

## Why not today?
- DemandGreen=FALSE (monthly)
