# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-06**
- 실행시간(UTC): **2026-08-07 03:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.75
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.41
- VIX: 15.81
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 7.12% / slope_proxy: 0.010501
- GDXJ/GLD gap: 4.35% / slope_proxy: -0.007546

## VZLA (Vizsla Silver)
- close: 3.53 | RSI14: 58.20393 | ATR14%: 5.36%
- MA20 gap: 8.82% | MA50 gap: 4.47% | MA200 gap: -13.78%
- vol_ratio(Volume/Vol20): 0.662925 | gap_open: 1.39%
- RS vs SILJ gap: 1.95% / slope_proxy: 0.006066
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
- close: 7.97 | RSI14: 66.455135 | ATR14%: 6.11%
- MA20 gap: 21.01% | MA50 gap: 16.71% | MA200 gap: -5.58%
- vol_ratio(Volume/Vol20): 1.067003 | gap_open: 3.39%
- SilverMarginGate: SI=62.34 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.21% / slope_proxy: -0.004923
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
- close: 23.799999 | RSI14: 56.400441 | ATR14%: 7.40%
- MA20 gap: 14.84% | MA50 gap: -0.51% | MA200 gap: -15.19%
- vol_ratio(Volume/Vol20): 0.857629 | gap_open: 3.92%
- RS vs SILJ gap: -8.67% / slope_proxy: -0.146158
- RS vs GDXJ gap: -11.40% / slope_proxy: -0.035607
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
