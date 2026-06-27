# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-26**
- 실행시간(UTC): **2026-06-27 15:01:06**

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
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.19
- VIX: 18.89
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 9.78% / slope_proxy: 0.005097
- GDXJ/GLD gap: -4.06% / slope_proxy: -0.001691

## VZLA (Vizsla Silver)
- close: 3.28 | RSI14: 43.73333 | ATR14%: 6.86%
- MA20 gap: -7.62% | MA50 gap: -6.69% | MA200 gap: -22.65%
- vol_ratio(Volume/Vol20): 0.63506 | gap_open: 1.28%
- RS vs SILJ gap: 6.91% / slope_proxy: 0.004446
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
- close: 6.61 | RSI14: 41.549482 | ATR14%: 8.50%
- MA20 gap: -6.52% | MA50 gap: -17.17% | MA200 gap: -22.39%
- vol_ratio(Volume/Vol20): 0.632543 | gap_open: 3.26%
- SilverMarginGate: SI=59.216999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.91% / slope_proxy: -0.00963
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
- close: 23.74 | RSI14: 38.163472 | ATR14%: 10.10%
- MA20 gap: -11.29% | MA50 gap: -28.74% | MA200 gap: -8.77%
- vol_ratio(Volume/Vol20): 3.92136 | gap_open: 1.32%
- RS vs SILJ gap: -20.04% / slope_proxy: -0.078992
- RS vs GDXJ gap: -18.41% / slope_proxy: -0.016894
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
