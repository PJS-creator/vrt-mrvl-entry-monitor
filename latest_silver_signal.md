# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-21**
- 실행시간(UTC): **2026-07-21 15:02:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 4.0 bp / latest 2.69
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.31
- VIX: 18.65
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 1.92% / slope_proxy: 0.008293
- GDXJ/GLD gap: -5.84% / slope_proxy: -0.00817

## VZLA (Vizsla Silver)
- close: 3.255 | RSI14: 49.882599 | ATR14%: 5.95%
- MA20 gap: 2.33% | MA50 gap: -5.35% | MA200 gap: -22.00%
- vol_ratio(Volume/Vol20): 0.334767 | gap_open: 3.49%
- RS vs SILJ gap: 8.13% / slope_proxy: 0.005961
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
- close: 6.385 | RSI14: 45.787228 | ATR14%: 6.85%
- MA20 gap: -0.54% | MA50 gap: -12.82% | MA200 gap: -24.55%
- vol_ratio(Volume/Vol20): 0.347768 | gap_open: 4.99%
- SilverMarginGate: SI=59.330002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.75% / slope_proxy: -0.005962
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
- close: 19.955 | RSI14: 38.77764 | ATR14%: 9.40%
- MA20 gap: -7.72% | MA50 gap: -28.21% | MA200 gap: -26.73%
- vol_ratio(Volume/Vol20): 0.231711 | gap_open: 3.04%
- RS vs SILJ gap: -21.21% / slope_proxy: -0.123885
- RS vs GDXJ gap: -21.68% / slope_proxy: -0.027638
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
