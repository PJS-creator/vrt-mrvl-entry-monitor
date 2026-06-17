# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-16**
- 실행시간(UTC): **2026-06-17 03:00:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -17.0 bp / latest 2.66
- IG OAS 4주 변화: -2.0 bp / latest 0.73
- 10Y Real Yield 4주 변화: 2.0 bp / latest 2.15
- VIX: 16.2
- NFCI: -0.506

### Leadership ratios
- SILJ/SLV gap: 5.95% / slope_proxy: -0.005172
- GDXJ/GLD gap: 2.90% / slope_proxy: -0.006354

## VZLA (Vizsla Silver)
- close: 3.69 | RSI14: 53.199045 | ATR14%: 6.53%
- MA20 gap: 2.49% | MA50 gap: 5.14% | MA200 gap: -13.24%
- vol_ratio(Volume/Vol20): 0.737338 | gap_open: 0.00%
- RS vs SILJ gap: 7.18% / slope_proxy: 0.004379
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 7.97 | RSI14: 53.243688 | ATR14%: 7.80%
- MA20 gap: 5.91% | MA50 gap: -2.73% | MA200 gap: -5.99%
- vol_ratio(Volume/Vol20): 0.715407 | gap_open: 0.66%
- SilverMarginGate: SI=70.355003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.24% / slope_proxy: -0.011313
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
- close: 26.57 | RSI14: 39.186669 | ATR14%: 10.60%
- MA20 gap: -11.34% | MA50 gap: -24.96% | MA200 gap: 4.71%
- vol_ratio(Volume/Vol20): 1.084545 | gap_open: 0.72%
- RS vs SILJ gap: -23.47% / slope_proxy: -0.063476
- RS vs GDXJ gap: -21.92% / slope_proxy: -0.013677
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
