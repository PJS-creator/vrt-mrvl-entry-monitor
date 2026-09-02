# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-01**
- 실행시간(UTC): **2026-09-02 03:00:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -15.0 bp / latest 2.63
- IG OAS 4주 변화: 2.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 1.0 bp / latest 2.44
- VIX: 14.92
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 7.71% / slope_proxy: 0.02491
- GDXJ/GLD gap: 11.27% / slope_proxy: 0.007497

## VZLA (Vizsla Silver)
- close: 3.86 | RSI14: 54.690673 | ATR14%: 4.91%
- MA20 gap: 1.22% | MA50 gap: 11.77% | MA200 gap: -5.28%
- vol_ratio(Volume/Vol20): 1.036965 | gap_open: 3.95%
- RS vs SILJ gap: 1.00% / slope_proxy: 0.002179
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
- close: 9.2 | RSI14: 57.69794 | ATR14%: 6.09%
- MA20 gap: 2.42% | MA50 gap: 23.10% | MA200 gap: 5.13%
- vol_ratio(Volume/Vol20): 0.907626 | gap_open: 4.38%
- SilverMarginGate: SI=64.449997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.75% / slope_proxy: 0.006238
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
- close: 21.629999 | RSI14: 40.739831 | ATR14%: 9.02%
- MA20 gap: -15.67% | MA50 gap: -6.25% | MA200 gap: -26.98%
- vol_ratio(Volume/Vol20): 1.062096 | gap_open: 5.63%
- RS vs SILJ gap: -16.69% / slope_proxy: -0.103033
- RS vs GDXJ gap: -19.72% / slope_proxy: -0.030207
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
