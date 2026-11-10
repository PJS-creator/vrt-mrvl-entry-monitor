# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-10**
- 실행시간(UTC): **2026-11-10 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 31.0 bp / latest 3.42
- IG OAS 4주 변화: 10.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -28.0 bp / latest 2.63
- VIX: 19.92
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 6.04% / slope_proxy: 0.005153
- GDXJ/GLD gap: -2.05% / slope_proxy: 0.00138

## VZLA (Vizsla Silver)
- close: 3.38 | RSI14: 51.173086 | ATR14%: 6.05%
- MA20 gap: 4.77% | MA50 gap: -5.91% | MA200 gap: -7.11%
- vol_ratio(Volume/Vol20): 0.155776 | gap_open: 4.57%
- RS vs SILJ gap: 2.23% / slope_proxy: 0.000979
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
- close: 7.73 | RSI14: 48.851382 | ATR14%: 7.02%
- MA20 gap: 1.96% | MA50 gap: -9.48% | MA200 gap: -10.09%
- vol_ratio(Volume/Vol20): 0.190149 | gap_open: 4.82%
- SilverMarginGate: SI=51.645 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.77% / slope_proxy: 0.011084
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
- close: 20.106001 | RSI14: 58.761774 | ATR14%: 7.63%
- MA20 gap: 17.05% | MA50 gap: 4.88% | MA200 gap: -31.12%
- vol_ratio(Volume/Vol20): 0.201692 | gap_open: 4.51%
- RS vs SILJ gap: 10.33% / slope_proxy: -0.051096
- RS vs GDXJ gap: 7.16% / slope_proxy: -0.017273
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
