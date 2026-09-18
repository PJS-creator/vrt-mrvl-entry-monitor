# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-17**
- 실행시간(UTC): **2026-09-18 03:00:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.7
- IG OAS 4주 변화: -3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 33.0 bp / latest 2.68
- VIX: 17.71
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 2.90% / slope_proxy: 0.024716
- GDXJ/GLD gap: 8.88% / slope_proxy: 0.013806

## VZLA (Vizsla Silver)
- close: 4.01 | RSI14: 55.084962 | ATR14%: 5.39%
- MA20 gap: 0.75% | MA50 gap: 10.47% | MA200 gap: -0.81%
- vol_ratio(Volume/Vol20): 0.850593 | gap_open: 4.34%
- RS vs SILJ gap: 4.54% / slope_proxy: -0.00023
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.92 | RSI14: 48.294024 | ATR14%: 7.13%
- MA20 gap: -6.90% | MA50 gap: 8.90% | MA200 gap: -0.71%
- vol_ratio(Volume/Vol20): 1.203985 | gap_open: 5.42%
- SilverMarginGate: SI=66.394997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.54% / slope_proxy: 0.016523
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

## HYMC (Hycroft Mining)
- close: 21.51 | RSI14: 43.89851 | ATR14%: 7.78%
- MA20 gap: -7.62% | MA50 gap: -5.89% | MA200 gap: -29.11%
- vol_ratio(Volume/Vol20): 1.155758 | gap_open: 6.51%
- RS vs SILJ gap: -12.80% / slope_proxy: -0.0839
- RS vs GDXJ gap: -15.73% / slope_proxy: -0.026154
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
