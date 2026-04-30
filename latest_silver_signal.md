# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-29**
- 실행시간(UTC): **2026-04-30 03:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -43.0 bp / latest 2.85
- IG OAS 4주 변화: -9.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.92
- VIX: 17.83
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -3.69% / slope_proxy: 0.015199
- GDXJ/GLD gap: -5.43% / slope_proxy: -0.00371

## VZLA (Vizsla Silver)
- close: 3.4 | RSI14: 48.114754 | ATR14%: 5.74%
- MA20 gap: 0.94% | MA50 gap: -4.76% | MA200 gap: -19.18%
- vol_ratio(Volume/Vol20): 0.996473 | gap_open: 0.88%
- RS vs SILJ gap: 5.51% / slope_proxy: -0.023353
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
- close: 7.73 | RSI14: 40.224766 | ATR14%: 8.47%
- MA20 gap: -8.22% | MA50 gap: -15.87% | MA200 gap: -1.12%
- vol_ratio(Volume/Vol20): 1.403874 | gap_open: 1.65%
- SilverMarginGate: SI=72.745003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.56% / slope_proxy: -0.030942
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
- close: 34.209999 | RSI14: 41.406666 | ATR14%: 10.09%
- MA20 gap: -11.30% | MA50 gap: -13.54% | MA200 gap: 67.19%
- vol_ratio(Volume/Vol20): 1.00229 | gap_open: 1.32%
- RS vs SILJ gap: 0.29% / slope_proxy: 0.040123
- RS vs GDXJ gap: -0.31% / slope_proxy: 0.006665
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
