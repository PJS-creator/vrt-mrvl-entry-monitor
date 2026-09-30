# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-30**
- 실행시간(UTC): **2026-09-30 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 43.0 bp / latest 3.08
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 46.0 bp / latest 2.9
- VIX: 16.04
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: 1.46% / slope_proxy: 0.016226
- GDXJ/GLD gap: 3.65% / slope_proxy: 0.014134

## VZLA (Vizsla Silver)
- close: 3.8191 | RSI14: 46.571765 | ATR14%: 5.12%
- MA20 gap: -4.01% | MA50 gap: 1.00% | MA200 gap: -4.35%
- vol_ratio(Volume/Vol20): 0.236054 | gap_open: 0.52%
- RS vs SILJ gap: 6.90% / slope_proxy: 0.002051
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
- close: 9.06 | RSI14: 49.454904 | ATR14%: 6.90%
- MA20 gap: -3.39% | MA50 gap: 4.10% | MA200 gap: 0.65%
- vol_ratio(Volume/Vol20): 0.130286 | gap_open: 0.84%
- SilverMarginGate: SI=60.970001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.98% / slope_proxy: 0.019926
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
- close: 19.398399 | RSI14: 39.219216 | ATR14%: 7.88%
- MA20 gap: -9.14% | MA50 gap: -15.38% | MA200 gap: -36.91%
- vol_ratio(Volume/Vol20): 0.152273 | gap_open: 1.29%
- RS vs SILJ gap: -11.57% / slope_proxy: -0.066563
- RS vs GDXJ gap: -14.90% / slope_proxy: -0.021231
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
