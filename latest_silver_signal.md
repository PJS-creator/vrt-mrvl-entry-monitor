# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-27**
- 실행시간(UTC): **2026-04-28 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -56.0 bp / latest 2.86
- IG OAS 4주 변화: -11.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -24.0 bp / latest 1.89
- VIX: 18.71
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -1.18% / slope_proxy: 0.015158
- GDXJ/GLD gap: -1.86% / slope_proxy: -0.00379

## VZLA (Vizsla Silver)
- close: 3.52 | RSI14: 52.581336 | ATR14%: 5.70%
- MA20 gap: 5.11% | MA50 gap: -1.76% | MA200 gap: -16.30%
- vol_ratio(Volume/Vol20): 1.393612 | gap_open: 0.60%
- RS vs SILJ gap: -0.10% / slope_proxy: -0.024863
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
- close: 8.41 | RSI14: 46.514829 | ATR14%: 8.02%
- MA20 gap: -0.47% | MA50 gap: -9.11% | MA200 gap: 8.13%
- vol_ratio(Volume/Vol20): 0.697133 | gap_open: 0.12%
- SilverMarginGate: SI=74.345001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.97% / slope_proxy: -0.029698
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
- close: 38.119999 | RSI14: 48.720279 | ATR14%: 9.36%
- MA20 gap: -0.62% | MA50 gap: -3.62% | MA200 gap: 89.17%
- vol_ratio(Volume/Vol20): 0.478353 | gap_open: 1.41%
- RS vs SILJ gap: 3.63% / slope_proxy: 0.047047
- RS vs GDXJ gap: 3.93% / slope_proxy: 0.008701
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
