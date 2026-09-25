# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-25**
- 실행시간(UTC): **2026-09-25 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 17.0 bp / latest 2.8
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 42.0 bp / latest 2.76
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 0.67% / slope_proxy: 0.019031
- GDXJ/GLD gap: 6.01% / slope_proxy: 0.014762

## VZLA (Vizsla Silver)
- close: 3.935 | RSI14: 50.201708 | ATR14%: 5.26%
- MA20 gap: -1.61% | MA50 gap: 5.17% | MA200 gap: -1.98%
- vol_ratio(Volume/Vol20): 0.346848 | gap_open: 0.76%
- RS vs SILJ gap: 5.34% / slope_proxy: 0.001228
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
- close: 9.07 | RSI14: 49.642352 | ATR14%: 6.63%
- MA20 gap: -3.60% | MA50 gap: 6.41% | MA200 gap: 0.67%
- vol_ratio(Volume/Vol20): 0.121299 | gap_open: 1.01%
- SilverMarginGate: SI=64.580002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.01% / slope_proxy: 0.018592
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
- close: 21.2901 | RSI14: 45.395145 | ATR14%: 7.42%
- MA20 gap: -2.63% | MA50 gap: -7.12% | MA200 gap: -30.50%
- vol_ratio(Volume/Vol20): 0.177706 | gap_open: 0.05%
- RS vs SILJ gap: -8.69% / slope_proxy: -0.073035
- RS vs GDXJ gap: -11.84% / slope_proxy: -0.023091
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
