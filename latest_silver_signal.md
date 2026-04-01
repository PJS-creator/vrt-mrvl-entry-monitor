# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-01**
- 실행시간(UTC): **2026-04-01 15:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.28
- IG OAS 4주 변화: 6.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.04
- VIX: 25.25
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 3.87% / slope_proxy: -0.003685
- GDXJ/GLD gap: -1.30% / slope_proxy: -0.002768

## VZLA (Vizsla Silver)
- close: 3.37 | RSI14: 42.604907 | ATR14%: 7.33%
- MA20 gap: -3.76% | MA50 gap: -20.46% | MA200 gap: -19.39%
- vol_ratio(Volume/Vol20): 0.294 | gap_open: 3.03%
- RS vs SILJ gap: -20.12% / slope_proxy: -0.027347
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
- close: 8.59 | RSI14: 46.022252 | ATR14%: 9.91%
- MA20 gap: -0.97% | MA50 gap: -19.97% | MA200 gap: 17.45%
- vol_ratio(Volume/Vol20): 0.414574 | gap_open: 3.62%
- SilverMarginGate: SI=75.410004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.18% / slope_proxy: -0.02002
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
- close: 36.02 | RSI14: 48.801555 | ATR14%: 12.02%
- MA20 gap: -1.22% | MA50 gap: -10.73% | MA200 gap: 110.67%
- vol_ratio(Volume/Vol20): 0.237223 | gap_open: 3.41%
- RS vs SILJ gap: -0.73% / slope_proxy: 0.176026
- RS vs GDXJ gap: -3.29% / slope_proxy: 0.046181
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
