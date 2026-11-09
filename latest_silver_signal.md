# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-08**
- 실행시간(UTC): **2026-11-09 01:56:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.48
- IG OAS 4주 변화: 11.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -27.0 bp / latest 2.6
- VIX: 28.18
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 4.41% / slope_proxy: 0.004901
- GDXJ/GLD gap: -2.97% / slope_proxy: 0.002828

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 48.773418 | ATR14%: 6.07%
- MA20 gap: 2.33% | MA50 gap: -8.73% | MA200 gap: -10.10%
- vol_ratio(Volume/Vol20): 0.827751 | gap_open: 0.63%
- RS vs SILJ gap: 1.88% / slope_proxy: 0.000578
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
- close: 7.52 | RSI14: 46.410472 | ATR14%: 7.10%
- MA20 gap: -1.81% | MA50 gap: -12.56% | MA200 gap: -13.31%
- vol_ratio(Volume/Vol20): 0.677489 | gap_open: 1.44%
- SilverMarginGate: SI=53.310001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.57% / slope_proxy: 0.013117
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
- close: 18.77 | RSI14: 55.562341 | ATR14%: 7.47%
- MA20 gap: 11.06% | MA50 gap: -2.69% | MA200 gap: -36.34%
- vol_ratio(Volume/Vol20): 1.286552 | gap_open: 1.82%
- RS vs SILJ gap: 4.44% / slope_proxy: -0.052245
- RS vs GDXJ gap: -0.19% / slope_proxy: -0.01755
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
