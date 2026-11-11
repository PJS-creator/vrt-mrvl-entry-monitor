# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-10**
- 실행시간(UTC): **2026-11-11 03:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.34
- IG OAS 4주 변화: 8.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -25.0 bp / latest 2.66
- VIX: 19.92
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 4.69% / slope_proxy: 0.005036
- GDXJ/GLD gap: -3.42% / slope_proxy: 0.00131

## VZLA (Vizsla Silver)
- close: 3.32 | RSI14: 49.236546 | ATR14%: 6.26%
- MA20 gap: 3.01% | MA50 gap: -7.55% | MA200 gap: -8.75%
- vol_ratio(Volume/Vol20): 0.907259 | gap_open: 4.57%
- RS vs SILJ gap: 2.60% / slope_proxy: 0.000987
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
- close: 7.57 | RSI14: 47.267688 | ATR14%: 7.29%
- MA20 gap: -0.05% | MA50 gap: -11.32% | MA200 gap: -11.94%
- vol_ratio(Volume/Vol20): 1.100436 | gap_open: 4.20%
- SilverMarginGate: SI=52.294998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.70% / slope_proxy: 0.011088
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
- close: 18.870001 | RSI14: 53.286282 | ATR14%: 8.49%
- MA20 gap: 10.25% | MA50 gap: -1.44% | MA200 gap: -35.34%
- vol_ratio(Volume/Vol20): 1.10583 | gap_open: 4.47%
- RS vs SILJ gap: 5.89% / slope_proxy: -0.051639
- RS vs GDXJ gap: 2.51% / slope_proxy: -0.017409
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
