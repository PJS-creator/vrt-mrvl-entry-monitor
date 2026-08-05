# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-05**
- 실행시간(UTC): **2026-08-05 23:34:47**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.73
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.4
- VIX: 16.5
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 7.98% / slope_proxy: 0.00967
- GDXJ/GLD gap: 4.32% / slope_proxy: -0.007837

## VZLA (Vizsla Silver)
- close: 3.59 | RSI14: 60.629215 | ATR14%: 5.42%
- MA20 gap: 11.30% | MA50 gap: 6.13% | MA200 gap: -12.42%
- vol_ratio(Volume/Vol20): 1.545125 | gap_open: 5.00%
- RS vs SILJ gap: 2.92% / slope_proxy: 0.006081
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
- close: 7.96 | RSI14: 66.366754 | ATR14%: 6.09%
- MA20 gap: 22.06% | MA50 gap: 16.54% | MA200 gap: -5.61%
- vol_ratio(Volume/Vol20): 1.327783 | gap_open: 7.29%
- SilverMarginGate: SI=62.355 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.08% / slope_proxy: -0.005294
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
- close: 24.48 | RSI14: 59.164672 | ATR14%: 7.38%
- MA20 gap: 18.69% | MA50 gap: 1.53% | MA200 gap: -12.51%
- vol_ratio(Volume/Vol20): 1.766018 | gap_open: 7.71%
- RS vs SILJ gap: -7.67% / slope_proxy: -0.145661
- RS vs GDXJ gap: -9.67% / slope_proxy: -0.035046
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
