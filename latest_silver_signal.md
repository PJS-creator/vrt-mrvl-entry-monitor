# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-29 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.71
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.09
- VIX: 16.29
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 1.68% / slope_proxy: -0.013143
- GDXJ/GLD gap: -0.11% / slope_proxy: -0.006273

## VZLA (Vizsla Silver)
- close: 3.87 | RSI14: 60.68752 | ATR14%: 5.67%
- MA20 gap: 9.01% | MA50 gap: 13.77% | MA200 gap: -8.75%
- vol_ratio(Volume/Vol20): 0.273075 | gap_open: 0.26%
- RS vs SILJ gap: 11.35% / slope_proxy: 0.000214
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
- close: 8.165 | RSI14: 45.480856 | ATR14%: 7.17%
- MA20 gap: -5.02% | MA50 gap: -2.26% | MA200 gap: -1.69%
- vol_ratio(Volume/Vol20): 0.230336 | gap_open: 0.00%
- SilverMarginGate: SI=75.379997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.43% / slope_proxy: -0.011723
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
- close: 33.131599 | RSI14: 42.698043 | ATR14%: 8.88%
- MA20 gap: -9.78% | MA50 gap: -9.67% | MA200 gap: 38.42%
- vol_ratio(Volume/Vol20): 0.23609 | gap_open: 0.69%
- RS vs SILJ gap: -10.95% / slope_proxy: 0.008754
- RS vs GDXJ gap: -8.07% / slope_proxy: 0.004034
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
