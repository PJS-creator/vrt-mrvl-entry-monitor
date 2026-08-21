# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-20**
- 실행시간(UTC): **2026-08-21 03:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.73
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -4.0 bp / latest 2.35
- VIX: 14.89
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 8.52% / slope_proxy: 0.019726
- GDXJ/GLD gap: 14.45% / slope_proxy: 0.00048

## VZLA (Vizsla Silver)
- close: 3.87 | RSI14: 61.727052 | ATR14%: 4.88%
- MA20 gap: 9.29% | MA50 gap: 14.24% | MA200 gap: -5.03%
- vol_ratio(Volume/Vol20): 0.997254 | gap_open: 1.54%
- RS vs SILJ gap: -4.14% / slope_proxy: 0.004387
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

## SCZM (Santacruz Silver)
- close: 9.76 | RSI14: 72.639166 | ATR14%: 5.65%
- MA20 gap: 25.93% | MA50 gap: 38.10% | MA200 gap: 13.75%
- vol_ratio(Volume/Vol20): 1.59177 | gap_open: 0.94%
- SilverMarginGate: SI=69.074997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 16.71% / slope_proxy: -0.000138
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
- close: 26.139999 | RSI14: 55.157234 | ATR14%: 7.55%
- MA20 gap: 9.42% | MA50 gap: 12.85% | MA200 gap: -9.91%
- vol_ratio(Volume/Vol20): 1.68024 | gap_open: 2.33%
- RS vs SILJ gap: -8.05% / slope_proxy: -0.119586
- RS vs GDXJ gap: -12.47% / slope_proxy: -0.03216
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
