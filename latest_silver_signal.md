# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-28**
- 실행시간(UTC): **2026-10-29 03:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 10.0 bp / latest 3.18
- IG OAS 4주 변화: 4.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: -27.0 bp / latest 2.64
- VIX: 17.52
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -1.17% / slope_proxy: 0.006763
- GDXJ/GLD gap: -6.79% / slope_proxy: 0.008865

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 42.811236 | ATR14%: 5.44%
- MA20 gap: -2.88% | MA50 gap: -12.58% | MA200 gap: -13.62%
- vol_ratio(Volume/Vol20): 1.099776 | gap_open: 0.92%
- RS vs SILJ gap: 2.32% / slope_proxy: 0.00057
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
- close: 7.5 | RSI14: 40.127844 | ATR14%: 6.65%
- MA20 gap: -8.74% | MA50 gap: -16.25% | MA200 gap: -15.21%
- vol_ratio(Volume/Vol20): 0.717675 | gap_open: 0.27%
- SilverMarginGate: SI=53.689999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.39% / slope_proxy: 0.019901
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
- close: 17.440001 | RSI14: 45.845078 | ATR14%: 6.83%
- MA20 gap: -0.21% | MA50 gap: -15.29% | MA200 gap: -42.29%
- vol_ratio(Volume/Vol20): 1.197667 | gap_open: 0.00%
- RS vs SILJ gap: -4.63% / slope_proxy: -0.04831
- RS vs GDXJ gap: -7.85% / slope_proxy: -0.016538
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
