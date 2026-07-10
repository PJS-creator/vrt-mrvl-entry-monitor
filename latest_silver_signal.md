# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-09**
- 실행시간(UTC): **2026-07-10 03:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.31
- VIX: 16.9
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 5.27% / slope_proxy: 0.008145
- GDXJ/GLD gap: -5.35% / slope_proxy: -0.002493

## VZLA (Vizsla Silver)
- close: 3.16 | RSI14: 43.543631 | ATR14%: 6.71%
- MA20 gap: -5.35% | MA50 gap: -9.19% | MA200 gap: -25.04%
- vol_ratio(Volume/Vol20): 1.087633 | gap_open: 2.03%
- RS vs SILJ gap: 3.01% / slope_proxy: 0.005132
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
- close: 6.67 | RSI14: 45.708327 | ATR14%: 7.50%
- MA20 gap: -1.40% | MA50 gap: -12.47% | MA200 gap: -21.66%
- vol_ratio(Volume/Vol20): 1.044348 | gap_open: 2.40%
- SilverMarginGate: SI=60.790001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.73% / slope_proxy: -0.005139
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
- close: 21.799999 | RSI14: 36.613356 | ATR14%: 9.68%
- MA20 gap: -8.54% | MA50 gap: -28.49% | MA200 gap: -18.31%
- vol_ratio(Volume/Vol20): 0.464312 | gap_open: 2.21%
- RS vs SILJ gap: -22.14% / slope_proxy: -0.09758
- RS vs GDXJ gap: -21.68% / slope_proxy: -0.02127
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
