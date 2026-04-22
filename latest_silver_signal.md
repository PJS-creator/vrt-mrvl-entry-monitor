# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-22**
- 실행시간(UTC): **2026-04-22 15:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.85
- IG OAS 4주 변화: -7.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -10.0 bp / latest 1.91
- VIX: 19.5
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.19% / slope_proxy: 0.012346
- GDXJ/GLD gap: 0.80% / slope_proxy: -0.003928

## VZLA (Vizsla Silver)
- close: 3.465 | RSI14: 49.920932 | ATR14%: 5.75%
- MA20 gap: 4.58% | MA50 gap: -4.07% | MA200 gap: -17.47%
- vol_ratio(Volume/Vol20): 0.282954 | gap_open: 2.40%
- RS vs SILJ gap: -6.99% / slope_proxy: -0.02627
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
- close: 8.95 | RSI14: 51.88556 | ATR14%: 7.95%
- MA20 gap: 7.51% | MA50 gap: -4.79% | MA200 gap: 16.25%
- vol_ratio(Volume/Vol20): 0.187707 | gap_open: 4.00%
- SilverMarginGate: SI=77.989998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.85% / slope_proxy: -0.028523
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
- close: 41.029999 | RSI14: 54.091908 | ATR14%: 9.14%
- MA20 gap: 9.07% | MA50 gap: 4.15% | MA200 gap: 108.96%
- vol_ratio(Volume/Vol20): 0.206281 | gap_open: 4.34%
- RS vs SILJ gap: 7.75% / slope_proxy: 0.068918
- RS vs GDXJ gap: 6.70% / slope_proxy: 0.01516
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
