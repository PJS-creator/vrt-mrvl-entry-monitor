# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-26**
- 실행시간(UTC): **2026-06-28 03:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.78
- IG OAS 4주 변화: 3.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.19
- VIX: 18.89
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 9.49% / slope_proxy: 0.003529
- GDXJ/GLD gap: -5.35% / slope_proxy: -0.001906

## VZLA (Vizsla Silver)
- close: 3.13 | RSI14: 38.400358 | ATR14%: 7.19%
- MA20 gap: -12.46% | MA50 gap: -11.03% | MA200 gap: -26.22%
- vol_ratio(Volume/Vol20): 0.634227 | gap_open: 1.93%
- RS vs SILJ gap: 4.51% / slope_proxy: 0.004418
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
- close: 6.44 | RSI14: 39.216221 | ATR14%: 8.93%
- MA20 gap: -9.89% | MA50 gap: -19.74% | MA200 gap: -24.36%
- vol_ratio(Volume/Vol20): 0.652344 | gap_open: 2.21%
- SilverMarginGate: SI=59.216999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.49% / slope_proxy: -0.009692
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
- close: 21.889999 | RSI14: 31.686395 | ATR14%: 10.99%
- MA20 gap: -19.62% | MA50 gap: -34.94% | MA200 gap: -15.59%
- vol_ratio(Volume/Vol20): 0.815762 | gap_open: 3.00%
- RS vs SILJ gap: -24.93% / slope_proxy: -0.078558
- RS vs GDXJ gap: -23.18% / slope_proxy: -0.016862
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
