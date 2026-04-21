# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-21**
- 실행시간(UTC): **2026-04-21 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -32.0 bp / latest 2.87
- IG OAS 4주 변화: -7.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -11.0 bp / latest 1.9
- VIX: 18.87
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.23% / slope_proxy: 0.011426
- GDXJ/GLD gap: -0.18% / slope_proxy: -0.003831

## VZLA (Vizsla Silver)
- close: 3.39 | RSI14: 46.407605 | ATR14%: 5.77%
- MA20 gap: 2.74% | MA50 gap: -6.50% | MA200 gap: -19.22%
- vol_ratio(Volume/Vol20): 0.315511 | gap_open: 1.14%
- RS vs SILJ gap: -8.50% / slope_proxy: -0.026659
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
- close: 8.755 | RSI14: 49.800544 | ATR14%: 8.05%
- MA20 gap: 5.66% | MA50 gap: -7.50% | MA200 gap: 14.11%
- vol_ratio(Volume/Vol20): 0.250219 | gap_open: 1.10%
- SilverMarginGate: SI=77.040001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.23% / slope_proxy: -0.027403
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
- close: 38.856998 | RSI14: 50.28084 | ATR14%: 9.90%
- MA20 gap: 4.46% | MA50 gap: -1.22% | MA200 gap: 99.84%
- vol_ratio(Volume/Vol20): 0.602452 | gap_open: 1.30%
- RS vs SILJ gap: 3.57% / slope_proxy: 0.073503
- RS vs GDXJ gap: 1.88% / slope_proxy: 0.016829
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
