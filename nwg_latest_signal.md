# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-12**
- 실행시간(UTC): **2026-10-14 01:22:24**

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
- TERM_SPREAD_10Y_POLICY: 164.93 bp / 4주 변화 9.53 bp
- CURVE_10s5s: 42.56 bp / 4주 변화 -1.41 bp

## NWG Price
- close: 653.6
- MA50: 689.5728 / gap50: -5.22%
- MA200: 635.2559 / gap200: 2.89%

## Relative Strength
- RS vs FTSE gap: -4.28% / slope_proxy: 0.000268
- RS vs Peers gap: 2.13% / slope_proxy: 0.01341

## Why not today?
- DemandGreen=FALSE (monthly)
