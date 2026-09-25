# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-24**
- 실행시간(UTC): **2026-09-25 03:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.73
- IG OAS 4주 변화: -3.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 42.0 bp / latest 2.76
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 1.00% / slope_proxy: 0.020701
- GDXJ/GLD gap: 6.28% / slope_proxy: 0.014393

## VZLA (Vizsla Silver)
- close: 3.94 | RSI14: 51.438311 | ATR14%: 5.13%
- MA20 gap: -1.41% | MA50 gap: 6.42% | MA200 gap: -2.07%
- vol_ratio(Volume/Vol20): 0.900404 | gap_open: 0.99%
- RS vs SILJ gap: 6.23% / slope_proxy: 0.000622
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
- close: 8.92 | RSI14: 48.248292 | ATR14%: 6.87%
- MA20 gap: -5.71% | MA50 gap: 6.22% | MA200 gap: -0.88%
- vol_ratio(Volume/Vol20): 0.837324 | gap_open: 1.46%
- SilverMarginGate: SI=64.205002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.41% / slope_proxy: 0.017772
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
- close: 20.889999 | RSI14: 42.547435 | ATR14%: 7.37%
- MA20 gap: -6.06% | MA50 gap: -8.49% | MA200 gap: -31.57%
- vol_ratio(Volume/Vol20): 0.718642 | gap_open: 1.55%
- RS vs SILJ gap: -10.62% / slope_proxy: -0.077411
- RS vs GDXJ gap: -13.94% / slope_proxy: -0.02432
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
