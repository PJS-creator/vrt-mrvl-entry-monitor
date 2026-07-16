# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-16**
- 실행시간(UTC): **2026-07-16 15:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 8.0 bp / latest 2.71
- IG OAS 4주 변화: 5.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.33
- VIX: 15.67
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 5.09% / slope_proxy: 0.008917
- GDXJ/GLD gap: -7.22% / slope_proxy: -0.006159

## VZLA (Vizsla Silver)
- close: 3.075 | RSI14: 42.550055 | ATR14%: 6.46%
- MA20 gap: -5.09% | MA50 gap: -10.92% | MA200 gap: -26.64%
- vol_ratio(Volume/Vol20): 0.290211 | gap_open: 0.94%
- RS vs SILJ gap: 5.26% / slope_proxy: 0.005502
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
- close: 5.9988 | RSI14: 37.890948 | ATR14%: 7.57%
- MA20 gap: -8.96% | MA50 gap: -19.63% | MA200 gap: -29.34%
- vol_ratio(Volume/Vol20): 0.316884 | gap_open: 1.73%
- SilverMarginGate: SI=56.369999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.25% / slope_proxy: -0.005753
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
- close: 19.145 | RSI14: 32.850461 | ATR14%: 10.36%
- MA20 gap: -15.30% | MA50 gap: -33.83% | MA200 gap: -29.21%
- vol_ratio(Volume/Vol20): 0.288907 | gap_open: 3.02%
- RS vs SILJ gap: -24.58% / slope_proxy: -0.113975
- RS vs GDXJ gap: -24.44% / slope_proxy: -0.025079
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
