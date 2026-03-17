# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-16**
- 실행시간(UTC): **2026-03-17 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.28
- IG OAS 4주 변화: 14.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 15.0 bp / latest 1.92
- VIX: 27.19
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -1.27% / slope_proxy: -0.004418
- GDXJ/GLD gap: -7.36% / slope_proxy: 0.009953

## VZLA (Vizsla Silver)
- close: 3.63 | RSI14: 36.047009 | ATR14%: 8.31%
- MA20 gap: -8.68% | MA50 gap: -25.50% | MA200 gap: -13.27%
- vol_ratio(Volume/Vol20): 0.670841 | gap_open: 0.00%
- RS vs SILJ gap: -24.92% / slope_proxy: -0.028184
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
- close: 8.9 | RSI14: 36.697527 | ATR14%: 10.91%
- MA20 gap: -16.81% | MA50 gap: -22.15% | MA200 gap: 27.11%
- vol_ratio(Volume/Vol20): 2.909234 | gap_open: 3.54%
- SilverMarginGate: SI=81.455002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.10% / slope_proxy: -0.002139
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
- close: 39.32 | RSI14: 47.074599 | ATR14%: 13.39%
- MA20 gap: -9.87% | MA50 gap: -1.24% | MA200 gap: 156.96%
- vol_ratio(Volume/Vol20): 0.781548 | gap_open: 2.87%
- RS vs SILJ gap: 13.70% / slope_proxy: 0.254893
- RS vs GDXJ gap: 13.28% / slope_proxy: 0.066938
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
