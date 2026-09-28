# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-28**
- 실행시간(UTC): **2026-09-28 15:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 2.93
- IG OAS 4주 변화: 2.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 51.0 bp / latest 2.85
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 1.43% / slope_proxy: 0.018
- GDXJ/GLD gap: 4.75% / slope_proxy: 0.014587

## VZLA (Vizsla Silver)
- close: 3.81 | RSI14: 46.268941 | ATR14%: 5.55%
- MA20 gap: -4.52% | MA50 gap: 1.42% | MA200 gap: -4.93%
- vol_ratio(Volume/Vol20): 0.266543 | gap_open: 4.81%
- RS vs SILJ gap: 6.46% / slope_proxy: 0.001504
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.945 | RSI14: 48.373861 | ATR14%: 7.29%
- MA20 gap: -4.85% | MA50 gap: 4.11% | MA200 gap: -0.74%
- vol_ratio(Volume/Vol20): 0.713359 | gap_open: 7.17%
- SilverMarginGate: SI=61.345001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.83% / slope_proxy: 0.019194
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 20.129999 | RSI14: 41.429052 | ATR14%: 7.94%
- MA20 gap: -7.19% | MA50 gap: -12.28% | MA200 gap: -34.38%
- vol_ratio(Volume/Vol20): 0.360506 | gap_open: 6.10%
- RS vs SILJ gap: -9.46% / slope_proxy: -0.070012
- RS vs GDXJ gap: -12.09% / slope_proxy: -0.022232
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
