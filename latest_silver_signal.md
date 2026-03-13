# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-12**
- 실행시간(UTC): **2026-03-13 03:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 25.0 bp / latest 3.09
- IG OAS 4주 변화: 11.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: -1.0 bp / latest 1.85
- VIX: 24.23
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -0.93% / slope_proxy: -0.003551
- GDXJ/GLD gap: -4.54% / slope_proxy: 0.011446

## VZLA (Vizsla Silver)
- close: 3.88 | RSI14: 39.773066 | ATR14%: 8.03%
- MA20 gap: -2.70% | MA50 gap: -21.63% | MA200 gap: -7.13%
- vol_ratio(Volume/Vol20): 0.482277 | gap_open: 0.98%
- RS vs SILJ gap: -24.89% / slope_proxy: -0.028697
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
- close: 9.86 | RSI14: 41.960445 | ATR14%: 10.09%
- MA20 gap: -8.53% | MA50 gap: -14.00% | MA200 gap: 42.27%
- vol_ratio(Volume/Vol20): 0.663391 | gap_open: 0.00%
- SilverMarginGate: SI=84.82 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.96% / slope_proxy: 0.001441
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
- close: 40.119999 | RSI14: 47.679065 | ATR14%: 13.81%
- MA20 gap: -7.12% | MA50 gap: 2.31% | MA200 gap: 168.44%
- vol_ratio(Volume/Vol20): 0.480076 | gap_open: 0.40%
- RS vs SILJ gap: 12.95% / slope_proxy: 0.250437
- RS vs GDXJ gap: 13.14% / slope_proxy: 0.065774
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
