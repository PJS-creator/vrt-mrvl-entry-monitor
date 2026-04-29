# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-29**
- 실행시간(UTC): **2026-04-29 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -43.0 bp / latest 2.85
- IG OAS 4주 변화: -9.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -13.0 bp / latest 1.91
- VIX: 17.83
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.38% / slope_proxy: 0.015223
- GDXJ/GLD gap: -4.52% / slope_proxy: -0.003666

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 50.367287 | ATR14%: 5.60%
- MA20 gap: 2.62% | MA50 gap: -3.11% | MA200 gap: -17.76%
- vol_ratio(Volume/Vol20): 0.22561 | gap_open: 0.88%
- RS vs SILJ gap: 6.51% / slope_proxy: -0.023334
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
- close: 7.7 | RSI14: 39.972235 | ATR14%: 8.50%
- MA20 gap: -8.56% | MA50 gap: -16.19% | MA200 gap: -1.50%
- vol_ratio(Volume/Vol20): 0.544217 | gap_open: 1.65%
- SilverMarginGate: SI=72.160004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.64% / slope_proxy: -0.030995
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
- close: 34.174999 | RSI14: 41.348491 | ATR14%: 10.10%
- MA20 gap: -11.39% | MA50 gap: -13.63% | MA200 gap: 67.02%
- vol_ratio(Volume/Vol20): 0.292898 | gap_open: 1.32%
- RS vs SILJ gap: -0.59% / slope_proxy: 0.039945
- RS vs GDXJ gap: -1.33% / slope_proxy: 0.006612
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
