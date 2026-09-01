# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-31**
- 실행시간(UTC): **2026-09-01 01:23:22**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -25.0 bp / latest 2.6
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -5.0 bp / latest 2.42
- VIX: 14.43
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 8.24% / slope_proxy: 0.025074
- GDXJ/GLD gap: 13.46% / slope_proxy: 0.006405

## VZLA (Vizsla Silver)
- close: 4.05 | RSI14: 62.042537 | ATR14%: 4.70%
- MA20 gap: 6.01% | MA50 gap: 17.18% | MA200 gap: -0.64%
- vol_ratio(Volume/Vol20): 0.936059 | gap_open: 0.00%
- RS vs SILJ gap: 1.57% / slope_proxy: 0.002139
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
- close: 9.36 | RSI14: 59.846102 | ATR14%: 5.91%
- MA20 gap: 4.01% | MA50 gap: 25.13% | MA200 gap: 6.93%
- vol_ratio(Volume/Vol20): 0.443781 | gap_open: 2.73%
- SilverMarginGate: SI=67.379997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.93% / slope_proxy: 0.006136
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
- close: 23.43 | RSI14: 45.386951 | ATR14%: 8.10%
- MA20 gap: -9.05% | MA50 gap: 1.35% | MA200 gap: -20.94%
- vol_ratio(Volume/Vol20): 0.806828 | gap_open: 0.02%
- RS vs SILJ gap: -13.59% / slope_proxy: -0.102515
- RS vs GDXJ gap: -16.93% / slope_proxy: -0.030072
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
