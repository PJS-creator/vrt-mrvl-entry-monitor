# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-06**
- 실행시간(UTC): **2026-11-07 02:20:41**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.48
- IG OAS 4주 변화: 11.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -27.0 bp / latest 2.6
- VIX: 28.18
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 1.07% / slope_proxy: 0.00498
- GDXJ/GLD gap: -2.97% / slope_proxy: 0.002828

## VZLA (Vizsla Silver)
- close: 3.19 | RSI14: 44.454377 | ATR14%: 6.29%
- MA20 gap: -1.47% | MA50 gap: -12.19% | MA200 gap: -13.45%
- vol_ratio(Volume/Vol20): 1.25348 | gap_open: 1.52%
- RS vs SILJ gap: 1.76% / slope_proxy: 0.000488
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
- close: 7.315 | RSI14: 43.856818 | ATR14%: 7.49%
- MA20 gap: -5.47% | MA50 gap: -15.44% | MA200 gap: -16.01%
- vol_ratio(Volume/Vol20): 1.276416 | gap_open: 3.06%
- SilverMarginGate: SI=51.965 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.11% / slope_proxy: 0.014355
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
- close: 17.02 | RSI14: 46.029773 | ATR14%: 7.83%
- MA20 gap: 0.58% | MA50 gap: -12.41% | MA200 gap: -42.55%
- vol_ratio(Volume/Vol20): 1.44113 | gap_open: 1.52%
- RS vs SILJ gap: -2.55% / slope_proxy: -0.051048
- RS vs GDXJ gap: -7.43% / slope_proxy: -0.017154
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
