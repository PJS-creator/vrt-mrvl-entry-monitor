# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-09**
- 실행시간(UTC): **2026-10-10 01:54:28**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 45.0 bp / latest 3.15
- IG OAS 4주 변화: 2.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 32.0 bp / latest 2.87
- VIX: 15.41
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -0.30% / slope_proxy: 0.008257
- GDXJ/GLD gap: 0.77% / slope_proxy: 0.012268

## VZLA (Vizsla Silver)
- close: 3.55 | RSI14: 41.347337 | ATR14%: 5.31%
- MA20 gap: -6.48% | MA50 gap: -7.09% | MA200 gap: -9.72%
- vol_ratio(Volume/Vol20): 0.740686 | gap_open: 2.88%
- RS vs SILJ gap: -0.41% / slope_proxy: 0.002845
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
- close: 9.11 | RSI14: 51.743552 | ATR14%: 6.27%
- MA20 gap: 2.08% | MA50 gap: 0.97% | MA200 gap: 1.31%
- vol_ratio(Volume/Vol20): 0.569297 | gap_open: 3.07%
- SilverMarginGate: SI=61.110001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.49% / slope_proxy: 0.020101
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 19.190001 | RSI14: 42.85497 | ATR14%: 6.73%
- MA20 gap: -4.04% | MA50 gap: -15.42% | MA200 gap: -37.80%
- vol_ratio(Volume/Vol20): 0.736414 | gap_open: 2.69%
- RS vs SILJ gap: -9.89% / slope_proxy: -0.055595
- RS vs GDXJ gap: -12.70% / slope_proxy: -0.018639
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
