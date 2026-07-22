# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-21**
- 실행시간(UTC): **2026-07-22 03:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 4.0 bp / latest 2.69
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 7.0 bp / latest 2.35
- VIX: 18.65
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 4.44% / slope_proxy: 0.008487
- GDXJ/GLD gap: -4.73% / slope_proxy: -0.008119

## VZLA (Vizsla Silver)
- close: 3.29 | RSI14: 51.120969 | ATR14%: 5.89%
- MA20 gap: 3.38% | MA50 gap: -4.35% | MA200 gap: -21.16%
- vol_ratio(Volume/Vol20): 1.120763 | gap_open: 3.49%
- RS vs SILJ gap: 7.09% / slope_proxy: 0.00594
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 6.56 | RSI14: 48.579115 | ATR14%: 6.85%
- MA20 gap: 2.05% | MA50 gap: -10.47% | MA200 gap: -22.49%
- vol_ratio(Volume/Vol20): 1.042288 | gap_open: 4.99%
- SilverMarginGate: SI=59.919998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.12% / slope_proxy: -0.005934
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 20.719999 | RSI14: 41.766907 | ATR14%: 9.26%
- MA20 gap: -4.35% | MA50 gap: -25.50% | MA200 gap: -23.93%
- vol_ratio(Volume/Vol20): 0.713611 | gap_open: 3.04%
- RS vs SILJ gap: -19.87% / slope_proxy: -0.123652
- RS vs GDXJ gap: -19.97% / slope_proxy: -0.027561
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
