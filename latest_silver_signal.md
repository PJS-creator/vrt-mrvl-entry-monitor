# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-16**
- 실행시간(UTC): **2026-08-16 22:54:16**

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
- IG OAS 4주 변화: 1.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.39
- VIX: 14.63
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 9.32% / slope_proxy: 0.015747
- GDXJ/GLD gap: 8.99% / slope_proxy: -0.003101

## VZLA (Vizsla Silver)
- close: 3.76 | RSI14: 61.28576 | ATR14%: 4.91%
- MA20 gap: 9.08% | MA50 gap: 11.66% | MA200 gap: -7.90%
- vol_ratio(Volume/Vol20): 0.90165 | gap_open: 0.80%
- RS vs SILJ gap: -1.08% / slope_proxy: 0.005482
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
- close: 8.85 | RSI14: 70.455669 | ATR14%: 5.74%
- MA20 gap: 23.04% | MA50 gap: 28.37% | MA200 gap: 3.98%
- vol_ratio(Volume/Vol20): 0.66613 | gap_open: 1.49%
- SilverMarginGate: SI=65.089996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.53% / slope_proxy: -0.002692
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
- close: 27.07 | RSI14: 62.912349 | ATR14%: 6.73%
- MA20 gap: 19.02% | MA50 gap: 16.52% | MA200 gap: -5.52%
- vol_ratio(Volume/Vol20): 0.701832 | gap_open: 3.20%
- RS vs SILJ gap: -1.13% / slope_proxy: -0.129974
- RS vs GDXJ gap: -3.11% / slope_proxy: -0.033659
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
