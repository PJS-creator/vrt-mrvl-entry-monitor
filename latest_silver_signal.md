# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-28**
- 실행시간(UTC): **2026-09-29 03:00:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 2.93
- IG OAS 4주 변화: 2.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 41.0 bp / latest 2.83
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 0.83% / slope_proxy: 0.017949
- GDXJ/GLD gap: 4.13% / slope_proxy: 0.014556

## VZLA (Vizsla Silver)
- close: 3.82 | RSI14: 46.558076 | ATR14%: 5.54%
- MA20 gap: -4.28% | MA50 gap: 1.68% | MA200 gap: -4.68%
- vol_ratio(Volume/Vol20): 0.91343 | gap_open: 4.81%
- RS vs SILJ gap: 7.49% / slope_proxy: 0.001526
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
- close: 9.02 | RSI14: 49.005019 | ATR14%: 7.23%
- MA20 gap: -4.09% | MA50 gap: 4.96% | MA200 gap: 0.09%
- vol_ratio(Volume/Vol20): 1.500103 | gap_open: 7.17%
- SilverMarginGate: SI=61.115002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.55% / slope_proxy: 0.019278
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

## HYMC (Hycroft Mining)
- close: 19.6 | RSI14: 39.809071 | ATR14%: 8.30%
- MA20 gap: -9.52% | MA50 gap: -14.55% | MA200 gap: -36.10%
- vol_ratio(Volume/Vol20): 1.066325 | gap_open: 5.68%
- RS vs SILJ gap: -11.18% / slope_proxy: -0.070244
- RS vs GDXJ gap: -13.95% / slope_proxy: -0.022295
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
