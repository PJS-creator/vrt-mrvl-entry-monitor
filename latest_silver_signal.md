# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-09**
- 실행시간(UTC): **2026-11-09 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 31.0 bp / latest 3.42
- IG OAS 4주 변화: 10.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -27.0 bp / latest 2.6
- VIX: 28.18
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 7.22% / slope_proxy: 0.004969
- GDXJ/GLD gap: -0.67% / slope_proxy: 0.002107

## VZLA (Vizsla Silver)
- close: 3.415 | RSI14: 52.897015 | ATR14%: 5.76%
- MA20 gap: 6.03% | MA50 gap: -5.25% | MA200 gap: -6.55%
- vol_ratio(Volume/Vol20): 0.096589 | gap_open: 4.24%
- RS vs SILJ gap: 1.20% / slope_proxy: 0.000678
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
- close: 7.87 | RSI14: 50.546302 | ATR14%: 6.73%
- MA20 gap: 3.45% | MA50 gap: -8.14% | MA200 gap: -8.86%
- vol_ratio(Volume/Vol20): 0.202962 | gap_open: 5.45%
- SilverMarginGate: SI=52.779999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.09% / slope_proxy: 0.011943
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
- close: 20.059999 | RSI14: 61.026917 | ATR14%: 7.07%
- MA20 gap: 18.07% | MA50 gap: 4.41% | MA200 gap: -31.61%
- vol_ratio(Volume/Vol20): 0.236008 | gap_open: 5.17%
- RS vs SILJ gap: 7.54% / slope_proxy: -0.052313
- RS vs GDXJ gap: 3.36% / slope_proxy: -0.017631
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
