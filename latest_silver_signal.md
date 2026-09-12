# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-11**
- 실행시간(UTC): **2026-09-12 00:36:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.55
- VIX: 17.84
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 8.24% / slope_proxy: 0.028267
- GDXJ/GLD gap: 10.81% / slope_proxy: 0.013358

## VZLA (Vizsla Silver)
- close: 4.0 | RSI14: 54.88655 | ATR14%: 5.01%
- MA20 gap: 1.28% | MA50 gap: 12.23% | MA200 gap: -1.45%
- vol_ratio(Volume/Vol20): 0.848915 | gap_open: 3.91%
- RS vs SILJ gap: 2.64% / slope_proxy: 0.000208
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
- close: 9.69 | RSI14: 55.589102 | ATR14%: 6.21%
- MA20 gap: 1.27% | MA50 gap: 21.80% | MA200 gap: 8.74%
- vol_ratio(Volume/Vol20): 0.925091 | gap_open: 4.79%
- SilverMarginGate: SI=65.019997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.00% / slope_proxy: 0.013966
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
- close: 21.389999 | RSI14: 40.373899 | ATR14%: 8.24%
- MA20 gap: -13.36% | MA50 gap: -7.12% | MA200 gap: -28.89%
- vol_ratio(Volume/Vol20): 0.83127 | gap_open: 5.39%
- RS vs SILJ gap: -16.54% / slope_proxy: -0.089881
- RS vs GDXJ gap: -18.62% / slope_proxy: -0.027204
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
