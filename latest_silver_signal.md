# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-19**
- 실행시간(UTC): **2026-08-19 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.75
- IG OAS 4주 변화: 4.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 9.0 bp / latest 2.44
- VIX: 15.84
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 11.69% / slope_proxy: 0.018879
- GDXJ/GLD gap: 12.58% / slope_proxy: -0.000346

## VZLA (Vizsla Silver)
- close: 3.855 | RSI14: 61.720522 | ATR14%: 4.87%
- MA20 gap: 9.90% | MA50 gap: 14.19% | MA200 gap: -5.42%
- vol_ratio(Volume/Vol20): 0.416644 | gap_open: 4.48%
- RS vs SILJ gap: -3.26% / slope_proxy: 0.004667
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
- close: 9.4201 | RSI14: 70.475326 | ATR14%: 5.71%
- MA20 gap: 24.04% | MA50 gap: 34.64% | MA200 gap: 10.04%
- vol_ratio(Volume/Vol20): 0.961431 | gap_open: 4.78%
- SilverMarginGate: SI=65.599998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.37% / slope_proxy: -0.000882
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
- close: 27.24 | RSI14: 59.735773 | ATR14%: 7.01%
- MA20 gap: 15.55% | MA50 gap: 17.80% | MA200 gap: -5.81%
- vol_ratio(Volume/Vol20): 0.703703 | gap_open: 8.06%
- RS vs SILJ gap: -3.38% / slope_proxy: -0.122168
- RS vs GDXJ gap: -6.78% / slope_proxy: -0.032582
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
