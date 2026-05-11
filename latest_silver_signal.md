# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-11**
- 실행시간(UTC): **2026-05-11 15:01:37**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -13.0 bp / latest 2.81
- IG OAS 4주 변화: -3.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 1.0 bp / latest 1.96
- VIX: 17.19
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -4.28% / slope_proxy: 0.006063
- GDXJ/GLD gap: 3.51% / slope_proxy: -0.003945

## VZLA (Vizsla Silver)
- close: 3.685 | RSI14: 58.809262 | ATR14%: 5.63%
- MA20 gap: 7.30% | MA50 gap: 5.77% | MA200 gap: -12.53%
- vol_ratio(Volume/Vol20): 0.340264 | gap_open: 1.97%
- RS vs SILJ gap: -0.34% / slope_proxy: -0.014571
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

## SCZM (Santacruz Silver)
- close: 9.2499 | RSI14: 58.390917 | ATR14%: 7.06%
- MA20 gap: 7.97% | MA50 gap: 6.45% | MA200 gap: 15.73%
- vol_ratio(Volume/Vol20): 0.576025 | gap_open: 1.77%
- SilverMarginGate: SI=85.614998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.58% / slope_proxy: -0.02838
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
- close: 43.345501 | RSI14: 59.347947 | ATR14%: 8.52%
- MA20 gap: 10.88% | MA50 gap: 12.66% | MA200 gap: 98.43%
- vol_ratio(Volume/Vol20): 1.079115 | gap_open: 3.90%
- RS vs SILJ gap: 6.63% / slope_proxy: 0.033015
- RS vs GDXJ gap: 9.45% / slope_proxy: 0.005442
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
