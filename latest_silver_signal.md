# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-18**
- 실행시간(UTC): **2026-11-18 22:35:44**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 10.0 bp / latest 3.43
- IG OAS 4주 변화: 5.0 bp / latest 0.92
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.89
- VIX: 25.46
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 0.93% / slope_proxy: 0.003328
- GDXJ/GLD gap: -10.42% / slope_proxy: -0.004229

## VZLA (Vizsla Silver)
- close: 2.98 | RSI14: 40.006438 | ATR14%: 6.45%
- MA20 gap: -5.71% | MA50 gap: -14.13% | MA200 gap: -16.21%
- vol_ratio(Volume/Vol20): 2.20364 | gap_open: 2.69%
- RS vs SILJ gap: 8.04% / slope_proxy: 0.002575
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
- close: 6.8 | RSI14: 43.134274 | ATR14%: 8.58%
- MA20 gap: -5.50% | MA50 gap: -16.78% | MA200 gap: -19.03%
- vol_ratio(Volume/Vol20): 1.933086 | gap_open: 4.86%
- SilverMarginGate: SI=44.974998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.23% / slope_proxy: 0.005454
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

## HYMC (Hycroft Mining)
- close: 15.25 | RSI14: 40.490826 | ATR14%: 9.74%
- MA20 gap: -9.84% | MA50 gap: -16.99% | MA200 gap: -46.19%
- vol_ratio(Volume/Vol20): 1.322956 | gap_open: 5.86%
- RS vs SILJ gap: 2.91% / slope_proxy: -0.046911
- RS vs GDXJ gap: -0.14% / slope_proxy: -0.015732
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
