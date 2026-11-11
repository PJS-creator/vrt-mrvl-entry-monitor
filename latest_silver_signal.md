# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-11**
- 실행시간(UTC): **2026-11-11 22:35:50**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.34
- IG OAS 4주 변화: 8.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -25.0 bp / latest 2.66
- VIX: 19.46
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 2.63% / slope_proxy: 0.005061
- GDXJ/GLD gap: -3.94% / slope_proxy: 0.000928

## VZLA (Vizsla Silver)
- close: 3.24 | RSI14: 46.698999 | ATR14%: 6.24%
- MA20 gap: 0.42% | MA50 gap: -9.47% | MA200 gap: -10.53%
- vol_ratio(Volume/Vol20): 0.607551 | gap_open: 0.60%
- RS vs SILJ gap: 1.58% / slope_proxy: 0.001186
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
- close: 7.36 | RSI14: 45.196664 | ATR14%: 7.29%
- MA20 gap: -2.44% | MA50 gap: -13.41% | MA200 gap: -13.94%
- vol_ratio(Volume/Vol20): 0.864608 | gap_open: 0.79%
- SilverMarginGate: SI=51.68 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.99% / slope_proxy: 0.010268
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
- close: 18.700001 | RSI14: 52.560834 | ATR14%: 8.28%
- MA20 gap: 8.51% | MA50 gap: -2.03% | MA200 gap: -35.53%
- vol_ratio(Volume/Vol20): 1.007318 | gap_open: 0.42%
- RS vs SILJ gap: 6.76% / slope_proxy: -0.050113
- RS vs GDXJ gap: 3.63% / slope_proxy: -0.016964
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
