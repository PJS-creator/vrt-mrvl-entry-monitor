# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-15**
- 실행시간(UTC): **2026-10-15 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 55.0 bp / latest 3.25
- IG OAS 4주 변화: 6.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.88
- VIX: 16.87
- NFCI: -0.499

### Leadership ratios
- SILJ/SLV gap: -2.79% / slope_proxy: 0.007042
- GDXJ/GLD gap: -5.00% / slope_proxy: 0.012265

## VZLA (Vizsla Silver)
- close: 3.25 | RSI14: 34.648856 | ATR14%: 5.56%
- MA20 gap: -12.10% | MA50 gap: -14.89% | MA200 gap: -16.33%
- vol_ratio(Volume/Vol20): 0.27388 | gap_open: 1.89%
- RS vs SILJ gap: -0.80% / slope_proxy: 0.002462
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
- close: 8.12 | RSI14: 41.729053 | ATR14%: 6.63%
- MA20 gap: -8.30% | MA50 gap: -11.01% | MA200 gap: -9.34%
- vol_ratio(Volume/Vol20): 0.27186 | gap_open: 0.63%
- SilverMarginGate: SI=57.244999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.37% / slope_proxy: 0.021895
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
- close: 16.67 | RSI14: 34.290223 | ATR14%: 7.49%
- MA20 gap: -13.63% | MA50 gap: -25.34% | MA200 gap: -45.69%
- vol_ratio(Volume/Vol20): 0.389167 | gap_open: 1.56%
- RS vs SILJ gap: -13.86% / slope_proxy: -0.052199
- RS vs GDXJ gap: -17.89% / slope_proxy: -0.017859
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
