# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-31**
- 실행시간(UTC): **2026-07-31 15:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 9.0 bp / latest 2.84
- IG OAS 4주 변화: 5.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.41
- VIX: 17.09
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 2.63% / slope_proxy: 0.007789
- GDXJ/GLD gap: -4.01% / slope_proxy: -0.008639

## VZLA (Vizsla Silver)
- close: 3.175 | RSI14: 47.007188 | ATR14%: 5.91%
- MA20 gap: -0.18% | MA50 gap: -6.10% | MA200 gap: -22.95%
- vol_ratio(Volume/Vol20): 0.205267 | gap_open: 2.78%
- RS vs SILJ gap: 4.66% / slope_proxy: 0.006033
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
- close: 6.54 | RSI14: 49.474489 | ATR14%: 6.86%
- MA20 gap: 2.16% | MA50 gap: -5.02% | MA200 gap: -22.45%
- vol_ratio(Volume/Vol20): 0.263694 | gap_open: 3.83%
- SilverMarginGate: SI=57.825001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 2.16% / slope_proxy: -0.005041
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
- close: 19.370001 | RSI14: 40.06698 | ATR14%: 8.81%
- MA20 gap: -5.71% | MA50 gap: -21.74% | MA200 gap: -30.25%
- vol_ratio(Volume/Vol20): 0.22403 | gap_open: 2.79%
- RS vs SILJ gap: -18.29% / slope_proxy: -0.143278
- RS vs GDXJ gap: -20.28% / slope_proxy: -0.033915
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
