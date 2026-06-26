# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-26**
- 실행시간(UTC): **2026-06-26 15:01:05**

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
- IG OAS 4주 변화: 3.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 14.0 bp / latest 2.23
- VIX: 18.89
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 10.22% / slope_proxy: 0.005131
- GDXJ/GLD gap: -3.09% / slope_proxy: -0.001645

## VZLA (Vizsla Silver)
- close: 3.2701 | RSI14: 43.409983 | ATR14%: 6.74%
- MA20 gap: -7.88% | MA50 gap: -6.97% | MA200 gap: -22.89%
- vol_ratio(Volume/Vol20): 0.194285 | gap_open: 1.28%
- RS vs SILJ gap: 5.62% / slope_proxy: 0.004421
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
- close: 6.705 | RSI14: 42.776977 | ATR14%: 8.38%
- MA20 gap: -5.24% | MA50 gap: -16.00% | MA200 gap: -21.27%
- vol_ratio(Volume/Vol20): 0.151942 | gap_open: 3.26%
- SilverMarginGate: SI=59.830002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.45% / slope_proxy: -0.00961
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
- close: 23.370001 | RSI14: 36.968218 | ATR14%: 10.05%
- MA20 gap: -12.61% | MA50 gap: -29.84% | MA200 gap: -10.19%
- vol_ratio(Volume/Vol20): 0.375656 | gap_open: 1.32%
- RS vs SILJ gap: -21.99% / slope_proxy: -0.079367
- RS vs GDXJ gap: -20.67% / slope_proxy: -0.017004
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
