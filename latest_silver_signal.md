# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-12**
- 실행시간(UTC): **2026-11-12 15:01:06**

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
- 10Y Real Yield 4주 변화: -25.0 bp / latest 2.66
- VIX: 17.49
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 2.47% / slope_proxy: 0.004754
- GDXJ/GLD gap: -4.94% / slope_proxy: 0.000193

## VZLA (Vizsla Silver)
- close: 3.125 | RSI14: 43.248436 | ATR14%: 6.35%
- MA20 gap: -2.85% | MA50 gap: -12.18% | MA200 gap: -13.26%
- vol_ratio(Volume/Vol20): 0.129176 | gap_open: 3.70%
- RS vs SILJ gap: 1.32% / slope_proxy: 0.001391
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
- close: 7.035 | RSI14: 42.120805 | ATR14%: 7.58%
- MA20 gap: -5.94% | MA50 gap: -16.61% | MA200 gap: -17.35%
- vol_ratio(Volume/Vol20): 0.170297 | gap_open: 5.16%
- SilverMarginGate: SI=50.165001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.98% / slope_proxy: 0.009158
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
- close: 17.575001 | RSI14: 47.912207 | ATR14%: 8.67%
- MA20 gap: 1.94% | MA50 gap: -7.38% | MA200 gap: -39.05%
- vol_ratio(Volume/Vol20): 0.194637 | gap_open: 5.62%
- RS vs SILJ gap: 4.22% / slope_proxy: -0.049748
- RS vs GDXJ gap: 1.97% / slope_proxy: -0.016769
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
