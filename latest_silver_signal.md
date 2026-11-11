# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-11**
- 실행시간(UTC): **2026-11-11 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.34
- IG OAS 4주 변화: 8.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -25.0 bp / latest 2.66
- VIX: 19.46
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 3.05% / slope_proxy: 0.005097
- GDXJ/GLD gap: -3.15% / slope_proxy: 0.000968

## VZLA (Vizsla Silver)
- close: 3.335 | RSI14: 49.748534 | ATR14%: 6.01%
- MA20 gap: 3.21% | MA50 gap: -6.86% | MA200 gap: -7.92%
- vol_ratio(Volume/Vol20): 0.051915 | gap_open: 0.60%
- RS vs SILJ gap: 3.05% / slope_proxy: 0.001218
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

## SCZM (Santacruz Silver)
- close: 7.59 | RSI14: 47.496814 | ATR14%: 6.89%
- MA20 gap: 0.46% | MA50 gap: -10.75% | MA200 gap: -11.27%
- vol_ratio(Volume/Vol20): 0.112736 | gap_open: 0.79%
- SilverMarginGate: SI=52.275002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.40% / slope_proxy: 0.010352
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
- close: 19.040001 | RSI14: 53.922249 | ATR14%: 8.06%
- MA20 gap: 10.37% | MA50 gap: -0.28% | MA200 gap: -34.36%
- vol_ratio(Volume/Vol20): 0.151679 | gap_open: 0.42%
- RS vs SILJ gap: 7.15% / slope_proxy: -0.050065
- RS vs GDXJ gap: 3.88% / slope_proxy: -0.016957
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
