# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-01**
- 실행시간(UTC): **2026-05-01 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.83
- IG OAS 4주 변화: -5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -6.0 bp / latest 1.96
- VIX: 16.89
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -5.64% / slope_proxy: 0.01381
- GDXJ/GLD gap: -5.13% / slope_proxy: -0.003953

## VZLA (Vizsla Silver)
- close: 3.365 | RSI14: 46.744853 | ATR14%: 5.81%
- MA20 gap: -0.33% | MA50 gap: -5.25% | MA200 gap: -20.03%
- vol_ratio(Volume/Vol20): 0.206496 | gap_open: 0.59%
- RS vs SILJ gap: 2.02% / slope_proxy: -0.021639
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.1 | RSI14: 45.064467 | ATR14%: 7.68%
- MA20 gap: -3.83% | MA50 gap: -11.11% | MA200 gap: 3.09%
- vol_ratio(Volume/Vol20): 0.27808 | gap_open: 0.64%
- SilverMarginGate: SI=76.294998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.24% / slope_proxy: -0.031536
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 37.259998 | RSI14: 48.362365 | ATR14%: 8.95%
- MA20 gap: -3.73% | MA50 gap: -5.39% | MA200 gap: 79.20%
- vol_ratio(Volume/Vol20): 0.366925 | gap_open: 0.03%
- RS vs SILJ gap: 5.45% / slope_proxy: 0.035145
- RS vs GDXJ gap: 6.37% / slope_proxy: 0.005153
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
