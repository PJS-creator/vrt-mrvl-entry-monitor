# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-01**
- 실행시간(UTC): **2026-10-02 03:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 46.0 bp / latest 3.12
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 48.0 bp / latest 2.93
- VIX: 16.34
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: -1.38% / slope_proxy: 0.014819
- GDXJ/GLD gap: 0.72% / slope_proxy: 0.013698

## VZLA (Vizsla Silver)
- close: 3.75 | RSI14: 44.317995 | ATR14%: 5.21%
- MA20 gap: -5.23% | MA50 gap: -0.99% | MA200 gap: -5.91%
- vol_ratio(Volume/Vol20): 1.479608 | gap_open: 0.00%
- RS vs SILJ gap: 6.73% / slope_proxy: 0.002343
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.71 | RSI14: 46.067783 | ATR14%: 7.01%
- MA20 gap: -6.28% | MA50 gap: -0.31% | MA200 gap: -3.15%
- vol_ratio(Volume/Vol20): 0.630573 | gap_open: 0.23%
- SilverMarginGate: SI=61.035 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.31% / slope_proxy: 0.01961
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 18.93 | RSI14: 37.672711 | ATR14%: 7.84%
- MA20 gap: -10.36% | MA50 gap: -17.19% | MA200 gap: -38.49%
- vol_ratio(Volume/Vol20): 0.726607 | gap_open: 0.26%
- RS vs SILJ gap: -11.76% / slope_proxy: -0.064719
- RS vs GDXJ gap: -14.54% / slope_proxy: -0.020773
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
