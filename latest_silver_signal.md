# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-03**
- 실행시간(UTC): **2026-09-03 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -9.0 bp / latest 2.66
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.44
- VIX: 15.2
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 9.31% / slope_proxy: 0.027109
- GDXJ/GLD gap: 14.51% / slope_proxy: 0.010053

## VZLA (Vizsla Silver)
- close: 4.1309 | RSI14: 61.316797 | ATR14%: 4.87%
- MA20 gap: 5.88% | MA50 gap: 18.05% | MA200 gap: 1.58%
- vol_ratio(Volume/Vol20): 0.229175 | gap_open: 2.89%
- RS vs SILJ gap: 1.11% / slope_proxy: 0.001242
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
- close: 10.09 | RSI14: 65.13059 | ATR14%: 5.98%
- MA20 gap: 8.31% | MA50 gap: 31.56% | MA200 gap: 14.45%
- vol_ratio(Volume/Vol20): 0.309351 | gap_open: 3.14%
- SilverMarginGate: SI=67.199997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 15.13% / slope_proxy: 0.009772
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
- close: 22.885 | RSI14: 45.065795 | ATR14%: 8.38%
- MA20 gap: -10.66% | MA50 gap: -0.82% | MA200 gap: -23.30%
- vol_ratio(Volume/Vol20): 0.316958 | gap_open: 3.49%
- RS vs SILJ gap: -16.32% / slope_proxy: -0.096586
- RS vs GDXJ gap: -19.60% / slope_proxy: -0.02906
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
