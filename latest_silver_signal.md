# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-23**
- 실행시간(UTC): **2026-04-24 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -33.0 bp / latest 2.84
- IG OAS 4주 변화: -8.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -10.0 bp / latest 1.92
- VIX: 18.92
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.52% / slope_proxy: 0.01307
- GDXJ/GLD gap: -1.85% / slope_proxy: -0.004082

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 43.982553 | ATR14%: 6.14%
- MA20 gap: -0.48% | MA50 gap: -8.23% | MA200 gap: -21.44%
- vol_ratio(Volume/Vol20): 1.262239 | gap_open: 2.31%
- RS vs SILJ gap: -7.89% / slope_proxy: -0.025889
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
- close: 8.61 | RSI14: 48.462767 | ATR14%: 8.30%
- MA20 gap: 3.03% | MA50 gap: -7.87% | MA200 gap: 11.44%
- vol_ratio(Volume/Vol20): 0.778508 | gap_open: 2.11%
- SilverMarginGate: SI=74.949997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.97% / slope_proxy: -0.02919
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
- close: 37.860001 | RSI14: 48.198153 | ATR14%: 10.03%
- MA20 gap: 0.26% | MA50 gap: -3.93% | MA200 gap: 91.15%
- vol_ratio(Volume/Vol20): 0.971299 | gap_open: 2.71%
- RS vs SILJ gap: 2.72% / slope_proxy: 0.059661
- RS vs GDXJ gap: 2.55% / slope_proxy: 0.012462
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
