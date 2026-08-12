# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-12**
- 실행시간(UTC): **2026-08-12 23:21:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.72
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.43
- VIX: 15.28
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 10.01% / slope_proxy: 0.013568
- GDXJ/GLD gap: 9.62% / slope_proxy: -0.005087

## VZLA (Vizsla Silver)
- close: 3.8 | RSI14: 63.354092 | ATR14%: 4.96%
- MA20 gap: 12.46% | MA50 gap: 12.52% | MA200 gap: -6.99%
- vol_ratio(Volume/Vol20): 0.613145 | gap_open: 2.61%
- RS vs SILJ gap: -0.74% / slope_proxy: 0.005809
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

## SCZM (Santacruz Silver)
- close: 8.87 | RSI14: 72.159234 | ATR14%: 5.86%
- MA20 gap: 27.98% | MA50 gap: 29.07% | MA200 gap: 4.57%
- vol_ratio(Volume/Vol20): 0.820273 | gap_open: 4.67%
- SilverMarginGate: SI=65.360001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.77% / slope_proxy: -0.003828
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
- close: 27.450001 | RSI14: 65.641857 | ATR14%: 6.84%
- MA20 gap: 25.13% | MA50 gap: 16.92% | MA200 gap: -3.52%
- vol_ratio(Volume/Vol20): 1.211516 | gap_open: 7.77%
- RS vs SILJ gap: -1.72% / slope_proxy: -0.13854
- RS vs GDXJ gap: -3.88% / slope_proxy: -0.035433
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
