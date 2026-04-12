# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-10**
- 실행시간(UTC): **2026-04-12 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -27.0 bp / latest 2.9
- IG OAS 4주 변화: -8.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.95
- VIX: 19.49
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 2.44% / slope_proxy: 0.003438
- GDXJ/GLD gap: 1.44% / slope_proxy: -0.004706

## VZLA (Vizsla Silver)
- close: 3.25 | RSI14: 40.610788 | ATR14%: 6.83%
- MA20 gap: -0.66% | MA50 gap: -15.48% | MA200 gap: -22.24%
- vol_ratio(Volume/Vol20): 0.641437 | gap_open: 1.53%
- RS vs SILJ gap: -18.72% / slope_proxy: -0.027499
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
- close: 7.99 | RSI14: 43.405859 | ATR14%: 9.77%
- MA20 gap: -0.24% | MA50 gap: -19.26% | MA200 gap: 7.05%
- vol_ratio(Volume/Vol20): 0.625312 | gap_open: 0.12%
- SilverMarginGate: SI=76.480003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.66% / slope_proxy: -0.022885
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
- close: 37.5 | RSI14: 51.198048 | ATR14%: 11.12%
- MA20 gap: 6.78% | MA50 gap: -3.63% | MA200 gap: 107.09%
- vol_ratio(Volume/Vol20): 0.7082 | gap_open: 0.41%
- RS vs SILJ gap: 0.45% / slope_proxy: 0.124203
- RS vs GDXJ gap: -3.53% / slope_proxy: 0.032231
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
