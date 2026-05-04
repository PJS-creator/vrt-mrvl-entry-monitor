# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-03**
- 실행시간(UTC): **2026-05-04 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.83
- IG OAS 4주 변화: -5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -3.0 bp / latest 1.94
- VIX: 16.89
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -5.08% / slope_proxy: 0.013854
- GDXJ/GLD gap: -5.05% / slope_proxy: -0.003949

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 50.732864 | ATR14%: 5.71%
- MA20 gap: 2.34% | MA50 gap: -2.62% | MA200 gap: -17.79%
- vol_ratio(Volume/Vol20): 0.766698 | gap_open: 0.59%
- RS vs SILJ gap: 4.47% / slope_proxy: -0.021592
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
- close: 8.16 | RSI14: 45.794469 | ATR14%: 7.65%
- MA20 gap: -3.15% | MA50 gap: -10.46% | MA200 gap: 3.85%
- vol_ratio(Volume/Vol20): 1.030662 | gap_open: 0.64%
- SilverMarginGate: SI=75.989998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.90% / slope_proxy: -0.031519
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
- close: 38.73 | RSI14: 51.303517 | ATR14%: 8.62%
- MA20 gap: -0.12% | MA50 gap: -1.73% | MA200 gap: 86.20%
- vol_ratio(Volume/Vol20): 0.991 | gap_open: 0.00%
- RS vs SILJ gap: 9.13% / slope_proxy: 0.035898
- RS vs GDXJ gap: 10.90% / slope_proxy: 0.005386
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
