# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-10**
- 실행시간(UTC): **2026-11-11 02:13:51**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.34
- IG OAS 4주 변화: 8.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -25.0 bp / latest 2.66
- VIX: 19.92
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 7.32% / slope_proxy: 0.004978
- GDXJ/GLD gap: -3.42% / slope_proxy: 0.00131

## VZLA (Vizsla Silver)
- close: 3.5 | RSI14: 55.542165 | ATR14%: 5.85%
- MA20 gap: 8.53% | MA50 gap: -2.93% | MA200 gap: -4.24%
- vol_ratio(Volume/Vol20): 1.022931 | gap_open: 4.24%
- RS vs SILJ gap: 2.14% / slope_proxy: 0.000699
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

## SCZM (Santacruz Silver)
- close: 8.09 | RSI14: 52.834343 | ATR14%: 6.68%
- MA20 gap: 6.19% | MA50 gap: -5.62% | MA200 gap: -6.33%
- vol_ratio(Volume/Vol20): 0.8737 | gap_open: 4.39%
- SilverMarginGate: SI=52.264999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.89% / slope_proxy: 0.012006
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

## HYMC (Hycroft Mining)
- close: 21.27 | RSI14: 65.057399 | ATR14%: 7.10%
- MA20 gap: 24.75% | MA50 gap: 10.57% | MA200 gap: -27.50%
- vol_ratio(Volume/Vol20): 1.294527 | gap_open: 5.11%
- RS vs SILJ gap: 12.22% / slope_proxy: -0.051739
- RS vs GDXJ gap: 8.21% / slope_proxy: -0.017488
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
