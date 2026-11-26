# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-25**
- 실행시간(UTC): **2026-11-26 04:21:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 54.0 bp / latest 3.72
- IG OAS 4주 변화: 10.0 bp / latest 0.98
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.79
- VIX: 26.36
- NFCI: -0.444

### Leadership ratios
- SILJ/SLV gap: 5.90% / slope_proxy: 0.000831
- GDXJ/GLD gap: -7.72% / slope_proxy: -0.009844

## VZLA (Vizsla Silver)
- close: 2.86 | RSI14: 43.838092 | ATR14%: 8.10%
- MA20 gap: -6.04% | MA50 gap: -14.80% | MA200 gap: -18.62%
- vol_ratio(Volume/Vol20): 1.202741 | gap_open: 3.72%
- RS vs SILJ gap: 7.76% / slope_proxy: 0.003428
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
- close: 7.51 | RSI14: 51.968668 | ATR14%: 8.57%
- MA20 gap: 5.94% | MA50 gap: -5.48% | MA200 gap: -9.32%
- vol_ratio(Volume/Vol20): 1.220345 | gap_open: 6.42%
- SilverMarginGate: SI=41.965 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 19.03% / slope_proxy: 0.00684
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## HYMC (Hycroft Mining)
- close: 13.72 | RSI14: 39.230528 | ATR14%: 11.49%
- MA20 gap: -15.16% | MA50 gap: -22.11% | MA200 gap: -50.57%
- vol_ratio(Volume/Vol20): 1.367501 | gap_open: 4.97%
- RS vs SILJ gap: -2.13% / slope_proxy: -0.041365
- RS vs GDXJ gap: -6.28% / slope_proxy: -0.014254
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
