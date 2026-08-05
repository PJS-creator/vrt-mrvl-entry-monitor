# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-05**
- 실행시간(UTC): **2026-08-05 15:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.78
- IG OAS 4주 변화: 3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.43
- VIX: 16.5
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 7.57% / slope_proxy: 0.009638
- GDXJ/GLD gap: 3.83% / slope_proxy: -0.007859

## VZLA (Vizsla Silver)
- close: 3.58 | RSI14: 60.373675 | ATR14%: 5.44%
- MA20 gap: 11.01% | MA50 gap: 5.84% | MA200 gap: -12.66%
- vol_ratio(Volume/Vol20): 0.624445 | gap_open: 5.00%
- RS vs SILJ gap: 2.55% / slope_proxy: 0.006073
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
- close: 7.79 | RSI14: 64.907165 | ATR14%: 6.15%
- MA20 gap: 19.61% | MA50 gap: 14.11% | MA200 gap: -7.62%
- vol_ratio(Volume/Vol20): 0.541913 | gap_open: 7.29%
- SilverMarginGate: SI=62.535 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.70% / slope_proxy: -0.0054
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
- close: 24.450001 | RSI14: 59.082522 | ATR14%: 7.39%
- MA20 gap: 18.56% | MA50 gap: 1.41% | MA200 gap: -12.62%
- vol_ratio(Volume/Vol20): 0.826719 | gap_open: 7.71%
- RS vs SILJ gap: -7.87% / slope_proxy: -0.145693
- RS vs GDXJ gap: -9.39% / slope_proxy: -0.035034
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
