# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-03**
- 실행시간(UTC): **2026-09-04 00:22:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -9.0 bp / latest 2.66
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.45
- VIX: 15.2
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 10.48% / slope_proxy: 0.026483
- GDXJ/GLD gap: 14.35% / slope_proxy: 0.008685

## VZLA (Vizsla Silver)
- close: 4.15 | RSI14: 62.079789 | ATR14%: 4.85%
- MA20 gap: 7.19% | MA50 gap: 19.29% | MA200 gap: 1.99%
- vol_ratio(Volume/Vol20): 1.109579 | gap_open: 2.85%
- RS vs SILJ gap: 3.07% / slope_proxy: 0.001559
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

## SCZM (Santacruz Silver)
- close: 10.18 | RSI14: 66.51211 | ATR14%: 5.85%
- MA20 gap: 10.54% | MA50 gap: 34.05% | MA200 gap: 15.77%
- vol_ratio(Volume/Vol20): 1.167472 | gap_open: 1.96%
- SilverMarginGate: SI=67.57 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 18.44% / slope_proxy: 0.008675
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
- close: 23.209999 | RSI14: 46.013439 | ATR14%: 8.34%
- MA20 gap: -9.55% | MA50 gap: 0.69% | MA200 gap: -22.03%
- vol_ratio(Volume/Vol20): 1.099976 | gap_open: 2.70%
- RS vs SILJ gap: -14.30% / slope_proxy: -0.099468
- RS vs GDXJ gap: -16.75% / slope_proxy: -0.0298
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
