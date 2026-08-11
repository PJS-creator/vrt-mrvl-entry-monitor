# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-11**
- 실행시간(UTC): **2026-08-11 23:22:27**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.7
- IG OAS 4주 변화: 0.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 7.0 bp / latest 2.43
- VIX: 15.46
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 10.89% / slope_proxy: 0.012888
- GDXJ/GLD gap: 9.99% / slope_proxy: -0.006011

## VZLA (Vizsla Silver)
- close: 3.83 | RSI14: 64.66448 | ATR14%: 4.98%
- MA20 gap: 14.36% | MA50 gap: 13.24% | MA200 gap: -6.29%
- vol_ratio(Volume/Vol20): 1.069471 | gap_open: 0.77%
- RS vs SILJ gap: 0.51% / slope_proxy: 0.005993
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
- close: 9.06 | RSI14: 74.677688 | ATR14%: 5.63%
- MA20 gap: 30.54% | MA50 gap: 31.76% | MA200 gap: 6.79%
- vol_ratio(Volume/Vol20): 1.118451 | gap_open: 0.22%
- SilverMarginGate: SI=64.964996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.49% / slope_proxy: -0.003706
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
- close: 27.530001 | RSI14: 66.020084 | ATR14%: 6.58%
- MA20 gap: 27.40% | MA50 gap: 16.72% | MA200 gap: -2.89%
- vol_ratio(Volume/Vol20): 0.774374 | gap_open: 0.29%
- RS vs SILJ gap: -1.61% / slope_proxy: -0.142184
- RS vs GDXJ gap: -3.42% / slope_proxy: -0.036006
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
