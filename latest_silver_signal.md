# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-23**
- 실행시간(UTC): **2026-09-24 03:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.68
- IG OAS 4주 변화: -4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 31.0 bp / latest 2.63
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 1.73% / slope_proxy: 0.021722
- GDXJ/GLD gap: 7.48% / slope_proxy: 0.014292

## VZLA (Vizsla Silver)
- close: 4.04 | RSI14: 55.484408 | ATR14%: 5.08%
- MA20 gap: 0.96% | MA50 gap: 9.56% | MA200 gap: 0.29%
- vol_ratio(Volume/Vol20): 1.275999 | gap_open: 1.47%
- RS vs SILJ gap: 7.32% / slope_proxy: 0.000427
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
- close: 8.88 | RSI14: 47.825728 | ATR14%: 7.11%
- MA20 gap: -6.56% | MA50 gap: 6.35% | MA200 gap: -1.27%
- vol_ratio(Volume/Vol20): 1.216939 | gap_open: 2.44%
- SilverMarginGate: SI=64.57 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.55% / slope_proxy: 0.017412
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
- close: 21.26 | RSI14: 44.013217 | ATR14%: 7.42%
- MA20 gap: -5.50% | MA50 gap: -6.95% | MA200 gap: -30.26%
- vol_ratio(Volume/Vol20): 0.888761 | gap_open: 6.04%
- RS vs SILJ gap: -10.83% / slope_proxy: -0.078901
- RS vs GDXJ gap: -13.91% / slope_proxy: -0.024706
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
