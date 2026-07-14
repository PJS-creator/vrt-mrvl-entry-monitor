# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-13**
- 실행시간(UTC): **2026-07-14 03:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.69
- IG OAS 4주 변화: 3.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.32
- VIX: 15.03
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 5.28% / slope_proxy: 0.009193
- GDXJ/GLD gap: -5.65% / slope_proxy: -0.003129

## VZLA (Vizsla Silver)
- close: 3.02 | RSI14: 39.592099 | ATR14%: 6.73%
- MA20 gap: -8.83% | MA50 gap: -12.88% | MA200 gap: -28.19%
- vol_ratio(Volume/Vol20): 1.257862 | gap_open: 1.60%
- RS vs SILJ gap: 1.54% / slope_proxy: 0.005095
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
- close: 6.35 | RSI14: 41.667104 | ATR14%: 7.43%
- MA20 gap: -6.22% | MA50 gap: -16.07% | MA200 gap: -25.34%
- vol_ratio(Volume/Vol20): 0.674395 | gap_open: 2.77%
- SilverMarginGate: SI=57.860001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.82% / slope_proxy: -0.004893
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
- close: 20.43 | RSI14: 33.207415 | ATR14%: 9.81%
- MA20 gap: -13.13% | MA50 gap: -31.72% | MA200 gap: -23.85%
- vol_ratio(Volume/Vol20): 0.700475 | gap_open: 1.96%
- RS vs SILJ gap: -23.38% / slope_proxy: -0.101767
- RS vs GDXJ gap: -22.94% / slope_proxy: -0.022159
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
