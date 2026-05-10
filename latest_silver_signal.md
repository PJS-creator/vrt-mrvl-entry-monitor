# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-08**
- 실행시간(UTC): **2026-05-10 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.79
- IG OAS 4주 변화: -4.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 1.0 bp / latest 1.96
- VIX: 17.08
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -3.78% / slope_proxy: 0.008104
- GDXJ/GLD gap: 1.29% / slope_proxy: -0.004148

## VZLA (Vizsla Silver)
- close: 3.56 | RSI14: 54.830144 | ATR14%: 5.82%
- MA20 gap: 4.23% | MA50 gap: 1.78% | MA200 gap: -15.46%
- vol_ratio(Volume/Vol20): 0.749913 | gap_open: 1.75%
- RS vs SILJ gap: 0.61% / slope_proxy: -0.015845
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
- close: 9.03 | RSI14: 56.209296 | ATR14%: 7.18%
- MA20 gap: 5.80% | MA50 gap: 3.14% | MA200 gap: 13.35%
- vol_ratio(Volume/Vol20): 0.84927 | gap_open: 1.93%
- SilverMarginGate: SI=80.394997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 0.26% / slope_proxy: -0.029057
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
- close: 38.439999 | RSI14: 50.892541 | ATR14%: 8.90%
- MA20 gap: -1.19% | MA50 gap: -0.45% | MA200 gap: 77.59%
- vol_ratio(Volume/Vol20): 0.812452 | gap_open: 1.93%
- RS vs SILJ gap: -0.78% / slope_proxy: 0.031637
- RS vs GDXJ gap: -0.31% / slope_proxy: 0.004714
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
