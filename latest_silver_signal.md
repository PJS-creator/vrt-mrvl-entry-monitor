# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-14**
- 실행시간(UTC): **2026-04-15 03:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -32.0 bp / latest 2.95
- IG OAS 4주 변화: -12.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 5.0 bp / latest 1.92
- VIX: 19.12
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 1.64% / slope_proxy: 0.006863
- GDXJ/GLD gap: 2.68% / slope_proxy: -0.0045

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 49.272339 | ATR14%: 6.16%
- MA20 gap: 6.49% | MA50 gap: -8.03% | MA200 gap: -17.30%
- vol_ratio(Volume/Vol20): 0.930576 | gap_open: 1.81%
- RS vs SILJ gap: -15.08% / slope_proxy: -0.027522
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
- close: 9.03 | RSI14: 53.308838 | ATR14%: 8.50%
- MA20 gap: 13.16% | MA50 gap: -7.18% | MA200 gap: 20.02%
- vol_ratio(Volume/Vol20): 1.221335 | gap_open: 1.63%
- SilverMarginGate: SI=80.275002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.95% / slope_proxy: -0.023594
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
- close: 41.700001 | RSI14: 58.287489 | ATR14%: 9.59%
- MA20 gap: 18.07% | MA50 gap: 7.27% | MA200 gap: 125.63%
- vol_ratio(Volume/Vol20): 0.717985 | gap_open: 4.40%
- RS vs SILJ gap: 6.77% / slope_proxy: 0.106609
- RS vs GDXJ gap: 3.65% / slope_proxy: 0.027199
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trigger(Breakout/Retest)=FALSE
