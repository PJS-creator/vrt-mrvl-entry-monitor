# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-13**
- 실행시간(UTC): **2026-08-13 15:01:26**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.71
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.43
- VIX: 14.55
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 8.50% / slope_proxy: 0.014611
- GDXJ/GLD gap: 7.99% / slope_proxy: -0.004108

## VZLA (Vizsla Silver)
- close: 3.75 | RSI14: 62.044207 | ATR14%: 4.93%
- MA20 gap: 10.34% | MA50 gap: 10.23% | MA200 gap: -8.36%
- vol_ratio(Volume/Vol20): 0.278005 | gap_open: 1.32%
- RS vs SILJ gap: -0.26% / slope_proxy: 0.005816
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
- close: 8.9 | RSI14: 72.180539 | ATR14%: 5.71%
- MA20 gap: 24.25% | MA50 gap: 27.78% | MA200 gap: 4.63%
- vol_ratio(Volume/Vol20): 0.297415 | gap_open: 2.82%
- SilverMarginGate: SI=65.18 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.33% / slope_proxy: -0.00254
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
- close: 26.950001 | RSI14: 63.204662 | ATR14%: 6.81%
- MA20 gap: 20.51% | MA50 gap: 15.46% | MA200 gap: -5.61%
- vol_ratio(Volume/Vol20): 0.282397 | gap_open: 4.30%
- RS vs SILJ gap: -1.53% / slope_proxy: -0.133523
- RS vs GDXJ gap: -3.13% / slope_proxy: -0.034366
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
