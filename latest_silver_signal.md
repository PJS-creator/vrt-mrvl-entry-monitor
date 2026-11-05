# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-04**
- 실행시간(UTC): **2026-11-05 03:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 37.0 bp / latest 3.4
- IG OAS 4주 변화: 10.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -26.0 bp / latest 2.65
- VIX: 20.83
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 2.26% / slope_proxy: 0.005271
- GDXJ/GLD gap: -6.21% / slope_proxy: 0.004404

## VZLA (Vizsla Silver)
- close: 3.29 | RSI14: 47.860766 | ATR14%: 5.75%
- MA20 gap: 1.18% | MA50 gap: -9.85% | MA200 gap: -11.09%
- vol_ratio(Volume/Vol20): 1.384477 | gap_open: 7.26%
- RS vs SILJ gap: 3.32% / slope_proxy: 0.000416
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
- close: 7.69 | RSI14: 47.719325 | ATR14%: 6.73%
- MA20 gap: -1.37% | MA50 gap: -11.58% | MA200 gap: -11.96%
- vol_ratio(Volume/Vol20): 1.156327 | gap_open: 8.49%
- SilverMarginGate: SI=53.314999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.28% / slope_proxy: 0.01526
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
- close: 17.469999 | RSI14: 48.514743 | ATR14%: 7.10%
- MA20 gap: 2.88% | MA50 gap: -10.87% | MA200 gap: -41.25%
- vol_ratio(Volume/Vol20): 1.353811 | gap_open: 9.01%
- RS vs SILJ gap: -2.06% / slope_proxy: -0.050189
- RS vs GDXJ gap: -5.09% / slope_proxy: -0.016901
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
