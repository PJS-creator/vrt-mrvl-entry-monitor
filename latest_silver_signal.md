# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-18**
- 실행시간(UTC): **2026-05-19 03:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.8
- IG OAS 4주 변화: -5.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 20.0 bp / latest 2.1
- VIX: 18.43
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -5.44% / slope_proxy: -0.000906
- GDXJ/GLD gap: -3.53% / slope_proxy: -0.00363

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 46.458854 | ATR14%: 6.53%
- MA20 gap: -1.96% | MA50 gap: -0.55% | MA200 gap: -19.10%
- vol_ratio(Volume/Vol20): 0.714351 | gap_open: 1.14%
- RS vs SILJ gap: 3.62% / slope_proxy: -0.008415
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
- close: 8.56 | RSI14: 47.30804 | ATR14%: 8.10%
- MA20 gap: -1.31% | MA50 gap: -0.04% | MA200 gap: 5.16%
- vol_ratio(Volume/Vol20): 0.809172 | gap_open: 1.21%
- SilverMarginGate: SI=76.705002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 2.21% / slope_proxy: -0.021944
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
- close: 34.830002 | RSI14: 43.045632 | ATR14%: 10.63%
- MA20 gap: -9.58% | MA50 gap: -7.93% | MA200 gap: 53.06%
- vol_ratio(Volume/Vol20): 0.895754 | gap_open: 0.95%
- RS vs SILJ gap: -4.49% / slope_proxy: 0.027265
- RS vs GDXJ gap: -3.02% / slope_proxy: 0.006597
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
