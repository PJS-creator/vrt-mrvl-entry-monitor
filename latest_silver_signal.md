# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-05**
- 실행시간(UTC): **2026-05-05 15:01:36**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -27.0 bp / latest 2.78
- IG OAS 4주 변화: -5.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.91
- VIX: 18.29
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -4.26% / slope_proxy: 0.011571
- GDXJ/GLD gap: -5.17% / slope_proxy: -0.003816

## VZLA (Vizsla Silver)
- close: 3.315 | RSI14: 44.955647 | ATR14%: 5.94%
- MA20 gap: -2.16% | MA50 gap: -6.12% | MA200 gap: -21.24%
- vol_ratio(Volume/Vol20): 0.252217 | gap_open: 1.49%
- RS vs SILJ gap: 2.75% / slope_proxy: -0.019561
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
- close: 8.09 | RSI14: 45.674515 | ATR14%: 7.48%
- MA20 gap: -3.96% | MA50 gap: -9.74% | MA200 gap: 2.44%
- vol_ratio(Volume/Vol20): 0.231127 | gap_open: 1.90%
- SilverMarginGate: SI=74.114998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.21% / slope_proxy: -0.031064
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
- close: 36.060001 | RSI14: 46.156697 | ATR14%: 8.80%
- MA20 gap: -6.95% | MA50 gap: -8.00% | MA200 gap: 70.71%
- vol_ratio(Volume/Vol20): 0.153098 | gap_open: 1.91%
- RS vs SILJ gap: 3.05% / slope_proxy: 0.03345
- RS vs GDXJ gap: 3.64% / slope_proxy: 0.004659
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
