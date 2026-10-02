# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-02**
- 실행시간(UTC): **2026-10-02 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 59.0 bp / latest 3.24
- IG OAS 4주 변화: 5.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 48.0 bp / latest 2.93
- VIX: 16.39
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: -0.40% / slope_proxy: 0.013583
- GDXJ/GLD gap: 1.81% / slope_proxy: 0.013164

## VZLA (Vizsla Silver)
- close: 3.69 | RSI14: 42.342458 | ATR14%: 5.21%
- MA20 gap: -6.18% | MA50 gap: -2.80% | MA200 gap: -7.24%
- vol_ratio(Volume/Vol20): 0.437677 | gap_open: 2.13%
- RS vs SILJ gap: 4.06% / slope_proxy: 0.00255
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
- close: 8.81 | RSI14: 47.228584 | ATR14%: 6.70%
- MA20 gap: -4.37% | MA50 gap: 0.26% | MA200 gap: -2.01%
- vol_ratio(Volume/Vol20): 0.165497 | gap_open: 2.30%
- SilverMarginGate: SI=61.404999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.33% / slope_proxy: 0.019236
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
- close: 18.98 | RSI14: 37.963998 | ATR14%: 7.48%
- MA20 gap: -9.19% | MA50 gap: -16.86% | MA200 gap: -38.39%
- vol_ratio(Volume/Vol20): 0.189311 | gap_open: 2.43%
- RS vs SILJ gap: -11.91% / slope_proxy: -0.063205
- RS vs GDXJ gap: -14.61% / slope_proxy: -0.020426
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
