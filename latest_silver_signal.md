# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-09**
- 실행시간(UTC): **2026-04-10 03:01:14**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -15.0 bp / latest 2.94
- IG OAS 4주 변화: -5.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 11.0 bp / latest 1.96
- VIX: 21.04
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 3.62% / slope_proxy: 0.001888
- GDXJ/GLD gap: 0.47% / slope_proxy: -0.004642

## VZLA (Vizsla Silver)
- close: 3.27 | RSI14: 41.200512 | ATR14%: 6.98%
- MA20 gap: -1.00% | MA50 gap: -16.53% | MA200 gap: -21.74%
- vol_ratio(Volume/Vol20): 0.660132 | gap_open: 0.61%
- RS vs SILJ gap: -19.03% / slope_proxy: -0.02743
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
- close: 8.13 | RSI14: 44.551418 | ATR14%: 9.96%
- MA20 gap: 0.34% | MA50 gap: -19.02% | MA200 gap: 9.31%
- vol_ratio(Volume/Vol20): 0.358157 | gap_open: 0.50%
- SilverMarginGate: SI=75.599998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.62% / slope_proxy: -0.022582
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
- close: 38.970001 | RSI14: 54.072179 | ATR14%: 10.78%
- MA20 gap: 10.55% | MA50 gap: -0.58% | MA200 gap: 117.27%
- vol_ratio(Volume/Vol20): 0.686621 | gap_open: 0.49%
- RS vs SILJ gap: 4.62% / slope_proxy: 0.133664
- RS vs GDXJ gap: 1.14% / slope_proxy: 0.034933
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
