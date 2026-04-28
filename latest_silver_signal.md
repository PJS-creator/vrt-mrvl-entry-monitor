# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-28**
- 실행시간(UTC): **2026-04-28 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -56.0 bp / latest 2.86
- IG OAS 4주 변화: -11.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -24.0 bp / latest 1.89
- VIX: 18.02
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -2.16% / slope_proxy: 0.015529
- GDXJ/GLD gap: -3.23% / slope_proxy: -0.003456

## VZLA (Vizsla Silver)
- close: 3.385 | RSI14: 47.666278 | ATR14%: 5.84%
- MA20 gap: 0.69% | MA50 gap: -5.29% | MA200 gap: -19.52%
- vol_ratio(Volume/Vol20): 0.330508 | gap_open: 3.41%
- RS vs SILJ gap: 0.88% / slope_proxy: -0.024219
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
- close: 7.825 | RSI14: 41.0806 | ATR14%: 8.58%
- MA20 gap: -7.52% | MA50 gap: -15.05% | MA200 gap: 0.34%
- vol_ratio(Volume/Vol20): 0.381073 | gap_open: 3.57%
- SilverMarginGate: SI=73.010002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -9.11% / slope_proxy: -0.030401
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
- close: 35.810001 | RSI14: 44.232584 | ATR14%: 9.86%
- MA20 gap: -7.29% | MA50 gap: -9.47% | MA200 gap: 76.31%
- vol_ratio(Volume/Vol20): 0.334133 | gap_open: 2.64%
- RS vs SILJ gap: 1.50% / slope_proxy: 0.043523
- RS vs GDXJ gap: 1.19% / slope_proxy: 0.007668
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
