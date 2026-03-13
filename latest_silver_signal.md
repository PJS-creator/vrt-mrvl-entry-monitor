# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-13**
- 실행시간(UTC): **2026-03-13 15:01:21**

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
- VIX: 27.29
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -1.71% / slope_proxy: -0.003796
- GDXJ/GLD gap: -7.89% / slope_proxy: 0.010808

## VZLA (Vizsla Silver)
- close: 3.63 | RSI14: 35.480119 | ATR14%: 8.48%
- MA20 gap: -8.97% | MA50 gap: -26.08% | MA200 gap: -13.20%
- vol_ratio(Volume/Vol20): 0.176845 | gap_open: 0.77%
- RS vs SILJ gap: -25.50% / slope_proxy: -0.028457
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
- close: 9.415 | RSI14: 39.426732 | ATR14%: 10.18%
- MA20 gap: -12.46% | MA50 gap: -17.76% | MA200 gap: 35.12%
- vol_ratio(Volume/Vol20): 0.613145 | gap_open: 1.62%
- SilverMarginGate: SI=81.785004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.38% / slope_proxy: -0.000537
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
- close: 37.330002 | RSI14: 44.532507 | ATR14%: 14.48%
- MA20 gap: -14.00% | MA50 gap: -5.47% | MA200 gap: 146.94%
- vol_ratio(Volume/Vol20): 0.26278 | gap_open: 0.09%
- RS vs SILJ gap: 9.31% / slope_proxy: 0.251437
- RS vs GDXJ gap: 8.71% / slope_proxy: 0.066034
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
