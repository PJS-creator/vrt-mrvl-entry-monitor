# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-26**
- 실행시간(UTC): **2026-10-27 03:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 45.0 bp / latest 3.38
- IG OAS 4주 변화: 10.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -17.0 bp / latest 2.66
- VIX: 19.45
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.16% / slope_proxy: 0.007159
- GDXJ/GLD gap: -9.31% / slope_proxy: 0.009667

## VZLA (Vizsla Silver)
- close: 3.07 | RSI14: 33.993693 | ATR14%: 5.90%
- MA20 gap: -10.02% | MA50 gap: -17.98% | MA200 gap: -19.19%
- vol_ratio(Volume/Vol20): 0.972617 | gap_open: 0.32%
- RS vs SILJ gap: 1.43% / slope_proxy: 0.001025
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

## SCZM (Santacruz Silver)
- close: 7.04 | RSI14: 32.92306 | ATR14%: 7.34%
- MA20 gap: -15.77% | MA50 gap: -21.75% | MA200 gap: -20.72%
- vol_ratio(Volume/Vol20): 1.168057 | gap_open: 0.58%
- SilverMarginGate: SI=53.705002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.28% / slope_proxy: 0.021112
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

## HYMC (Hycroft Mining)
- close: 15.39 | RSI14: 31.741832 | ATR14%: 7.62%
- MA20 gap: -12.96% | MA50 gap: -26.40% | MA200 gap: -49.29%
- vol_ratio(Volume/Vol20): 0.75975 | gap_open: 0.06%
- RS vs SILJ gap: -12.03% / slope_proxy: -0.04933
- RS vs GDXJ gap: -15.80% / slope_proxy: -0.016756
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
