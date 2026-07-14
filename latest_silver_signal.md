# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-14**
- 실행시간(UTC): **2026-07-14 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 3.0 bp / latest 2.69
- IG OAS 4주 변화: 5.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.32
- VIX: 17.16
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 6.25% / slope_proxy: 0.009415
- GDXJ/GLD gap: -3.48% / slope_proxy: -0.003743

## VZLA (Vizsla Silver)
- close: 3.185 | RSI14: 45.918133 | ATR14%: 6.36%
- MA20 gap: -3.26% | MA50 gap: -8.01% | MA200 gap: -24.20%
- vol_ratio(Volume/Vol20): 0.222281 | gap_open: 3.31%
- RS vs SILJ gap: 3.06% / slope_proxy: 0.005088
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
- close: 6.6 | RSI14: 45.844707 | ATR14%: 7.05%
- MA20 gap: -2.26% | MA50 gap: -12.47% | MA200 gap: -22.39%
- vol_ratio(Volume/Vol20): 0.310672 | gap_open: 2.52%
- SilverMarginGate: SI=59.5 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.42% / slope_proxy: -0.005144
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
- close: 21.719999 | RSI14: 39.082439 | ATR14%: 9.16%
- MA20 gap: -6.84% | MA50 gap: -26.69% | MA200 gap: -19.28%
- vol_ratio(Volume/Vol20): 0.187431 | gap_open: 6.95%
- RS vs SILJ gap: -20.90% / slope_proxy: -0.104072
- RS vs GDXJ gap: -20.89% / slope_proxy: -0.022687
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
