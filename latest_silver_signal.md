# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-29**
- 실행시간(UTC): **2026-03-30 03:00:49**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.21
- IG OAS 4주 변화: 6.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 34.0 bp / latest 2.08
- VIX: 27.44
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.12% / slope_proxy: -0.004493
- GDXJ/GLD gap: -8.59% / slope_proxy: -0.000526

## VZLA (Vizsla Silver)
- close: 3.15 | RSI14: 34.873812 | ATR14%: 8.49%
- MA20 gap: -13.50% | MA50 gap: -28.65% | MA200 gap: -24.70%
- vol_ratio(Volume/Vol20): 0.802854 | gap_open: 0.00%
- RS vs SILJ gap: -19.15% / slope_proxy: -0.027254
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.73 | RSI14: 37.701043 | ATR14%: 11.29%
- MA20 gap: -15.21% | MA50 gap: -29.39% | MA200 gap: 6.88%
- vol_ratio(Volume/Vol20): 0.60972 | gap_open: 0.14%
- SilverMarginGate: SI=69.290001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.56% / slope_proxy: -0.018248
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 33.049999 | RSI14: 43.318327 | ATR14%: 13.58%
- MA20 gap: -15.20% | MA50 gap: -18.51% | MA200 gap: 98.58%
- vol_ratio(Volume/Vol20): 0.522497 | gap_open: 1.51%
- RS vs SILJ gap: 2.84% / slope_proxy: 0.208319
- RS vs GDXJ gap: 1.93% / slope_proxy: 0.054714
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
