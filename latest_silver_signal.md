# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-10**
- 실행시간(UTC): **2026-07-11 03:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.31
- VIX: 15.84
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 4.95% / slope_proxy: 0.008584
- GDXJ/GLD gap: -4.97% / slope_proxy: -0.002745

## VZLA (Vizsla Silver)
- close: 3.13 | RSI14: 42.682803 | ATR14%: 6.54%
- MA20 gap: -6.15% | MA50 gap: -9.90% | MA200 gap: -25.66%
- vol_ratio(Volume/Vol20): 0.79289 | gap_open: 0.95%
- RS vs SILJ gap: 2.38% / slope_proxy: 0.005148
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
- close: 6.51 | RSI14: 43.669068 | ATR14%: 7.39%
- MA20 gap: -4.10% | MA50 gap: -14.26% | MA200 gap: -23.50%
- vol_ratio(Volume/Vol20): 0.496769 | gap_open: 1.20%
- SilverMarginGate: SI=60.299999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.38% / slope_proxy: -0.004908
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
- close: 21.379999 | RSI14: 35.552083 | ATR14%: 9.50%
- MA20 gap: -10.00% | MA50 gap: -29.20% | MA200 gap: -20.10%
- vol_ratio(Volume/Vol20): 0.469817 | gap_open: 0.00%
- RS vs SILJ gap: -22.67% / slope_proxy: -0.099827
- RS vs GDXJ gap: -22.64% / slope_proxy: -0.021744
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
