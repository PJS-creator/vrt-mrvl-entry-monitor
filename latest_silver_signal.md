# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-13**
- 실행시간(UTC): **2026-11-14 03:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 3.2
- IG OAS 4주 변화: 5.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.86
- VIX: 18.7
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 2.16% / slope_proxy: 0.004409
- GDXJ/GLD gap: -6.20% / slope_proxy: -0.0008

## VZLA (Vizsla Silver)
- close: 3.07 | RSI14: 41.672801 | ATR14%: 6.39%
- MA20 gap: -4.29% | MA50 gap: -13.18% | MA200 gap: -14.46%
- vol_ratio(Volume/Vol20): 0.94131 | gap_open: 0.32%
- RS vs SILJ gap: 1.94% / slope_proxy: 0.00167
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
- close: 6.83 | RSI14: 40.250346 | ATR14%: 7.63%
- MA20 gap: -7.76% | MA50 gap: -18.35% | MA200 gap: -19.43%
- vol_ratio(Volume/Vol20): 0.926797 | gap_open: 0.57%
- SilverMarginGate: SI=48.650002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.34% / slope_proxy: 0.007862
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
- close: 15.9 | RSI14: 42.089773 | ATR14%: 9.87%
- MA20 gap: -7.28% | MA50 gap: -15.49% | MA200 gap: -44.56%
- vol_ratio(Volume/Vol20): 0.911347 | gap_open: 0.06%
- RS vs SILJ gap: -2.95% / slope_proxy: -0.049633
- RS vs GDXJ gap: -6.17% / slope_proxy: -0.01665
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
