# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-03**
- 실행시간(UTC): **2026-08-04 03:00:55**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 9.0 bp / latest 2.84
- IG OAS 4주 변화: 5.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.47
- VIX: 15.99
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 3.70% / slope_proxy: 0.008016
- GDXJ/GLD gap: -1.57% / slope_proxy: -0.008654

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 50.39216 | ATR14%: 5.82%
- MA20 gap: 2.56% | MA50 gap: -3.49% | MA200 gap: -20.74%
- vol_ratio(Volume/Vol20): 0.527109 | gap_open: 0.96%
- RS vs SILJ gap: 4.96% / slope_proxy: 0.006064
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 6.73 | RSI14: 52.44718 | ATR14%: 6.72%
- MA20 gap: 5.25% | MA50 gap: -1.77% | MA200 gap: -20.17%
- vol_ratio(Volume/Vol20): 0.660192 | gap_open: 1.08%
- SilverMarginGate: SI=58.98 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.02% / slope_proxy: -0.005278
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
- close: 20.620001 | RSI14: 45.551575 | ATR14%: 8.31%
- MA20 gap: 1.04% | MA50 gap: -15.79% | MA200 gap: -25.92%
- vol_ratio(Volume/Vol20): 0.823955 | gap_open: 1.64%
- RS vs SILJ gap: -14.18% / slope_proxy: -0.145612
- RS vs GDXJ gap: -16.59% / slope_proxy: -0.034693
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
