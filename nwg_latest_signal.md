# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-02**
- 실행시간(UTC): **2026-10-05 03:00:49**

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
- close: 662.8
- MA50: 692.7311 / gap50: -4.32%
- MA200: 634.981 / gap200: 4.38%

## Relative Strength
- RS vs FTSE gap: -1.23% / slope_proxy: 0.000766
- RS vs Peers gap: 3.15% / slope_proxy: 0.009749

## Why not today?
- DemandGreen=FALSE (monthly)
