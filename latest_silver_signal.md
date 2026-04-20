# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-20**
- 실행시간(UTC): **2026-04-20 15:01:40**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -41.0 bp / latest 2.83
- IG OAS 4주 변화: -8.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 5.0 bp / latest 1.93
- VIX: 17.48
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.14% / slope_proxy: 0.010662
- GDXJ/GLD gap: 2.27% / slope_proxy: -0.003684

## VZLA (Vizsla Silver)
- close: 3.455 | RSI14: 49.204839 | ATR14%: 5.67%
- MA20 gap: 5.28% | MA50 gap: -5.30% | MA200 gap: -17.63%
- vol_ratio(Volume/Vol20): 0.451096 | gap_open: 1.99%
- RS vs SILJ gap: -10.82% / slope_proxy: -0.027043
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
- close: 8.8699 | RSI14: 51.190446 | ATR14%: 8.16%
- MA20 gap: 7.95% | MA50 gap: -6.71% | MA200 gap: 16.05%
- vol_ratio(Volume/Vol20): 0.403266 | gap_open: 1.09%
- SilverMarginGate: SI=79.714996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -9.94% / slope_proxy: -0.026216
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

## HYMC (Hycroft Mining)
- close: 43.375 | RSI14: 59.715718 | ATR14%: 8.62%
- MA20 gap: 17.75% | MA50 gap: 10.53% | MA200 gap: 125.18%
- vol_ratio(Volume/Vol20): 0.346653 | gap_open: 2.33%
- RS vs SILJ gap: 11.42% / slope_proxy: 0.07846
- RS vs GDXJ gap: 8.99% / slope_proxy: 0.018555
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
