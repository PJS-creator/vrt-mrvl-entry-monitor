# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-04**
- 실행시간(UTC): **2026-09-05 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.65
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -1.0 bp / latest 2.42
- VIX: 14.32
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 8.47% / slope_proxy: 0.027707
- GDXJ/GLD gap: 13.20% / slope_proxy: 0.011263

## VZLA (Vizsla Silver)
- close: 4.0 | RSI14: 55.976941 | ATR14%: 5.07%
- MA20 gap: 2.13% | MA50 gap: 13.71% | MA200 gap: -1.58%
- vol_ratio(Volume/Vol20): 0.998983 | gap_open: 3.60%
- RS vs SILJ gap: -0.71% / slope_proxy: 0.000911
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 9.94 | RSI14: 61.243092 | ATR14%: 6.09%
- MA20 gap: 5.64% | MA50 gap: 28.33% | MA200 gap: 12.43%
- vol_ratio(Volume/Vol20): 0.897891 | gap_open: 3.74%
- SilverMarginGate: SI=66.82 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.44% / slope_proxy: 0.011172
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
- close: 22.690001 | RSI14: 44.447723 | ATR14%: 8.17%
- MA20 gap: -10.82% | MA50 gap: -1.77% | MA200 gap: -24.11%
- vol_ratio(Volume/Vol20): 0.883588 | gap_open: 3.86%
- RS vs SILJ gap: -15.56% / slope_proxy: -0.093317
- RS vs GDXJ gap: -18.36% / slope_proxy: -0.028112
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
