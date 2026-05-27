# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-27**
- 실행시간(UTC): **2026-05-27 15:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -13.0 bp / latest 2.72
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 27.0 bp / latest 2.16
- VIX: 17.01
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -1.23% / slope_proxy: -0.011757
- GDXJ/GLD gap: -1.46% / slope_proxy: -0.005987

## VZLA (Vizsla Silver)
- close: 3.6301 | RSI14: 54.270405 | ATR14%: 5.90%
- MA20 gap: 3.51% | MA50 gap: 7.16% | MA200 gap: -14.31%
- vol_ratio(Volume/Vol20): 0.361213 | gap_open: 2.15%
- RS vs SILJ gap: 9.72% / slope_proxy: -0.00153
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 7.85 | RSI14: 40.786619 | ATR14%: 7.60%
- MA20 gap: -8.34% | MA50 gap: -6.08% | MA200 gap: -5.02%
- vol_ratio(Volume/Vol20): 0.386276 | gap_open: 3.60%
- SilverMarginGate: SI=74.830002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.16% / slope_proxy: -0.014057
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
- close: 32.439999 | RSI14: 40.556076 | ATR14%: 9.45%
- MA20 gap: -12.24% | MA50 gap: -12.06% | MA200 gap: 37.21%
- vol_ratio(Volume/Vol20): 0.264613 | gap_open: 3.64%
- RS vs SILJ gap: -9.35% / slope_proxy: 0.018339
- RS vs GDXJ gap: -6.79% / slope_proxy: 0.005995
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
