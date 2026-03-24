# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-24**
- 실행시간(UTC): **2026-03-24 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 24.0 bp / latest 3.19
- IG OAS 4주 변화: 8.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.01
- VIX: 26.15
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: 0.11% / slope_proxy: -0.00657
- GDXJ/GLD gap: -8.11% / slope_proxy: 0.002818

## VZLA (Vizsla Silver)
- close: 3.11 | RSI14: 30.413737 | ATR14%: 9.00%
- MA20 gap: -18.02% | MA50 gap: -32.07% | MA200 gap: -25.75%
- vol_ratio(Volume/Vol20): 0.189915 | gap_open: 2.26%
- RS vs SILJ gap: -22.00% / slope_proxy: -0.027451
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.89 | RSI14: 36.036645 | ATR14%: 11.49%
- MA20 gap: -19.64% | MA50 gap: -29.30% | MA200 gap: 10.17%
- vol_ratio(Volume/Vol20): 0.175089 | gap_open: 1.19%
- SilverMarginGate: SI=69.610001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.39% / slope_proxy: -0.012395
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 33.330002 | RSI14: 42.331063 | ATR14%: 14.14%
- MA20 gap: -19.67% | MA50 gap: -17.92% | MA200 gap: 105.55%
- vol_ratio(Volume/Vol20): 0.177511 | gap_open: 2.77%
- RS vs SILJ gap: 6.04% / slope_proxy: 0.231871
- RS vs GDXJ gap: 5.91% / slope_proxy: 0.06093
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
