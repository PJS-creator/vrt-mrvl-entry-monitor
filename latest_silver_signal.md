# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-17**
- 실행시간(UTC): **2026-07-17 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 8.0 bp / latest 2.71
- IG OAS 4주 변화: 5.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 9.0 bp / latest 2.32
- VIX: 16.73
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 3.19% / slope_proxy: 0.008694
- GDXJ/GLD gap: -8.64% / slope_proxy: -0.006924

## VZLA (Vizsla Silver)
- close: 3.01 | RSI14: 40.658646 | ATR14%: 6.55%
- MA20 gap: -6.26% | MA50 gap: -12.69% | MA200 gap: -28.07%
- vol_ratio(Volume/Vol20): 0.324032 | gap_open: 1.63%
- RS vs SILJ gap: 5.42% / slope_proxy: 0.005636
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
- close: 5.7526 | RSI14: 35.174298 | ATR14%: 7.87%
- MA20 gap: -11.51% | MA50 gap: -22.51% | MA200 gap: -32.15%
- vol_ratio(Volume/Vol20): 0.442041 | gap_open: 2.68%
- SilverMarginGate: SI=55.919998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.58% / slope_proxy: -0.00603
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
- close: 18.385 | RSI14: 31.299217 | ATR14%: 10.69%
- MA20 gap: -17.22% | MA50 gap: -35.67% | MA200 gap: -32.16%
- vol_ratio(Volume/Vol20): 0.274684 | gap_open: 1.27%
- RS vs SILJ gap: -25.06% / slope_proxy: -0.118166
- RS vs GDXJ gap: -25.61% / slope_proxy: -0.026213
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
