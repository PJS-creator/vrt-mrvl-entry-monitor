# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-06**
- 실행시간(UTC): **2026-08-06 15:01:22**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.75
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.4
- VIX: 15.81
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 8.43% / slope_proxy: 0.010603
- GDXJ/GLD gap: 4.34% / slope_proxy: -0.007546

## VZLA (Vizsla Silver)
- close: 3.59 | RSI14: 60.629215 | ATR14%: 5.24%
- MA20 gap: 10.56% | MA50 gap: 6.21% | MA200 gap: -12.32%
- vol_ratio(Volume/Vol20): 0.183826 | gap_open: 1.39%
- RS vs SILJ gap: 2.66% / slope_proxy: 0.006082
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
- close: 7.98 | RSI14: 66.543058 | ATR14%: 6.04%
- MA20 gap: 21.15% | MA50 gap: 16.86% | MA200 gap: -5.47%
- vol_ratio(Volume/Vol20): 0.297265 | gap_open: 3.39%
- SilverMarginGate: SI=61.799999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.29% / slope_proxy: -0.004964
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
- close: 24.370001 | RSI14: 58.699297 | ATR14%: 7.22%
- MA20 gap: 17.43% | MA50 gap: 1.82% | MA200 gap: -13.16%
- vol_ratio(Volume/Vol20): 0.256067 | gap_open: 3.92%
- RS vs SILJ gap: -7.42% / slope_proxy: -0.145956
- RS vs GDXJ gap: -9.78% / slope_proxy: -0.03554
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
