# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-31**
- 실행시간(UTC): **2026-08-31 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -25.0 bp / latest 2.6
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -7.0 bp / latest 2.34
- VIX: 14.43
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 7.84% / slope_proxy: 0.025041
- GDXJ/GLD gap: 12.84% / slope_proxy: 0.006376

## VZLA (Vizsla Silver)
- close: 3.99 | RSI14: 60.157834 | ATR14%: 4.66%
- MA20 gap: 4.52% | MA50 gap: 15.48% | MA200 gap: -2.10%
- vol_ratio(Volume/Vol20): 0.256992 | gap_open: 0.00%
- RS vs SILJ gap: 0.71% / slope_proxy: 0.00212
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
- close: 9.26 | RSI14: 58.383061 | ATR14%: 5.97%
- MA20 gap: 2.96% | MA50 gap: 23.83% | MA200 gap: 5.80%
- vol_ratio(Volume/Vol20): 0.095089 | gap_open: 2.73%
- SilverMarginGate: SI=66.940002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.44% / slope_proxy: 0.006113
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
- close: 23.66 | RSI14: 46.069117 | ATR14%: 8.02%
- MA20 gap: -8.19% | MA50 gap: 2.33% | MA200 gap: -20.16%
- vol_ratio(Volume/Vol20): 0.301813 | gap_open: 0.02%
- RS vs SILJ gap: -12.21% / slope_proxy: -0.102314
- RS vs GDXJ gap: -15.31% / slope_proxy: -0.030012
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
