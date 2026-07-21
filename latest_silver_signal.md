# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-20**
- 실행시간(UTC): **2026-07-21 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 7.0 bp / latest 2.73
- IG OAS 4주 변화: 5.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.31
- VIX: 18.77
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 3.07% / slope_proxy: 0.008603
- GDXJ/GLD gap: -8.43% / slope_proxy: -0.007656

## VZLA (Vizsla Silver)
- close: 3.15 | RSI14: 45.760006 | ATR14%: 6.18%
- MA20 gap: -1.38% | MA50 gap: -8.49% | MA200 gap: -24.62%
- vol_ratio(Volume/Vol20): 0.700061 | gap_open: 0.65%
- RS vs SILJ gap: 8.63% / slope_proxy: 0.005779
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
- close: 6.01 | RSI14: 38.649306 | ATR14%: 7.32%
- MA20 gap: -6.87% | MA50 gap: -18.48% | MA200 gap: -29.04%
- vol_ratio(Volume/Vol20): 0.920286 | gap_open: 0.00%
- SilverMarginGate: SI=57.755001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.45% / slope_proxy: -0.006052
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
- close: 18.76 | RSI14: 33.440461 | ATR14%: 10.20%
- MA20 gap: -14.26% | MA50 gap: -33.41% | MA200 gap: -30.95%
- vol_ratio(Volume/Vol20): 0.523596 | gap_open: 1.52%
- RS vs SILJ gap: -23.89% / slope_proxy: -0.121844
- RS vs GDXJ gap: -23.71% / slope_proxy: -0.027083
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
