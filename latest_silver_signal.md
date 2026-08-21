# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-21**
- 실행시간(UTC): **2026-08-21 15:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.75
- IG OAS 4주 변화: 3.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -4.0 bp / latest 2.35
- VIX: 16.01
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 7.49% / slope_proxy: 0.020489
- GDXJ/GLD gap: 14.94% / slope_proxy: 0.001333

## VZLA (Vizsla Silver)
- close: 3.8906 | RSI14: 62.292462 | ATR14%: 4.79%
- MA20 gap: 8.96% | MA50 gap: 14.38% | MA200 gap: -4.49%
- vol_ratio(Volume/Vol20): 0.253995 | gap_open: 3.36%
- RS vs SILJ gap: -4.19% / slope_proxy: 0.004095
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 9.715 | RSI14: 71.253203 | ATR14%: 5.71%
- MA20 gap: 20.54% | MA50 gap: 34.93% | MA200 gap: 12.72%
- vol_ratio(Volume/Vol20): 0.467983 | gap_open: 5.12%
- SilverMarginGate: SI=69.330002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.95% / slope_proxy: 0.001683
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 26.4 | RSI14: 55.860531 | ATR14%: 7.36%
- MA20 gap: 9.10% | MA50 gap: 13.63% | MA200 gap: -9.30%
- vol_ratio(Volume/Vol20): 0.421003 | gap_open: 4.82%
- RS vs SILJ gap: -7.24% / slope_proxy: -0.117213
- RS vs GDXJ gap: -12.83% / slope_proxy: -0.03191
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
