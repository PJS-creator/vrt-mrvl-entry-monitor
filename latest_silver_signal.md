# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-27**
- 실행시간(UTC): **2026-08-29 15:00:52**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -21.0 bp / latest 2.63
- IG OAS 4주 변화: -1.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -7.0 bp / latest 2.34
- VIX: 14.51
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 10.33% / slope_proxy: 0.023351
- GDXJ/GLD gap: 16.12% / slope_proxy: 0.004447

## VZLA (Vizsla Silver)
- close: 4.16 | RSI14: 68.258398 | ATR14%: 4.42%
- MA20 gap: 11.29% | MA50 gap: 21.01% | MA200 gap: 2.01%
- vol_ratio(Volume/Vol20): 1.265354 | gap_open: 0.75%
- RS vs SILJ gap: -1.46% / slope_proxy: 0.002838
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
- close: 10.02 | RSI14: 70.944936 | ATR14%: 5.31%
- MA20 gap: 14.98% | MA50 gap: 35.49% | MA200 gap: 15.01%
- vol_ratio(Volume/Vol20): 0.83007 | gap_open: 0.21%
- SilverMarginGate: SI=69.429001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.86% / slope_proxy: 0.004378
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
- close: 25.959999 | RSI14: 53.589599 | ATR14%: 7.29%
- MA20 gap: 2.18% | MA50 gap: 11.88% | MA200 gap: -11.93%
- vol_ratio(Volume/Vol20): 0.93497 | gap_open: 0.67%
- RS vs SILJ gap: -10.57% / slope_proxy: -0.106953
- RS vs GDXJ gap: -13.90% / slope_proxy: -0.030572
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
