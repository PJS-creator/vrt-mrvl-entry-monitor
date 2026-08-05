# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-04**
- 실행시간(UTC): **2026-08-05 03:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.78
- IG OAS 4주 변화: 3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.43
- VIX: 15.86
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 6.04% / slope_proxy: 0.008811
- GDXJ/GLD gap: 1.08% / slope_proxy: -0.008342

## VZLA (Vizsla Silver)
- close: 3.4 | RSI14: 55.131682 | ATR14%: 5.60%
- MA20 gap: 6.45% | MA50 gap: 0.65% | MA200 gap: -17.19%
- vol_ratio(Volume/Vol20): 1.337957 | gap_open: 2.76%
- RS vs SILJ gap: 3.84% / slope_proxy: 0.006085
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
- close: 7.2 | RSI14: 58.684479 | ATR14%: 6.42%
- MA20 gap: 11.88% | MA50 gap: 5.39% | MA200 gap: -14.59%
- vol_ratio(Volume/Vol20): 1.200868 | gap_open: 2.97%
- SilverMarginGate: SI=61.005001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.88% / slope_proxy: -0.005324
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
- close: 22.360001 | RSI14: 52.412805 | ATR14%: 7.69%
- MA20 gap: 9.39% | MA50 gap: -7.86% | MA200 gap: -19.87%
- vol_ratio(Volume/Vol20): 0.896334 | gap_open: 3.69%
- RS vs SILJ gap: -10.88% / slope_proxy: -0.145923
- RS vs GDXJ gap: -11.86% / slope_proxy: -0.034908
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
