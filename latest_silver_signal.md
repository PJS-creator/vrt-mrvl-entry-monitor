# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-08**
- 실행시간(UTC): **2026-10-09 02:32:50**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 38.0 bp / latest 3.09
- IG OAS 4주 변화: 1.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 46.0 bp / latest 2.92
- VIX: 15.08
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -0.41% / slope_proxy: 0.008736
- GDXJ/GLD gap: -0.55% / slope_proxy: 0.011984

## VZLA (Vizsla Silver)
- close: 3.47 | RSI14: 37.488905 | ATR14%: 5.50%
- MA20 gap: -9.09% | MA50 gap: -9.04% | MA200 gap: -12.00%
- vol_ratio(Volume/Vol20): 0.787826 | gap_open: 0.29%
- RS vs SILJ gap: -0.01% / slope_proxy: 0.002932
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
- close: 8.48 | RSI14: 43.719668 | ATR14%: 6.61%
- MA20 gap: -5.27% | MA50 gap: -5.53% | MA200 gap: -5.69%
- vol_ratio(Volume/Vol20): 1.043995 | gap_open: 1.07%
- SilverMarginGate: SI=60.395 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.07% / slope_proxy: 0.019545
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
- close: 18.209999 | RSI14: 36.638542 | ATR14%: 7.19%
- MA20 gap: -9.39% | MA50 gap: -19.81% | MA200 gap: -41.03%
- vol_ratio(Volume/Vol20): 1.228849 | gap_open: 1.11%
- RS vs SILJ gap: -12.32% / slope_proxy: -0.057707
- RS vs GDXJ gap: -14.75% / slope_proxy: -0.019172
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
