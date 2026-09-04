# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-03**
- 실행시간(UTC): **2026-09-04 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -9.0 bp / latest 2.66
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.45
- VIX: 15.2
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 9.96% / slope_proxy: 0.027162
- GDXJ/GLD gap: 15.56% / slope_proxy: 0.010102

## VZLA (Vizsla Silver)
- close: 4.17 | RSI14: 62.567521 | ATR14%: 4.83%
- MA20 gap: 6.83% | MA50 gap: 19.14% | MA200 gap: 2.54%
- vol_ratio(Volume/Vol20): 0.675115 | gap_open: 2.89%
- RS vs SILJ gap: 1.18% / slope_proxy: 0.001243
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
- close: 10.42 | RSI14: 68.304909 | ATR14%: 5.80%
- MA20 gap: 11.66% | MA50 gap: 35.75% | MA200 gap: 18.17%
- vol_ratio(Volume/Vol20): 0.870307 | gap_open: 3.14%
- SilverMarginGate: SI=67.360001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 17.82% / slope_proxy: 0.009897
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
- close: 23.299999 | RSI14: 46.325991 | ATR14%: 8.23%
- MA20 gap: -9.11% | MA50 gap: 0.95% | MA200 gap: -21.91%
- vol_ratio(Volume/Vol20): 0.996192 | gap_open: 4.09%
- RS vs SILJ gap: -15.55% / slope_proxy: -0.096476
- RS vs GDXJ gap: -18.68% / slope_proxy: -0.029026
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
