# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-13**
- 실행시간(UTC): **2026-11-13 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 3.3
- IG OAS 4주 변화: 6.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: -10.0 bp / latest 2.78
- VIX: 18.7
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 2.08% / slope_proxy: 0.004402
- GDXJ/GLD gap: -5.33% / slope_proxy: -0.000756

## VZLA (Vizsla Silver)
- close: 3.115 | RSI14: 42.961783 | ATR14%: 6.15%
- MA20 gap: -2.95% | MA50 gap: -11.93% | MA200 gap: -13.21%
- vol_ratio(Volume/Vol20): 0.121714 | gap_open: 0.32%
- RS vs SILJ gap: 1.62% / slope_proxy: 0.001663
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
- close: 7.02 | RSI14: 41.968702 | ATR14%: 7.31%
- MA20 gap: -5.32% | MA50 gap: -16.12% | MA200 gap: -17.19%
- vol_ratio(Volume/Vol20): 0.052083 | gap_open: 0.57%
- SilverMarginGate: SI=49.82 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.42% / slope_proxy: 0.00791
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
- close: 16.41 | RSI14: 43.74923 | ATR14%: 9.29%
- MA20 gap: -4.45% | MA50 gap: -12.83% | MA200 gap: -42.79%
- vol_ratio(Volume/Vol20): 0.093064 | gap_open: 0.06%
- RS vs SILJ gap: -1.62% / slope_proxy: -0.049472
- RS vs GDXJ gap: -4.38% / slope_proxy: -0.016599
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
