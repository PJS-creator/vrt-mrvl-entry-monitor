# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-15**
- 실행시간(UTC): **2026-09-15 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.71
- IG OAS 4주 변화: -1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.6
- VIX: 17.1
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 1.86% / slope_proxy: 0.026404
- GDXJ/GLD gap: 6.79% / slope_proxy: 0.01356

## VZLA (Vizsla Silver)
- close: 3.655 | RSI14: 42.862823 | ATR14%: 5.49%
- MA20 gap: -7.77% | MA50 gap: 1.67% | MA200 gap: -9.80%
- vol_ratio(Volume/Vol20): 0.119658 | gap_open: 0.53%
- RS vs SILJ gap: -0.02% / slope_proxy: -9.6e-05
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
- close: 8.565 | RSI14: 43.688435 | ATR14%: 7.15%
- MA20 gap: -10.89% | MA50 gap: 5.77% | MA200 gap: -4.46%
- vol_ratio(Volume/Vol20): 0.269219 | gap_open: 0.45%
- SilverMarginGate: SI=63.669998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.70% / slope_proxy: 0.015893
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
- close: 19.719999 | RSI14: 35.290146 | ATR14%: 8.44%
- MA20 gap: -17.01% | MA50 gap: -13.72% | MA200 gap: -34.79%
- vol_ratio(Volume/Vol20): 0.279075 | gap_open: 0.19%
- RS vs SILJ gap: -16.81% / slope_proxy: -0.08676
- RS vs GDXJ gap: -20.40% / slope_proxy: -0.026822
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
