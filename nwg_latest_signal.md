# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-14**
- 실행시간(UTC): **2026-10-14 15:01:26**

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
- TERM_SPREAD_10Y_POLICY: 163.68 bp / 4주 변화 1.69 bp
- CURVE_10s5s: 41.46 bp / 4주 변화 -1.32 bp

## NWG Price
- close: 665.4
- MA50: 687.4537 / gap50: -3.21%
- MA200: 635.4266 / gap200: 4.72%

## Relative Strength
- RS vs FTSE gap: -2.81% / slope_proxy: 0.000162
- RS vs Peers gap: 4.91% / slope_proxy: 0.014335

## Why not today?
- DemandGreen=FALSE (monthly)
