# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-16**
- 실행시간(UTC): **2026-07-17 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 8.0 bp / latest 2.71
- IG OAS 4주 변화: 5.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 9.0 bp / latest 2.32
- VIX: 15.67
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 4.82% / slope_proxy: 0.008897
- GDXJ/GLD gap: -7.20% / slope_proxy: -0.006158

## VZLA (Vizsla Silver)
- close: 3.07 | RSI14: 42.408359 | ATR14%: 6.55%
- MA20 gap: -5.23% | MA50 gap: -11.06% | MA200 gap: -26.76%
- vol_ratio(Volume/Vol20): 1.249814 | gap_open: 0.94%
- RS vs SILJ gap: 6.09% / slope_proxy: 0.005519
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
- close: 5.98 | RSI14: 37.68345 | ATR14%: 7.68%
- MA20 gap: -9.23% | MA50 gap: -19.88% | MA200 gap: -29.56%
- vol_ratio(Volume/Vol20): 1.144244 | gap_open: 1.73%
- SilverMarginGate: SI=55.040001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.65% / slope_proxy: -0.005726
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
- close: 18.434999 | RSI14: 31.403752 | ATR14%: 11.09%
- MA20 gap: -18.31% | MA50 gap: -36.26% | MA200 gap: -31.83%
- vol_ratio(Volume/Vol20): 1.085483 | gap_open: 3.02%
- RS vs SILJ gap: -26.65% / slope_proxy: -0.114343
- RS vs GDXJ gap: -26.89% / slope_proxy: -0.025191
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
