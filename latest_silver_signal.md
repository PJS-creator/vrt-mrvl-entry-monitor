# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-12**
- 실행시간(UTC): **2026-11-13 03:01:05**

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
- VIX: 17.49
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 1.47% / slope_proxy: 0.004667
- GDXJ/GLD gap: -5.65% / slope_proxy: 0.000157

## VZLA (Vizsla Silver)
- close: 3.12 | RSI14: 43.109939 | ATR14%: 6.45%
- MA20 gap: -3.00% | MA50 gap: -12.32% | MA200 gap: -13.40%
- vol_ratio(Volume/Vol20): 1.115768 | gap_open: 3.70%
- RS vs SILJ gap: 2.19% / slope_proxy: 0.00141
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
- close: 7.05 | RSI14: 42.253526 | ATR14%: 7.57%
- MA20 gap: -5.75% | MA50 gap: -16.44% | MA200 gap: -17.18%
- vol_ratio(Volume/Vol20): 1.283336 | gap_open: 5.16%
- SilverMarginGate: SI=50.459999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.80% / slope_proxy: 0.00922
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
- close: 17.0 | RSI14: 45.840047 | ATR14%: 9.29%
- MA20 gap: -1.23% | MA50 gap: -10.35% | MA200 gap: -41.04%
- vol_ratio(Volume/Vol20): 1.269616 | gap_open: 5.62%
- RS vs SILJ gap: 1.89% / slope_proxy: -0.050031
- RS vs GDXJ gap: -0.69% / slope_proxy: -0.016847
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
