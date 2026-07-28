# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-27**
- 실행시간(UTC): **2026-07-28 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -4.0 bp / latest 2.79
- IG OAS 4주 변화: 3.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 25.0 bp / latest 2.43
- VIX: 18.58
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 3.69% / slope_proxy: 0.007479
- GDXJ/GLD gap: -2.44% / slope_proxy: -0.008908

## VZLA (Vizsla Silver)
- close: 3.32 | RSI14: 51.736376 | ATR14%: 5.82%
- MA20 gap: 3.65% | MA50 gap: -2.51% | MA200 gap: -20.00%
- vol_ratio(Volume/Vol20): 0.992631 | gap_open: 1.52%
- RS vs SILJ gap: 7.66% / slope_proxy: 0.006287
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 6.31 | RSI14: 45.16548 | ATR14%: 7.00%
- MA20 gap: -1.83% | MA50 gap: -11.65% | MA200 gap: -25.31%
- vol_ratio(Volume/Vol20): 0.800162 | gap_open: 0.71%
- SilverMarginGate: SI=57.525002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.05% / slope_proxy: -0.005631
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
- close: 20.43 | RSI14: 42.046838 | ATR14%: 8.84%
- MA20 gap: -4.00% | MA50 gap: -21.57% | MA200 gap: -25.78%
- vol_ratio(Volume/Vol20): 0.595288 | gap_open: 0.79%
- RS vs SILJ gap: -18.44% / slope_proxy: -0.131529
- RS vs GDXJ gap: -20.69% / slope_proxy: -0.029955
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
