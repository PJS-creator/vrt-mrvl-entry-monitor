# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-20**
- 실행시간(UTC): **2026-11-20 15:01:15**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 12.0 bp / latest 3.52
- IG OAS 4주 변화: 5.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.88
- VIX: 28.44
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 0.87% / slope_proxy: 0.002075
- GDXJ/GLD gap: -10.87% / slope_proxy: -0.006629

## VZLA (Vizsla Silver)
- close: 2.815 | RSI14: 35.399979 | ATR14%: 7.02%
- MA20 gap: -10.01% | MA50 gap: -17.78% | MA200 gap: -20.45%
- vol_ratio(Volume/Vol20): 0.428436 | gap_open: 5.67%
- RS vs SILJ gap: 8.06% / slope_proxy: 0.003076
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
- close: 6.54 | RSI14: 41.039167 | ATR14%: 8.38%
- MA20 gap: -8.52% | MA50 gap: -18.73% | MA200 gap: -21.68%
- vol_ratio(Volume/Vol20): 0.276357 | gap_open: 2.12%
- SilverMarginGate: SI=42.095001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.24% / slope_proxy: 0.005543
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

## HYMC (Hycroft Mining)
- close: 14.3594 | RSI14: 38.809347 | ATR14%: 10.35%
- MA20 gap: -14.33% | MA50 gap: -20.59% | MA200 gap: -48.93%
- vol_ratio(Volume/Vol20): 0.256907 | gap_open: 2.25%
- RS vs SILJ gap: 3.41% / slope_proxy: -0.044565
- RS vs GDXJ gap: -0.51% / slope_proxy: -0.01511
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
