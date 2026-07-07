# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-07**
- 실행시간(UTC): **2026-07-07 15:01:15**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.72
- IG OAS 4주 변화: 0.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.26
- VIX: 15.57
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 2.42% / slope_proxy: 0.007653
- GDXJ/GLD gap: -5.77% / slope_proxy: -0.001935

## VZLA (Vizsla Silver)
- close: 3.18 | RSI14: 41.337046 | ATR14%: 6.49%
- MA20 gap: -5.79% | MA50 gap: -9.05% | MA200 gap: -24.71%
- vol_ratio(Volume/Vol20): 0.253336 | gap_open: 0.61%
- RS vs SILJ gap: 5.26% / slope_proxy: 0.005084
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
- close: 6.36 | RSI14: 39.919434 | ATR14%: 7.95%
- MA20 gap: -5.64% | MA50 gap: -17.40% | MA200 gap: -25.31%
- vol_ratio(Volume/Vol20): 0.265 | gap_open: 2.35%
- SilverMarginGate: SI=61.465 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.31% / slope_proxy: -0.006861
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
- close: 21.810101 | RSI14: 34.372543 | ATR14%: 9.92%
- MA20 gap: -10.13% | MA50 gap: -30.00% | MA200 gap: -17.80%
- vol_ratio(Volume/Vol20): 0.198366 | gap_open: 2.08%
- RS vs SILJ gap: -22.14% / slope_proxy: -0.092478
- RS vs GDXJ gap: -22.97% / slope_proxy: -0.020321
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
