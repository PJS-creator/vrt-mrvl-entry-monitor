# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-12**
- 실행시간(UTC): **2026-08-12 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.72
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 7.0 bp / latest 2.43
- VIX: 15.28
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 10.56% / slope_proxy: 0.012862
- GDXJ/GLD gap: 9.99% / slope_proxy: -0.00507

## VZLA (Vizsla Silver)
- close: 3.8509 | RSI14: 65.541445 | ATR14%: 4.97%
- MA20 gap: 14.95% | MA50 gap: 13.84% | MA200 gap: -5.78%
- vol_ratio(Volume/Vol20): 0.207997 | gap_open: 1.29%
- RS vs SILJ gap: -0.24% / slope_proxy: 0.005977
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
- close: 9.03 | RSI14: 74.488056 | ATR14%: 5.63%
- MA20 gap: 30.13% | MA50 gap: 31.33% | MA200 gap: 6.44%
- vol_ratio(Volume/Vol20): 0.363373 | gap_open: 4.67%
- SilverMarginGate: SI=66.074997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.66% / slope_proxy: -0.003788
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
- close: 27.870001 | RSI14: 66.775583 | ATR14%: 6.86%
- MA20 gap: 28.87% | MA50 gap: 18.13% | MA200 gap: -1.70%
- vol_ratio(Volume/Vol20): 0.395162 | gap_open: 8.72%
- RS vs SILJ gap: -1.69% / slope_proxy: -0.142196
- RS vs GDXJ gap: -3.42% / slope_proxy: -0.036007
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
