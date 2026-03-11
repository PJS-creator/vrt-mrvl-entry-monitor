# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-11**
- 실행시간(UTC): **2026-03-11 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.06
- IG OAS 4주 변화: 7.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -9.0 bp / latest 1.78
- VIX: 24.93
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: 0.92% / slope_proxy: -0.003035
- GDXJ/GLD gap: -3.46% / slope_proxy: 0.012308

## VZLA (Vizsla Silver)
- close: 4.0539 | RSI14: 43.199272 | ATR14%: 7.86%
- MA20 gap: 1.71% | MA50 gap: -18.63% | MA200 gap: -2.84%
- vol_ratio(Volume/Vol20): 0.120814 | gap_open: 2.17%
- RS vs SILJ gap: -24.81% / slope_proxy: -0.029069
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.09 | RSI14: 43.33006 | ATR14%: 10.32%
- MA20 gap: -7.12% | MA50 gap: -12.04% | MA200 gap: 46.45%
- vol_ratio(Volume/Vol20): 0.420448 | gap_open: 0.75%
- SilverMarginGate: SI=86.029999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.32% / slope_proxy: 0.004119
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 43.660099 | RSI14: 51.905141 | ATR14%: 13.13%
- MA20 gap: 1.44% | MA50 gap: 12.24% | MA200 gap: 195.68%
- vol_ratio(Volume/Vol20): 0.255455 | gap_open: 4.57%
- RS vs SILJ gap: 19.97% / slope_proxy: 0.249362
- RS vs GDXJ gap: 20.63% / slope_proxy: 0.065469
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
