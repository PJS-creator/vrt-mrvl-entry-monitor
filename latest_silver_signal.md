# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-31**
- 실행시간(UTC): **2026-08-02 03:01:10**

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
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.41
- VIX: 17.09
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 0.91% / slope_proxy: 0.007656
- GDXJ/GLD gap: -4.91% / slope_proxy: -0.00868

## VZLA (Vizsla Silver)
- close: 3.14 | RSI14: 45.838584 | ATR14%: 5.98%
- MA20 gap: -1.23% | MA50 gap: -7.11% | MA200 gap: -23.80%
- vol_ratio(Volume/Vol20): 0.96659 | gap_open: 2.78%
- RS vs SILJ gap: 4.48% / slope_proxy: 0.006029
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
- close: 6.46 | RSI14: 48.282286 | ATR14%: 6.95%
- MA20 gap: 0.97% | MA50 gap: -6.16% | MA200 gap: -23.39%
- vol_ratio(Volume/Vol20): 0.701964 | gap_open: 3.83%
- SilverMarginGate: SI=57.591 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.86% / slope_proxy: -0.005054
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
- close: 19.530001 | RSI14: 40.566948 | ATR14%: 8.74%
- MA20 gap: -4.97% | MA50 gap: -21.11% | MA200 gap: -29.68%
- vol_ratio(Volume/Vol20): 0.706727 | gap_open: 2.79%
- RS vs SILJ gap: -16.86% / slope_proxy: -0.143044
- RS vs GDXJ gap: -18.90% / slope_proxy: -0.033856
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
