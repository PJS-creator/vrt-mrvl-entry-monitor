# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-09**
- 실행시간(UTC): **2026-04-09 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -15.0 bp / latest 2.94
- IG OAS 4주 변화: -5.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 14.0 bp / latest 1.96
- VIX: 21.04
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 3.08% / slope_proxy: 0.001848
- GDXJ/GLD gap: -0.62% / slope_proxy: -0.004696

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 40.924596 | ATR14%: 7.01%
- MA20 gap: -1.29% | MA50 gap: -16.78% | MA200 gap: -21.98%
- vol_ratio(Volume/Vol20): 0.226276 | gap_open: 0.61%
- RS vs SILJ gap: -18.10% / slope_proxy: -0.02741
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
- close: 7.9515 | RSI14: 42.762991 | ATR14%: 10.13%
- MA20 gap: -1.76% | MA50 gap: -20.77% | MA200 gap: 6.92%
- vol_ratio(Volume/Vol20): 0.124829 | gap_open: 0.50%
- SilverMarginGate: SI=74.870003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.24% / slope_proxy: -0.022615
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
- close: 36.470001 | RSI14: 49.62016 | ATR14%: 11.35%
- MA20 gap: 3.83% | MA50 gap: -6.84% | MA200 gap: 103.47%
- vol_ratio(Volume/Vol20): 0.186495 | gap_open: 0.49%
- RS vs SILJ gap: -0.56% / slope_proxy: 0.132621
- RS vs GDXJ gap: -4.19% / slope_proxy: 0.034661
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
