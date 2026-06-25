# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-24**
- 실행시간(UTC): **2026-06-25 03:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.71
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.29
- VIX: 19.49
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 8.13% / slope_proxy: 0.001626
- GDXJ/GLD gap: -6.22% / slope_proxy: -0.002557

## VZLA (Vizsla Silver)
- close: 3.11 | RSI14: 37.668912 | ATR14%: 7.48%
- MA20 gap: -13.61% | MA50 gap: -11.76% | MA200 gap: -26.75%
- vol_ratio(Volume/Vol20): 0.970146 | gap_open: 2.99%
- RS vs SILJ gap: 6.67% / slope_proxy: 0.004512
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
- close: 6.33 | RSI14: 37.722515 | ATR14%: 9.34%
- MA20 gap: -12.25% | MA50 gap: -21.62% | MA200 gap: -25.63%
- vol_ratio(Volume/Vol20): 0.921008 | gap_open: 5.29%
- SilverMarginGate: SI=56.73 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.83% / slope_proxy: -0.009894
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
- close: 21.700001 | RSI14: 30.997116 | ATR14%: 11.56%
- MA20 gap: -21.77% | MA50 gap: -36.26% | MA200 gap: -16.06%
- vol_ratio(Volume/Vol20): 1.375053 | gap_open: 5.10%
- RS vs SILJ gap: -23.93% / slope_proxy: -0.079286
- RS vs GDXJ gap: -22.64% / slope_proxy: -0.017255
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
