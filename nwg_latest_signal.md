# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-05**
- 실행시간(UTC): **2026-10-05 15:00:48**

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
- TERM_SPREAD_10Y_POLICY: 161.65 bp / 4주 변화 28.22 bp
- CURVE_10s5s: 45.33 bp / 4주 변화 -2.25 bp

## NWG Price
- close: 664.8
- MA50: 692.5094 / gap50: -4.00%
- MA200: 635.1178 / gap200: 4.67%

## Relative Strength
- RS vs FTSE gap: -1.33% / slope_proxy: 0.000669
- RS vs Peers gap: 2.25% / slope_proxy: 0.010264

## Why not today?
- DemandGreen=FALSE (monthly)
