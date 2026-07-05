# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-03**
- 실행시간(UTC): **2026-07-05 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.75
- IG OAS 4주 변화: 1.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 14.0 bp / latest 2.25
- VIX: 16.59
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 8.38% / slope_proxy: 0.007288
- GDXJ/GLD gap: -2.34% / slope_proxy: -0.0019

## VZLA (Vizsla Silver)
- close: 3.34 | RSI14: 46.500424 | ATR14%: 6.42%
- MA20 gap: -2.14% | MA50 gap: -4.65% | MA200 gap: -21.02%
- vol_ratio(Volume/Vol20): 1.351179 | gap_open: 3.99%
- RS vs SILJ gap: 5.24% / slope_proxy: 0.004781
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
- close: 6.69 | RSI14: 43.567324 | ATR14%: 7.64%
- MA20 gap: -1.35% | MA50 gap: -14.11% | MA200 gap: -21.43%
- vol_ratio(Volume/Vol20): 1.248563 | gap_open: 3.19%
- SilverMarginGate: SI=62.814999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.73% / slope_proxy: -0.008399
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
- close: 23.620001 | RSI14: 38.953731 | ATR14%: 9.42%
- MA20 gap: -4.92% | MA50 gap: -25.77% | MA200 gap: -10.42%
- vol_ratio(Volume/Vol20): 0.685231 | gap_open: 4.51%
- RS vs SILJ gap: -20.98% / slope_proxy: -0.089211
- RS vs GDXJ gap: -19.84% / slope_proxy: -0.019533
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
