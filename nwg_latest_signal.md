# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-09**
- 실행시간(UTC): **2026-10-10 03:00:55**

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
- close: 639.8
- MA50: 691.4362 / gap50: -7.47%
- MA200: 635.2483 / gap200: 0.72%

## Relative Strength
- RS vs FTSE gap: -4.47% / slope_proxy: 0.000433
- RS vs Peers gap: 3.45% / slope_proxy: 0.012433

## Why not today?
- DemandGreen=FALSE (monthly)
