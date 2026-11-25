# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-25**
- 실행시간(UTC): **2026-11-25 15:01:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.63
- IG OAS 4주 변화: 7.0 bp / latest 0.97
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.79
- VIX: 26.36
- NFCI: -0.444

### Leadership ratios
- SILJ/SLV gap: 2.94% / slope_proxy: 0.000577
- GDXJ/GLD gap: -12.01% / slope_proxy: -0.010054

## VZLA (Vizsla Silver)
- close: 2.61 | RSI14: 36.461998 | ATR14%: 8.27%
- MA20 gap: -13.90% | MA50 gap: -22.14% | MA200 gap: -25.70%
- vol_ratio(Volume/Vol20): 0.155432 | gap_open: 3.72%
- RS vs SILJ gap: 6.77% / slope_proxy: 0.003406
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
- close: 6.525 | RSI14: 42.807968 | ATR14%: 9.09%
- MA20 gap: -7.31% | MA50 gap: -17.67% | MA200 gap: -21.17%
- vol_ratio(Volume/Vol20): 0.095883 | gap_open: 6.42%
- SilverMarginGate: SI=38.924999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.40% / slope_proxy: 0.006483
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
- close: 12.21 | RSI14: 32.594948 | ATR14%: 12.27%
- MA20 gap: -24.14% | MA50 gap: -30.57% | MA200 gap: -56.00%
- vol_ratio(Volume/Vol20): 0.141314 | gap_open: 4.97%
- RS vs SILJ gap: -5.40% / slope_proxy: -0.041754
- RS vs GDXJ gap: -9.68% / slope_proxy: -0.01435
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
