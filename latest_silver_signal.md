# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-30**
- 실행시간(UTC): **2026-03-31 03:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 32.0 bp / latest 3.42
- IG OAS 4주 변화: 6.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 41.0 bp / latest 2.13
- VIX: 31.05
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -1.95% / slope_proxy: -0.004631
- GDXJ/GLD gap: -8.44% / slope_proxy: -0.001624

## VZLA (Vizsla Silver)
- close: 3.13 | RSI14: 34.501156 | ATR14%: 8.33%
- MA20 gap: -12.52% | MA50 gap: -28.17% | MA200 gap: -25.16%
- vol_ratio(Volume/Vol20): 0.828038 | gap_open: 1.90%
- RS vs SILJ gap: -17.26% / slope_proxy: -0.027162
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.59 | RSI14: 36.871433 | ATR14%: 11.23%
- MA20 gap: -14.61% | MA50 gap: -30.19% | MA200 gap: 4.60%
- vol_ratio(Volume/Vol20): 0.675197 | gap_open: 3.75%
- SilverMarginGate: SI=72.364998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.13% / slope_proxy: -0.019182
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 30.469999 | RSI14: 40.219022 | ATR14%: 14.72%
- MA20 gap: -19.20% | MA50 gap: -24.72% | MA200 gap: 81.65%
- vol_ratio(Volume/Vol20): 0.681857 | gap_open: 1.19%
- RS vs SILJ gap: -3.67% / slope_proxy: 0.196901
- RS vs GDXJ gap: -6.41% / slope_proxy: 0.051673
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
