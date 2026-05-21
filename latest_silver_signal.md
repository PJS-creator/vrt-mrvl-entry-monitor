# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-20**
- 실행시간(UTC): **2026-05-21 03:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.86
- IG OAS 4주 변화: -4.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.18
- VIX: 18.06
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -4.22% / slope_proxy: -0.003757
- GDXJ/GLD gap: -4.63% / slope_proxy: -0.003992

## VZLA (Vizsla Silver)
- close: 3.39 | RSI14: 46.495705 | ATR14%: 6.46%
- MA20 gap: -2.63% | MA50 gap: -0.57% | MA200 gap: -19.88%
- vol_ratio(Volume/Vol20): 0.698361 | gap_open: 1.84%
- RS vs SILJ gap: 3.18% / slope_proxy: -0.005987
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
- close: 8.38 | RSI14: 45.96304 | ATR14%: 8.20%
- MA20 gap: -2.88% | MA50 gap: -1.20% | MA200 gap: 2.37%
- vol_ratio(Volume/Vol20): 1.981009 | gap_open: 3.28%
- SilverMarginGate: SI=75.660004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.30% / slope_proxy: -0.019095
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
- close: 34.064999 | RSI14: 42.496214 | ATR14%: 10.47%
- MA20 gap: -10.09% | MA50 gap: -9.07% | MA200 gap: 47.75%
- vol_ratio(Volume/Vol20): 0.75778 | gap_open: 3.30%
- RS vs SILJ gap: -5.79% / slope_proxy: 0.026791
- RS vs GDXJ gap: -3.37% / slope_proxy: 0.007332
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
