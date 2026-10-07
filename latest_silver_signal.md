# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-07**
- 실행시간(UTC): **2026-10-07 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 44.0 bp / latest 3.12
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 52.0 bp / latest 2.95
- VIX: 15.01
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.67% / slope_proxy: 0.00966
- GDXJ/GLD gap: -0.84% / slope_proxy: 0.01196

## VZLA (Vizsla Silver)
- close: 3.385 | RSI14: 34.127077 | ATR14%: 5.81%
- MA20 gap: -11.89% | MA50 gap: -11.09% | MA200 gap: -14.36%
- vol_ratio(Volume/Vol20): 0.25441 | gap_open: 3.40%
- RS vs SILJ gap: -1.04% / slope_proxy: 0.002949
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.46 | RSI14: 43.40232 | ATR14%: 6.86%
- MA20 gap: -6.13% | MA50 gap: -5.29% | MA200 gap: -5.92%
- vol_ratio(Volume/Vol20): 0.373711 | gap_open: 3.91%
- SilverMarginGate: SI=60.049999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.71% / slope_proxy: 0.019409
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 17.950001 | RSI14: 34.928309 | ATR14%: 7.60%
- MA20 gap: -11.39% | MA50 gap: -21.02% | MA200 gap: -41.85%
- vol_ratio(Volume/Vol20): 0.325744 | gap_open: 4.92%
- RS vs SILJ gap: -12.64% / slope_proxy: -0.059543
- RS vs GDXJ gap: -15.35% / slope_proxy: -0.01959
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
