# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-26**
- 실행시간(UTC): **2026-05-26 06:04:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.78
- IG OAS 4주 변화: -5.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.18
- VIX: 16.76
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -4.97% / slope_proxy: -0.008262
- GDXJ/GLD gap: -4.77% / slope_proxy: -0.004815

## VZLA (Vizsla Silver)
- close: 3.37 | RSI14: 45.843016 | ATR14%: 6.20%
- MA20 gap: -3.34% | MA50 gap: -0.44% | MA200 gap: -20.38%
- vol_ratio(Volume/Vol20): 0.593593 | gap_open: 0.00%
- RS vs SILJ gap: 4.07% / slope_proxy: -0.003406
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
- close: 8.03 | RSI14: 42.580766 | ATR14%: 7.94%
- MA20 gap: -6.45% | MA50 gap: -4.46% | MA200 gap: -2.39%
- vol_ratio(Volume/Vol20): 0.803816 | gap_open: 0.24%
- SilverMarginGate: SI=76.629997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.73% / slope_proxy: -0.016187
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
- close: 32.32 | RSI14: 39.758028 | ATR14%: 10.16%
- MA20 gap: -13.52% | MA50 gap: -12.94% | MA200 gap: 38.42%
- vol_ratio(Volume/Vol20): 0.610742 | gap_open: 1.47%
- RS vs SILJ gap: -8.65% / slope_proxy: 0.026713
- RS vs GDXJ gap: -6.54% / slope_proxy: 0.007832
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
