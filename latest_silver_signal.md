# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-14**
- 실행시간(UTC): **2026-07-15 03:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 3.0 bp / latest 2.69
- IG OAS 4주 변화: 5.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.36
- VIX: 17.16
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 5.97% / slope_proxy: 0.009394
- GDXJ/GLD gap: -3.86% / slope_proxy: -0.00376

## VZLA (Vizsla Silver)
- close: 3.2 | RSI14: 46.42815 | ATR14%: 6.37%
- MA20 gap: -2.82% | MA50 gap: -7.59% | MA200 gap: -23.84%
- vol_ratio(Volume/Vol20): 0.800244 | gap_open: 3.31%
- RS vs SILJ gap: 4.48% / slope_proxy: 0.005117
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
- close: 6.5 | RSI14: 44.247589 | ATR14%: 7.16%
- MA20 gap: -3.67% | MA50 gap: -13.77% | MA200 gap: -23.56%
- vol_ratio(Volume/Vol20): 0.758217 | gap_open: 2.52%
- SilverMarginGate: SI=58.880001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.99% / slope_proxy: -0.005169
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
- close: 21.860001 | RSI14: 39.658463 | ATR14%: 9.10%
- MA20 gap: -6.27% | MA50 gap: -26.22% | MA200 gap: -18.76%
- vol_ratio(Volume/Vol20): 0.528509 | gap_open: 6.95%
- RS vs SILJ gap: -19.67% / slope_proxy: -0.103849
- RS vs GDXJ gap: -19.59% / slope_proxy: -0.022626
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
