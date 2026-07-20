# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-20**
- 실행시간(UTC): **2026-07-20 15:01:15**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.71
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 14.0 bp / latest 2.35
- VIX: 18.77
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 1.90% / slope_proxy: 0.008514
- GDXJ/GLD gap: -8.23% / slope_proxy: -0.007647

## VZLA (Vizsla Silver)
- close: 3.14 | RSI14: 45.362542 | ATR14%: 6.12%
- MA20 gap: -1.68% | MA50 gap: -8.78% | MA200 gap: -24.86%
- vol_ratio(Volume/Vol20): 0.222975 | gap_open: 0.65%
- RS vs SILJ gap: 8.81% / slope_proxy: 0.005783
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
- close: 5.86 | RSI14: 36.24893 | ATR14%: 7.45%
- MA20 gap: -9.09% | MA50 gap: -20.48% | MA200 gap: -30.80%
- vol_ratio(Volume/Vol20): 0.347001 | gap_open: 0.00%
- SilverMarginGate: SI=57.215 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.35% / slope_proxy: -0.006137
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
- close: 18.629999 | RSI14: 33.148543 | ATR14%: 10.27%
- MA20 gap: -14.83% | MA50 gap: -33.87% | MA200 gap: -31.43%
- vol_ratio(Volume/Vol20): 0.115563 | gap_open: 1.52%
- RS vs SILJ gap: -24.04% / slope_proxy: -0.121872
- RS vs GDXJ gap: -24.41% / slope_proxy: -0.027114
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
