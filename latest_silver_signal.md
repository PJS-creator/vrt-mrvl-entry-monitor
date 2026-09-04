# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-04**
- 실행시간(UTC): **2026-09-04 15:01:28**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.65
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.45
- VIX: 14.32
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 9.59% / slope_proxy: 0.0278
- GDXJ/GLD gap: 13.64% / slope_proxy: 0.011284

## VZLA (Vizsla Silver)
- close: 4.035 | RSI14: 57.217802 | ATR14%: 4.95%
- MA20 gap: 2.98% | MA50 gap: 14.69% | MA200 gap: -0.72%
- vol_ratio(Volume/Vol20): 0.245157 | gap_open: 3.60%
- RS vs SILJ gap: -0.35% / slope_proxy: 0.000919
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.13 | RSI14: 63.856347 | ATR14%: 5.97%
- MA20 gap: 7.55% | MA50 gap: 30.71% | MA200 gap: 14.57%
- vol_ratio(Volume/Vol20): 0.325437 | gap_open: 3.74%
- SilverMarginGate: SI=66.464996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 16.01% / slope_proxy: 0.011246
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 22.865 | RSI14: 44.970806 | ATR14%: 8.11%
- MA20 gap: -10.16% | MA50 gap: -1.02% | MA200 gap: -23.53%
- vol_ratio(Volume/Vol20): 0.183785 | gap_open: 3.86%
- RS vs SILJ gap: -15.34% / slope_proxy: -0.093286
- RS vs GDXJ gap: -17.86% / slope_proxy: -0.028094
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
