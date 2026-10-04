# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-02**
- 실행시간(UTC): **2026-10-04 01:58:39**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 59.0 bp / latest 3.24
- IG OAS 4주 변화: 5.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 46.0 bp / latest 2.88
- VIX: 16.39
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: -0.52% / slope_proxy: 0.013572
- GDXJ/GLD gap: 2.27% / slope_proxy: 0.013187

## VZLA (Vizsla Silver)
- close: 3.61 | RSI14: 39.967003 | ATR14%: 5.51%
- MA20 gap: -8.12% | MA50 gap: -4.87% | MA200 gap: -9.24%
- vol_ratio(Volume/Vol20): 1.205737 | gap_open: 2.13%
- RS vs SILJ gap: 2.18% / slope_proxy: 0.002509
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.8 | RSI14: 47.114755 | ATR14%: 6.80%
- MA20 gap: -4.47% | MA50 gap: 0.15% | MA200 gap: -2.12%
- vol_ratio(Volume/Vol20): 0.657111 | gap_open: 2.30%
- SilverMarginGate: SI=59.977001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.56% / slope_proxy: 0.019247
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 18.709999 | RSI14: 36.910133 | ATR14%: 7.72%
- MA20 gap: -10.42% | MA50 gap: -18.03% | MA200 gap: -39.26%
- vol_ratio(Volume/Vol20): 0.746228 | gap_open: 2.43%
- RS vs SILJ gap: -12.86% / slope_proxy: -0.063332
- RS vs GDXJ gap: -16.02% / slope_proxy: -0.020473
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
