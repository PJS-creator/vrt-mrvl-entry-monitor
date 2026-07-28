# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-28**
- 실행시간(UTC): **2026-07-28 15:01:14**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.81
- IG OAS 4주 변화: 5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 25.0 bp / latest 2.43
- VIX: 18.67
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 2.00% / slope_proxy: 0.007251
- GDXJ/GLD gap: -3.85% / slope_proxy: -0.008853

## VZLA (Vizsla Silver)
- close: 3.165 | RSI14: 46.182744 | ATR14%: 6.12%
- MA20 gap: -1.02% | MA50 gap: -6.73% | MA200 gap: -23.59%
- vol_ratio(Volume/Vol20): 0.150337 | gap_open: 2.11%
- RS vs SILJ gap: 6.68% / slope_proxy: 0.006259
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
- close: 6.13 | RSI14: 42.681171 | ATR14%: 7.04%
- MA20 gap: -4.27% | MA50 gap: -13.23% | MA200 gap: -27.40%
- vol_ratio(Volume/Vol20): 0.447268 | gap_open: 0.16%
- SilverMarginGate: SI=57.355 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.79% / slope_proxy: -0.005316
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
- close: 19.309999 | RSI14: 38.69768 | ATR14%: 9.27%
- MA20 gap: -8.38% | MA50 gap: -24.71% | MA200 gap: -30.00%
- vol_ratio(Volume/Vol20): 0.212031 | gap_open: 2.40%
- RS vs SILJ gap: -19.10% / slope_proxy: -0.134949
- RS vs GDXJ gap: -22.27% / slope_proxy: -0.031106
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
