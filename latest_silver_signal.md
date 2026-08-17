# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-17**
- 실행시간(UTC): **2026-08-17 15:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.67
- IG OAS 4주 변화: 1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.39
- VIX: 14.25
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 7.43% / slope_proxy: 0.016722
- GDXJ/GLD gap: 10.59% / slope_proxy: -0.001987

## VZLA (Vizsla Silver)
- close: 3.75 | RSI14: 60.801524 | ATR14%: 4.69%
- MA20 gap: 7.85% | MA50 gap: 11.42% | MA200 gap: -8.11%
- vol_ratio(Volume/Vol20): 0.338115 | gap_open: 0.53%
- RS vs SILJ gap: -2.22% / slope_proxy: 0.005251
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
- close: 8.76 | RSI14: 68.692125 | ATR14%: 5.69%
- MA20 gap: 19.44% | MA50 gap: 26.58% | MA200 gap: 2.72%
- vol_ratio(Volume/Vol20): 0.624995 | gap_open: 0.00%
- SilverMarginGate: SI=66.550003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.54% / slope_proxy: -0.002239
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
- close: 26.385 | RSI14: 59.619773 | ATR14%: 6.67%
- MA20 gap: 14.09% | MA50 gap: 13.96% | MA200 gap: -8.20%
- vol_ratio(Volume/Vol20): 0.331296 | gap_open: 0.89%
- RS vs SILJ gap: -3.87% / slope_proxy: -0.126441
- RS vs GDXJ gap: -7.37% / slope_proxy: -0.033072
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
