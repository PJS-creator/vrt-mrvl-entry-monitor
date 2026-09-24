# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-24**
- 실행시간(UTC): **2026-09-24 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.73
- IG OAS 4주 변화: -3.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 31.0 bp / latest 2.63
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 0.97% / slope_proxy: 0.020698
- GDXJ/GLD gap: 5.77% / slope_proxy: 0.014368

## VZLA (Vizsla Silver)
- close: 3.94 | RSI14: 51.438311 | ATR14%: 5.02%
- MA20 gap: -1.41% | MA50 gap: 6.42% | MA200 gap: -2.07%
- vol_ratio(Volume/Vol20): 0.196745 | gap_open: 0.99%
- RS vs SILJ gap: 7.03% / slope_proxy: 0.00064
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
- close: 8.665 | RSI14: 45.814994 | ATR14%: 7.00%
- MA20 gap: -8.29% | MA50 gap: 3.24% | MA200 gap: -3.70%
- vol_ratio(Volume/Vol20): 0.251221 | gap_open: 2.25%
- SilverMarginGate: SI=63.790001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.16% / slope_proxy: 0.017663
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
- close: 20.459999 | RSI14: 40.962052 | ATR14%: 7.48%
- MA20 gap: -7.90% | MA50 gap: -10.34% | MA200 gap: -32.98%
- vol_ratio(Volume/Vol20): 0.162862 | gap_open: 1.55%
- RS vs SILJ gap: -11.77% / slope_proxy: -0.077568
- RS vs GDXJ gap: -14.87% / slope_proxy: -0.024352
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
