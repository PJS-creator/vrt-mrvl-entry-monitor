# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-10**
- 실행시간(UTC): **2026-08-10 23:16:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.4
- VIX: 14.9
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 8.90% / slope_proxy: 0.012088
- GDXJ/GLD gap: 9.74% / slope_proxy: -0.006535

## VZLA (Vizsla Silver)
- close: 3.88 | RSI14: 66.802868 | ATR14%: 5.08%
- MA20 gap: 16.96% | MA50 gap: 14.68% | MA200 gap: -5.09%
- vol_ratio(Volume/Vol20): 1.130671 | gap_open: 0.27%
- RS vs SILJ gap: 2.64% / slope_proxy: 0.006083
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
- close: 8.98 | RSI14: 74.165618 | ATR14%: 5.74%
- MA20 gap: 31.82% | MA50 gap: 30.94% | MA200 gap: 6.05%
- vol_ratio(Volume/Vol20): 1.511159 | gap_open: 1.19%
- SilverMarginGate: SI=65.964996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.25% / slope_proxy: -0.004267
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
- close: 27.290001 | RSI14: 65.465768 | ATR14%: 6.85%
- MA20 gap: 27.97% | MA50 gap: 15.17% | MA200 gap: -3.40%
- vol_ratio(Volume/Vol20): 1.130655 | gap_open: 0.94%
- RS vs SILJ gap: -2.34% / slope_proxy: -0.144443
- RS vs GDXJ gap: -4.94% / slope_proxy: -0.036195
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
