# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-16**
- 실행시간(UTC): **2026-09-16 15:00:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.76
- IG OAS 4주 변화: -2.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.6
- VIX: 17.2
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 0.71% / slope_proxy: 0.025643
- GDXJ/GLD gap: 6.94% / slope_proxy: 0.013723

## VZLA (Vizsla Silver)
- close: 3.7308 | RSI14: 45.077179 | ATR14%: 5.33%
- MA20 gap: -6.17% | MA50 gap: 3.35% | MA200 gap: -7.85%
- vol_ratio(Volume/Vol20): 0.133695 | gap_open: 2.13%
- RS vs SILJ gap: 0.33% / slope_proxy: -0.00021
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
- close: 8.575 | RSI14: 43.732148 | ATR14%: 6.99%
- MA20 gap: -10.91% | MA50 gap: 5.31% | MA200 gap: -4.45%
- vol_ratio(Volume/Vol20): 0.268617 | gap_open: 2.78%
- SilverMarginGate: SI=65.084999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.82% / slope_proxy: 0.016296
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
- close: 20.379999 | RSI14: 37.464807 | ATR14%: 8.02%
- MA20 gap: -13.72% | MA50 gap: -10.81% | MA200 gap: -32.73%
- vol_ratio(Volume/Vol20): 0.201764 | gap_open: 2.32%
- RS vs SILJ gap: -15.13% / slope_proxy: -0.084922
- RS vs GDXJ gap: -19.10% / slope_proxy: -0.026406
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
