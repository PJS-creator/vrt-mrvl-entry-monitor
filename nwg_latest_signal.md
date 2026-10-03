# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-02**
- 실행시간(UTC): **2026-10-03 03:00:44**

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
- TERM_SPREAD_10Y_POLICY: 162.14 bp / 4주 변화 20.04 bp
- CURVE_10s5s: 44.9 bp / 4주 변화 -2.45 bp

## NWG Price
- close: 651.4
- MA50: 692.8849 / gap50: -5.99%
- MA200: 634.8332 / gap200: 2.61%

## Relative Strength
- RS vs FTSE gap: -2.62% / slope_proxy: 0.000892
- RS vs Peers gap: 2.06% / slope_proxy: 0.009331

## Why not today?
- DemandGreen=FALSE (monthly)
