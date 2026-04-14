# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-14**
- 실행시간(UTC): **2026-04-14 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -32.0 bp / latest 2.95
- IG OAS 4주 변화: -12.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 3.0 bp / latest 1.95
- VIX: 19.12
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 1.97% / slope_proxy: 0.006888
- GDXJ/GLD gap: 2.74% / slope_proxy: -0.004497

## VZLA (Vizsla Silver)
- close: 3.395 | RSI14: 46.821744 | ATR14%: 6.26%
- MA20 gap: 4.60% | MA50 gap: -9.73% | MA200 gap: -18.85%
- vol_ratio(Volume/Vol20): 0.280921 | gap_open: 1.81%
- RS vs SILJ gap: -16.27% / slope_proxy: -0.027547
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 9.05 | RSI14: 53.472373 | ATR14%: 8.48%
- MA20 gap: 13.40% | MA50 gap: -6.98% | MA200 gap: 20.28%
- vol_ratio(Volume/Vol20): 0.604349 | gap_open: 1.63%
- SilverMarginGate: SI=79.195 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.35% / slope_proxy: -0.023563
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
- close: 41.759998 | RSI14: 58.377001 | ATR14%: 9.58%
- MA20 gap: 18.22% | MA50 gap: 7.42% | MA200 gap: 125.95%
- vol_ratio(Volume/Vol20): 0.362318 | gap_open: 4.40%
- RS vs SILJ gap: 7.40% / slope_proxy: 0.106738
- RS vs GDXJ gap: 4.71% / slope_proxy: 0.027254
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trigger(Breakout/Retest)=FALSE
