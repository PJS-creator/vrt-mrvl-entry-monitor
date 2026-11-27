# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-27**
- 실행시간(UTC): **2026-11-27 15:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 54.0 bp / latest 3.72
- IG OAS 4주 변화: 10.0 bp / latest 0.98
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.79
- VIX: 26.8
- NFCI: -0.444

### Leadership ratios
- SILJ/SLV gap: 4.47% / slope_proxy: 0.000559
- GDXJ/GLD gap: -5.04% / slope_proxy: -0.010444

## VZLA (Vizsla Silver)
- close: 3.005 | RSI14: 48.188241 | ATR14%: 7.58%
- MA20 gap: -0.82% | MA50 gap: -9.95% | MA200 gap: -14.38%
- vol_ratio(Volume/Vol20): 0.115081 | gap_open: 4.55%
- RS vs SILJ gap: 8.19% / slope_proxy: 0.003509
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
- close: 8.0 | RSI14: 56.078616 | ATR14%: 8.13%
- MA20 gap: 12.25% | MA50 gap: 0.92% | MA200 gap: -3.20%
- vol_ratio(Volume/Vol20): 0.206104 | gap_open: 6.79%
- SilverMarginGate: SI=44.055 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 20.97% / slope_proxy: 0.007614
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
- close: 14.71 | RSI14: 44.236453 | ATR14%: 10.61%
- MA20 gap: -8.31% | MA50 gap: -15.84% | MA200 gap: -46.80%
- vol_ratio(Volume/Vol20): 0.167745 | gap_open: 8.09%
- RS vs SILJ gap: 0.50% / slope_proxy: -0.03916
- RS vs GDXJ gap: -3.46% / slope_proxy: -0.013718
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
