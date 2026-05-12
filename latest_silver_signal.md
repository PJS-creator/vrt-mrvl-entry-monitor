# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-11**
- 실행시간(UTC): **2026-05-12 03:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -13.0 bp / latest 2.81
- IG OAS 4주 변화: -3.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -2.0 bp / latest 1.93
- VIX: 17.19
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -4.04% / slope_proxy: 0.006082
- GDXJ/GLD gap: 3.95% / slope_proxy: -0.003923

## VZLA (Vizsla Silver)
- close: 3.73 | RSI14: 60.075402 | ATR14%: 5.58%
- MA20 gap: 8.54% | MA50 gap: 7.04% | MA200 gap: -11.46%
- vol_ratio(Volume/Vol20): 1.012948 | gap_open: 1.97%
- RS vs SILJ gap: -0.88% / slope_proxy: -0.014581
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
- close: 9.43 | RSI14: 60.022114 | ATR14%: 6.93%
- MA20 gap: 9.96% | MA50 gap: 8.48% | MA200 gap: 17.97%
- vol_ratio(Volume/Vol20): 1.255076 | gap_open: 1.77%
- SilverMarginGate: SI=86.900002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.42% / slope_proxy: -0.028372
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
- close: 43.709999 | RSI14: 59.861471 | ATR14%: 8.44%
- MA20 gap: 11.77% | MA50 gap: 13.59% | MA200 gap: 100.08%
- vol_ratio(Volume/Vol20): 1.993135 | gap_open: 3.90%
- RS vs SILJ gap: 5.67% / slope_proxy: 0.032815
- RS vs GDXJ gap: 9.67% / slope_proxy: 0.005453
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
