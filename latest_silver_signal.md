# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-14**
- 실행시간(UTC): **2026-09-14 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.65
- IG OAS 4주 변화: 0.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.55
- VIX: 15.84
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 3.72% / slope_proxy: 0.027005
- GDXJ/GLD gap: 8.14% / slope_proxy: 0.013524

## VZLA (Vizsla Silver)
- close: 3.77 | RSI14: 46.476766 | ATR14%: 5.40%
- MA20 gap: -4.83% | MA50 gap: 5.11% | MA200 gap: -7.05%
- vol_ratio(Volume/Vol20): 0.333415 | gap_open: 3.02%
- RS vs SILJ gap: 1.62% / slope_proxy: 1.6e-05
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
- close: 8.78 | RSI14: 45.780262 | ATR14%: 7.09%
- MA20 gap: -8.65% | MA50 gap: 8.95% | MA200 gap: -1.90%
- vol_ratio(Volume/Vol20): 0.36541 | gap_open: 5.18%
- SilverMarginGate: SI=63.415001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.08% / slope_proxy: 0.015239
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
- close: 20.389999 | RSI14: 37.295095 | ATR14%: 8.45%
- MA20 gap: -15.34% | MA50 gap: -11.07% | MA200 gap: -32.46%
- vol_ratio(Volume/Vol20): 0.283007 | gap_open: 5.51%
- RS vs SILJ gap: -15.65% / slope_proxy: -0.087355
- RS vs GDXJ gap: -19.12% / slope_proxy: -0.026914
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
