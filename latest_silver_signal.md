# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-10**
- 실행시간(UTC): **2026-09-11 00:30:40**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.71
- IG OAS 4주 변화: 2.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.46
- VIX: 16.46
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 7.08% / slope_proxy: 0.02825
- GDXJ/GLD gap: 13.62% / slope_proxy: 0.013112

## VZLA (Vizsla Silver)
- close: 4.09 | RSI14: 58.49109 | ATR14%: 4.90%
- MA20 gap: 3.82% | MA50 gap: 15.21% | MA200 gap: 0.76%
- vol_ratio(Volume/Vol20): 1.011902 | gap_open: 2.57%
- RS vs SILJ gap: 0.78% / slope_proxy: 0.000291
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
- close: 10.43 | RSI14: 65.453201 | ATR14%: 5.60%
- MA20 gap: 9.48% | MA50 gap: 32.17% | MA200 gap: 17.34%
- vol_ratio(Volume/Vol20): 1.019472 | gap_open: 1.50%
- SilverMarginGate: SI=63.994999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 18.15% / slope_proxy: 0.013118
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
- close: 22.809999 | RSI14: 44.990636 | ATR14%: 7.76%
- MA20 gap: -8.72% | MA50 gap: -1.13% | MA200 gap: -24.02%
- vol_ratio(Volume/Vol20): 0.998625 | gap_open: 1.92%
- RS vs SILJ gap: -15.03% / slope_proxy: -0.090366
- RS vs GDXJ gap: -17.17% / slope_proxy: -0.02728
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
