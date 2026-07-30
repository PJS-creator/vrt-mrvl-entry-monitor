# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-30**
- 실행시간(UTC): **2026-07-30 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 13.0 bp / latest 2.87
- IG OAS 4주 변화: 5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.41
- VIX: 18.21
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 1.08% / slope_proxy: 0.007457
- GDXJ/GLD gap: -4.64% / slope_proxy: -0.008741

## VZLA (Vizsla Silver)
- close: 3.1809 | RSI14: 47.12475 | ATR14%: 5.97%
- MA20 gap: -0.16% | MA50 gap: -5.94% | MA200 gap: -22.96%
- vol_ratio(Volume/Vol20): 0.157562 | gap_open: 2.24%
- RS vs SILJ gap: 5.34% / slope_proxy: 0.00609
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
- close: 6.47 | RSI14: 48.489883 | ATR14%: 6.60%
- MA20 gap: 1.19% | MA50 gap: -6.41% | MA200 gap: -23.29%
- vol_ratio(Volume/Vol20): 0.187738 | gap_open: 0.63%
- SilverMarginGate: SI=58.450001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.32% / slope_proxy: -0.005167
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 19.665001 | RSI14: 40.529581 | ATR14%: 8.84%
- MA20 gap: -5.16% | MA50 gap: -21.40% | MA200 gap: -29.03%
- vol_ratio(Volume/Vol20): 0.313633 | gap_open: 4.12%
- RS vs SILJ gap: -17.48% / slope_proxy: -0.140956
- RS vs GDXJ gap: -20.12% / slope_proxy: -0.033185
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
