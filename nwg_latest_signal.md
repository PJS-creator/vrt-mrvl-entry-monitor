# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-01**
- 실행시간(UTC): **2026-10-01 15:00:55**

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
- TERM_SPREAD_10Y_POLICY: 161.4 bp / 4주 변화 23.07 bp
- CURVE_10s5s: 42.83 bp / 4주 변화 -4.34 bp

## NWG Price
- close: 652.4
- MA50: 692.9049 / gap50: -5.85%
- MA200: 634.8382 / gap200: 2.77%

## Relative Strength
- RS vs FTSE gap: -2.59% / slope_proxy: 0.000892
- RS vs Peers gap: 2.21% / slope_proxy: 0.009356

## Why not today?
- DemandGreen=FALSE (monthly)
