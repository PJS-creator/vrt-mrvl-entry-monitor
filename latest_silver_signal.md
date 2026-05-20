# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-19**
- 실행시간(UTC): **2026-05-20 03:01:23**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -4.0 bp / latest 2.83
- IG OAS 4주 변화: -6.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 22.0 bp / latest 2.13
- VIX: 17.82
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -5.73% / slope_proxy: -0.001975
- GDXJ/GLD gap: -6.10% / slope_proxy: -0.003715

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 41.668807 | ATR14%: 6.83%
- MA20 gap: -6.46% | MA50 gap: -4.80% | MA200 gap: -22.91%
- vol_ratio(Volume/Vol20): 1.259434 | gap_open: 0.00%
- RS vs SILJ gap: 3.56% / slope_proxy: -0.007211
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
- close: 8.23 | RSI14: 44.257204 | ATR14%: 8.33%
- MA20 gap: -4.97% | MA50 gap: -3.48% | MA200 gap: 0.81%
- vol_ratio(Volume/Vol20): 1.252094 | gap_open: 1.17%
- SilverMarginGate: SI=73.644997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.44% / slope_proxy: -0.020498
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
- close: 33.185001 | RSI14: 40.660961 | ATR14%: 11.11%
- MA20 gap: -13.15% | MA50 gap: -11.93% | MA200 gap: 44.89%
- vol_ratio(Volume/Vol20): 1.488131 | gap_open: 3.62%
- RS vs SILJ gap: -4.49% / slope_proxy: 0.028119
- RS vs GDXJ gap: -3.35% / slope_proxy: 0.00729
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
