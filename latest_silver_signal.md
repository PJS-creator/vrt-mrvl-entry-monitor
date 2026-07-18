# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-17**
- 실행시간(UTC): **2026-07-18 15:00:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.71
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 14.0 bp / latest 2.35
- VIX: 16.73
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 3.80% / slope_proxy: 0.00874
- GDXJ/GLD gap: -8.32% / slope_proxy: -0.006909

## VZLA (Vizsla Silver)
- close: 3.07 | RSI14: 42.408359 | ATR14%: 6.49%
- MA20 gap: -4.48% | MA50 gap: -10.98% | MA200 gap: -26.64%
- vol_ratio(Volume/Vol20): 0.969017 | gap_open: 1.63%
- RS vs SILJ gap: 5.93% / slope_proxy: 0.005647
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
- close: 5.94 | RSI14: 37.216462 | ATR14%: 7.72%
- MA20 gap: -8.76% | MA50 gap: -20.02% | MA200 gap: -29.95%
- vol_ratio(Volume/Vol20): 1.331019 | gap_open: 2.68%
- SilverMarginGate: SI=56.037998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.99% / slope_proxy: -0.005959
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
- close: 19.049999 | RSI14: 34.110553 | ATR14%: 10.49%
- MA20 gap: -14.35% | MA50 gap: -33.38% | MA200 gap: -29.72%
- vol_ratio(Volume/Vol20): 0.778347 | gap_open: 0.79%
- RS vs SILJ gap: -23.51% / slope_proxy: -0.117893
- RS vs GDXJ gap: -23.55% / slope_proxy: -0.026119
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
