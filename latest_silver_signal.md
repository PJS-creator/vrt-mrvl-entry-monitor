# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-03**
- 실행시간(UTC): **2026-03-03 23:01:28**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 22.0 bp / latest 3.03
- IG OAS 4주 변화: 11.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: -18.0 bp / latest 1.76
- VIX: 21.44
- NFCI: -0.56294

### Leadership ratios
- SILJ/SLV gap: 8.98% / slope_proxy: -0.0041
- GDXJ/GLD gap: 2.77% / slope_proxy: 0.01435

## VZLA (Vizsla Silver)
- close: 4.04 | RSI14: 41.380088 | ATR14%: 8.91%
- MA20 gap: -2.11% | MA50 gap: -21.80% | MA200 gap: -2.09%
- vol_ratio(Volume/Vol20): 0.535912 | gap_open: 7.73%
- RS vs SILJ gap: -31.82% / slope_proxy: -0.025996
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
- close: 11.08 | RSI14: 47.344522 | ATR14%: 10.32%
- MA20 gap: -1.97% | MA50 gap: -2.61% | MA200 gap: 67.10%
- vol_ratio(Volume/Vol20): 0.838259 | gap_open: 9.46%
- SilverMarginGate: SI=82.300003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.24% / slope_proxy: 0.020175
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 48.509998 | RSI14: 58.192213 | ATR14%: 12.35%
- MA20 gap: 16.99% | MA50 gap: 33.14% | MA200 gap: 257.50%
- vol_ratio(Volume/Vol20): 1.252609 | gap_open: 10.66%
- RS vs SILJ gap: 37.77% / slope_proxy: 0.249145
- RS vs GDXJ gap: 39.32% / slope_proxy: 0.065778
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
