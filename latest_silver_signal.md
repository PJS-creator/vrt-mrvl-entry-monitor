# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-30**
- 실행시간(UTC): **2026-10-30 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 2.0 bp / latest 3.26
- IG OAS 4주 변화: 3.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: -26.0 bp / latest 2.67
- VIX: 17.2
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: 0.29% / slope_proxy: 0.006283
- GDXJ/GLD gap: -10.69% / slope_proxy: 0.007265

## VZLA (Vizsla Silver)
- close: 3.1599 | RSI14: 39.74458 | ATR14%: 5.74%
- MA20 gap: -4.56% | MA50 gap: -14.66% | MA200 gap: -15.68%
- vol_ratio(Volume/Vol20): 0.264798 | gap_open: 4.26%
- RS vs SILJ gap: 6.62% / slope_proxy: 0.000444
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 6.88 | RSI14: 34.191515 | ATR14%: 7.23%
- MA20 gap: -14.52% | MA50 gap: -22.27% | MA200 gap: -21.86%
- vol_ratio(Volume/Vol20): 0.4004 | gap_open: 5.80%
- SilverMarginGate: SI=49.715 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.68% / slope_proxy: 0.018234
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 16.575001 | RSI14: 41.480222 | ATR14%: 7.28%
- MA20 gap: -4.12% | MA50 gap: -17.88% | MA200 gap: -44.84%
- vol_ratio(Volume/Vol20): 0.293578 | gap_open: 6.83%
- RS vs SILJ gap: -1.68% / slope_proxy: -0.04798
- RS vs GDXJ gap: -4.05% / slope_proxy: -0.016421
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
