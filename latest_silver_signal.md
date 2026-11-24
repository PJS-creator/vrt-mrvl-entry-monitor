# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-24**
- 실행시간(UTC): **2026-11-24 22:35:43**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.63
- IG OAS 4주 변화: 7.0 bp / latest 0.97
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.79
- VIX: 26.62
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 2.27% / slope_proxy: 0.000779
- GDXJ/GLD gap: -11.05% / slope_proxy: -0.009049

## VZLA (Vizsla Silver)
- close: 2.69 | RSI14: 38.188168 | ATR14%: 8.15%
- MA20 gap: -12.21% | MA50 gap: -20.26% | MA200 gap: -23.59%
- vol_ratio(Volume/Vol20): 1.032594 | gap_open: 2.92%
- RS vs SILJ gap: 5.96% / slope_proxy: 0.003221
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
- close: 6.85 | RSI14: 45.602089 | ATR14%: 8.76%
- MA20 gap: -3.36% | MA50 gap: -13.96% | MA200 gap: -17.49%
- vol_ratio(Volume/Vol20): 0.979906 | gap_open: 1.17%
- SilverMarginGate: SI=40.709999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.72% / slope_proxy: 0.00616
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
- close: 12.87 | RSI14: 34.545957 | ATR14%: 11.88%
- MA20 gap: -21.32% | MA50 gap: -27.46% | MA200 gap: -53.82%
- vol_ratio(Volume/Vol20): 0.840064 | gap_open: 2.94%
- RS vs SILJ gap: -4.27% / slope_proxy: -0.043269
- RS vs GDXJ gap: -8.62% / slope_proxy: -0.014787
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
