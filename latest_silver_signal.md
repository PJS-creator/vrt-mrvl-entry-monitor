# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-08**
- 실행시간(UTC): **2026-09-08 15:01:25**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.65
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -1.0 bp / latest 2.42
- VIX: 15.3
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 8.84% / slope_proxy: 0.028197
- GDXJ/GLD gap: 13.90% / slope_proxy: 0.012314

## VZLA (Vizsla Silver)
- close: 4.145 | RSI14: 59.860665 | ATR14%: 4.84%
- MA20 gap: 5.48% | MA50 gap: 17.26% | MA200 gap: 2.04%
- vol_ratio(Volume/Vol20): 0.222099 | gap_open: 0.00%
- RS vs SILJ gap: 2.19% / slope_proxy: 0.000587
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
- close: 10.095 | RSI14: 62.588178 | ATR14%: 5.81%
- MA20 gap: 6.66% | MA50 gap: 29.16% | MA200 gap: 13.88%
- vol_ratio(Volume/Vol20): 0.175636 | gap_open: 0.40%
- SilverMarginGate: SI=66.709999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.97% / slope_proxy: 0.012074
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
- close: 23.075001 | RSI14: 45.937582 | ATR14%: 7.84%
- MA20 gap: -8.55% | MA50 gap: -0.04% | MA200 gap: -22.98%
- vol_ratio(Volume/Vol20): 0.26391 | gap_open: 1.06%
- RS vs SILJ gap: -14.34% / slope_proxy: -0.091217
- RS vs GDXJ gap: -16.66% / slope_proxy: -0.027479
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
