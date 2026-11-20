# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-20**
- 실행시간(UTC): **2026-11-20 22:35:38**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 12.0 bp / latest 3.52
- IG OAS 4주 변화: 5.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.88
- VIX: 28.44
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: -1.17% / slope_proxy: 0.0019
- GDXJ/GLD gap: -13.98% / slope_proxy: -0.006783

## VZLA (Vizsla Silver)
- close: 2.43 | RSI14: 27.470364 | ATR14%: 8.81%
- MA20 gap: -21.84% | MA50 gap: -28.86% | MA200 gap: -31.29%
- vol_ratio(Volume/Vol20): 3.57637 | gap_open: 5.67%
- RS vs SILJ gap: -1.07% / slope_proxy: 0.00287
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 6.16 | RSI14: 38.179556 | ATR14%: 9.26%
- MA20 gap: -13.61% | MA50 gap: -23.38% | MA200 gap: -26.21%
- vol_ratio(Volume/Vol20): 2.497297 | gap_open: 2.12%
- SilverMarginGate: SI=41.080002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.97% / slope_proxy: 0.005529
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

## HYMC (Hycroft Mining)
- close: 12.61 | RSI14: 32.567648 | ATR14%: 12.17%
- MA20 gap: -24.37% | MA50 gap: -30.13% | MA200 gap: -55.14%
- vol_ratio(Volume/Vol20): 2.653404 | gap_open: 2.25%
- RS vs SILJ gap: -3.73% / slope_proxy: -0.045421
- RS vs GDXJ gap: -7.85% / slope_proxy: -0.01532
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
