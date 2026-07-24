# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-24**
- 실행시간(UTC): **2026-07-24 15:01:03**

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
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.39
- VIX: 18.7
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 3.65% / slope_proxy: 0.007805
- GDXJ/GLD gap: -2.86% / slope_proxy: -0.008951

## VZLA (Vizsla Silver)
- close: 3.255 | RSI14: 49.488035 | ATR14%: 5.86%
- MA20 gap: 1.76% | MA50 gap: -4.69% | MA200 gap: -21.67%
- vol_ratio(Volume/Vol20): 0.136599 | gap_open: 0.31%
- RS vs SILJ gap: 5.99% / slope_proxy: 0.006269
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
- close: 6.31 | RSI14: 45.16548 | ATR14%: 6.89%
- MA20 gap: -1.83% | MA50 gap: -11.65% | MA200 gap: -25.31%
- vol_ratio(Volume/Vol20): 0.131004 | gap_open: 0.95%
- SilverMarginGate: SI=58.849998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.86% / slope_proxy: -0.005622
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
- close: 20.280001 | RSI14: 41.327963 | ATR14%: 9.09%
- MA20 gap: -5.45% | MA50 gap: -23.51% | MA200 gap: -26.14%
- vol_ratio(Volume/Vol20): 0.149492 | gap_open: 1.71%
- RS vs SILJ gap: -19.39% / slope_proxy: -0.129688
- RS vs GDXJ gap: -21.07% / slope_proxy: -0.029316
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
