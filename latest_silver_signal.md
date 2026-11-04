# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-03**
- 실행시간(UTC): **2026-11-04 03:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 31.0 bp / latest 3.43
- IG OAS 4주 변화: 10.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: -33.0 bp / latest 2.62
- VIX: 21.15
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -1.29% / slope_proxy: 0.005387
- GDXJ/GLD gap: -11.37% / slope_proxy: 0.005104

## VZLA (Vizsla Silver)
- close: 3.03 | RSI14: 36.025578 | ATR14%: 5.96%
- MA20 gap: -7.00% | MA50 gap: -17.32% | MA200 gap: -18.47%
- vol_ratio(Volume/Vol20): 0.997311 | gap_open: 0.16%
- RS vs SILJ gap: 3.79% / slope_proxy: 0.00036
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
- close: 6.77 | RSI14: 34.597343 | ATR14%: 7.15%
- MA20 gap: -13.59% | MA50 gap: -22.53% | MA200 gap: -22.70%
- vol_ratio(Volume/Vol20): 1.276869 | gap_open: 2.01%
- SilverMarginGate: SI=49.325001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.76% / slope_proxy: 0.016122
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
- close: 16.09 | RSI14: 39.161974 | ATR14%: 7.43%
- MA20 gap: -5.38% | MA50 gap: -18.63% | MA200 gap: -46.12%
- vol_ratio(Volume/Vol20): 0.99694 | gap_open: 1.35%
- RS vs SILJ gap: -2.15% / slope_proxy: -0.049825
- RS vs GDXJ gap: -4.76% / slope_proxy: -0.016787
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
