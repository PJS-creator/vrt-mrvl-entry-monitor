# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-28**
- 실행시간(UTC): **2026-08-28 15:01:03**

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
- SILJ/SLV gap: 8.52% / slope_proxy: 0.024147
- GDXJ/GLD gap: 15.83% / slope_proxy: 0.005463

## VZLA (Vizsla Silver)
- close: 4.18 | RSI14: 68.751205 | ATR14%: 4.51%
- MA20 gap: 10.29% | MA50 gap: 21.17% | MA200 gap: 2.51%
- vol_ratio(Volume/Vol20): 0.546535 | gap_open: 0.96%
- RS vs SILJ gap: -0.28% / slope_proxy: 0.002488
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
- close: 10.04 | RSI14: 71.104349 | ATR14%: 5.45%
- MA20 gap: 12.89% | MA50 gap: 34.83% | MA200 gap: 14.94%
- vol_ratio(Volume/Vol20): 0.437328 | gap_open: 1.40%
- SilverMarginGate: SI=70.110001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.47% / slope_proxy: 0.00533
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
- close: 25.68 | RSI14: 52.550983 | ATR14%: 7.33%
- MA20 gap: -0.13% | MA50 gap: 10.66% | MA200 gap: -13.15%
- vol_ratio(Volume/Vol20): 0.354525 | gap_open: 0.15%
- RS vs SILJ gap: -10.41% / slope_proxy: -0.104952
- RS vs GDXJ gap: -13.65% / slope_proxy: -0.030412
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
