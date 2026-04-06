# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-06**
- 실행시간(UTC): **2026-04-06 15:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 3.13
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 15.0 bp / latest 1.97
- VIX: 23.87
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 5.22% / slope_proxy: -0.001611
- GDXJ/GLD gap: -2.28% / slope_proxy: -0.003889

## VZLA (Vizsla Silver)
- close: 3.325 | RSI14: 42.000101 | ATR14%: 7.18%
- MA20 gap: -2.93% | MA50 gap: -19.29% | MA200 gap: -20.41%
- vol_ratio(Volume/Vol20): 0.257458 | gap_open: 0.00%
- RS vs SILJ gap: -17.95% / slope_proxy: -0.027494
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
- close: 8.14 | RSI14: 43.788841 | ATR14%: 10.22%
- MA20 gap: -3.67% | MA50 gap: -22.54% | MA200 gap: 10.57%
- vol_ratio(Volume/Vol20): 0.276517 | gap_open: 0.89%
- SilverMarginGate: SI=72.660004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.39% / slope_proxy: -0.021648
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
- close: 35.84 | RSI14: 48.638983 | ATR14%: 11.83%
- MA20 gap: -0.49% | MA50 gap: -10.50% | MA200 gap: 105.73%
- vol_ratio(Volume/Vol20): 0.190429 | gap_open: 0.58%
- RS vs SILJ gap: 0.05% / slope_proxy: 0.158842
- RS vs GDXJ gap: -1.60% / slope_proxy: 0.041754
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
