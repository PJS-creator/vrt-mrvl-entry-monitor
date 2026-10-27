# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-27**
- 실행시간(UTC): **2026-10-27 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 45.0 bp / latest 3.38
- IG OAS 4주 변화: 10.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -17.0 bp / latest 2.66
- VIX: 18.39
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -3.55% / slope_proxy: 0.006989
- GDXJ/GLD gap: -8.30% / slope_proxy: 0.009315

## VZLA (Vizsla Silver)
- close: 3.2099 | RSI14: 40.723231 | ATR14%: 5.55%
- MA20 gap: -5.05% | MA50 gap: -14.04% | MA200 gap: -15.23%
- vol_ratio(Volume/Vol20): 0.181215 | gap_open: 0.98%
- RS vs SILJ gap: 3.14% / slope_proxy: 0.000804
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
- close: 7.32 | RSI14: 37.475341 | ATR14%: 6.88%
- MA20 gap: -11.54% | MA50 gap: -18.38% | MA200 gap: -17.42%
- vol_ratio(Volume/Vol20): 0.277798 | gap_open: 0.43%
- SilverMarginGate: SI=54.299999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.33% / slope_proxy: 0.020544
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
- close: 16.09 | RSI14: 37.214192 | ATR14%: 7.09%
- MA20 gap: -8.14% | MA50 gap: -22.30% | MA200 gap: -46.89%
- vol_ratio(Volume/Vol20): 0.329596 | gap_open: 0.39%
- RS vs SILJ gap: -10.20% / slope_proxy: -0.048942
- RS vs GDXJ gap: -13.50% / slope_proxy: -0.016636
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
