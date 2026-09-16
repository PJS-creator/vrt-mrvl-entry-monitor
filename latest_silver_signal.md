# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-15**
- 실행시간(UTC): **2026-09-16 03:00:52**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.71
- IG OAS 4주 변화: -1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.6
- VIX: 17.1
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 2.51% / slope_proxy: 0.026458
- GDXJ/GLD gap: 7.52% / slope_proxy: 0.013596

## VZLA (Vizsla Silver)
- close: 3.76 | RSI14: 46.095271 | ATR14%: 5.39%
- MA20 gap: -5.24% | MA50 gap: 4.53% | MA200 gap: -7.23%
- vol_ratio(Volume/Vol20): 0.702133 | gap_open: 0.53%
- RS vs SILJ gap: 1.19% / slope_proxy: -7e-05
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
- close: 8.64 | RSI14: 44.353429 | ATR14%: 7.16%
- MA20 gap: -10.14% | MA50 gap: 6.68% | MA200 gap: -3.63%
- vol_ratio(Volume/Vol20): 0.995017 | gap_open: 0.45%
- SilverMarginGate: SI=64.970001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.93% / slope_proxy: 0.015857
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
- close: 20.700001 | RSI14: 38.54112 | ATR14%: 8.10%
- MA20 gap: -13.06% | MA50 gap: -9.51% | MA200 gap: -31.56%
- vol_ratio(Volume/Vol20): 0.92296 | gap_open: 0.24%
- RS vs SILJ gap: -14.11% / slope_proxy: -0.086382
- RS vs GDXJ gap: -17.48% / slope_proxy: -0.026719
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
