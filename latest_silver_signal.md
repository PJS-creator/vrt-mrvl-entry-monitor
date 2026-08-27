# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-26**
- 실행시간(UTC): **2026-08-27 03:01:13**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -14.0 bp / latest 2.7
- IG OAS 4주 변화: 0.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -9.0 bp / latest 2.32
- VIX: 15.45
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 9.97% / slope_proxy: 0.022681
- GDXJ/GLD gap: 15.07% / slope_proxy: 0.003655

## VZLA (Vizsla Silver)
- close: 4.02 | RSI14: 64.633006 | ATR14%: 4.64%
- MA20 gap: 8.88% | MA50 gap: 17.26% | MA200 gap: -1.39%
- vol_ratio(Volume/Vol20): 0.473677 | gap_open: 2.48%
- RS vs SILJ gap: -2.49% / slope_proxy: 0.003175
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
- close: 9.63 | RSI14: 67.720284 | ATR14%: 5.45%
- MA20 gap: 12.60% | MA50 gap: 30.94% | MA200 gap: 10.83%
- vol_ratio(Volume/Vol20): 0.645641 | gap_open: 1.64%
- SilverMarginGate: SI=69.220001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.42% / slope_proxy: 0.003765
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
- close: 25.459999 | RSI14: 52.017102 | ATR14%: 7.50%
- MA20 gap: 1.39% | MA50 gap: 9.67% | MA200 gap: -13.36%
- vol_ratio(Volume/Vol20): 0.961605 | gap_open: 3.37%
- RS vs SILJ gap: -10.61% / slope_proxy: -0.109402
- RS vs GDXJ gap: -14.96% / slope_proxy: -0.030863
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
