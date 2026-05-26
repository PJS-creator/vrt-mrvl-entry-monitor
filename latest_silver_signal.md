# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-26**
- 실행시간(UTC): **2026-05-26 15:01:15**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.74
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.18
- VIX: 16.59
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -2.89% / slope_proxy: -0.010558
- GDXJ/GLD gap: -1.52% / slope_proxy: -0.005441

## VZLA (Vizsla Silver)
- close: 3.585 | RSI14: 53.653742 | ATR14%: 6.05%
- MA20 gap: 2.73% | MA50 gap: 5.91% | MA200 gap: -15.33%
- vol_ratio(Volume/Vol20): 0.417731 | gap_open: 2.67%
- RS vs SILJ gap: 7.35% / slope_proxy: -0.002518
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.14 | RSI14: 44.033995 | ATR14%: 7.52%
- MA20 gap: -5.02% | MA50 gap: -2.88% | MA200 gap: -1.29%
- vol_ratio(Volume/Vol20): 0.368186 | gap_open: 0.50%
- SilverMarginGate: SI=76.690002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.04% / slope_proxy: -0.015178
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
- close: 33.2099 | RSI14: 41.882027 | ATR14%: 9.60%
- MA20 gap: -10.55% | MA50 gap: -10.31% | MA200 gap: 41.33%
- vol_ratio(Volume/Vol20): 0.269183 | gap_open: 3.65%
- RS vs SILJ gap: -8.67% / slope_proxy: 0.024156
- RS vs GDXJ gap: -6.84% / slope_proxy: 0.007333
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
