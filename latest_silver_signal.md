# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-31**
- 실행시간(UTC): **2026-09-01 03:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -25.0 bp / latest 2.6
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -5.0 bp / latest 2.42
- VIX: 14.43
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 8.57% / slope_proxy: 0.024151
- GDXJ/GLD gap: 13.46% / slope_proxy: 0.006405

## VZLA (Vizsla Silver)
- close: 4.05 | RSI14: 62.810402 | ATR14%: 4.64%
- MA20 gap: 7.04% | MA50 gap: 17.49% | MA200 gap: -0.66%
- vol_ratio(Volume/Vol20): 0.97839 | gap_open: 3.85%
- RS vs SILJ gap: 1.53% / slope_proxy: 0.002527
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
- close: 9.36 | RSI14: 60.017991 | ATR14%: 5.92%
- MA20 gap: 5.65% | MA50 gap: 25.93% | MA200 gap: 7.19%
- vol_ratio(Volume/Vol20): 0.455431 | gap_open: 7.58%
- SilverMarginGate: SI=67.160004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.23% / slope_proxy: 0.005227
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
- close: 23.43 | RSI14: 45.469544 | ATR14%: 8.34%
- MA20 gap: -8.48% | MA50 gap: 1.16% | MA200 gap: -20.73%
- vol_ratio(Volume/Vol20): 0.833484 | gap_open: 8.24%
- RS vs SILJ gap: -14.04% / slope_proxy: -0.105485
- RS vs GDXJ gap: -17.46% / slope_proxy: -0.030555
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
