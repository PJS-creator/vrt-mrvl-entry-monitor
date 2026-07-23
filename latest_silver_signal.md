# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-22**
- 실행시간(UTC): **2026-07-23 03:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.69
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.37
- VIX: 17.05
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 5.74% / slope_proxy: 0.00851
- GDXJ/GLD gap: -2.33% / slope_proxy: -0.008495

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 55.517527 | ATR14%: 5.78%
- MA20 gap: 7.34% | MA50 gap: -0.49% | MA200 gap: -17.95%
- vol_ratio(Volume/Vol20): 1.304874 | gap_open: 0.30%
- RS vs SILJ gap: 7.77% / slope_proxy: 0.006108
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
- close: 6.76 | RSI14: 51.644069 | ATR14%: 6.54%
- MA20 gap: 5.04% | MA50 gap: -7.17% | MA200 gap: -20.09%
- vol_ratio(Volume/Vol20): 0.910165 | gap_open: 2.29%
- SilverMarginGate: SI=59.970001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.95% / slope_proxy: -0.005826
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
- close: 21.700001 | RSI14: 45.44196 | ATR14%: 8.75%
- MA20 gap: 0.51% | MA50 gap: -21.02% | MA200 gap: -20.56%
- vol_ratio(Volume/Vol20): 0.828288 | gap_open: 1.64%
- RS vs SILJ gap: -17.97% / slope_proxy: -0.125497
- RS vs GDXJ gap: -18.61% / slope_proxy: -0.028017
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
