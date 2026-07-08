# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-08**
- 실행시간(UTC): **2026-07-08 15:01:22**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.67
- IG OAS 4주 변화: 1.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 3.0 bp / latest 2.24
- VIX: 16.13
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 2.88% / slope_proxy: 0.008008
- GDXJ/GLD gap: -7.88% / slope_proxy: -0.002152

## VZLA (Vizsla Silver)
- close: 2.95 | RSI14: 35.255983 | ATR14%: 7.07%
- MA20 gap: -11.85% | MA50 gap: -15.40% | MA200 gap: -30.08%
- vol_ratio(Volume/Vol20): 0.321796 | gap_open: 1.29%
- RS vs SILJ gap: 2.19% / slope_proxy: 0.005097
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
- close: 6.11 | RSI14: 37.17032 | ATR14%: 8.12%
- MA20 gap: -9.21% | MA50 gap: -20.16% | MA200 gap: -28.24%
- vol_ratio(Volume/Vol20): 0.336451 | gap_open: 2.20%
- SilverMarginGate: SI=58.195 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.60% / slope_proxy: -0.005965
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
- close: 20.395 | RSI14: 31.275258 | ATR14%: 10.38%
- MA20 gap: -14.91% | MA50 gap: -33.79% | MA200 gap: -23.35%
- vol_ratio(Volume/Vol20): 0.185545 | gap_open: 3.22%
- RS vs SILJ gap: -23.24% / slope_proxy: -0.094991
- RS vs GDXJ gap: -23.73% / slope_proxy: -0.020804
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
