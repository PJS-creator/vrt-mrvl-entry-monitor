# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-23**
- 실행시간(UTC): **2026-11-23 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 12.0 bp / latest 3.52
- IG OAS 4주 변화: 7.0 bp / latest 0.98
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.88
- VIX: 35.89
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: -1.26% / slope_proxy: 0.001109
- GDXJ/GLD gap: -11.47% / slope_proxy: -0.007979

## VZLA (Vizsla Silver)
- close: 2.695 | RSI14: 37.798452 | ATR14%: 8.28%
- MA20 gap: -12.79% | MA50 gap: -20.60% | MA200 gap: -23.59%
- vol_ratio(Volume/Vol20): 0.184397 | gap_open: 11.93%
- RS vs SILJ gap: 2.95% / slope_proxy: 0.003025
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.01 | RSI14: 47.064864 | ATR14%: 8.72%
- MA20 gap: -1.67% | MA50 gap: -12.38% | MA200 gap: -15.82%
- vol_ratio(Volume/Vol20): 0.438727 | gap_open: 13.72%
- SilverMarginGate: SI=43.605 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.97% / slope_proxy: 0.00589
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 13.905 | RSI14: 39.121317 | ATR14%: 11.34%
- MA20 gap: -16.23% | MA50 gap: -22.38% | MA200 gap: -50.35%
- vol_ratio(Volume/Vol20): 0.268283 | gap_open: 16.93%
- RS vs SILJ gap: -0.14% / slope_proxy: -0.043673
- RS vs GDXJ gap: -4.60% / slope_proxy: -0.014886
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **False**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Breakout/Retest)=FALSE
