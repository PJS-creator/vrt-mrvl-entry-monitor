# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-09**
- 실행시간(UTC): **2026-09-10 00:33:44**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -5.0 bp / latest 2.67
- IG OAS 4주 변화: 2.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 0.0 bp / latest 2.43
- VIX: 15.72
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 8.48% / slope_proxy: 0.028167
- GDXJ/GLD gap: 13.47% / slope_proxy: 0.012294

## VZLA (Vizsla Silver)
- close: 4.08 | RSI14: 58.207912 | ATR14%: 4.92%
- MA20 gap: 3.91% | MA50 gap: 15.46% | MA200 gap: 0.45%
- vol_ratio(Volume/Vol20): 0.647842 | gap_open: 0.00%
- RS vs SILJ gap: 1.72% / slope_proxy: 0.000577
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 9.97 | RSI14: 61.510932 | ATR14%: 5.90%
- MA20 gap: 5.41% | MA50 gap: 27.61% | MA200 gap: 12.48%
- vol_ratio(Volume/Vol20): 0.540265 | gap_open: 0.40%
- SilverMarginGate: SI=67.910004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.82% / slope_proxy: 0.012067
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
- close: 22.959999 | RSI14: 45.500991 | ATR14%: 7.88%
- MA20 gap: -8.98% | MA50 gap: -0.53% | MA200 gap: -23.37%
- vol_ratio(Volume/Vol20): 0.835605 | gap_open: 1.06%
- RS vs SILJ gap: -13.81% / slope_proxy: -0.091142
- RS vs GDXJ gap: -15.97% / slope_proxy: -0.027455
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
