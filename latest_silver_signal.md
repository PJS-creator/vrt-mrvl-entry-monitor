# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-04**
- 실행시간(UTC): **2026-05-04 15:01:39**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -36.0 bp / latest 2.77
- IG OAS 4주 변화: -5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -3.0 bp / latest 1.94
- VIX: 16.99
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.75% / slope_proxy: 0.01281
- GDXJ/GLD gap: -4.60% / slope_proxy: -0.003782

## VZLA (Vizsla Silver)
- close: 3.465 | RSI14: 50.945169 | ATR14%: 5.51%
- MA20 gap: 2.23% | MA50 gap: -2.25% | MA200 gap: -17.68%
- vol_ratio(Volume/Vol20): 0.166961 | gap_open: 1.73%
- RS vs SILJ gap: 5.75% / slope_proxy: -0.020503
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.27 | RSI14: 47.180267 | ATR14%: 7.50%
- MA20 gap: -1.92% | MA50 gap: -8.65% | MA200 gap: 4.97%
- vol_ratio(Volume/Vol20): 0.377056 | gap_open: 1.59%
- SilverMarginGate: SI=74.690002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.55% / slope_proxy: -0.031207
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 37.209999 | RSI14: 48.243654 | ATR14%: 8.71%
- MA20 gap: -4.19% | MA50 gap: -5.41% | MA200 gap: 77.47%
- vol_ratio(Volume/Vol20): 0.218974 | gap_open: 4.47%
- RS vs SILJ gap: 5.39% / slope_proxy: 0.035681
- RS vs GDXJ gap: 6.89% / slope_proxy: 0.00533
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
