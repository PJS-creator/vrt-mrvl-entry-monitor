# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-22**
- 실행시간(UTC): **2026-09-22 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.68
- IG OAS 4주 변화: -4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.68
- VIX: 14.87
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 2.30% / slope_proxy: 0.02177
- GDXJ/GLD gap: 8.93% / slope_proxy: 0.014362

## VZLA (Vizsla Silver)
- close: 4.085 | RSI14: 57.206789 | ATR14%: 4.86%
- MA20 gap: 2.03% | MA50 gap: 10.75% | MA200 gap: 1.40%
- vol_ratio(Volume/Vol20): 0.158244 | gap_open: 0.00%
- RS vs SILJ gap: 5.81% / slope_proxy: 0.000394
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
- close: 9.15 | RSI14: 50.386847 | ATR14%: 6.68%
- MA20 gap: -3.85% | MA50 gap: 9.52% | MA200 gap: 1.71%
- vol_ratio(Volume/Vol20): 0.177964 | gap_open: 0.22%
- SilverMarginGate: SI=66.114998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.01% / slope_proxy: 0.017434
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
- close: 21.09 | RSI14: 43.178049 | ATR14%: 7.31%
- MA20 gap: -6.22% | MA50 gap: -7.68% | MA200 gap: -30.81%
- vol_ratio(Volume/Vol20): 0.269442 | gap_open: 0.83%
- RS vs SILJ gap: -13.73% / slope_proxy: -0.079299
- RS vs GDXJ gap: -16.55% / slope_proxy: -0.024797
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
