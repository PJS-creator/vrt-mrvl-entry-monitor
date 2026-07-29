# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-29**
- 실행시간(UTC): **2026-07-29 15:01:35**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 9.0 bp / latest 2.84
- IG OAS 4주 변화: 5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.44
- VIX: 18.21
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: -0.03% / slope_proxy: 0.007095
- GDXJ/GLD gap: -5.38% / slope_proxy: -0.008923

## VZLA (Vizsla Silver)
- close: 3.055 | RSI14: 42.913582 | ATR14%: 6.57%
- MA20 gap: -4.30% | MA50 gap: -9.92% | MA200 gap: -26.24%
- vol_ratio(Volume/Vol20): 0.20988 | gap_open: 5.12%
- RS vs SILJ gap: 5.33% / slope_proxy: 0.006231
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
- close: 6.22 | RSI14: 43.888194 | ATR14%: 6.92%
- MA20 gap: -2.93% | MA50 gap: -11.98% | MA200 gap: -26.33%
- vol_ratio(Volume/Vol20): 0.166972 | gap_open: 1.74%
- SilverMarginGate: SI=57.099998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 0.81% / slope_proxy: -0.005155
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
- close: 18.955 | RSI14: 37.744734 | ATR14%: 9.50%
- MA20 gap: -9.99% | MA50 gap: -26.07% | MA200 gap: -31.29%
- vol_ratio(Volume/Vol20): 0.26346 | gap_open: 2.10%
- RS vs SILJ gap: -18.79% / slope_proxy: -0.134897
- RS vs GDXJ gap: -22.00% / slope_proxy: -0.031095
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
