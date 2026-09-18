# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-18**
- 실행시간(UTC): **2026-09-18 15:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -5.0 bp / latest 2.7
- IG OAS 4주 변화: -4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 33.0 bp / latest 2.68
- VIX: 15.44
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 0.02% / slope_proxy: 0.023604
- GDXJ/GLD gap: 7.40% / slope_proxy: 0.014058

## VZLA (Vizsla Silver)
- close: 3.965 | RSI14: 53.45121 | ATR14%: 5.32%
- MA20 gap: -0.50% | MA50 gap: 8.75% | MA200 gap: -1.79%
- vol_ratio(Volume/Vol20): 0.147902 | gap_open: 0.25%
- RS vs SILJ gap: 4.54% / slope_proxy: -6.4e-05
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

## SCZM (Santacruz Silver)
- close: 8.995 | RSI14: 49.090137 | ATR14%: 6.88%
- MA20 gap: -5.74% | MA50 gap: 9.19% | MA200 gap: 0.09%
- vol_ratio(Volume/Vol20): 0.38122 | gap_open: 1.57%
- SilverMarginGate: SI=66.864998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.44% / slope_proxy: 0.016654
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
- close: 21.059999 | RSI14: 42.24826 | ATR14%: 7.77%
- MA20 gap: -8.56% | MA50 gap: -7.80% | MA200 gap: -30.70%
- vol_ratio(Volume/Vol20): 0.253749 | gap_open: 2.74%
- RS vs SILJ gap: -13.28% / slope_proxy: -0.081955
- RS vs GDXJ gap: -16.37% / slope_proxy: -0.025681
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
