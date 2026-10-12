# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-12**
- 실행시간(UTC): **2026-10-12 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 45.0 bp / latest 3.15
- IG OAS 4주 변화: 2.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 32.0 bp / latest 2.87
- VIX: 14.84
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -1.17% / slope_proxy: 0.007972
- GDXJ/GLD gap: -0.25% / slope_proxy: 0.012598

## VZLA (Vizsla Silver)
- close: 3.49 | RSI14: 39.383894 | ATR14%: 5.16%
- MA20 gap: -7.70% | MA50 gap: -8.83% | MA200 gap: -10.99%
- vol_ratio(Volume/Vol20): 0.070408 | gap_open: 0.85%
- RS vs SILJ gap: -0.82% / slope_proxy: 0.00278
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
- close: 8.96 | RSI14: 49.918709 | ATR14%: 6.13%
- MA20 gap: 0.40% | MA50 gap: -1.24% | MA200 gap: -0.33%
- vol_ratio(Volume/Vol20): 0.115921 | gap_open: 0.99%
- SilverMarginGate: SI=60.630001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.57% / slope_proxy: 0.020735
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

## HYMC (Hycroft Mining)
- close: 18.360001 | RSI14: 39.33506 | ATR14%: 6.89%
- MA20 gap: -7.69% | MA50 gap: -19.00% | MA200 gap: -40.40%
- vol_ratio(Volume/Vol20): 0.173328 | gap_open: 2.08%
- RS vs SILJ gap: -12.44% / slope_proxy: -0.054388
- RS vs GDXJ gap: -14.87% / slope_proxy: -0.018318
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
