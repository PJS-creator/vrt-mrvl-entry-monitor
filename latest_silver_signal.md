# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-29**
- 실행시간(UTC): **2026-07-30 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 9.0 bp / latest 2.84
- IG OAS 4주 변화: 5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.41
- VIX: 18.21
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 0.79% / slope_proxy: 0.00744
- GDXJ/GLD gap: -5.34% / slope_proxy: -0.008804

## VZLA (Vizsla Silver)
- close: 3.12 | RSI14: 44.625588 | ATR14%: 6.26%
- MA20 gap: -2.19% | MA50 gap: -7.87% | MA200 gap: -24.56%
- vol_ratio(Volume/Vol20): 0.85444 | gap_open: 1.25%
- RS vs SILJ gap: 5.77% / slope_proxy: 0.006141
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
- close: 6.31 | RSI14: 45.504468 | ATR14%: 6.95%
- MA20 gap: -1.41% | MA50 gap: -9.28% | MA200 gap: -25.21%
- vol_ratio(Volume/Vol20): 0.985563 | gap_open: 0.62%
- SilverMarginGate: SI=58.07 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 0.91% / slope_proxy: -0.005271
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
- close: 19.16 | RSI14: 38.091281 | ATR14%: 9.36%
- MA20 gap: -8.35% | MA50 gap: -24.34% | MA200 gap: -30.70%
- vol_ratio(Volume/Vol20): 1.236184 | gap_open: 0.60%
- RS vs SILJ gap: -18.46% / slope_proxy: -0.138427
- RS vs GDXJ gap: -21.26% / slope_proxy: -0.032278
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
