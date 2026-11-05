# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-05**
- 실행시간(UTC): **2026-11-05 15:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 37.0 bp / latest 3.4
- IG OAS 4주 변화: 10.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -26.0 bp / latest 2.65
- VIX: 16.61
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: -0.02% / slope_proxy: 0.004887
- GDXJ/GLD gap: -7.34% / slope_proxy: 0.003529

## VZLA (Vizsla Silver)
- close: 3.185 | RSI14: 44.296737 | ATR14%: 6.03%
- MA20 gap: -1.61% | MA50 gap: -12.33% | MA200 gap: -13.59%
- vol_ratio(Volume/Vol20): 0.130309 | gap_open: 1.52%
- RS vs SILJ gap: 2.23% / slope_proxy: 0.000498
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
- close: 7.38 | RSI14: 44.480884 | ATR14%: 7.07%
- MA20 gap: -4.67% | MA50 gap: -14.70% | MA200 gap: -15.26%
- vol_ratio(Volume/Vol20): 0.14075 | gap_open: 2.34%
- SilverMarginGate: SI=52.154999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.64% / slope_proxy: 0.014433
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

## HYMC (Hycroft Mining)
- close: 16.35 | RSI14: 42.768166 | ATR14%: 7.81%
- MA20 gap: -3.19% | MA50 gap: -15.80% | MA200 gap: -44.80%
- vol_ratio(Volume/Vol20): 0.23676 | gap_open: 1.52%
- RS vs SILJ gap: -5.75% / slope_proxy: -0.051442
- RS vs GDXJ gap: -10.38% / slope_proxy: -0.017241
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
