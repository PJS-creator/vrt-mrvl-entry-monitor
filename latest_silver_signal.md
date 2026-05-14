# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-14**
- 실행시간(UTC): **2026-05-14 15:01:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.82
- IG OAS 4주 변화: -4.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 10.0 bp / latest 1.99
- VIX: 17.87
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -4.13% / slope_proxy: 0.001531
- GDXJ/GLD gap: 1.65% / slope_proxy: -0.003236

## VZLA (Vizsla Silver)
- close: 3.65 | RSI14: 54.732431 | ATR14%: 5.94%
- MA20 gap: 4.63% | MA50 gap: 5.50% | MA200 gap: -13.54%
- vol_ratio(Volume/Vol20): 0.377661 | gap_open: 0.00%
- RS vs SILJ gap: -0.38% / slope_proxy: -0.010787
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
- close: 9.5 | RSI14: 57.261247 | ATR14%: 7.10%
- MA20 gap: 9.00% | MA50 gap: 10.28% | MA200 gap: 17.49%
- vol_ratio(Volume/Vol20): 0.348684 | gap_open: 0.80%
- SilverMarginGate: SI=85.404999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.83% / slope_proxy: -0.02456
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
- close: 40.389999 | RSI14: 51.975067 | ATR14%: 9.24%
- MA20 gap: 2.43% | MA50 gap: 6.22% | MA200 gap: 80.00%
- vol_ratio(Volume/Vol20): 0.462454 | gap_open: 1.44%
- RS vs SILJ gap: -0.45% / slope_proxy: 0.032624
- RS vs GDXJ gap: 3.71% / slope_proxy: 0.007187
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
