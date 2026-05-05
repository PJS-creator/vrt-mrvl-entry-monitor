# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-04**
- 실행시간(UTC): **2026-05-05 03:00:51**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -36.0 bp / latest 2.77
- IG OAS 4주 변화: -5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.91
- VIX: 16.99
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.89% / slope_proxy: 0.012799
- GDXJ/GLD gap: -5.03% / slope_proxy: -0.003803

## VZLA (Vizsla Silver)
- close: 3.36 | RSI14: 46.691234 | ATR14%: 5.91%
- MA20 gap: -0.71% | MA50 gap: -5.16% | MA200 gap: -20.17%
- vol_ratio(Volume/Vol20): 0.725238 | gap_open: 1.73%
- RS vs SILJ gap: 4.21% / slope_proxy: -0.020532
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
- close: 7.88 | RSI14: 42.927633 | ATR14%: 7.94%
- MA20 gap: -6.32% | MA50 gap: -12.88% | MA200 gap: 0.04%
- vol_ratio(Volume/Vol20): 0.952685 | gap_open: 1.59%
- SilverMarginGate: SI=73.480003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.64% / slope_proxy: -0.031358
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
- close: 36.09 | RSI14: 46.212744 | ATR14%: 9.16%
- MA20 gap: -6.94% | MA50 gap: -8.20% | MA200 gap: 72.18%
- vol_ratio(Volume/Vol20): 0.702971 | gap_open: 4.47%
- RS vs SILJ gap: 3.88% / slope_proxy: 0.035372
- RS vs GDXJ gap: 5.20% / slope_proxy: 0.005243
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
