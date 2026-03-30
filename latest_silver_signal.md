# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-30**
- 실행시간(UTC): **2026-03-30 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 32.0 bp / latest 3.42
- IG OAS 4주 변화: 6.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 34.0 bp / latest 2.08
- VIX: 31.05
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -1.07% / slope_proxy: -0.004565
- GDXJ/GLD gap: -7.54% / slope_proxy: -0.00158

## VZLA (Vizsla Silver)
- close: 3.155 | RSI14: 35.049196 | ATR14%: 8.15%
- MA20 gap: -11.85% | MA50 gap: -27.61% | MA200 gap: -24.56%
- vol_ratio(Volume/Vol20): 0.178992 | gap_open: 1.90%
- RS vs SILJ gap: -18.38% / slope_proxy: -0.027188
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.66 | RSI14: 37.281622 | ATR14%: 10.98%
- MA20 gap: -13.86% | MA50 gap: -29.55% | MA200 gap: 5.56%
- vol_ratio(Volume/Vol20): 0.240069 | gap_open: 3.75%
- SilverMarginGate: SI=70.919998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.19% / slope_proxy: -0.01924
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 31.889999 | RSI14: 41.867718 | ATR14%: 13.78%
- MA20 gap: -15.60% | MA50 gap: -21.27% | MA200 gap: 90.03%
- vol_ratio(Volume/Vol20): 0.18939 | gap_open: 1.19%
- RS vs SILJ gap: -1.38% / slope_proxy: 0.197349
- RS vs GDXJ gap: -3.68% / slope_proxy: 0.051809
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
