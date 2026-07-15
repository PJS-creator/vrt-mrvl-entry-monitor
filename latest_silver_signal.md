# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-15**
- 실행시간(UTC): **2026-07-15 15:01:23**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.72
- IG OAS 4주 변화: 4.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.36
- VIX: 16.5
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 5.46% / slope_proxy: 0.009355
- GDXJ/GLD gap: -5.63% / slope_proxy: -0.003843

## VZLA (Vizsla Silver)
- close: 3.175 | RSI14: 45.655368 | ATR14%: 6.17%
- MA20 gap: -2.88% | MA50 gap: -8.16% | MA200 gap: -24.36%
- vol_ratio(Volume/Vol20): 0.183583 | gap_open: 0.00%
- RS vs SILJ gap: 5.16% / slope_proxy: 0.005335
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
- close: 6.41 | RSI14: 43.017961 | ATR14%: 6.95%
- MA20 gap: -4.19% | MA50 gap: -14.57% | MA200 gap: -24.58%
- vol_ratio(Volume/Vol20): 0.315085 | gap_open: 0.31%
- SilverMarginGate: SI=58.43 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.54% / slope_proxy: -0.005249
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
- close: 20.9 | RSI14: 37.069984 | ATR14%: 9.22%
- MA20 gap: -9.03% | MA50 gap: -28.60% | MA200 gap: -22.54%
- vol_ratio(Volume/Vol20): 0.142328 | gap_open: 1.01%
- RS vs SILJ gap: -21.24% / slope_proxy: -0.108809
- RS vs GDXJ gap: -21.72% / slope_proxy: -0.022726
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
