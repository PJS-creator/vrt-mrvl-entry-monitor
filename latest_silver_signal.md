# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-20**
- 실행시간(UTC): **2026-03-20 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 39.0 bp / latest 3.27
- IG OAS 4주 변화: 11.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.86
- VIX: 24.06
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -3.05% / slope_proxy: -0.00703
- GDXJ/GLD gap: -13.62% / slope_proxy: 0.005116

## VZLA (Vizsla Silver)
- close: 3.09 | RSI14: 27.82125 | ATR14%: 9.41%
- MA20 gap: -20.31% | MA50 gap: -33.99% | MA200 gap: -26.28%
- vol_ratio(Volume/Vol20): 0.190133 | gap_open: 0.31%
- RS vs SILJ gap: -21.45% / slope_proxy: -0.027537
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.27 | RSI14: 29.012132 | ATR14%: 12.76%
- MA20 gap: -29.17% | MA50 gap: -35.43% | MA200 gap: 2.19%
- vol_ratio(Volume/Vol20): 0.223989 | gap_open: 2.51%
- SilverMarginGate: SI=69.474998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.95% / slope_proxy: -0.008072
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
- close: 31.0375 | RSI14: 38.005574 | ATR14%: 15.80%
- MA20 gap: -27.34% | MA50 gap: -23.14% | MA200 gap: 94.81%
- vol_ratio(Volume/Vol20): 0.224142 | gap_open: 0.91%
- RS vs SILJ gap: 2.91% / slope_proxy: 0.247901
- RS vs GDXJ gap: 2.12% / slope_proxy: 0.065062
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
