# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-06**
- 실행시간(UTC): **2026-10-07 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 44.0 bp / latest 3.12
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 52.0 bp / latest 2.95
- VIX: 15.52
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: -1.53% / slope_proxy: 0.01086
- GDXJ/GLD gap: 1.19% / slope_proxy: 0.012352

## VZLA (Vizsla Silver)
- close: 3.53 | RSI14: 38.096828 | ATR14%: 5.53%
- MA20 gap: -8.95% | MA50 gap: -7.18% | MA200 gap: -10.89%
- vol_ratio(Volume/Vol20): 0.968025 | gap_open: 0.28%
- RS vs SILJ gap: -0.66% / slope_proxy: 0.002841
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.96 | RSI14: 49.036204 | ATR14%: 6.44%
- MA20 gap: -1.66% | MA50 gap: 0.75% | MA200 gap: -0.36%
- vol_ratio(Volume/Vol20): 0.846891 | gap_open: 0.56%
- SilverMarginGate: SI=61.25 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.21% / slope_proxy: 0.019484
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 19.09 | RSI14: 39.32871 | ATR14%: 7.16%
- MA20 gap: -6.88% | MA50 gap: -16.16% | MA200 gap: -38.13%
- vol_ratio(Volume/Vol20): 0.679199 | gap_open: 1.65%
- RS vs SILJ gap: -10.93% / slope_proxy: -0.060441
- RS vs GDXJ gap: -13.54% / slope_proxy: -0.019793
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
