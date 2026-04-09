# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-08**
- 실행시간(UTC): **2026-04-09 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 3.12
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 14.0 bp / latest 1.96
- VIX: 25.78
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 5.10% / slope_proxy: 0.000552
- GDXJ/GLD gap: 0.72% / slope_proxy: -0.004545

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 42.051045 | ATR14%: 7.10%
- MA20 gap: -1.32% | MA50 gap: -17.19% | MA200 gap: -20.99%
- vol_ratio(Volume/Vol20): 0.861257 | gap_open: 6.81%
- RS vs SILJ gap: -19.03% / slope_proxy: -0.02738
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
- close: 7.94 | RSI14: 42.643808 | ATR14%: 10.53%
- MA20 gap: -3.22% | MA50 gap: -22.15% | MA200 gap: 7.13%
- vol_ratio(Volume/Vol20): 0.681671 | gap_open: 9.92%
- SilverMarginGate: SI=74.059998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -19.88% / slope_proxy: -0.022296
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
- close: 37.0 | RSI14: 50.622776 | ATR14%: 11.39%
- MA20 gap: 4.43% | MA50 gap: -6.36% | MA200 gap: 108.36%
- vol_ratio(Volume/Vol20): 0.841846 | gap_open: 11.46%
- RS vs SILJ gap: -0.27% / slope_proxy: 0.143246
- RS vs GDXJ gap: -3.28% / slope_proxy: 0.037615
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
