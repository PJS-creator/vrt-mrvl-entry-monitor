# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-22**
- 실행시간(UTC): **2026-05-22 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.78
- IG OAS 4주 변화: -5.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.13
- VIX: 16.76
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -5.34% / slope_proxy: -0.00829
- GDXJ/GLD gap: -5.43% / slope_proxy: -0.004847

## VZLA (Vizsla Silver)
- close: 3.33 | RSI14: 44.546069 | ATR14%: 6.17%
- MA20 gap: -4.43% | MA50 gap: -1.60% | MA200 gap: -21.32%
- vol_ratio(Volume/Vol20): 0.347515 | gap_open: 0.00%
- RS vs SILJ gap: 3.60% / slope_proxy: -0.003415
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
- close: 8.01 | RSI14: 42.394916 | ATR14%: 7.92%
- MA20 gap: -6.68% | MA50 gap: -4.70% | MA200 gap: -2.63%
- vol_ratio(Volume/Vol20): 0.180961 | gap_open: 0.24%
- SilverMarginGate: SI=75.639999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.26% / slope_proxy: -0.016165
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
- close: 32.450001 | RSI14: 39.956111 | ATR14%: 10.10%
- MA20 gap: -13.18% | MA50 gap: -12.59% | MA200 gap: 38.98%
- vol_ratio(Volume/Vol20): 0.163518 | gap_open: 1.47%
- RS vs SILJ gap: -7.63% / slope_proxy: 0.026926
- RS vs GDXJ gap: -5.39% / slope_proxy: 0.007893
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
