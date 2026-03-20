# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-19**
- 실행시간(UTC): **2026-03-20 03:00:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 34.0 bp / latest 3.2
- IG OAS 4주 변화: 13.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.86
- VIX: 25.09
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -4.72% / slope_proxy: -0.006292
- GDXJ/GLD gap: -13.08% / slope_proxy: 0.006752

## VZLA (Vizsla Silver)
- close: 3.22 | RSI14: 29.615204 | ATR14%: 9.28%
- MA20 gap: -17.79% | MA50 gap: -32.00% | MA200 gap: -23.19%
- vol_ratio(Volume/Vol20): 1.425533 | gap_open: 8.63%
- RS vs SILJ gap: -20.87% / slope_proxy: -0.027522
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.57 | RSI14: 30.328072 | ATR14%: 12.37%
- MA20 gap: -27.67% | MA50 gap: -33.12% | MA200 gap: 6.76%
- vol_ratio(Volume/Vol20): 1.023969 | gap_open: 9.59%
- SilverMarginGate: SI=74.135002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.79% / slope_proxy: -0.006279
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
- close: 31.76 | RSI14: 38.724074 | ATR14%: 16.26%
- MA20 gap: -26.51% | MA50 gap: -21.30% | MA200 gap: 101.07%
- vol_ratio(Volume/Vol20): 1.617467 | gap_open: 8.47%
- RS vs SILJ gap: 3.25% / slope_proxy: 0.254046
- RS vs GDXJ gap: 2.45% / slope_proxy: 0.066679
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
