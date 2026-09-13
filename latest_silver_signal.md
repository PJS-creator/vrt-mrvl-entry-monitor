# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-11**
- 실행시간(UTC): **2026-09-13 00:16:47**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.55
- VIX: 17.84
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 6.32% / slope_proxy: 0.027817
- GDXJ/GLD gap: 11.13% / slope_proxy: 0.01356

## VZLA (Vizsla Silver)
- close: 3.97 | RSI14: 53.698634 | ATR14%: 5.06%
- MA20 gap: 0.23% | MA50 gap: 10.95% | MA200 gap: -2.19%
- vol_ratio(Volume/Vol20): 0.688704 | gap_open: 1.75%
- RS vs SILJ gap: 2.33% / slope_proxy: 0.000117
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 9.65 | RSI14: 55.10567 | ATR14%: 6.24%
- MA20 gap: 0.37% | MA50 gap: 20.37% | MA200 gap: 8.02%
- vol_ratio(Volume/Vol20): 0.692537 | gap_open: 2.48%
- SilverMarginGate: SI=64.554001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.80% / slope_proxy: 0.014654
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
- close: 21.18 | RSI14: 39.724686 | ATR14%: 8.27%
- MA20 gap: -13.26% | MA50 gap: -7.88% | MA200 gap: -29.72%
- vol_ratio(Volume/Vol20): 1.093831 | gap_open: 2.81%
- RS vs SILJ gap: -16.59% / slope_proxy: -0.088636
- RS vs GDXJ gap: -19.86% / slope_proxy: -0.027053
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
