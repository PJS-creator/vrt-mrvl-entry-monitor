# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-18**
- 실행시간(UTC): **2026-03-19 03:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 28.0 bp / latest 3.22
- IG OAS 4주 변화: 12.0 bp / latest 0.92
- 10Y Real Yield 4주 변화: 4.0 bp / latest 1.83
- VIX: 22.37
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -2.91% / slope_proxy: -0.00515
- GDXJ/GLD gap: -11.17% / slope_proxy: 0.008237

## VZLA (Vizsla Silver)
- close: 3.36 | RSI14: 31.656454 | ATR14%: 8.66%
- MA20 gap: -14.99% | MA50 gap: -29.84% | MA200 gap: -19.84%
- vol_ratio(Volume/Vol20): 0.935711 | gap_open: 3.07%
- RS vs SILJ gap: -23.29% / slope_proxy: -0.027542
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.82 | RSI14: 31.431267 | ATR14%: 11.99%
- MA20 gap: -26.21% | MA50 gap: -31.26% | MA200 gap: 10.71%
- vol_ratio(Volume/Vol20): 1.233198 | gap_open: 1.73%
- SilverMarginGate: SI=76.305 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -19.61% / slope_proxy: -0.004909
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 36.240002 | RSI14: 43.45413 | ATR14%: 13.99%
- MA20 gap: -17.14% | MA50 gap: -10.06% | MA200 gap: 131.50%
- vol_ratio(Volume/Vol20): 1.039052 | gap_open: 6.33%
- RS vs SILJ gap: 11.31% / slope_proxy: 0.2571
- RS vs GDXJ gap: 10.43% / slope_proxy: 0.06751
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
