# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-01**
- 실행시간(UTC): **2026-09-01 15:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -25.0 bp / latest 2.6
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -5.0 bp / latest 2.42
- VIX: 14.92
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 8.64% / slope_proxy: 0.025791
- GDXJ/GLD gap: 13.18% / slope_proxy: 0.007586

## VZLA (Vizsla Silver)
- close: 3.945 | RSI14: 57.331739 | ATR14%: 4.86%
- MA20 gap: 2.53% | MA50 gap: 13.86% | MA200 gap: -3.12%
- vol_ratio(Volume/Vol20): 0.299053 | gap_open: 3.95%
- RS vs SILJ gap: 0.81% / slope_proxy: 0.001833
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
- close: 9.15 | RSI14: 56.636351 | ATR14%: 6.11%
- MA20 gap: 0.59% | MA50 gap: 21.64% | MA200 gap: 4.34%
- vol_ratio(Volume/Vol20): 0.305968 | gap_open: 4.38%
- SilverMarginGate: SI=65.389999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.13% / slope_proxy: 0.007218
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
- close: 22.290001 | RSI14: 42.062375 | ATR14%: 8.45%
- MA20 gap: -13.46% | MA50 gap: -3.35% | MA200 gap: -24.95%
- vol_ratio(Volume/Vol20): 0.327011 | gap_open: 5.63%
- RS vs SILJ gap: -15.78% / slope_proxy: -0.100435
- RS vs GDXJ gap: -18.89% / slope_proxy: -0.029853
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
