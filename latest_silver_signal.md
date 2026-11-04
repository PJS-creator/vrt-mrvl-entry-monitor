# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-04**
- 실행시간(UTC): **2026-11-04 15:01:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 37.0 bp / latest 3.4
- IG OAS 4주 변화: 10.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -33.0 bp / latest 2.62
- VIX: 20.83
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: -0.14% / slope_proxy: 0.005066
- GDXJ/GLD gap: -8.22% / slope_proxy: 0.004303

## VZLA (Vizsla Silver)
- close: 3.185 | RSI14: 43.650863 | ATR14%: 5.76%
- MA20 gap: -1.89% | MA50 gap: -12.68% | MA200 gap: -13.91%
- vol_ratio(Volume/Vol20): 0.124729 | gap_open: 7.26%
- RS vs SILJ gap: 2.77% / slope_proxy: 0.000404
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
- close: 7.3162 | RSI14: 43.079233 | ATR14%: 6.79%
- MA20 gap: -5.93% | MA50 gap: -15.80% | MA200 gap: -16.22%
- vol_ratio(Volume/Vol20): 0.289764 | gap_open: 9.01%
- SilverMarginGate: SI=52.200001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.97% / slope_proxy: 0.015142
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
- close: 17.27 | RSI14: 47.341516 | ATR14%: 7.09%
- MA20 gap: 1.76% | MA50 gap: -11.87% | MA200 gap: -41.92%
- vol_ratio(Volume/Vol20): 0.231037 | gap_open: 9.01%
- RS vs SILJ gap: -0.56% / slope_proxy: -0.050003
- RS vs GDXJ gap: -3.51% / slope_proxy: -0.016854
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
