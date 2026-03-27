# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-27**
- 실행시간(UTC): **2026-03-27 15:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.21
- IG OAS 4주 변화: 6.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 25.0 bp / latest 2.02
- VIX: 27.44
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: -0.23% / slope_proxy: -0.004519
- GDXJ/GLD gap: -8.13% / slope_proxy: -0.000503

## VZLA (Vizsla Silver)
- close: 3.19 | RSI14: 36.154522 | ATR14%: 8.25%
- MA20 gap: -12.45% | MA50 gap: -27.76% | MA200 gap: -23.75%
- vol_ratio(Volume/Vol20): 0.174739 | gap_open: 0.00%
- RS vs SILJ gap: -18.26% / slope_proxy: -0.027233
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.5899 | RSI14: 36.37069 | ATR14%: 11.31%
- MA20 gap: -16.68% | MA50 gap: -30.65% | MA200 gap: 4.95%
- vol_ratio(Volume/Vol20): 0.139226 | gap_open: 0.14%
- SilverMarginGate: SI=69.75 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.20% / slope_proxy: -0.018338
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 33.209999 | RSI14: 43.568746 | ATR14%: 13.41%
- MA20 gap: -14.81% | MA50 gap: -18.12% | MA200 gap: 99.53%
- vol_ratio(Volume/Vol20): 0.185473 | gap_open: 1.51%
- RS vs SILJ gap: 3.19% / slope_proxy: 0.208387
- RS vs GDXJ gap: 2.08% / slope_proxy: 0.054721
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
