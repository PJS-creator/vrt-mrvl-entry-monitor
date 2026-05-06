# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-05**
- 실행시간(UTC): **2026-05-06 03:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -27.0 bp / latest 2.78
- IG OAS 4주 변화: -5.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -3.0 bp / latest 1.95
- VIX: 18.29
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -4.59% / slope_proxy: 0.011546
- GDXJ/GLD gap: -5.71% / slope_proxy: -0.003842

## VZLA (Vizsla Silver)
- close: 3.23 | RSI14: 42.006251 | ATR14%: 6.21%
- MA20 gap: -4.55% | MA50 gap: -8.48% | MA200 gap: -23.26%
- vol_ratio(Volume/Vol20): 0.568498 | gap_open: 1.49%
- RS vs SILJ gap: 1.50% / slope_proxy: -0.019585
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

## SCZM (Santacruz Silver)
- close: 7.78 | RSI14: 41.918332 | ATR14%: 7.91%
- MA20 gap: -7.47% | MA50 gap: -13.14% | MA200 gap: -1.47%
- vol_ratio(Volume/Vol20): 0.622958 | gap_open: 1.90%
- SilverMarginGate: SI=75.605003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.63% / slope_proxy: -0.031182
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
- close: 35.369999 | RSI14: 44.904056 | ATR14%: 9.19%
- MA20 gap: -8.65% | MA50 gap: -9.73% | MA200 gap: 67.47%
- vol_ratio(Volume/Vol20): 0.71031 | gap_open: 1.91%
- RS vs SILJ gap: 2.47% / slope_proxy: 0.033331
- RS vs GDXJ gap: 2.79% / slope_proxy: 0.004615
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
