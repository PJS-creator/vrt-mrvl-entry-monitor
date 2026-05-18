# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-18**
- 실행시간(UTC): **2026-05-18 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.8
- IG OAS 4주 변화: -5.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 7.0 bp / latest 2.0
- VIX: 18.43
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -3.86% / slope_proxy: -0.000787
- GDXJ/GLD gap: -2.87% / slope_proxy: -0.003597

## VZLA (Vizsla Silver)
- close: 3.395 | RSI14: 45.696687 | ATR14%: 6.56%
- MA20 gap: -2.65% | MA50 gap: -1.27% | MA200 gap: -19.69%
- vol_ratio(Volume/Vol20): 0.245945 | gap_open: 1.14%
- RS vs SILJ gap: 2.02% / slope_proxy: -0.008445
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
- close: 8.6 | RSI14: 47.677964 | ATR14%: 8.06%
- MA20 gap: -0.87% | MA50 gap: 0.41% | MA200 gap: 5.65%
- vol_ratio(Volume/Vol20): 0.310428 | gap_open: 1.21%
- SilverMarginGate: SI=76.910004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.84% / slope_proxy: -0.021962
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
- close: 34.82 | RSI14: 43.031383 | ATR14%: 10.53%
- MA20 gap: -9.61% | MA50 gap: -7.95% | MA200 gap: 53.02%
- vol_ratio(Volume/Vol20): 0.389088 | gap_open: 0.95%
- RS vs SILJ gap: -5.31% / slope_proxy: 0.027095
- RS vs GDXJ gap: -3.45% / slope_proxy: 0.006574
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
