# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-08**
- 실행시간(UTC): **2026-04-08 15:01:18**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 3.12
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 20.0 bp / latest 1.98
- VIX: 25.78
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 4.47% / slope_proxy: 0.000504
- GDXJ/GLD gap: 0.14% / slope_proxy: -0.004574

## VZLA (Vizsla Silver)
- close: 3.27 | RSI14: 40.9185 | ATR14%: 7.17%
- MA20 gap: -2.17% | MA50 gap: -17.93% | MA200 gap: -21.71%
- vol_ratio(Volume/Vol20): 0.354543 | gap_open: 6.81%
- RS vs SILJ gap: -19.93% / slope_proxy: -0.0274
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
- close: 8.19 | RSI14: 44.957462 | ATR14%: 10.07%
- MA20 gap: -0.33% | MA50 gap: -19.74% | MA200 gap: 10.49%
- vol_ratio(Volume/Vol20): 0.347448 | gap_open: 9.92%
- SilverMarginGate: SI=75.455002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.57% / slope_proxy: -0.022173
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
- close: 37.380001 | RSI14: 51.278204 | ATR14%: 11.28%
- MA20 gap: 5.45% | MA50 gap: -5.42% | MA200 gap: 110.48%
- vol_ratio(Volume/Vol20): 0.358438 | gap_open: 11.46%
- RS vs SILJ gap: 0.52% / slope_proxy: 0.143404
- RS vs GDXJ gap: -2.03% / slope_proxy: 0.037679
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
