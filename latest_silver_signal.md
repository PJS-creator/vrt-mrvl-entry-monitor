# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-24**
- 실행시간(UTC): **2026-07-26 15:00:54**

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
- VIX: 18.7
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 3.86% / slope_proxy: 0.007821
- GDXJ/GLD gap: -2.96% / slope_proxy: -0.008956

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 51.030817 | ATR14%: 5.88%
- MA20 gap: 3.09% | MA50 gap: -3.40% | MA200 gap: -20.59%
- vol_ratio(Volume/Vol20): 0.888907 | gap_open: 0.31%
- RS vs SILJ gap: 7.85% / slope_proxy: 0.006308
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
- close: 6.29 | RSI14: 44.865211 | ATR14%: 7.05%
- MA20 gap: -2.12% | MA50 gap: -11.93% | MA200 gap: -25.55%
- vol_ratio(Volume/Vol20): 0.552475 | gap_open: 0.95%
- SilverMarginGate: SI=58.905998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.78% / slope_proxy: -0.005619
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
- close: 20.219999 | RSI14: 41.160213 | ATR14%: 9.12%
- MA20 gap: -5.72% | MA50 gap: -23.73% | MA200 gap: -26.36%
- vol_ratio(Volume/Vol20): 0.507543 | gap_open: 1.76%
- RS vs SILJ gap: -19.31% / slope_proxy: -0.129673
- RS vs GDXJ gap: -21.02% / slope_proxy: -0.029313
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
