# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-17**
- 실행시간(UTC): **2026-11-18 03:51:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 3.34
- IG OAS 4주 변화: 3.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.92
- VIX: 22.91
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 1.46% / slope_proxy: 0.003886
- GDXJ/GLD gap: -8.01% / slope_proxy: -0.002932

## VZLA (Vizsla Silver)
- close: 2.97 | RSI14: 39.564894 | ATR14%: 6.56%
- MA20 gap: -6.59% | MA50 gap: -14.96% | MA200 gap: -16.76%
- vol_ratio(Volume/Vol20): 2.066198 | gap_open: 1.19%
- RS vs SILJ gap: 2.45% / slope_proxy: 0.002246
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
- close: 7.41 | RSI14: 48.409037 | ATR14%: 7.77%
- MA20 gap: 2.01% | MA50 gap: -10.11% | MA200 gap: -12.08%
- vol_ratio(Volume/Vol20): 2.52176 | gap_open: 7.17%
- SilverMarginGate: SI=45.965 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.96% / slope_proxy: 0.005879
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

## HYMC (Hycroft Mining)
- close: 15.69 | RSI14: 42.020793 | ATR14%: 9.59%
- MA20 gap: -7.75% | MA50 gap: -15.29% | MA200 gap: -44.90%
- vol_ratio(Volume/Vol20): 1.20542 | gap_open: 1.14%
- RS vs SILJ gap: 0.33% / slope_proxy: -0.048508
- RS vs GDXJ gap: -3.66% / slope_proxy: -0.016189
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
