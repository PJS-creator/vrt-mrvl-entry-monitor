# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-18**
- 실행시간(UTC): **2026-08-19 03:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.7
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 9.0 bp / latest 2.44
- VIX: 15.19
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 6.31% / slope_proxy: 0.017621
- GDXJ/GLD gap: 7.01% / slope_proxy: -0.001279

## VZLA (Vizsla Silver)
- close: 3.57 | RSI14: 53.005229 | ATR14%: 5.04%
- MA20 gap: 2.41% | MA50 gap: 6.00% | MA200 gap: -12.44%
- vol_ratio(Volume/Vol20): 0.760269 | gap_open: 1.92%
- RS vs SILJ gap: -2.41% / slope_proxy: 0.004959
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.37 | RSI14: 61.519272 | ATR14%: 5.89%
- MA20 gap: 12.33% | MA50 gap: 20.67% | MA200 gap: -2.01%
- vol_ratio(Volume/Vol20): 0.809098 | gap_open: 1.37%
- SilverMarginGate: SI=63.174999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.76% / slope_proxy: -0.00156
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
- close: 24.190001 | RSI14: 50.515703 | ATR14%: 7.46%
- MA20 gap: 3.84% | MA50 gap: 4.69% | MA200 gap: -16.08%
- vol_ratio(Volume/Vol20): 1.287067 | gap_open: 4.58%
- RS vs SILJ gap: -7.04% / slope_proxy: -0.124528
- RS vs GDXJ gap: -10.35% / slope_proxy: -0.032896
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
