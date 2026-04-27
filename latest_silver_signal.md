# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-27**
- 실행시간(UTC): **2026-04-27 15:01:36**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -56.0 bp / latest 2.86
- IG OAS 4주 변화: -11.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -16.0 bp / latest 1.92
- VIX: 18.71
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.86% / slope_proxy: 0.015183
- GDXJ/GLD gap: -1.63% / slope_proxy: -0.003779

## VZLA (Vizsla Silver)
- close: 3.345 | RSI14: 45.895014 | ATR14%: 5.65%
- MA20 gap: 0.14% | MA50 gap: -6.56% | MA200 gap: -20.44%
- vol_ratio(Volume/Vol20): 0.301664 | gap_open: 0.60%
- RS vs SILJ gap: -4.59% / slope_proxy: -0.02495
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.21 | RSI14: 44.640196 | ATR14%: 8.21%
- MA20 gap: -2.73% | MA50 gap: -11.24% | MA200 gap: 5.57%
- vol_ratio(Volume/Vol20): 0.412193 | gap_open: 0.12%
- SilverMarginGate: SI=75.154999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.77% / slope_proxy: -0.029788
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
- close: 37.275002 | RSI14: 47.07879 | ATR14%: 9.53%
- MA20 gap: -2.72% | MA50 gap: -5.72% | MA200 gap: 85.01%
- vol_ratio(Volume/Vol20): 0.163301 | gap_open: 1.41%
- RS vs SILJ gap: 1.80% / slope_proxy: 0.046673
- RS vs GDXJ gap: 1.54% / slope_proxy: 0.008578
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
