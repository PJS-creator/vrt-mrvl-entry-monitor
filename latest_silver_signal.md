# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-27**
- 실행시간(UTC): **2026-07-27 15:01:15**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.77
- IG OAS 4주 변화: 3.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.43
- VIX: 18.58
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 3.14% / slope_proxy: 0.007765
- GDXJ/GLD gap: -2.92% / slope_proxy: -0.008954

## VZLA (Vizsla Silver)
- close: 3.305 | RSI14: 51.196444 | ATR14%: 5.97%
- MA20 gap: 3.24% | MA50 gap: -3.25% | MA200 gap: -20.47%
- vol_ratio(Volume/Vol20): 0.257474 | gap_open: 3.40%
- RS vs SILJ gap: 7.91% / slope_proxy: 0.006309
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 6.2792 | RSI14: 44.720188 | ATR14%: 7.03%
- MA20 gap: -2.28% | MA50 gap: -12.08% | MA200 gap: -25.68%
- vol_ratio(Volume/Vol20): 0.232033 | gap_open: 0.71%
- SilverMarginGate: SI=58.759998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.04% / slope_proxy: -0.00563
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
- close: 20.129999 | RSI14: 40.911131 | ATR14%: 9.25%
- MA20 gap: -6.12% | MA50 gap: -24.07% | MA200 gap: -26.68%
- vol_ratio(Volume/Vol20): 0.152573 | gap_open: 0.49%
- RS vs SILJ gap: -19.74% / slope_proxy: -0.129747
- RS vs GDXJ gap: -21.79% / slope_proxy: -0.029348
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
