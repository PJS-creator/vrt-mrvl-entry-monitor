# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-19**
- 실행시간(UTC): **2026-10-19 15:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 63.0 bp / latest 3.31
- IG OAS 4주 변화: 8.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: 17.0 bp / latest 2.78
- VIX: 19.99
- NFCI: -0.499

### Leadership ratios
- SILJ/SLV gap: -2.08% / slope_proxy: 0.007277
- GDXJ/GLD gap: -4.14% / slope_proxy: 0.011619

## VZLA (Vizsla Silver)
- close: 3.195 | RSI14: 34.493152 | ATR14%: 5.53%
- MA20 gap: -11.64% | MA50 gap: -16.00% | MA200 gap: -17.26%
- vol_ratio(Volume/Vol20): 0.170758 | gap_open: 1.23%
- RS vs SILJ gap: -3.26% / slope_proxy: 0.001872
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
- close: 8.4 | RSI14: 45.301734 | ATR14%: 6.20%
- MA20 gap: -4.26% | MA50 gap: -8.06% | MA200 gap: -6.06%
- vol_ratio(Volume/Vol20): 0.172024 | gap_open: 0.48%
- SilverMarginGate: SI=57.27 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.11% / slope_proxy: 0.022514
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
- close: 17.084999 | RSI14: 37.521975 | ATR14%: 7.23%
- MA20 gap: -9.86% | MA50 gap: -22.41% | MA200 gap: -44.23%
- vol_ratio(Volume/Vol20): 0.227144 | gap_open: 0.00%
- RS vs SILJ gap: -12.01% / slope_proxy: -0.051409
- RS vs GDXJ gap: -15.87% / slope_proxy: -0.017674
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
