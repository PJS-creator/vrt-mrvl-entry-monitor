# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-22**
- 실행시간(UTC): **2026-10-23 03:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 54.0 bp / latest 3.27
- IG OAS 4주 변화: 11.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 0.0 bp / latest 2.76
- VIX: 16.68
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.05% / slope_proxy: 0.007284
- GDXJ/GLD gap: -8.34% / slope_proxy: 0.010494

## VZLA (Vizsla Silver)
- close: 3.19 | RSI14: 37.153239 | ATR14%: 5.63%
- MA20 gap: -8.66% | MA50 gap: -15.38% | MA200 gap: -16.61%
- vol_ratio(Volume/Vol20): 1.28736 | gap_open: 3.57%
- RS vs SILJ gap: 3.99% / slope_proxy: 0.001324
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
- close: 7.13 | RSI14: 32.78557 | ATR14%: 7.76%
- MA20 gap: -16.93% | MA50 gap: -21.38% | MA200 gap: -19.98%
- vol_ratio(Volume/Vol20): 1.664324 | gap_open: 5.39%
- SilverMarginGate: SI=54.259998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.08% / slope_proxy: 0.022519
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
- close: 15.76 | RSI14: 33.069107 | ATR14%: 7.85%
- MA20 gap: -13.37% | MA50 gap: -26.24% | MA200 gap: -48.29%
- vol_ratio(Volume/Vol20): 0.882517 | gap_open: 5.08%
- RS vs SILJ gap: -11.73% / slope_proxy: -0.050006
- RS vs GDXJ gap: -15.60% / slope_proxy: -0.017051
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
