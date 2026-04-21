# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-20**
- 실행시간(UTC): **2026-04-21 03:00:50**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -41.0 bp / latest 2.83
- IG OAS 4주 변화: -8.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -11.0 bp / latest 1.9
- VIX: 17.48
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 1.10% / slope_proxy: 0.010755
- GDXJ/GLD gap: 2.73% / slope_proxy: -0.003661

## VZLA (Vizsla Silver)
- close: 3.52 | RSI14: 51.943606 | ATR14%: 5.65%
- MA20 gap: 7.15% | MA50 gap: -3.56% | MA200 gap: -16.09%
- vol_ratio(Volume/Vol20): 1.063704 | gap_open: 1.99%
- RS vs SILJ gap: -10.27% / slope_proxy: -0.027031
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
- close: 9.1 | RSI14: 53.62529 | ATR14%: 7.96%
- MA20 gap: 10.60% | MA50 gap: -4.34% | MA200 gap: 19.04%
- vol_ratio(Volume/Vol20): 0.69699 | gap_open: 1.09%
- SilverMarginGate: SI=79.220001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.75% / slope_proxy: -0.026155
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
- close: 43.970001 | RSI14: 61.104805 | ATR14%: 8.51%
- MA20 gap: 19.27% | MA50 gap: 12.02% | MA200 gap: 128.24%
- vol_ratio(Volume/Vol20): 0.753145 | gap_open: 2.33%
- RS vs SILJ gap: 11.57% / slope_proxy: 0.078489
- RS vs GDXJ gap: 9.78% / slope_proxy: 0.018595
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trigger(Breakout/Retest)=FALSE
