# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-13**
- 실행시간(UTC): **2026-04-13 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.94
- IG OAS 4주 변화: -11.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 6.0 bp / latest 1.95
- VIX: 19.23
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 4.52% / slope_proxy: 0.005337
- GDXJ/GLD gap: 1.10% / slope_proxy: -0.004616

## VZLA (Vizsla Silver)
- close: 3.2699 | RSI14: 41.507914 | ATR14%: 6.54%
- MA20 gap: 0.44% | MA50 gap: -13.81% | MA200 gap: -21.80%
- vol_ratio(Volume/Vol20): 0.165292 | gap_open: 1.54%
- RS vs SILJ gap: -16.65% / slope_proxy: -0.027518
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
- close: 8.285 | RSI14: 46.526016 | ATR14%: 9.21%
- MA20 gap: 4.13% | MA50 gap: -15.31% | MA200 gap: 10.59%
- vol_ratio(Volume/Vol20): 0.380044 | gap_open: 1.00%
- SilverMarginGate: SI=73.879997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.57% / slope_proxy: -0.023274
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
- close: 38.290001 | RSI14: 52.654532 | ATR14%: 10.42%
- MA20 gap: 8.97% | MA50 gap: -1.22% | MA200 gap: 109.43%
- vol_ratio(Volume/Vol20): 0.163596 | gap_open: 0.83%
- RS vs SILJ gap: 3.21% / slope_proxy: 0.115014
- RS vs GDXJ gap: -0.32% / slope_proxy: 0.029626
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
