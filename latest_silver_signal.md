# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-22**
- 실행시간(UTC): **2026-03-23 03:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 39.0 bp / latest 3.27
- IG OAS 4주 변화: 11.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.88
- VIX: 24.06
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -2.22% / slope_proxy: -0.006969
- GDXJ/GLD gap: -13.60% / slope_proxy: 0.005117

## VZLA (Vizsla Silver)
- close: 3.0 | RSI14: 26.701477 | ATR14%: 9.91%
- MA20 gap: -22.54% | MA50 gap: -35.88% | MA200 gap: -28.42%
- vol_ratio(Volume/Vol20): 0.743796 | gap_open: 0.31%
- RS vs SILJ gap: -22.45% / slope_proxy: -0.027562
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.14 | RSI14: 28.476701 | ATR14%: 13.11%
- MA20 gap: -30.40% | MA50 gap: -36.57% | MA200 gap: 0.38%
- vol_ratio(Volume/Vol20): 1.303587 | gap_open: 2.51%
- SilverMarginGate: SI=65.540001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.07% / slope_proxy: -0.008078
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
- close: 30.0 | RSI14: 37.019241 | ATR14%: 16.67%
- MA20 gap: -29.68% | MA50 gap: -25.68% | MA200 gap: 88.36%
- vol_ratio(Volume/Vol20): 2.496138 | gap_open: 0.91%
- RS vs SILJ gap: 1.16% / slope_proxy: 0.247567
- RS vs GDXJ gap: 0.17% / slope_proxy: 0.064967
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
