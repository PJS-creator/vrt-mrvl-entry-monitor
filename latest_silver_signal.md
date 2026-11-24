# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-24**
- 실행시간(UTC): **2026-11-24 15:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 38.0 bp / latest 3.76
- IG OAS 4주 변화: 7.0 bp / latest 0.98
- 10Y Real Yield 4주 변화: 11.0 bp / latest 2.77
- VIX: 26.62
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 0.93% / slope_proxy: 0.000664
- GDXJ/GLD gap: -10.44% / slope_proxy: -0.009019

## VZLA (Vizsla Silver)
- close: 2.69 | RSI14: 38.188168 | ATR14%: 8.02%
- MA20 gap: -12.21% | MA50 gap: -20.26% | MA200 gap: -23.59%
- vol_ratio(Volume/Vol20): 0.13592 | gap_open: 2.92%
- RS vs SILJ gap: 4.08% / slope_proxy: 0.003178
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
- close: 6.93 | RSI14: 46.388453 | ATR14%: 8.61%
- MA20 gap: -2.29% | MA50 gap: -12.97% | MA200 gap: -16.53%
- vol_ratio(Volume/Vol20): 0.079619 | gap_open: 1.17%
- SilverMarginGate: SI=42.224998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.99% / slope_proxy: 0.00612
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
- close: 13.02 | RSI14: 34.987926 | ATR14%: 11.65%
- MA20 gap: -20.44% | MA50 gap: -26.63% | MA200 gap: -53.28%
- vol_ratio(Volume/Vol20): 0.123138 | gap_open: 2.94%
- RS vs SILJ gap: -4.89% / slope_proxy: -0.043342
- RS vs GDXJ gap: -9.83% / slope_proxy: -0.014821
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
