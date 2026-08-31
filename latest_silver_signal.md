# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-30**
- 실행시간(UTC): **2026-08-31 00:48:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -21.0 bp / latest 2.63
- IG OAS 4주 변화: -1.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -7.0 bp / latest 2.34
- VIX: 14.51
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 10.02% / slope_proxy: 0.024269
- GDXJ/GLD gap: 14.38% / slope_proxy: 0.005396

## VZLA (Vizsla Silver)
- close: 4.0 | RSI14: 60.611451 | ATR14%: 4.83%
- MA20 gap: 5.79% | MA50 gap: 16.07% | MA200 gap: -1.88%
- vol_ratio(Volume/Vol20): 1.365234 | gap_open: 0.96%
- RS vs SILJ gap: -0.86% / slope_proxy: 0.002476
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
- close: 9.52 | RSI14: 62.345883 | ATR14%: 5.98%
- MA20 gap: 7.36% | MA50 gap: 28.03% | MA200 gap: 9.02%
- vol_ratio(Volume/Vol20): 1.06365 | gap_open: 1.40%
- SilverMarginGate: SI=67.535004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.80% / slope_proxy: 0.005253
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
- close: 23.825001 | RSI14: 46.571271 | ATR14%: 8.27%
- MA20 gap: -7.01% | MA50 gap: 2.83% | MA200 gap: -19.39%
- vol_ratio(Volume/Vol20): 1.298157 | gap_open: 0.15%
- RS vs SILJ gap: -13.61% / slope_proxy: -0.105423
- RS vs GDXJ gap: -16.65% / slope_proxy: -0.030524
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
