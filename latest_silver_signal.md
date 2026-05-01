# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-30**
- 실행시간(UTC): **2026-05-01 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.82
- IG OAS 4주 변화: -6.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -6.0 bp / latest 1.96
- VIX: 18.81
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.12% / slope_proxy: 0.014608
- GDXJ/GLD gap: -4.45% / slope_proxy: -0.003881

## VZLA (Vizsla Silver)
- close: 3.38 | RSI14: 47.347175 | ATR14%: 5.86%
- MA20 gap: 0.27% | MA50 gap: -5.13% | MA200 gap: -19.66%
- vol_ratio(Volume/Vol20): 0.56215 | gap_open: 3.24%
- RS vs SILJ gap: 2.02% / slope_proxy: -0.022557
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 7.86 | RSI14: 41.936605 | ATR14%: 8.10%
- MA20 gap: -6.53% | MA50 gap: -14.14% | MA200 gap: 0.29%
- vol_ratio(Volume/Vol20): 1.176477 | gap_open: 2.85%
- SilverMarginGate: SI=74.629997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.56% / slope_proxy: -0.031417
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
- close: 36.459999 | RSI14: 46.607382 | ATR14%: 9.30%
- MA20 gap: -5.64% | MA50 gap: -7.65% | MA200 gap: 76.77%
- vol_ratio(Volume/Vol20): 0.71475 | gap_open: 5.99%
- RS vs SILJ gap: 3.36% / slope_proxy: 0.037459
- RS vs GDXJ gap: 3.73% / slope_proxy: 0.005823
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
