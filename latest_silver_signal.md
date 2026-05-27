# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-26**
- 실행시간(UTC): **2026-05-27 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.74
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 27.0 bp / latest 2.16
- VIX: 16.59
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -2.79% / slope_proxy: -0.01055
- GDXJ/GLD gap: -0.27% / slope_proxy: -0.005381

## VZLA (Vizsla Silver)
- close: 3.72 | RSI14: 57.502294 | ATR14%: 5.91%
- MA20 gap: 6.39% | MA50 gap: 9.81% | MA200 gap: -12.15%
- vol_ratio(Volume/Vol20): 1.116972 | gap_open: 2.67%
- RS vs SILJ gap: 10.04% / slope_proxy: -0.002467
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
- close: 8.05 | RSI14: 42.850582 | ATR14%: 7.65%
- MA20 gap: -6.02% | MA50 gap: -3.93% | MA200 gap: -2.37%
- vol_ratio(Volume/Vol20): 1.439344 | gap_open: 0.50%
- SilverMarginGate: SI=77.105003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.21% / slope_proxy: -0.015281
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
- close: 33.220001 | RSI14: 41.905278 | ATR14%: 9.59%
- MA20 gap: -10.52% | MA50 gap: -10.28% | MA200 gap: 41.38%
- vol_ratio(Volume/Vol20): 0.708733 | gap_open: 3.65%
- RS vs SILJ gap: -9.69% / slope_proxy: 0.023945
- RS vs GDXJ gap: -7.90% / slope_proxy: 0.007278
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
