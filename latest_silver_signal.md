# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-06**
- 실행시간(UTC): **2026-10-06 15:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 44.0 bp / latest 3.12
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 49.0 bp / latest 2.92
- VIX: 15.52
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: -2.24% / slope_proxy: 0.0108
- GDXJ/GLD gap: 0.75% / slope_proxy: 0.01233

## VZLA (Vizsla Silver)
- close: 3.475 | RSI14: 36.202459 | ATR14%: 5.52%
- MA20 gap: -10.31% | MA50 gap: -8.60% | MA200 gap: -12.27%
- vol_ratio(Volume/Vol20): 0.435765 | gap_open: 0.28%
- RS vs SILJ gap: -0.99% / slope_proxy: 0.002833
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

## SCZM (Santacruz Silver)
- close: 8.77 | RSI14: 46.844936 | ATR14%: 6.47%
- MA20 gap: -3.64% | MA50 gap: -1.34% | MA200 gap: -2.46%
- vol_ratio(Volume/Vol20): 0.283356 | gap_open: 0.56%
- SilverMarginGate: SI=61.305 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.22% / slope_proxy: 0.019434
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 18.690001 | RSI14: 37.036895 | ATR14%: 7.28%
- MA20 gap: -8.74% | MA50 gap: -17.89% | MA200 gap: -39.42%
- vol_ratio(Volume/Vol20): 0.198175 | gap_open: 1.17%
- RS vs SILJ gap: -11.70% / slope_proxy: -0.060544
- RS vs GDXJ gap: -14.70% / slope_proxy: -0.019831
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
