# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-18**
- 실행시간(UTC): **2026-11-18 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 3.34
- IG OAS 4주 변화: 3.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.92
- VIX: 25.46
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 1.90% / slope_proxy: 0.003411
- GDXJ/GLD gap: -10.47% / slope_proxy: -0.004231

## VZLA (Vizsla Silver)
- close: 2.98 | RSI14: 40.006438 | ATR14%: 6.43%
- MA20 gap: -5.71% | MA50 gap: -14.13% | MA200 gap: -16.21%
- vol_ratio(Volume/Vol20): 0.251175 | gap_open: 2.69%
- RS vs SILJ gap: 6.51% / slope_proxy: 0.002541
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
- close: 7.11 | RSI14: 45.662822 | ATR14%: 8.16%
- MA20 gap: -1.40% | MA50 gap: -13.05% | MA200 gap: -15.36%
- vol_ratio(Volume/Vol20): 0.399714 | gap_open: 4.86%
- SilverMarginGate: SI=45.150002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.36% / slope_proxy: 0.00562
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
- close: 15.69 | RSI14: 42.020793 | ATR14%: 9.44%
- MA20 gap: -7.36% | MA50 gap: -14.63% | MA200 gap: -44.64%
- vol_ratio(Volume/Vol20): 0.283727 | gap_open: 5.86%
- RS vs SILJ gap: 4.33% / slope_proxy: -0.04674
- RS vs GDXJ gap: 1.58% / slope_proxy: -0.015682
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
