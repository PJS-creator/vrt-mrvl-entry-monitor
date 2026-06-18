# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-18**
- 실행시간(UTC): **2026-06-18 15:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -15.0 bp / latest 2.71
- IG OAS 4주 변화: -1.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: -4.0 bp / latest 2.14
- VIX: 18.44
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 6.22% / slope_proxy: -0.002787
- GDXJ/GLD gap: 0.02% / slope_proxy: -0.004795

## VZLA (Vizsla Silver)
- close: 3.525 | RSI14: 48.452658 | ATR14%: 6.74%
- MA20 gap: -2.71% | MA50 gap: 0.11% | MA200 gap: -17.08%
- vol_ratio(Volume/Vol20): 0.216644 | gap_open: 0.00%
- RS vs SILJ gap: 6.99% / slope_proxy: 0.004434
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
- close: 7.225 | RSI14: 45.639559 | ATR14%: 8.77%
- MA20 gap: -2.76% | MA50 gap: -11.59% | MA200 gap: -14.98%
- vol_ratio(Volume/Vol20): 0.413128 | gap_open: 0.80%
- SilverMarginGate: SI=66.165001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.86% / slope_proxy: -0.010766
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
- close: 25.620001 | RSI14: 37.510146 | ATR14%: 10.39%
- MA20 gap: -12.16% | MA50 gap: -26.71% | MA200 gap: 0.15%
- vol_ratio(Volume/Vol20): 0.277003 | gap_open: 0.51%
- RS vs SILJ gap: -21.99% / slope_proxy: -0.071958
- RS vs GDXJ gap: -20.63% / slope_proxy: -0.015729
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
