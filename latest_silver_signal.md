# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-13**
- 실행시간(UTC): **2026-08-14 03:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.71
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.42
- VIX: 14.55
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 8.72% / slope_proxy: 0.014629
- GDXJ/GLD gap: 7.81% / slope_proxy: -0.004116

## VZLA (Vizsla Silver)
- close: 3.74 | RSI14: 60.704554 | ATR14%: 4.98%
- MA20 gap: 9.60% | MA50 gap: 11.00% | MA200 gap: -8.42%
- vol_ratio(Volume/Vol20): 0.634052 | gap_open: 1.32%
- RS vs SILJ gap: -0.07% / slope_proxy: 0.005646
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

## SCZM (Santacruz Silver)
- close: 8.72 | RSI14: 69.40204 | ATR14%: 5.88%
- MA20 gap: 23.70% | MA50 gap: 26.67% | MA200 gap: 2.63%
- vol_ratio(Volume/Vol20): 0.757517 | gap_open: 2.82%
- SilverMarginGate: SI=64.07 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.51% / slope_proxy: -0.003264
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
- close: 26.57 | RSI14: 61.470106 | ATR14%: 6.91%
- MA20 gap: 18.91% | MA50 gap: 13.87% | MA200 gap: -6.93%
- vol_ratio(Volume/Vol20): 0.721097 | gap_open: 4.30%
- RS vs SILJ gap: -2.06% / slope_proxy: -0.133604
- RS vs GDXJ gap: -3.58% / slope_proxy: -0.034385
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
