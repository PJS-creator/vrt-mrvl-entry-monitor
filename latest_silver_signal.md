# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-10**
- 실행시간(UTC): **2026-07-10 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.31
- VIX: 15.84
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 5.19% / slope_proxy: 0.008602
- GDXJ/GLD gap: -4.85% / slope_proxy: -0.002739

## VZLA (Vizsla Silver)
- close: 3.1245 | RSI14: 42.528661 | ATR14%: 6.52%
- MA20 gap: -6.30% | MA50 gap: -10.06% | MA200 gap: -25.79%
- vol_ratio(Volume/Vol20): 0.264045 | gap_open: 0.95%
- RS vs SILJ gap: 2.33% / slope_proxy: 0.005147
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
- close: 6.5 | RSI14: 43.547637 | ATR14%: 7.40%
- MA20 gap: -4.24% | MA50 gap: -14.39% | MA200 gap: -23.62%
- vol_ratio(Volume/Vol20): 0.178578 | gap_open: 1.20%
- SilverMarginGate: SI=60.110001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.42% / slope_proxy: -0.004909
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
- close: 21.299999 | RSI14: 35.356873 | ATR14%: 9.54%
- MA20 gap: -10.32% | MA50 gap: -29.46% | MA200 gap: -20.40%
- vol_ratio(Volume/Vol20): 0.148976 | gap_open: 0.00%
- RS vs SILJ gap: -22.87% / slope_proxy: -0.099863
- RS vs GDXJ gap: -22.77% / slope_proxy: -0.02175
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
