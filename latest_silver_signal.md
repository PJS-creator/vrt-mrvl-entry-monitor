# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-31**
- 실행시간(UTC): **2026-03-31 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 43.0 bp / latest 3.46
- IG OAS 4주 변화: 8.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 41.0 bp / latest 2.13
- VIX: 30.61
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -1.81% / slope_proxy: -0.0045
- GDXJ/GLD gap: -6.19% / slope_proxy: -0.00234

## VZLA (Vizsla Silver)
- close: 3.255 | RSI14: 38.896006 | ATR14%: 7.85%
- MA20 gap: -8.02% | MA50 gap: -24.30% | MA200 gap: -22.14%
- vol_ratio(Volume/Vol20): 0.223595 | gap_open: 2.24%
- RS vs SILJ gap: -16.94% / slope_proxy: -0.027221
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.17 | RSI14: 42.515075 | ATR14%: 10.47%
- MA20 gap: -6.55% | MA50 gap: -24.38% | MA200 gap: 12.19%
- vol_ratio(Volume/Vol20): 0.337916 | gap_open: 2.50%
- SilverMarginGate: SI=73.650002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.45% / slope_proxy: -0.019512
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 33.580002 | RSI14: 45.299554 | ATR14%: 13.30%
- MA20 gap: -9.16% | MA50 gap: -16.99% | MA200 gap: 98.40%
- vol_ratio(Volume/Vol20): 0.296586 | gap_open: 3.45%
- RS vs SILJ gap: 1.00% / slope_proxy: 0.18677
- RS vs GDXJ gap: -1.69% / slope_proxy: 0.049025
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
