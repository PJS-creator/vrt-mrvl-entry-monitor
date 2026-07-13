# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-13**
- 실행시간(UTC): **2026-07-13 15:01:08**

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
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.31
- VIX: 15.03
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 5.24% / slope_proxy: 0.00919
- GDXJ/GLD gap: -4.85% / slope_proxy: -0.003092

## VZLA (Vizsla Silver)
- close: 3.045 | RSI14: 40.254572 | ATR14%: 6.55%
- MA20 gap: -8.11% | MA50 gap: -12.17% | MA200 gap: -27.59%
- vol_ratio(Volume/Vol20): 0.269113 | gap_open: 1.60%
- RS vs SILJ gap: 1.63% / slope_proxy: 0.005097
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
- close: 6.29 | RSI14: 40.962893 | ATR14%: 7.43%
- MA20 gap: -7.07% | MA50 gap: -16.85% | MA200 gap: -26.04%
- vol_ratio(Volume/Vol20): 0.240073 | gap_open: 2.77%
- SilverMarginGate: SI=58.27 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.40% / slope_proxy: -0.004964
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
- close: 20.459999 | RSI14: 33.276716 | ATR14%: 9.64%
- MA20 gap: -13.00% | MA50 gap: -31.62% | MA200 gap: -23.74%
- vol_ratio(Volume/Vol20): 0.164985 | gap_open: 1.96%
- RS vs SILJ gap: -23.82% / slope_proxy: -0.101847
- RS vs GDXJ gap: -23.77% / slope_proxy: -0.022198
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
