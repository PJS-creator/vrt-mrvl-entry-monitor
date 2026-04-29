# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-28**
- 실행시간(UTC): **2026-04-29 03:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -62.0 bp / latest 2.84
- IG OAS 4주 변화: -12.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -13.0 bp / latest 1.91
- VIX: 18.02
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -2.87% / slope_proxy: 0.015475
- GDXJ/GLD gap: -3.90% / slope_proxy: -0.003489

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 48.850132 | ATR14%: 5.82%
- MA20 gap: 1.68% | MA50 gap: -4.33% | MA200 gap: -18.69%
- vol_ratio(Volume/Vol20): 0.868294 | gap_open: 3.41%
- RS vs SILJ gap: 2.48% / slope_proxy: -0.024188
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 7.88 | RSI14: 41.536836 | ATR14%: 8.52%
- MA20 gap: -6.91% | MA50 gap: -14.46% | MA200 gap: 1.05%
- vol_ratio(Volume/Vol20): 0.808807 | gap_open: 3.57%
- SilverMarginGate: SI=74.214996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.96% / slope_proxy: -0.030344
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
- close: 35.66 | RSI14: 43.969588 | ATR14%: 9.90%
- MA20 gap: -7.66% | MA50 gap: -9.85% | MA200 gap: 75.58%
- vol_ratio(Volume/Vol20): 0.879205 | gap_open: 2.64%
- RS vs SILJ gap: 1.66% / slope_proxy: 0.043554
- RS vs GDXJ gap: 1.16% / slope_proxy: 0.007666
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
