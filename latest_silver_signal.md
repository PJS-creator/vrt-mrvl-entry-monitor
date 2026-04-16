# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-15**
- 실행시간(UTC): **2026-04-16 03:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -38.0 bp / latest 2.84
- IG OAS 4주 변화: -11.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.89
- VIX: 18.36
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.63% / slope_proxy: 0.007546
- GDXJ/GLD gap: 1.17% / slope_proxy: -0.004536

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 47.812159 | ATR14%: 6.11%
- MA20 gap: 5.52% | MA50 gap: -8.31% | MA200 gap: -18.31%
- vol_ratio(Volume/Vol20): 1.395911 | gap_open: 0.29%
- RS vs SILJ gap: -13.12% / slope_proxy: -0.027505
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.82 | RSI14: 51.271154 | ATR14%: 8.55%
- MA20 gap: 10.42% | MA50 gap: -8.85% | MA200 gap: 16.75%
- vol_ratio(Volume/Vol20): 0.84955 | gap_open: 0.44%
- SilverMarginGate: SI=80.43 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.56% / slope_proxy: -0.023921
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 40.330002 | RSI14: 55.359877 | ATR14%: 9.61%
- MA20 gap: 14.18% | MA50 gap: 3.47% | MA200 gap: 116.04%
- vol_ratio(Volume/Vol20): 0.463381 | gap_open: 0.96%
- RS vs SILJ gap: 5.45% / slope_proxy: 0.09776
- RS vs GDXJ gap: 2.64% / slope_proxy: 0.024605
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
