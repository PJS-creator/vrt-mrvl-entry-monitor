# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-23**
- 실행시간(UTC): **2026-07-23 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.68
- IG OAS 4주 변화: 3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.37
- VIX: 16.64
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 4.44% / slope_proxy: 0.008225
- GDXJ/GLD gap: -3.77% / slope_proxy: -0.008787

## VZLA (Vizsla Silver)
- close: 3.255 | RSI14: 49.43917 | ATR14%: 6.01%
- MA20 gap: 1.93% | MA50 gap: -5.03% | MA200 gap: -21.80%
- vol_ratio(Volume/Vol20): 0.351376 | gap_open: 3.51%
- RS vs SILJ gap: 6.90% / slope_proxy: 0.006192
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
- close: 6.32 | RSI14: 45.25345 | ATR14%: 6.99%
- MA20 gap: -1.79% | MA50 gap: -12.46% | MA200 gap: -25.24%
- vol_ratio(Volume/Vol20): 0.316632 | gap_open: 2.37%
- SilverMarginGate: SI=58.185001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.16% / slope_proxy: -0.005749
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
- close: 20.110001 | RSI14: 40.928826 | ATR14%: 9.37%
- MA20 gap: -6.51% | MA50 gap: -25.53% | MA200 gap: -26.57%
- vol_ratio(Volume/Vol20): 0.210517 | gap_open: 5.62%
- RS vs SILJ gap: -20.04% / slope_proxy: -0.127416
- RS vs GDXJ gap: -21.39% / slope_proxy: -0.028579
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
