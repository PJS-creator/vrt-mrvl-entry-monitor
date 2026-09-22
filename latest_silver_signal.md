# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-21**
- 실행시간(UTC): **2026-09-22 03:01:00**

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
- VIX: 14.81
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 0.59% / slope_proxy: 0.022662
- GDXJ/GLD gap: 7.47% / slope_proxy: 0.014202

## VZLA (Vizsla Silver)
- close: 4.07 | RSI14: 56.727442 | ATR14%: 5.07%
- MA20 gap: 1.85% | MA50 gap: 10.98% | MA200 gap: 0.92%
- vol_ratio(Volume/Vol20): 0.933858 | gap_open: 0.00%
- RS vs SILJ gap: 6.87% / slope_proxy: 0.000195
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
- close: 9.03 | RSI14: 49.225323 | ATR14%: 7.04%
- MA20 gap: -5.32% | MA50 gap: 8.81% | MA200 gap: 0.40%
- vol_ratio(Volume/Vol20): 0.682023 | gap_open: 0.42%
- SilverMarginGate: SI=66.644997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.24% / slope_proxy: 0.017109
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
- close: 20.530001 | RSI14: 40.241576 | ATR14%: 7.81%
- MA20 gap: -9.64% | MA50 gap: -10.08% | MA200 gap: -32.54%
- vol_ratio(Volume/Vol20): 0.67425 | gap_open: 0.47%
- RS vs SILJ gap: -15.34% / slope_proxy: -0.08066
- RS vs GDXJ gap: -18.22% / slope_proxy: -0.025285
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
