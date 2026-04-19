# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-17**
- 실행시간(UTC): **2026-04-19 15:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -41.0 bp / latest 2.86
- IG OAS 4주 변화: -9.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 5.0 bp / latest 1.93
- VIX: 17.94
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 0.09% / slope_proxy: 0.009797
- GDXJ/GLD gap: 2.95% / slope_proxy: -0.004055

## VZLA (Vizsla Silver)
- close: 3.51 | RSI14: 51.530609 | ATR14%: 5.70%
- MA20 gap: 7.70% | MA50 gap: -4.23% | MA200 gap: -16.27%
- vol_ratio(Volume/Vol20): 0.793256 | gap_open: 3.21%
- RS vs SILJ gap: -12.11% / slope_proxy: -0.027432
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
- close: 9.2 | RSI14: 54.757177 | ATR14%: 8.11%
- MA20 gap: 13.16% | MA50 gap: -3.54% | MA200 gap: 20.81%
- vol_ratio(Volume/Vol20): 1.030216 | gap_open: 4.21%
- SilverMarginGate: SI=81.842003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -9.14% / slope_proxy: -0.025075
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
- close: 44.169998 | RSI14: 61.586344 | ATR14%: 8.70%
- MA20 gap: 22.13% | MA50 gap: 13.12% | MA200 gap: 131.73%
- vol_ratio(Volume/Vol20): 0.95801 | gap_open: 3.73%
- RS vs SILJ gap: 11.18% / slope_proxy: 0.081656
- RS vs GDXJ gap: 9.02% / slope_proxy: 0.019868
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trigger(Breakout/Retest)=FALSE
