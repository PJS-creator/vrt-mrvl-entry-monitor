# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-23**
- 실행시간(UTC): **2026-06-23 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.66
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 3.0 bp / latest 2.21
- VIX: 17.28
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 5.69% / slope_proxy: 0.000241
- GDXJ/GLD gap: -4.34% / slope_proxy: -0.00315

## VZLA (Vizsla Silver)
- close: 3.39 | RSI14: 44.462187 | ATR14%: 6.71%
- MA20 gap: -6.68% | MA50 gap: -3.95% | MA200 gap: -20.22%
- vol_ratio(Volume/Vol20): 0.227727 | gap_open: 5.40%
- RS vs SILJ gap: 10.02% / slope_proxy: 0.004567
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
- close: 6.71 | RSI14: 40.891392 | ATR14%: 9.03%
- MA20 gap: -8.14% | MA50 gap: -17.40% | MA200 gap: -21.14%
- vol_ratio(Volume/Vol20): 0.388434 | gap_open: 4.67%
- SilverMarginGate: SI=62.134998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.85% / slope_proxy: -0.010224
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
- close: 23.719999 | RSI14: 34.348396 | ATR14%: 10.61%
- MA20 gap: -16.31% | MA50 gap: -31.07% | MA200 gap: -7.97%
- vol_ratio(Volume/Vol20): 0.356218 | gap_open: 5.51%
- RS vs SILJ gap: -21.82% / slope_proxy: -0.076245
- RS vs GDXJ gap: -20.37% / slope_proxy: -0.01661
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
