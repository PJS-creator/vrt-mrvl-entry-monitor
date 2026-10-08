# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-08**
- 실행시간(UTC): **2026-10-08 15:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 38.0 bp / latest 3.09
- IG OAS 4주 변화: 1.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 48.0 bp / latest 2.91
- VIX: 15.08
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -0.72% / slope_proxy: 0.00871
- GDXJ/GLD gap: -0.85% / slope_proxy: 0.011969

## VZLA (Vizsla Silver)
- close: 3.455 | RSI14: 36.76463 | ATR14%: 5.44%
- MA20 gap: -9.47% | MA50 gap: -9.42% | MA200 gap: -12.38%
- vol_ratio(Volume/Vol20): 0.14872 | gap_open: 0.29%
- RS vs SILJ gap: 0.34% / slope_proxy: 0.00294
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
- close: 8.555 | RSI14: 44.735486 | ATR14%: 6.56%
- MA20 gap: -4.47% | MA50 gap: -4.71% | MA200 gap: -4.86%
- vol_ratio(Volume/Vol20): 0.319332 | gap_open: 1.07%
- SilverMarginGate: SI=59.285 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.84% / slope_proxy: 0.019634
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
- close: 17.969999 | RSI14: 35.031357 | ATR14%: 7.26%
- MA20 gap: -10.53% | MA50 gap: -20.85% | MA200 gap: -41.80%
- vol_ratio(Volume/Vol20): 0.199687 | gap_open: 1.11%
- RS vs SILJ gap: -12.78% / slope_proxy: -0.057768
- RS vs GDXJ gap: -15.39% / slope_proxy: -0.019193
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
