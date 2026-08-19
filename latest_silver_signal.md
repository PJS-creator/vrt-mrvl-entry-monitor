# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-19**
- 실행시간(UTC): **2026-08-19 22:57:20**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.75
- IG OAS 4주 변화: 4.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.41
- VIX: 15.84
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 11.08% / slope_proxy: 0.01883
- GDXJ/GLD gap: 12.74% / slope_proxy: -0.000338

## VZLA (Vizsla Silver)
- close: 3.89 | RSI14: 62.57292 | ATR14%: 4.92%
- MA20 gap: 10.84% | MA50 gap: 15.20% | MA200 gap: -4.56%
- vol_ratio(Volume/Vol20): 1.003722 | gap_open: 4.48%
- RS vs SILJ gap: -3.02% / slope_proxy: 0.004672
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
- close: 9.54 | RSI14: 71.071735 | ATR14%: 5.67%
- MA20 gap: 23.65% | MA50 gap: 35.48% | MA200 gap: 11.34%
- vol_ratio(Volume/Vol20): 1.852241 | gap_open: 4.78%
- SilverMarginGate: SI=67.040001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.64% / slope_proxy: -0.000206
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
- close: 27.9 | RSI14: 61.296272 | ATR14%: 7.00%
- MA20 gap: 18.19% | MA50 gap: 20.58% | MA200 gap: -3.54%
- vol_ratio(Volume/Vol20): 1.836372 | gap_open: 8.06%
- RS vs SILJ gap: -1.71% / slope_proxy: -0.121913
- RS vs GDXJ gap: -5.23% / slope_proxy: -0.032521
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
