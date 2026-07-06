# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-06**
- 실행시간(UTC): **2026-07-06 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.75
- IG OAS 4주 변화: 1.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 14.0 bp / latest 2.25
- VIX: 15.81
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 6.30% / slope_proxy: 0.007482
- GDXJ/GLD gap: -2.14% / slope_proxy: -0.00193

## VZLA (Vizsla Silver)
- close: 3.3201 | RSI14: 45.818139 | ATR14%: 6.24%
- MA20 gap: -1.98% | MA50 gap: -5.14% | MA200 gap: -21.45%
- vol_ratio(Volume/Vol20): 0.166953 | gap_open: 2.10%
- RS vs SILJ gap: 4.80% / slope_proxy: 0.004895
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
- close: 6.76 | RSI14: 44.730261 | ATR14%: 7.39%
- MA20 gap: 0.30% | MA50 gap: -12.71% | MA200 gap: -20.61%
- vol_ratio(Volume/Vol20): 0.229845 | gap_open: 3.74%
- SilverMarginGate: SI=62.105 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.33% / slope_proxy: -0.007656
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
- close: 23.530001 | RSI14: 38.714247 | ATR14%: 9.28%
- MA20 gap: -3.97% | MA50 gap: -25.25% | MA200 gap: -11.06%
- vol_ratio(Volume/Vol20): 0.123579 | gap_open: 1.40%
- RS vs SILJ gap: -20.57% / slope_proxy: -0.090082
- RS vs GDXJ gap: -20.25% / slope_proxy: -0.019724
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
