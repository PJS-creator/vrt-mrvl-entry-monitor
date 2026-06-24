# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-24**
- 실행시간(UTC): **2026-06-24 15:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.71
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.28
- VIX: 19.49
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 6.01% / slope_proxy: 0.001466
- GDXJ/GLD gap: -5.40% / slope_proxy: -0.002518

## VZLA (Vizsla Silver)
- close: 3.1901 | RSI14: 39.409174 | ATR14%: 7.05%
- MA20 gap: -11.48% | MA50 gap: -9.53% | MA200 gap: -24.87%
- vol_ratio(Volume/Vol20): 0.330858 | gap_open: 2.99%
- RS vs SILJ gap: 8.60% / slope_proxy: 0.00455
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
- close: 6.365 | RSI14: 37.998402 | ATR14%: 9.27%
- MA20 gap: -11.79% | MA50 gap: -21.19% | MA200 gap: -25.22%
- vol_ratio(Volume/Vol20): 0.286463 | gap_open: 5.29%
- SilverMarginGate: SI=59.035 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.99% / slope_proxy: -0.009902
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
- close: 21.719999 | RSI14: 31.027714 | ATR14%: 11.34%
- MA20 gap: -21.70% | MA50 gap: -36.20% | MA200 gap: -15.98%
- vol_ratio(Volume/Vol20): 0.383045 | gap_open: 5.10%
- RS vs SILJ gap: -24.40% / slope_proxy: -0.079377
- RS vs GDXJ gap: -23.57% / slope_proxy: -0.017301
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
