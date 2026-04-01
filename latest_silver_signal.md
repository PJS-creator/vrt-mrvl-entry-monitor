# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-31**
- 실행시간(UTC): **2026-04-01 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 43.0 bp / latest 3.46
- IG OAS 4주 변화: 8.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.04
- VIX: 30.61
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -0.60% / slope_proxy: -0.00441
- GDXJ/GLD gap: -4.23% / slope_proxy: -0.002244

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 40.337176 | ATR14%: 7.81%
- MA20 gap: -6.81% | MA50 gap: -23.27% | MA200 gap: -21.07%
- vol_ratio(Volume/Vol20): 1.21327 | gap_open: 2.24%
- RS vs SILJ gap: -18.96% / slope_proxy: -0.027268
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
- close: 8.57 | RSI14: 45.853456 | ATR14%: 10.07%
- MA20 gap: -2.20% | MA50 gap: -20.74% | MA200 gap: 17.65%
- vol_ratio(Volume/Vol20): 1.414339 | gap_open: 2.50%
- SilverMarginGate: SI=74.184998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.66% / slope_proxy: -0.019469
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
- close: 35.200001 | RSI14: 47.618437 | ATR14%: 12.81%
- MA20 gap: -4.99% | MA50 gap: -13.06% | MA200 gap: 107.88%
- vol_ratio(Volume/Vol20): 0.85693 | gap_open: 3.45%
- RS vs SILJ gap: 1.83% / slope_proxy: 0.186934
- RS vs GDXJ gap: -0.81% / slope_proxy: 0.04907
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
