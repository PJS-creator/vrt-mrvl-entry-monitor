# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-17**
- 실행시간(UTC): **2026-09-17 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.7
- IG OAS 4주 변화: -3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.62
- VIX: 17.71
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 2.34% / slope_proxy: 0.024669
- GDXJ/GLD gap: 8.36% / slope_proxy: 0.013781

## VZLA (Vizsla Silver)
- close: 3.9273 | RSI14: 52.613285 | ATR14%: 5.38%
- MA20 gap: -1.22% | MA50 gap: 8.24% | MA200 gap: -2.85%
- vol_ratio(Volume/Vol20): 0.229796 | gap_open: 4.34%
- RS vs SILJ gap: 2.55% / slope_proxy: -0.000273
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

## SCZM (Santacruz Silver)
- close: 8.87 | RSI14: 47.788589 | ATR14%: 7.17%
- MA20 gap: -7.40% | MA50 gap: 8.30% | MA200 gap: -1.26%
- vol_ratio(Volume/Vol20): 0.394827 | gap_open: 6.02%
- SilverMarginGate: SI=66.25 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.09% / slope_proxy: 0.016502
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

## HYMC (Hycroft Mining)
- close: 21.360001 | RSI14: 43.211932 | ATR14%: 7.83%
- MA20 gap: -8.23% | MA50 gap: -6.54% | MA200 gap: -29.60%
- vol_ratio(Volume/Vol20): 0.487609 | gap_open: 6.51%
- RS vs SILJ gap: -13.29% / slope_proxy: -0.083967
- RS vs GDXJ gap: -16.03% / slope_proxy: -0.026165
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
