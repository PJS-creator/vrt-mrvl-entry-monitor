# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-06**
- 실행시간(UTC): **2026-04-07 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 3.13
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 19.0 bp / latest 1.99
- VIX: 23.87
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 4.41% / slope_proxy: -0.001671
- GDXJ/GLD gap: -2.57% / slope_proxy: -0.003903

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 41.125801 | ATR14%: 7.24%
- MA20 gap: -3.62% | MA50 gap: -19.88% | MA200 gap: -21.01%
- vol_ratio(Volume/Vol20): 0.893422 | gap_open: 0.00%
- RS vs SILJ gap: -18.24% / slope_proxy: -0.0275
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
- close: 8.15 | RSI14: 43.875411 | ATR14%: 10.24%
- MA20 gap: -3.56% | MA50 gap: -22.44% | MA200 gap: 10.71%
- vol_ratio(Volume/Vol20): 0.625872 | gap_open: 0.89%
- SilverMarginGate: SI=72.699997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.96% / slope_proxy: -0.021624
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
- close: 35.990002 | RSI14: 48.869594 | ATR14%: 11.78%
- MA20 gap: -0.09% | MA50 gap: -10.13% | MA200 gap: 106.58%
- vol_ratio(Volume/Vol20): 0.537736 | gap_open: 0.58%
- RS vs SILJ gap: 0.86% / slope_proxy: 0.159002
- RS vs GDXJ gap: -0.41% / slope_proxy: 0.041814
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
