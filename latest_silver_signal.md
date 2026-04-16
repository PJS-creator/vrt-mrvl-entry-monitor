# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-16**
- 실행시간(UTC): **2026-04-16 15:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.85
- IG OAS 4주 변화: -11.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.89
- VIX: 18.17
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 0.60% / slope_proxy: 0.008622
- GDXJ/GLD gap: 1.76% / slope_proxy: -0.004493

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 47.812159 | ATR14%: 5.88%
- MA20 gap: 5.43% | MA50 gap: -7.41% | MA200 gap: -18.36%
- vol_ratio(Volume/Vol20): 0.352524 | gap_open: 0.88%
- RS vs SILJ gap: -12.60% / slope_proxy: -0.027575
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
- close: 8.81 | RSI14: 51.170856 | ATR14%: 8.37%
- MA20 gap: 9.61% | MA50 gap: -8.21% | MA200 gap: 16.17%
- vol_ratio(Volume/Vol20): 0.279954 | gap_open: 0.91%
- SilverMarginGate: SI=78.510002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.70% / slope_proxy: -0.024511
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
- close: 40.169998 | RSI14: 55.012347 | ATR14%: 9.33%
- MA20 gap: 13.10% | MA50 gap: 3.16% | MA200 gap: 113.07%
- vol_ratio(Volume/Vol20): 0.212702 | gap_open: 2.50%
- RS vs SILJ gap: 4.47% / slope_proxy: 0.087341
- RS vs GDXJ gap: 1.85% / slope_proxy: 0.021621
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
