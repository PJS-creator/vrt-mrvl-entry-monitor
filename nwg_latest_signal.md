# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-02**
- 실행시간(UTC): **2026-10-02 15:00:50**

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
- close: 662.6
- MA50: 692.7271 / gap50: -4.35%
- MA200: 634.98 / gap200: 4.35%

## Relative Strength
- RS vs FTSE gap: -1.47% / slope_proxy: 0.000763
- RS vs Peers gap: 3.36% / slope_proxy: 0.009782

## Why not today?
- DemandGreen=FALSE (monthly)
