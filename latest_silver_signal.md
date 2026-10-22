# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-22**
- 실행시간(UTC): **2026-10-22 15:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 54.0 bp / latest 3.27
- IG OAS 4주 변화: 11.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 14.0 bp / latest 2.77
- VIX: 16.68
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.05% / slope_proxy: 0.007285
- GDXJ/GLD gap: -8.25% / slope_proxy: 0.010499

## VZLA (Vizsla Silver)
- close: 3.155 | RSI14: 36.252225 | ATR14%: 5.63%
- MA20 gap: -9.62% | MA50 gap: -16.29% | MA200 gap: -17.52%
- vol_ratio(Volume/Vol20): 0.310484 | gap_open: 3.57%
- RS vs SILJ gap: 1.73% / slope_proxy: 0.001274
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
- close: 7.26 | RSI14: 33.759766 | ATR14%: 7.51%
- MA20 gap: -15.48% | MA50 gap: -19.97% | MA200 gap: -18.53%
- vol_ratio(Volume/Vol20): 0.601541 | gap_open: 5.39%
- SilverMarginGate: SI=55.52 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.43% / slope_proxy: 0.022553
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
- close: 16.0 | RSI14: 33.914479 | ATR14%: 7.59%
- MA20 gap: -12.11% | MA50 gap: -25.14% | MA200 gap: -47.50%
- vol_ratio(Volume/Vol20): 0.249641 | gap_open: 5.08%
- RS vs SILJ gap: -11.41% / slope_proxy: -0.049964
- RS vs GDXJ gap: -15.11% / slope_proxy: -0.017036
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
