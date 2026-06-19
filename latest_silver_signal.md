# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-18**
- 실행시간(UTC): **2026-06-19 03:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -17.0 bp / latest 2.63
- IG OAS 4주 변화: -1.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.23
- VIX: 18.44
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 5.90% / slope_proxy: -0.002812
- GDXJ/GLD gap: -1.07% / slope_proxy: -0.004847

## VZLA (Vizsla Silver)
- close: 3.55 | RSI14: 49.150293 | ATR14%: 6.75%
- MA20 gap: -2.06% | MA50 gap: 0.81% | MA200 gap: -16.50%
- vol_ratio(Volume/Vol20): 0.726808 | gap_open: 0.00%
- RS vs SILJ gap: 9.22% / slope_proxy: 0.004478
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
- close: 7.15 | RSI14: 44.96193 | ATR14%: 8.89%
- MA20 gap: -3.72% | MA50 gap: -12.49% | MA200 gap: -15.86%
- vol_ratio(Volume/Vol20): 0.86849 | gap_open: 0.80%
- SilverMarginGate: SI=64.57 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.54% / slope_proxy: -0.010751
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
- close: 26.01 | RSI14: 38.711842 | ATR14%: 10.27%
- MA20 gap: -10.88% | MA50 gap: -25.61% | MA200 gap: 1.67%
- vol_ratio(Volume/Vol20): 1.470322 | gap_open: 0.51%
- RS vs SILJ gap: -19.72% / slope_proxy: -0.071515
- RS vs GDXJ gap: -17.87% / slope_proxy: -0.015592
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
