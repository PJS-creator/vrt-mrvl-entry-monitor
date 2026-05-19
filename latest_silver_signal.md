# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-19**
- 실행시간(UTC): **2026-05-19 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -4.0 bp / latest 2.83
- IG OAS 4주 변화: -6.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 20.0 bp / latest 2.1
- VIX: 17.82
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -6.36% / slope_proxy: -0.002024
- GDXJ/GLD gap: -6.68% / slope_proxy: -0.003743

## VZLA (Vizsla Silver)
- close: 3.24 | RSI14: 41.138618 | ATR14%: 6.88%
- MA20 gap: -7.00% | MA50 gap: -5.37% | MA200 gap: -23.39%
- vol_ratio(Volume/Vol20): 0.69001 | gap_open: 0.00%
- RS vs SILJ gap: 3.32% / slope_proxy: -0.007215
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
- close: 8.205 | RSI14: 44.042041 | ATR14%: 8.36%
- MA20 gap: -5.25% | MA50 gap: -3.76% | MA200 gap: 0.50%
- vol_ratio(Volume/Vol20): 0.556564 | gap_open: 1.17%
- SilverMarginGate: SI=74.300003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.51% / slope_proxy: -0.020495
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
- close: 31.725 | RSI14: 38.755417 | ATR14%: 11.59%
- MA20 gap: -16.81% | MA50 gap: -15.74% | MA200 gap: 38.55%
- vol_ratio(Volume/Vol20): 0.532195 | gap_open: 3.62%
- RS vs SILJ gap: -8.29% / slope_proxy: 0.027326
- RS vs GDXJ gap: -7.24% / slope_proxy: 0.007084
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
