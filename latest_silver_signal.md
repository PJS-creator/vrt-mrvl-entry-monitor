# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-29**
- 실행시간(UTC): **2026-10-30 02:07:43**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 2.0 bp / latest 3.14
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: -26.0 bp / latest 2.67
- VIX: 16.91
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -0.24% / slope_proxy: 0.006436
- GDXJ/GLD gap: -8.65% / slope_proxy: 0.008105

## VZLA (Vizsla Silver)
- close: 3.29 | RSI14: 44.176804 | ATR14%: 5.47%
- MA20 gap: -1.30% | MA50 gap: -11.49% | MA200 gap: -12.53%
- vol_ratio(Volume/Vol20): 0.850602 | gap_open: 3.07%
- RS vs SILJ gap: 6.01% / slope_proxy: 0.000422
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
- close: 7.24 | RSI14: 37.513334 | ATR14%: 6.82%
- MA20 gap: -11.11% | MA50 gap: -18.73% | MA200 gap: -17.97%
- vol_ratio(Volume/Vol20): 0.59911 | gap_open: 3.47%
- SilverMarginGate: SI=51.580002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.26% / slope_proxy: 0.019071
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
- close: 17.27 | RSI14: 44.969222 | ATR14%: 6.90%
- MA20 gap: -0.71% | MA50 gap: -15.24% | MA200 gap: -42.70%
- vol_ratio(Volume/Vol20): 0.869455 | gap_open: 4.01%
- RS vs SILJ gap: -2.60% / slope_proxy: -0.048432
- RS vs GDXJ gap: -5.15% / slope_proxy: -0.016594
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
