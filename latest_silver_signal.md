# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-24**
- 실행시간(UTC): **2026-08-25 03:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -9.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -3.0 bp / latest 2.4
- VIX: 15.13
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 8.30% / slope_proxy: 0.021118
- GDXJ/GLD gap: 14.71% / slope_proxy: 0.002045

## VZLA (Vizsla Silver)
- close: 3.93 | RSI14: 62.696422 | ATR14%: 4.79%
- MA20 gap: 9.03% | MA50 gap: 15.18% | MA200 gap: -3.55%
- vol_ratio(Volume/Vol20): 1.04627 | gap_open: 1.77%
- RS vs SILJ gap: -3.79% / slope_proxy: 0.003869
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
- close: 9.57 | RSI14: 68.728213 | ATR14%: 5.68%
- MA20 gap: 16.41% | MA50 gap: 31.87% | MA200 gap: 10.74%
- vol_ratio(Volume/Vol20): 0.73077 | gap_open: 1.40%
- SilverMarginGate: SI=67.735001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.36% / slope_proxy: 0.002482
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
- close: 25.74 | RSI14: 53.160546 | ATR14%: 7.58%
- MA20 gap: 5.07% | MA50 gap: 10.68% | MA200 gap: -11.85%
- vol_ratio(Volume/Vol20): 0.985225 | gap_open: 0.66%
- RS vs SILJ gap: -9.63% / slope_proxy: -0.115318
- RS vs GDXJ gap: -15.60% / slope_proxy: -0.031867
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
