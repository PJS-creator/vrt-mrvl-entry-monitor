# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-03**
- 실행시간(UTC): **2026-11-03 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 34.0 bp / latest 3.44
- IG OAS 4주 변화: 9.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: -32.0 bp / latest 2.6
- VIX: 21.15
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -1.16% / slope_proxy: 0.005399
- GDXJ/GLD gap: -10.95% / slope_proxy: 0.005125

## VZLA (Vizsla Silver)
- close: 3.005 | RSI14: 35.309951 | ATR14%: 5.93%
- MA20 gap: -7.73% | MA50 gap: -17.99% | MA200 gap: -19.14%
- vol_ratio(Volume/Vol20): 0.10642 | gap_open: 0.16%
- RS vs SILJ gap: 2.14% / slope_proxy: 0.000324
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
- close: 6.8652 | RSI14: 35.452346 | ATR14%: 6.97%
- MA20 gap: -12.43% | MA50 gap: -21.45% | MA200 gap: -21.62%
- vol_ratio(Volume/Vol20): 0.233656 | gap_open: 2.01%
- SilverMarginGate: SI=50.049999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.19% / slope_proxy: 0.016152
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
- close: 16.35 | RSI14: 40.495432 | ATR14%: 7.09%
- MA20 gap: -3.93% | MA50 gap: -17.33% | MA200 gap: -45.26%
- vol_ratio(Volume/Vol20): 0.102696 | gap_open: 1.35%
- RS vs SILJ gap: -1.38% / slope_proxy: -0.049729
- RS vs GDXJ gap: -4.19% / slope_proxy: -0.01677
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
