# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-09**
- 실행시간(UTC): **2026-07-09 15:01:14**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.67
- IG OAS 4주 변화: 1.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.3
- VIX: 16.9
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 4.46% / slope_proxy: 0.008083
- GDXJ/GLD gap: -6.02% / slope_proxy: -0.002524

## VZLA (Vizsla Silver)
- close: 3.08 | RSI14: 40.575994 | ATR14%: 6.70%
- MA20 gap: -7.63% | MA50 gap: -11.45% | MA200 gap: -26.93%
- vol_ratio(Volume/Vol20): 0.443542 | gap_open: 2.03%
- RS vs SILJ gap: 0.60% / slope_proxy: 0.005083
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
- close: 6.59 | RSI14: 44.505131 | ATR14%: 7.48%
- MA20 gap: -2.52% | MA50 gap: -13.50% | MA200 gap: -22.60%
- vol_ratio(Volume/Vol20): 0.429818 | gap_open: 2.40%
- SilverMarginGate: SI=60.439999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.73% / slope_proxy: -0.005185
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
- close: 22.059999 | RSI14: 37.682683 | ATR14%: 9.57%
- MA20 gap: -7.50% | MA50 gap: -27.65% | MA200 gap: -17.34%
- vol_ratio(Volume/Vol20): 0.158813 | gap_open: 2.21%
- RS vs SILJ gap: -21.10% / slope_proxy: -0.097388
- RS vs GDXJ gap: -20.28% / slope_proxy: -0.021203
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
