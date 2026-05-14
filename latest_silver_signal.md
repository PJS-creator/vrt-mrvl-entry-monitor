# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-13**
- 실행시간(UTC): **2026-05-14 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.82
- IG OAS 4주 변화: -4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 10.0 bp / latest 1.99
- VIX: 17.99
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -3.93% / slope_proxy: 0.002867
- GDXJ/GLD gap: 4.42% / slope_proxy: -0.003502

## VZLA (Vizsla Silver)
- close: 3.85 | RSI14: 63.313849 | ATR14%: 5.60%
- MA20 gap: 10.71% | MA50 gap: 10.95% | MA200 gap: -8.75%
- vol_ratio(Volume/Vol20): 0.884021 | gap_open: 1.56%
- RS vs SILJ gap: 0.87% / slope_proxy: -0.012062
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
- close: 10.02 | RSI14: 63.998191 | ATR14%: 6.76%
- MA20 gap: 15.28% | MA50 gap: 16.08% | MA200 gap: 24.37%
- vol_ratio(Volume/Vol20): 0.881012 | gap_open: 1.97%
- SilverMarginGate: SI=87.455002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.14% / slope_proxy: -0.025767
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
- close: 43.630001 | RSI14: 58.508831 | ATR14%: 8.59%
- MA20 gap: 10.60% | MA50 gap: 14.30% | MA200 gap: 96.05%
- vol_ratio(Volume/Vol20): 0.972715 | gap_open: 1.17%
- RS vs SILJ gap: 3.26% / slope_proxy: 0.033571
- RS vs GDXJ gap: 8.95% / slope_proxy: 0.006872
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
