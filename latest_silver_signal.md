# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-14**
- 실행시간(UTC): **2026-08-14 15:01:18**

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
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.42
- VIX: 14.63
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 9.34% / slope_proxy: 0.015749
- GDXJ/GLD gap: 9.47% / slope_proxy: -0.003079

## VZLA (Vizsla Silver)
- close: 3.85 | RSI14: 64.730863 | ATR14%: 4.75%
- MA20 gap: 12.23% | MA50 gap: 13.31% | MA200 gap: -5.88%
- vol_ratio(Volume/Vol20): 0.258738 | gap_open: 0.80%
- RS vs SILJ gap: 0.80% / slope_proxy: 0.005675
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
- close: 8.96 | RSI14: 71.040182 | ATR14%: 5.63%
- MA20 gap: 23.00% | MA50 gap: 28.40% | MA200 gap: 5.17%
- vol_ratio(Volume/Vol20): 0.277779 | gap_open: 1.49%
- SilverMarginGate: SI=65.400002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.46% / slope_proxy: -0.002013
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
- close: 27.620001 | RSI14: 64.379044 | ATR14%: 6.59%
- MA20 gap: 21.29% | MA50 gap: 18.83% | MA200 gap: -3.60%
- vol_ratio(Volume/Vol20): 0.1932 | gap_open: 3.42%
- RS vs SILJ gap: -0.01% / slope_proxy: -0.1298
- RS vs GDXJ gap: -1.76% / slope_proxy: -0.033605
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
