# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-03**
- 실행시간(UTC): **2026-08-03 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 9.0 bp / latest 2.84
- IG OAS 4주 변화: 5.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.41
- VIX: 15.99
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 3.84% / slope_proxy: 0.008027
- GDXJ/GLD gap: -2.45% / slope_proxy: -0.008694

## VZLA (Vizsla Silver)
- close: 3.2201 | RSI14: 48.965504 | ATR14%: 5.80%
- MA20 gap: 1.37% | MA50 gap: -4.65% | MA200 gap: -21.71%
- vol_ratio(Volume/Vol20): 0.19133 | gap_open: 0.96%
- RS vs SILJ gap: 4.90% / slope_proxy: 0.006062
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
- close: 6.465 | RSI14: 48.366035 | ATR14%: 6.67%
- MA20 gap: 1.32% | MA50 gap: -5.56% | MA200 gap: -23.30%
- vol_ratio(Volume/Vol20): 0.1872 | gap_open: 1.08%
- SilverMarginGate: SI=57.404999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 0.18% / slope_proxy: -0.005405
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
- close: 20.35 | RSI14: 44.396406 | ATR14%: 8.31%
- MA20 gap: -0.22% | MA50 gap: -16.87% | MA200 gap: -26.89%
- vol_ratio(Volume/Vol20): 0.249443 | gap_open: 1.64%
- RS vs SILJ gap: -14.30% / slope_proxy: -0.145632
- RS vs GDXJ gap: -16.56% / slope_proxy: -0.034692
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
