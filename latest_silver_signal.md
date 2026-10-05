# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-05**
- 실행시간(UTC): **2026-10-05 15:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 42.0 bp / latest 3.1
- IG OAS 4주 변화: 4.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: 46.0 bp / latest 2.88
- VIX: 15.31
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: -1.97% / slope_proxy: 0.012152
- GDXJ/GLD gap: 1.40% / slope_proxy: 0.012686

## VZLA (Vizsla Silver)
- close: 3.525 | RSI14: 37.556187 | ATR14%: 5.61%
- MA20 gap: -9.74% | MA50 gap: -7.22% | MA200 gap: -11.20%
- vol_ratio(Volume/Vol20): 0.371818 | gap_open: 1.11%
- RS vs SILJ gap: 0.05% / slope_proxy: 0.002694
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

## SCZM (Santacruz Silver)
- close: 8.86 | RSI14: 47.841696 | ATR14%: 6.53%
- MA20 gap: -3.26% | MA50 gap: 0.24% | MA200 gap: -1.46%
- vol_ratio(Volume/Vol20): 0.196704 | gap_open: 0.80%
- SilverMarginGate: SI=61.52 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.28% / slope_proxy: 0.019293
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
- close: 18.645 | RSI14: 36.673934 | ATR14%: 7.59%
- MA20 gap: -9.86% | MA50 gap: -18.20% | MA200 gap: -39.52%
- vol_ratio(Volume/Vol20): 0.251695 | gap_open: 0.69%
- RS vs SILJ gap: -12.56% / slope_proxy: -0.062207
- RS vs GDXJ gap: -15.41% / slope_proxy: -0.020205
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
