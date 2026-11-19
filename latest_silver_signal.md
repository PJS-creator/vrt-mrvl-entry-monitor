# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-19**
- 실행시간(UTC): **2026-11-19 22:35:43**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.47
- IG OAS 4주 변화: 5.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.88
- VIX: 24.56
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: -2.14% / slope_proxy: 0.002502
- GDXJ/GLD gap: -12.81% / slope_proxy: -0.005522

## VZLA (Vizsla Silver)
- close: 2.82 | RSI14: 35.533184 | ATR14%: 7.09%
- MA20 gap: -10.25% | MA50 gap: -18.19% | MA200 gap: -20.47%
- vol_ratio(Volume/Vol20): 2.974265 | gap_open: 6.71%
- RS vs SILJ gap: 8.11% / slope_proxy: 0.002835
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
- close: 6.61 | RSI14: 41.613314 | ATR14%: 8.58%
- MA20 gap: -7.81% | MA50 gap: -18.49% | MA200 gap: -21.02%
- vol_ratio(Volume/Vol20): 1.683407 | gap_open: 0.00%
- SilverMarginGate: SI=42.834999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.18% / slope_proxy: 0.005496
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
- close: 13.78 | RSI14: 35.800941 | ATR14%: 10.93%
- MA20 gap: -18.05% | MA50 gap: -24.36% | MA200 gap: -51.16%
- vol_ratio(Volume/Vol20): 1.420919 | gap_open: 0.33%
- RS vs SILJ gap: -1.24% / slope_proxy: -0.046013
- RS vs GDXJ gap: -5.02% / slope_proxy: -0.015483
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
