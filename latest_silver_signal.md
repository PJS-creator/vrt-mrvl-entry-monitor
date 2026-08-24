# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-24**
- 실행시간(UTC): **2026-08-24 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -9.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -8.0 bp / latest 2.35
- VIX: 15.13
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 7.58% / slope_proxy: 0.021059
- GDXJ/GLD gap: 13.81% / slope_proxy: 0.002003

## VZLA (Vizsla Silver)
- close: 3.985 | RSI14: 64.728878 | ATR14%: 4.61%
- MA20 gap: 10.47% | MA50 gap: 16.76% | MA200 gap: -2.21%
- vol_ratio(Volume/Vol20): 0.331122 | gap_open: 1.77%
- RS vs SILJ gap: -1.94% / slope_proxy: 0.003909
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
- close: 9.585 | RSI14: 68.986196 | ATR14%: 5.66%
- MA20 gap: 16.58% | MA50 gap: 32.08% | MA200 gap: 10.91%
- vol_ratio(Volume/Vol20): 0.306241 | gap_open: 1.40%
- SilverMarginGate: SI=68.75 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.14% / slope_proxy: 0.002518
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
- close: 26.209999 | RSI14: 54.641092 | ATR14%: 7.45%
- MA20 gap: 6.89% | MA50 gap: 12.65% | MA200 gap: -10.25%
- vol_ratio(Volume/Vol20): 0.405075 | gap_open: 0.66%
- RS vs SILJ gap: -7.51% / slope_proxy: -0.114998
- RS vs GDXJ gap: -13.68% / slope_proxy: -0.031793
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
