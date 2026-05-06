# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-06**
- 실행시간(UTC): **2026-05-06 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.77
- IG OAS 4주 변화: -7.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -3.0 bp / latest 1.95
- VIX: 17.38
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -2.39% / slope_proxy: 0.010595
- GDXJ/GLD gap: -0.58% / slope_proxy: -0.003952

## VZLA (Vizsla Silver)
- close: 3.45 | RSI14: 50.971909 | ATR14%: 5.94%
- MA20 gap: 1.72% | MA50 gap: -2.00% | MA200 gap: -18.04%
- vol_ratio(Volume/Vol20): 0.431704 | gap_open: 6.04%
- RS vs SILJ gap: -0.23% / slope_proxy: -0.018361
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.44 | RSI14: 50.234785 | ATR14%: 7.43%
- MA20 gap: 0.08% | MA50 gap: -5.00% | MA200 gap: 6.60%
- vol_ratio(Volume/Vol20): 0.459474 | gap_open: 4.50%
- SilverMarginGate: SI=78.080002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.49% / slope_proxy: -0.030855
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 39.080002 | RSI14: 52.386303 | ATR14%: 8.49%
- MA20 gap: 0.66% | MA50 gap: 0.14% | MA200 gap: 83.51%
- vol_ratio(Volume/Vol20): 0.458525 | gap_open: 6.70%
- RS vs SILJ gap: 3.88% / slope_proxy: 0.030869
- RS vs GDXJ gap: 4.19% / slope_proxy: 0.004049
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
