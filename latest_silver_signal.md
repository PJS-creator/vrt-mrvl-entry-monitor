# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-30**
- 실행시간(UTC): **2026-07-01 03:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 8.0 bp / latest 2.8
- IG OAS 4주 변화: 3.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 9.0 bp / latest 2.16
- VIX: 17.65
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 8.32% / slope_proxy: 0.006795
- GDXJ/GLD gap: -4.47% / slope_proxy: -0.001787

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 44.569418 | ATR14%: 6.44%
- MA20 gap: -5.24% | MA50 gap: -5.92% | MA200 gap: -22.08%
- vol_ratio(Volume/Vol20): 0.574167 | gap_open: 0.31%
- RS vs SILJ gap: 7.79% / slope_proxy: 0.00467
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
- close: 6.49 | RSI14: 40.356751 | ATR14%: 7.99%
- MA20 gap: -6.03% | MA50 gap: -17.59% | MA200 gap: -23.79%
- vol_ratio(Volume/Vol20): 0.363636 | gap_open: 0.46%
- SilverMarginGate: SI=58.32 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.80% / slope_proxy: -0.009197
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
- close: 23.4 | RSI14: 37.492815 | ATR14%: 9.68%
- MA20 gap: -9.32% | MA50 gap: -28.12% | MA200 gap: -10.68%
- vol_ratio(Volume/Vol20): 0.574824 | gap_open: 0.21%
- RS vs SILJ gap: -19.99% / slope_proxy: -0.081529
- RS vs GDXJ gap: -17.44% / slope_proxy: -0.017359
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
