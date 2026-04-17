# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-17**
- 실행시간(UTC): **2026-04-17 15:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -41.0 bp / latest 2.86
- IG OAS 4주 변화: -9.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 1.9
- VIX: 17.94
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 0.97% / slope_proxy: 0.009864
- GDXJ/GLD gap: 4.43% / slope_proxy: -0.003982

## VZLA (Vizsla Silver)
- close: 3.58 | RSI14: 54.094913 | ATR14%: 5.59%
- MA20 gap: 9.73% | MA50 gap: -2.36% | MA200 gap: -14.61%
- vol_ratio(Volume/Vol20): 0.296109 | gap_open: 3.21%
- RS vs SILJ gap: -12.51% / slope_proxy: -0.027441
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
- close: 9.675 | RSI14: 58.610499 | ATR14%: 7.71%
- MA20 gap: 18.66% | MA50 gap: 1.34% | MA200 gap: 27.01%
- vol_ratio(Volume/Vol20): 0.356999 | gap_open: 4.21%
- SilverMarginGate: SI=82.964996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.79% / slope_proxy: -0.024953
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
- close: 44.887501 | RSI14: 62.569002 | ATR14%: 8.54%
- MA20 gap: 23.99% | MA50 gap: 14.91% | MA200 gap: 135.45%
- vol_ratio(Volume/Vol20): 0.423111 | gap_open: 3.73%
- RS vs SILJ gap: 10.28% / slope_proxy: 0.081472
- RS vs GDXJ gap: 8.85% / slope_proxy: 0.01986
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trigger(Breakout/Retest)=FALSE
