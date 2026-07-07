# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-06**
- 실행시간(UTC): **2026-07-07 03:01:15**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.74
- IG OAS 4주 변화: 1.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.26
- VIX: 15.81
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 5.72% / slope_proxy: 0.007438
- GDXJ/GLD gap: -2.30% / slope_proxy: -0.001937

## VZLA (Vizsla Silver)
- close: 3.27 | RSI14: 44.185909 | ATR14%: 6.47%
- MA20 gap: -3.38% | MA50 gap: -6.54% | MA200 gap: -22.63%
- vol_ratio(Volume/Vol20): 0.773077 | gap_open: 2.10%
- RS vs SILJ gap: 3.28% / slope_proxy: 0.004865
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
- close: 6.81 | RSI14: 45.532005 | ATR14%: 7.34%
- MA20 gap: 1.00% | MA50 gap: -12.07% | MA200 gap: -20.02%
- vol_ratio(Volume/Vol20): 0.849856 | gap_open: 3.74%
- SilverMarginGate: SI=61.715 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.61% / slope_proxy: -0.007623
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
- close: 23.49 | RSI14: 38.608751 | ATR14%: 9.30%
- MA20 gap: -4.12% | MA50 gap: -25.38% | MA200 gap: -11.21%
- vol_ratio(Volume/Vol20): 0.375178 | gap_open: 1.40%
- RS vs SILJ gap: -20.68% / slope_proxy: -0.090102
- RS vs GDXJ gap: -20.75% / slope_proxy: -0.019747
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
