# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-28**
- 실행시간(UTC): **2026-07-29 03:00:55**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.81
- IG OAS 4주 변화: 5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.44
- VIX: 18.67
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 2.73% / slope_proxy: 0.007307
- GDXJ/GLD gap: -3.20% / slope_proxy: -0.008823

## VZLA (Vizsla Silver)
- close: 3.19 | RSI14: 46.996429 | ATR14%: 6.08%
- MA20 gap: -0.28% | MA50 gap: -6.01% | MA200 gap: -22.99%
- vol_ratio(Volume/Vol20): 0.507798 | gap_open: 2.11%
- RS vs SILJ gap: 6.55% / slope_proxy: 0.006256
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
- close: 6.46 | RSI14: 47.922364 | ATR14%: 6.79%
- MA20 gap: 0.80% | MA50 gap: -7.75% | MA200 gap: -23.46%
- vol_ratio(Volume/Vol20): 1.248603 | gap_open: 0.16%
- SilverMarginGate: SI=58.035 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.53% / slope_proxy: -0.005172
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## HYMC (Hycroft Mining)
- close: 20.120001 | RSI14: 41.063176 | ATR14%: 8.90%
- MA20 gap: -4.72% | MA50 gap: -21.60% | MA200 gap: -27.08%
- vol_ratio(Volume/Vol20): 1.079131 | gap_open: 2.40%
- RS vs SILJ gap: -16.51% / slope_proxy: -0.134512
- RS vs GDXJ gap: -19.55% / slope_proxy: -0.030988
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
