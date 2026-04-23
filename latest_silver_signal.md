# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-22**
- 실행시간(UTC): **2026-04-23 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.85
- IG OAS 4주 변화: -7.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -14.0 bp / latest 1.92
- VIX: 19.5
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.37% / slope_proxy: 0.012332
- GDXJ/GLD gap: 0.02% / slope_proxy: -0.003966

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 49.731008 | ATR14%: 5.75%
- MA20 gap: 4.44% | MA50 gap: -4.21% | MA200 gap: -17.59%
- vol_ratio(Volume/Vol20): 0.720422 | gap_open: 2.40%
- RS vs SILJ gap: -6.92% / slope_proxy: -0.026268
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
- close: 9.02 | RSI14: 52.524939 | ATR14%: 7.94%
- MA20 gap: 8.30% | MA50 gap: -4.06% | MA200 gap: 17.16%
- vol_ratio(Volume/Vol20): 0.8001 | gap_open: 4.00%
- SilverMarginGate: SI=76.224998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.91% / slope_proxy: -0.028476
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
- close: 40.544998 | RSI14: 53.280021 | ATR14%: 9.25%
- MA20 gap: 7.85% | MA50 gap: 2.94% | MA200 gap: 106.51%
- vol_ratio(Volume/Vol20): 0.655582 | gap_open: 4.34%
- RS vs SILJ gap: 6.73% / slope_proxy: 0.06871
- RS vs GDXJ gap: 6.21% / slope_proxy: 0.015134
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
