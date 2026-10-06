# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-05**
- 실행시간(UTC): **2026-10-06 02:29:27**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 42.0 bp / latest 3.1
- IG OAS 4주 변화: 4.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: 49.0 bp / latest 2.92
- VIX: 15.31
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: -1.73% / slope_proxy: 0.012173
- GDXJ/GLD gap: 1.47% / slope_proxy: 0.012689

## VZLA (Vizsla Silver)
- close: 3.51 | RSI14: 37.160619 | ATR14%: 5.67%
- MA20 gap: -10.10% | MA50 gap: -7.61% | MA200 gap: -11.58%
- vol_ratio(Volume/Vol20): 1.18403 | gap_open: 1.11%
- RS vs SILJ gap: -0.29% / slope_proxy: 0.002686
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.93 | RSI14: 48.664949 | ATR14%: 6.57%
- MA20 gap: -2.53% | MA50 gap: 1.02% | MA200 gap: -0.68%
- vol_ratio(Volume/Vol20): 0.693075 | gap_open: 0.80%
- SilverMarginGate: SI=60.990002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.22% / slope_proxy: 0.01934
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 18.799999 | RSI14: 37.467786 | ATR14%: 7.56%
- MA20 gap: -9.15% | MA50 gap: -17.53% | MA200 gap: -39.02%
- vol_ratio(Volume/Vol20): 0.719741 | gap_open: 0.75%
- RS vs SILJ gap: -11.78% / slope_proxy: -0.062104
- RS vs GDXJ gap: -14.63% / slope_proxy: -0.020179
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
