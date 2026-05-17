# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-15**
- 실행시간(UTC): **2026-05-17 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.76
- IG OAS 4주 변화: -5.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 7.0 bp / latest 2.0
- VIX: 17.26
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -2.40% / slope_proxy: 0.000259
- GDXJ/GLD gap: -2.67% / slope_proxy: -0.00346

## VZLA (Vizsla Silver)
- close: 3.5 | RSI14: 49.078259 | ATR14%: 6.47%
- MA20 gap: 0.19% | MA50 gap: 1.43% | MA200 gap: -17.16%
- vol_ratio(Volume/Vol20): 1.770662 | gap_open: 5.59%
- RS vs SILJ gap: 4.03% / slope_proxy: -0.009575
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.7 | RSI14: 48.628584 | ATR14%: 8.17%
- MA20 gap: -0.01% | MA50 gap: 1.24% | MA200 gap: 7.23%
- vol_ratio(Volume/Vol20): 0.972859 | gap_open: 9.28%
- SilverMarginGate: SI=77.546997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.65% / slope_proxy: -0.023316
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
- close: 36.16 | RSI14: 45.028237 | ATR14%: 10.50%
- MA20 gap: -7.23% | MA50 gap: -4.61% | MA200 gap: 60.01%
- vol_ratio(Volume/Vol20): 1.861848 | gap_open: 6.76%
- RS vs SILJ gap: -2.80% / slope_proxy: 0.028319
- RS vs GDXJ gap: -0.03% / slope_proxy: 0.006483
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
