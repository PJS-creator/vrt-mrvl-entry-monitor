# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-23**
- 실행시간(UTC): **2026-09-23 15:01:13**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.68
- IG OAS 4주 변화: -4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.62
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 1.42% / slope_proxy: 0.021696
- GDXJ/GLD gap: 7.53% / slope_proxy: 0.014294

## VZLA (Vizsla Silver)
- close: 4.0591 | RSI14: 56.269419 | ATR14%: 5.02%
- MA20 gap: 1.42% | MA50 gap: 10.06% | MA200 gap: 0.76%
- vol_ratio(Volume/Vol20): 0.347053 | gap_open: 1.47%
- RS vs SILJ gap: 7.42% / slope_proxy: 0.000429
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
- close: 8.955 | RSI14: 48.515434 | ATR14%: 6.90%
- MA20 gap: -5.80% | MA50 gap: 7.23% | MA200 gap: -0.44%
- vol_ratio(Volume/Vol20): 0.504514 | gap_open: 2.33%
- SilverMarginGate: SI=65.084999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.04% / slope_proxy: 0.017435
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
- close: 21.5 | RSI14: 45.15133 | ATR14%: 7.34%
- MA20 gap: -4.48% | MA50 gap: -5.92% | MA200 gap: -29.47%
- vol_ratio(Volume/Vol20): 0.463248 | gap_open: 6.04%
- RS vs SILJ gap: -10.17% / slope_proxy: -0.07881
- RS vs GDXJ gap: -13.19% / slope_proxy: -0.024681
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
