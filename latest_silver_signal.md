# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-05**
- 실행시간(UTC): **2026-03-06 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 11.0 bp / latest 2.97
- IG OAS 4주 변화: 7.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -14.0 bp / latest 1.8
- VIX: 21.15
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 4.62% / slope_proxy: -0.002946
- GDXJ/GLD gap: -0.40% / slope_proxy: 0.013744

## VZLA (Vizsla Silver)
- close: 4.07 | RSI14: 42.469471 | ATR14%: 8.32%
- MA20 gap: 0.99% | MA50 gap: -20.53% | MA200 gap: -1.77%
- vol_ratio(Volume/Vol20): 0.63126 | gap_open: 2.40%
- RS vs SILJ gap: -26.81% / slope_proxy: -0.027576
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 9.97 | RSI14: 41.746265 | ATR14%: 11.03%
- MA20 gap: -9.86% | MA50 gap: -12.88% | MA200 gap: 48.41%
- vol_ratio(Volume/Vol20): 1.125092 | gap_open: 1.64%
- SilverMarginGate: SI=83.730003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.04% / slope_proxy: 0.014514
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 41.060001 | RSI14: 48.663452 | ATR14%: 14.83%
- MA20 gap: -1.84% | MA50 gap: 9.28% | MA200 gap: 193.64%
- vol_ratio(Volume/Vol20): 1.178895 | gap_open: 2.17%
- RS vs SILJ gap: 19.02% / slope_proxy: 0.246764
- RS vs GDXJ gap: 18.53% / slope_proxy: 0.06496
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
