# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-07**
- 실행시간(UTC): **2026-08-07 23:15:44**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.71
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.43
- VIX: 15.15
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 10.05% / slope_proxy: 0.011398
- GDXJ/GLD gap: 9.75% / slope_proxy: -0.007025

## VZLA (Vizsla Silver)
- close: 3.74 | RSI14: 63.680119 | ATR14%: 5.23%
- MA20 gap: 14.22% | MA50 gap: 10.61% | MA200 gap: -8.55%
- vol_ratio(Volume/Vol20): 1.864358 | gap_open: 5.38%
- RS vs SILJ gap: 1.65% / slope_proxy: 0.006042
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.4 | RSI14: 70.094375 | ATR14%: 5.93%
- MA20 gap: 25.73% | MA50 gap: 22.79% | MA200 gap: -0.61%
- vol_ratio(Volume/Vol20): 1.200218 | gap_open: 6.21%
- SilverMarginGate: SI=63.799999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.60% / slope_proxy: -0.004728
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 26.540001 | RSI14: 63.74979 | ATR14%: 7.08%
- MA20 gap: 26.48% | MA50 gap: 11.45% | MA200 gap: -5.72%
- vol_ratio(Volume/Vol20): 1.372552 | gap_open: 11.05%
- RS vs SILJ gap: -3.26% / slope_proxy: -0.145738
- RS vs GDXJ gap: -7.34% / slope_proxy: -0.036011
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
