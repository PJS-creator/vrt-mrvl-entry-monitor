# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-02**
- 실행시간(UTC): **2026-07-02 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.74
- IG OAS 4주 변화: 2.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.2
- VIX: 16.59
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 8.31% / slope_proxy: 0.007283
- GDXJ/GLD gap: -2.31% / slope_proxy: -0.001898

## VZLA (Vizsla Silver)
- close: 3.375 | RSI14: 47.77064 | ATR14%: 6.35%
- MA20 gap: -1.16% | MA50 gap: -3.67% | MA200 gap: -20.20%
- vol_ratio(Volume/Vol20): 0.343912 | gap_open: 3.99%
- RS vs SILJ gap: 5.55% / slope_proxy: 0.004787
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
- close: 6.81 | RSI14: 45.396218 | ATR14%: 7.45%
- MA20 gap: 0.33% | MA50 gap: -12.60% | MA200 gap: -20.03%
- vol_ratio(Volume/Vol20): 0.653038 | gap_open: 3.19%
- SilverMarginGate: SI=61.740002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.77% / slope_proxy: -0.008356
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
- close: 24.0481 | RSI14: 40.577306 | ATR14%: 9.25%
- MA20 gap: -3.28% | MA50 gap: -24.44% | MA200 gap: -8.81%
- vol_ratio(Volume/Vol20): 0.263595 | gap_open: 4.55%
- RS vs SILJ gap: -20.15% / slope_proxy: -0.089056
- RS vs GDXJ gap: -18.59% / slope_proxy: -0.019473
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
