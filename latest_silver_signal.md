# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-01**
- 실행시간(UTC): **2026-07-01 15:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 4.0 bp / latest 2.75
- IG OAS 4주 변화: 2.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 9.0 bp / latest 2.16
- VIX: 16.45
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 8.04% / slope_proxy: 0.007022
- GDXJ/GLD gap: -4.65% / slope_proxy: -0.001978

## VZLA (Vizsla Silver)
- close: 3.38 | RSI14: 47.518446 | ATR14%: 6.24%
- MA20 gap: -1.89% | MA50 gap: -3.57% | MA200 gap: -20.15%
- vol_ratio(Volume/Vol20): 0.15303 | gap_open: 0.61%
- RS vs SILJ gap: 8.17% / slope_proxy: 0.004746
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
- close: 6.685 | RSI14: 43.38107 | ATR14%: 7.65%
- MA20 gap: -2.04% | MA50 gap: -14.59% | MA200 gap: -21.51%
- vol_ratio(Volume/Vol20): 0.141691 | gap_open: 0.00%
- SilverMarginGate: SI=60.755001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.59% / slope_proxy: -0.008983
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
- close: 23.83 | RSI14: 39.133594 | ATR14%: 9.34%
- MA20 gap: -5.83% | MA50 gap: -25.88% | MA200 gap: -9.34%
- vol_ratio(Volume/Vol20): 0.184947 | gap_open: 0.43%
- RS vs SILJ gap: -19.60% / slope_proxy: -0.085289
- RS vs GDXJ gap: -16.99% / slope_proxy: -0.018442
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
