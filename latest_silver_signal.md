# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-14**
- 실행시간(UTC): **2026-05-15 03:01:31**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.82
- IG OAS 4주 변화: -4.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.99
- VIX: 17.87
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -2.91% / slope_proxy: 0.001623
- GDXJ/GLD gap: 2.54% / slope_proxy: -0.003193

## VZLA (Vizsla Silver)
- close: 3.76 | RSI14: 59.141154 | ATR14%: 5.77%
- MA20 gap: 7.61% | MA50 gap: 8.61% | MA200 gap: -10.95%
- vol_ratio(Volume/Vol20): 1.205507 | gap_open: 0.00%
- RS vs SILJ gap: 2.55% / slope_proxy: -0.010732
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
- close: 9.7 | RSI14: 59.677438 | ATR14%: 6.95%
- MA20 gap: 11.17% | MA50 gap: 12.55% | MA200 gap: 19.95%
- vol_ratio(Volume/Vol20): 0.60382 | gap_open: 0.80%
- SilverMarginGate: SI=81.779999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.92% / slope_proxy: -0.024459
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
- close: 39.360001 | RSI14: 50.193188 | ATR14%: 9.64%
- MA20 gap: -0.05% | MA50 gap: 3.56% | MA200 gap: 75.45%
- vol_ratio(Volume/Vol20): 1.195524 | gap_open: 1.44%
- RS vs SILJ gap: -2.97% / slope_proxy: 0.032099
- RS vs GDXJ gap: 0.79% / slope_proxy: 0.007033
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
