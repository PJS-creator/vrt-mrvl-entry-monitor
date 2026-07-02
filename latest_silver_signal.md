# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-01**
- 실행시간(UTC): **2026-07-02 03:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 4.0 bp / latest 2.75
- IG OAS 4주 변화: 2.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.2
- VIX: 16.45
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 7.96% / slope_proxy: 0.007016
- GDXJ/GLD gap: -5.13% / slope_proxy: -0.002001

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 43.351426 | ATR14%: 6.49%
- MA20 gap: -5.21% | MA50 gap: -6.93% | MA200 gap: -22.98%
- vol_ratio(Volume/Vol20): 0.402925 | gap_open: 0.61%
- RS vs SILJ gap: 6.26% / slope_proxy: 0.004708
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
- close: 6.59 | RSI14: 41.946972 | ATR14%: 7.76%
- MA20 gap: -3.37% | MA50 gap: -15.78% | MA200 gap: -22.62%
- vol_ratio(Volume/Vol20): 0.428874 | gap_open: 0.00%
- SilverMarginGate: SI=60.595001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.25% / slope_proxy: -0.008968
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 23.07 | RSI14: 36.732887 | ATR14%: 9.71%
- MA20 gap: -8.70% | MA50 gap: -28.21% | MA200 gap: -12.22%
- vol_ratio(Volume/Vol20): 0.684769 | gap_open: 0.43%
- RS vs SILJ gap: -20.74% / slope_proxy: -0.085504
- RS vs GDXJ gap: -18.15% / slope_proxy: -0.018498
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
