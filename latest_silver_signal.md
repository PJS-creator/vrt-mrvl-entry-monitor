# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-13**
- 실행시간(UTC): **2026-10-14 01:22:47**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 40.0 bp / latest 3.11
- IG OAS 4주 변화: 3.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 31.0 bp / latest 2.91
- VIX: 15.21
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -0.92% / slope_proxy: 0.007994
- GDXJ/GLD gap: -0.18% / slope_proxy: 0.012601

## VZLA (Vizsla Silver)
- close: 3.5 | RSI14: 39.698081 | ATR14%: 5.17%
- MA20 gap: -7.44% | MA50 gap: -8.57% | MA200 gap: -10.73%
- vol_ratio(Volume/Vol20): 0.223539 | gap_open: 0.85%
- RS vs SILJ gap: -0.51% / slope_proxy: 0.002787
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
- close: 8.89 | RSI14: 49.110452 | ATR14%: 6.18%
- MA20 gap: -0.34% | MA50 gap: -2.00% | MA200 gap: -1.11%
- vol_ratio(Volume/Vol20): 0.349653 | gap_open: 0.99%
- SilverMarginGate: SI=59.215 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.76% / slope_proxy: 0.020693
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
- close: 18.27 | RSI14: 38.987824 | ATR14%: 6.97%
- MA20 gap: -8.12% | MA50 gap: -19.39% | MA200 gap: -40.70%
- vol_ratio(Volume/Vol20): 0.542023 | gap_open: 0.99%
- RS vs SILJ gap: -12.83% / slope_proxy: -0.05444
- RS vs GDXJ gap: -15.44% / slope_proxy: -0.018337
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
