# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-12**
- 실행시간(UTC): **2026-10-12 15:00:53**

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
- TERM_SPREAD_10Y_POLICY: 167.92 bp / 4주 변화 11.02 bp
- CURVE_10s5s: 43.54 bp / 4주 변화 1.13 bp

## NWG Price
- close: 650.8
- MA50: 689.5168 / gap50: -5.62%
- MA200: 635.2419 / gap200: 2.45%

## Relative Strength
- RS vs FTSE gap: -4.42% / slope_proxy: 0.000266
- RS vs Peers gap: 2.11% / slope_proxy: 0.013408

## Why not today?
- DemandGreen=FALSE (monthly)
