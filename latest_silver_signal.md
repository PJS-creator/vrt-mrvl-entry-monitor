# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-16**
- 실행시간(UTC): **2026-09-17 03:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.76
- IG OAS 4주 변화: -2.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.62
- VIX: 17.2
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 1.28% / slope_proxy: 0.025691
- GDXJ/GLD gap: 5.97% / slope_proxy: 0.013676

## VZLA (Vizsla Silver)
- close: 3.69 | RSI14: 43.727713 | ATR14%: 5.62%
- MA20 gap: -7.15% | MA50 gap: 2.24% | MA200 gap: -8.85%
- vol_ratio(Volume/Vol20): 0.744991 | gap_open: 2.13%
- RS vs SILJ gap: 1.23% / slope_proxy: -0.000191
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
- close: 8.31 | RSI14: 41.369652 | ATR14%: 7.54%
- MA20 gap: -13.55% | MA50 gap: 2.12% | MA200 gap: -7.39%
- vol_ratio(Volume/Vol20): 1.10871 | gap_open: 2.78%
- SilverMarginGate: SI=63.755001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.66% / slope_proxy: 0.016241
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
- close: 20.049999 | RSI14: 36.416066 | ATR14%: 8.35%
- MA20 gap: -15.06% | MA50 gap: -12.22% | MA200 gap: -33.81%
- vol_ratio(Volume/Vol20): 1.127962 | gap_open: 2.32%
- RS vs SILJ gap: -14.82% / slope_proxy: -0.084878
- RS vs GDXJ gap: -18.09% / slope_proxy: -0.026371
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
