# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-23**
- 실행시간(UTC): **2026-06-24 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -9.0 bp / latest 2.65
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.28
- VIX: 17.28
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 5.20% / slope_proxy: 0.000204
- GDXJ/GLD gap: -4.84% / slope_proxy: -0.003174

## VZLA (Vizsla Silver)
- close: 3.35 | RSI14: 43.412914 | ATR14%: 6.79%
- MA20 gap: -7.73% | MA50 gap: -5.06% | MA200 gap: -21.15%
- vol_ratio(Volume/Vol20): 0.790676 | gap_open: 5.40%
- RS vs SILJ gap: 10.10% / slope_proxy: 0.004569
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
- close: 6.62 | RSI14: 40.137107 | ATR14%: 9.16%
- MA20 gap: -9.32% | MA50 gap: -18.49% | MA200 gap: -22.19%
- vol_ratio(Volume/Vol20): 0.815946 | gap_open: 4.67%
- SilverMarginGate: SI=61.165001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.93% / slope_proxy: -0.010228
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
- close: 23.139999 | RSI14: 33.366442 | ATR14%: 10.93%
- MA20 gap: -18.27% | MA50 gap: -32.73% | MA200 gap: -10.21%
- vol_ratio(Volume/Vol20): 1.01384 | gap_open: 5.51%
- RS vs SILJ gap: -22.75% / slope_proxy: -0.076426
- RS vs GDXJ gap: -21.51% / slope_proxy: -0.016667
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
