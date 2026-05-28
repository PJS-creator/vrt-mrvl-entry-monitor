# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-28**
- 실행시간(UTC): **2026-05-28 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.71
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 18.0 bp / latest 2.1
- VIX: 16.29
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -0.30% / slope_proxy: -0.012559
- GDXJ/GLD gap: -1.55% / slope_proxy: -0.006125

## VZLA (Vizsla Silver)
- close: 3.7 | RSI14: 56.27047 | ATR14%: 5.75%
- MA20 gap: 5.07% | MA50 gap: 9.15% | MA200 gap: -12.70%
- vol_ratio(Volume/Vol20): 0.383895 | gap_open: 1.38%
- RS vs SILJ gap: 10.06% / slope_proxy: -0.000659
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
- close: 7.9 | RSI14: 41.84125 | ATR14%: 7.35%
- MA20 gap: -7.82% | MA50 gap: -5.30% | MA200 gap: -4.63%
- vol_ratio(Volume/Vol20): 0.358114 | gap_open: 0.26%
- SilverMarginGate: SI=74.93 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.66% / slope_proxy: -0.013277
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
- close: 32.119999 | RSI14: 40.165794 | ATR14%: 9.18%
- MA20 gap: -12.81% | MA50 gap: -12.52% | MA200 gap: 35.05%
- vol_ratio(Volume/Vol20): 0.241303 | gap_open: 1.81%
- RS vs SILJ gap: -11.17% / slope_proxy: 0.012201
- RS vs GDXJ gap: -7.99% / slope_proxy: 0.004634
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
