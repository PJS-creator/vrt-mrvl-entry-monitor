# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-21**
- 실행시간(UTC): **2026-09-21 15:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.68
- IG OAS 4주 변화: -4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.61
- VIX: 14.81
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: -0.30% / slope_proxy: 0.022587
- GDXJ/GLD gap: 7.23% / slope_proxy: 0.01419

## VZLA (Vizsla Silver)
- close: 3.9904 | RSI14: 53.760042 | ATR14%: 5.17%
- MA20 gap: -0.04% | MA50 gap: 8.86% | MA200 gap: -1.04%
- vol_ratio(Volume/Vol20): 0.162368 | gap_open: 0.00%
- RS vs SILJ gap: 5.79% / slope_proxy: 0.000172
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

## SCZM (Santacruz Silver)
- close: 9.085 | RSI14: 49.720737 | ATR14%: 6.94%
- MA20 gap: -4.77% | MA50 gap: 9.46% | MA200 gap: 1.01%
- vol_ratio(Volume/Vol20): 0.228857 | gap_open: 1.99%
- SilverMarginGate: SI=66.480003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.88% / slope_proxy: 0.017188
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
- close: 20.74 | RSI14: 40.978998 | ATR14%: 7.67%
- MA20 gap: -8.76% | MA50 gap: -9.18% | MA200 gap: -31.86%
- vol_ratio(Volume/Vol20): 0.247914 | gap_open: 0.47%
- RS vs SILJ gap: -13.69% / slope_proxy: -0.080433
- RS vs GDXJ gap: -17.14% / slope_proxy: -0.025248
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
