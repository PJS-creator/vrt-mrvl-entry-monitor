# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-16**
- 실행시간(UTC): **2026-10-17 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 53.0 bp / latest 3.23
- IG OAS 4주 변화: 6.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 17.0 bp / latest 2.78
- VIX: 16.46
- NFCI: -0.499

### Leadership ratios
- SILJ/SLV gap: -1.07% / slope_proxy: 0.007097
- GDXJ/GLD gap: -3.38% / slope_proxy: 0.011954

## VZLA (Vizsla Silver)
- close: 3.25 | RSI14: 35.93482 | ATR14%: 5.68%
- MA20 gap: -11.19% | MA50 gap: -14.80% | MA200 gap: -16.08%
- vol_ratio(Volume/Vol20): 0.640984 | gap_open: 0.60%
- RS vs SILJ gap: -2.46% / slope_proxy: 0.002236
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
- close: 8.34 | RSI14: 44.488218 | ATR14%: 6.51%
- MA20 gap: -5.28% | MA50 gap: -8.71% | MA200 gap: -6.79%
- vol_ratio(Volume/Vol20): 0.923886 | gap_open: 0.36%
- SilverMarginGate: SI=57.134998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.94% / slope_proxy: 0.022099
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
- close: 17.17 | RSI14: 37.850823 | ATR14%: 7.55%
- MA20 gap: -10.23% | MA50 gap: -22.69% | MA200 gap: -44.01%
- vol_ratio(Volume/Vol20): 1.081835 | gap_open: 1.03%
- RS vs SILJ gap: -12.54% / slope_proxy: -0.051781
- RS vs GDXJ gap: -16.81% / slope_proxy: -0.017787
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
