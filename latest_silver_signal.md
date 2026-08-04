# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-04**
- 실행시간(UTC): **2026-08-04 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 11.0 bp / latest 2.85
- IG OAS 4주 변화: 4.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.47
- VIX: 15.86
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 5.12% / slope_proxy: 0.00874
- GDXJ/GLD gap: 0.42% / slope_proxy: -0.008372

## VZLA (Vizsla Silver)
- close: 3.355 | RSI14: 53.710156 | ATR14%: 5.61%
- MA20 gap: 5.11% | MA50 gap: -0.66% | MA200 gap: -18.28%
- vol_ratio(Volume/Vol20): 0.508489 | gap_open: 2.76%
- RS vs SILJ gap: 3.42% / slope_proxy: 0.006076
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
- close: 7.03 | RSI14: 56.626729 | ATR14%: 6.38%
- MA20 gap: 9.38% | MA50 gap: 2.96% | MA200 gap: -16.60%
- vol_ratio(Volume/Vol20): 0.400523 | gap_open: 2.97%
- SilverMarginGate: SI=59.724998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.38% / slope_proxy: -0.005391
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
- close: 21.535 | RSI14: 49.388904 | ATR14%: 7.84%
- MA20 gap: 5.57% | MA50 gap: -11.20% | MA200 gap: -22.81%
- vol_ratio(Volume/Vol20): 0.241753 | gap_open: 3.69%
- RS vs SILJ gap: -13.34% / slope_proxy: -0.146323
- RS vs GDXJ gap: -14.58% / slope_proxy: -0.035023
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
