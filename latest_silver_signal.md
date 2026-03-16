# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-15**
- 실행시간(UTC): **2026-03-16 03:00:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 25.0 bp / latest 3.17
- IG OAS 4주 변화: 13.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.89
- VIX: 27.29
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -1.65% / slope_proxy: -0.003792
- GDXJ/GLD gap: -8.88% / slope_proxy: 0.010759

## VZLA (Vizsla Silver)
- close: 3.59 | RSI14: 34.877784 | ATR14%: 8.71%
- MA20 gap: -9.92% | MA50 gap: -26.88% | MA200 gap: -14.15%
- vol_ratio(Volume/Vol20): 0.591721 | gap_open: 0.77%
- RS vs SILJ gap: -25.64% / slope_proxy: -0.02846
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 9.33 | RSI14: 38.977173 | ATR14%: 10.52%
- MA20 gap: -13.21% | MA50 gap: -18.49% | MA200 gap: 33.91%
- vol_ratio(Volume/Vol20): 2.776973 | gap_open: 1.62%
- SilverMarginGate: SI=79.43 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.37% / slope_proxy: -0.000536
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
- close: 37.93 | RSI14: 45.173627 | ATR14%: 14.26%
- MA20 gap: -12.68% | MA50 gap: -3.98% | MA200 gap: 150.85%
- vol_ratio(Volume/Vol20): 0.733915 | gap_open: 0.09%
- RS vs SILJ gap: 12.04% / slope_proxy: 0.251936
- RS vs GDXJ gap: 12.27% / slope_proxy: 0.066199
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
