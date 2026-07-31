# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-30**
- 실행시간(UTC): **2026-07-31 03:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 13.0 bp / latest 2.87
- IG OAS 4주 변화: 5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.41
- VIX: 20.66
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 2.39% / slope_proxy: 0.007558
- GDXJ/GLD gap: -2.82% / slope_proxy: -0.008658

## VZLA (Vizsla Silver)
- close: 3.24 | RSI14: 49.343402 | ATR14%: 5.88%
- MA20 gap: 1.60% | MA50 gap: -4.22% | MA200 gap: -21.53%
- vol_ratio(Volume/Vol20): 0.454685 | gap_open: 2.24%
- RS vs SILJ gap: 4.33% / slope_proxy: 0.006069
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 6.78 | RSI14: 53.432628 | ATR14%: 6.56%
- MA20 gap: 5.78% | MA50 gap: -2.02% | MA200 gap: -19.63%
- vol_ratio(Volume/Vol20): 0.70341 | gap_open: 0.63%
- SilverMarginGate: SI=58.720001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.18% / slope_proxy: -0.005084
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
- close: 20.07 | RSI14: 42.350508 | ATR14%: 8.66%
- MA20 gap: -3.30% | MA50 gap: -19.81% | MA200 gap: -27.58%
- vol_ratio(Volume/Vol20): 1.110133 | gap_open: 4.12%
- RS vs SILJ gap: -18.11% / slope_proxy: -0.141062
- RS vs GDXJ gap: -20.30% / slope_proxy: -0.033193
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
