# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-30**
- 실행시간(UTC): **2026-10-01 01:31:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 43.0 bp / latest 3.08
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 47.0 bp / latest 2.91
- VIX: 16.04
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: 0.00% / slope_proxy: 0.017041
- GDXJ/GLD gap: 4.13% / slope_proxy: 0.014379

## VZLA (Vizsla Silver)
- close: 3.84 | RSI14: 47.26782 | ATR14%: 5.32%
- MA20 gap: -3.53% | MA50 gap: 1.84% | MA200 gap: -4.01%
- vol_ratio(Volume/Vol20): 0.773271 | gap_open: 0.26%
- RS vs SILJ gap: 7.60% / slope_proxy: 0.001798
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
- close: 8.975 | RSI14: 48.59533 | ATR14%: 7.23%
- MA20 gap: -4.37% | MA50 gap: 3.72% | MA200 gap: -0.37%
- vol_ratio(Volume/Vol20): 0.608765 | gap_open: 0.67%
- SilverMarginGate: SI=61.005001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.30% / slope_proxy: 0.019712
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
- close: 19.379999 | RSI14: 39.125165 | ATR14%: 8.22%
- MA20 gap: -9.69% | MA50 gap: -15.55% | MA200 gap: -36.90%
- vol_ratio(Volume/Vol20): 1.037479 | gap_open: 0.61%
- RS vs SILJ gap: -12.03% / slope_proxy: -0.068684
- RS vs GDXJ gap: -15.76% / slope_proxy: -0.02181
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
