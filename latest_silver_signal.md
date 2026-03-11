# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-10**
- 실행시간(UTC): **2026-03-11 03:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 35.0 bp / latest 3.19
- IG OAS 4주 변화: 9.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: -9.0 bp / latest 1.78
- VIX: 25.5
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 0.07% / slope_proxy: -0.002749
- GDXJ/GLD gap: -1.54% / slope_proxy: 0.012948

## VZLA (Vizsla Silver)
- close: 4.14 | RSI14: 44.953624 | ATR14%: 7.91%
- MA20 gap: 3.81% | MA50 gap: -17.52% | MA200 gap: -0.62%
- vol_ratio(Volume/Vol20): 0.474055 | gap_open: 2.26%
- RS vs SILJ gap: -25.67% / slope_proxy: -0.029171
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.62 | RSI14: 46.498937 | ATR14%: 10.00%
- MA20 gap: -2.83% | MA50 gap: -7.58% | MA200 gap: 55.09%
- vol_ratio(Volume/Vol20): 0.675004 | gap_open: 4.75%
- SilverMarginGate: SI=89.144997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.32% / slope_proxy: 0.006867
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 44.849998 | RSI14: 53.416092 | ATR14%: 13.16%
- MA20 gap: 5.06% | MA50 gap: 16.41% | MA200 gap: 207.98%
- vol_ratio(Volume/Vol20): 1.075242 | gap_open: 3.10%
- RS vs SILJ gap: 21.86% / slope_proxy: 0.247085
- RS vs GDXJ gap: 22.74% / slope_proxy: 0.064901
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
