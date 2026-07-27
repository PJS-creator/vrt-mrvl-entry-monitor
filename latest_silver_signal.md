# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-26**
- 실행시간(UTC): **2026-07-27 03:00:55**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.77
- IG OAS 4주 변화: 3.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.43
- VIX: 18.7
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 5.25% / slope_proxy: 0.008287
- GDXJ/GLD gap: -3.15% / slope_proxy: -0.008758

## VZLA (Vizsla Silver)
- close: 3.24 | RSI14: 48.951937 | ATR14%: 6.13%
- MA20 gap: 1.49% | MA50 gap: -5.46% | MA200 gap: -22.16%
- vol_ratio(Volume/Vol20): 1.067227 | gap_open: 3.51%
- RS vs SILJ gap: 5.91% / slope_proxy: 0.006172
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
- close: 6.3 | RSI14: 45.000337 | ATR14%: 7.14%
- MA20 gap: -2.08% | MA50 gap: -12.73% | MA200 gap: -25.48%
- vol_ratio(Volume/Vol20): 0.867422 | gap_open: 2.22%
- SilverMarginGate: SI=59.654999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.92% / slope_proxy: -0.005783
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
- close: 20.48 | RSI14: 41.897124 | ATR14%: 9.30%
- MA20 gap: -4.88% | MA50 gap: -24.18% | MA200 gap: -25.22%
- vol_ratio(Volume/Vol20): 0.670171 | gap_open: 5.76%
- RS vs SILJ gap: -18.97% / slope_proxy: -0.127233
- RS vs GDXJ gap: -20.34% / slope_proxy: -0.028532
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
