# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-25**
- 실행시간(UTC): **2026-09-26 00:51:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 17.0 bp / latest 2.8
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 51.0 bp / latest 2.85
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 0.91% / slope_proxy: 0.019912
- GDXJ/GLD gap: 5.96% / slope_proxy: 0.014682

## VZLA (Vizsla Silver)
- close: 3.94 | RSI14: 50.36125 | ATR14%: 5.48%
- MA20 gap: -1.76% | MA50 gap: 5.79% | MA200 gap: -1.98%
- vol_ratio(Volume/Vol20): 0.882484 | gap_open: 0.99%
- RS vs SILJ gap: 6.08% / slope_proxy: 0.000947
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
- close: 8.92 | RSI14: 48.171365 | ATR14%: 7.08%
- MA20 gap: -5.67% | MA50 gap: 5.41% | MA200 gap: -0.94%
- vol_ratio(Volume/Vol20): 0.82824 | gap_open: 1.46%
- SilverMarginGate: SI=64.709999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.05% / slope_proxy: 0.018205
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
- close: 20.889999 | RSI14: 43.571802 | ATR14%: 7.79%
- MA20 gap: -5.47% | MA50 gap: -8.64% | MA200 gap: -31.70%
- vol_ratio(Volume/Vol20): 0.70554 | gap_open: 1.55%
- RS vs SILJ gap: -10.30% / slope_proxy: -0.075465
- RS vs GDXJ gap: -13.51% / slope_proxy: -0.023767
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
