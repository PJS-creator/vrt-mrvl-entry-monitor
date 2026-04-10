# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-10**
- 실행시간(UTC): **2026-04-10 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -27.0 bp / latest 2.9
- IG OAS 4주 변화: -8.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 11.0 bp / latest 1.96
- VIX: 19.49
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 2.57% / slope_proxy: 0.003447
- GDXJ/GLD gap: 0.77% / slope_proxy: -0.004738

## VZLA (Vizsla Silver)
- close: 3.285 | RSI14: 41.834005 | ATR14%: 6.64%
- MA20 gap: 0.36% | MA50 gap: -14.58% | MA200 gap: -21.41%
- vol_ratio(Volume/Vol20): 0.173809 | gap_open: 1.53%
- RS vs SILJ gap: -17.96% / slope_proxy: -0.027483
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.05 | RSI14: 43.889521 | ATR14%: 9.59%
- MA20 gap: 0.47% | MA50 gap: -18.66% | MA200 gap: 7.85%
- vol_ratio(Volume/Vol20): 0.103115 | gap_open: 0.12%
- SilverMarginGate: SI=76.580002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.16% / slope_proxy: -0.022858
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
- close: 38.450001 | RSI14: 53.019312 | ATR14%: 10.69%
- MA20 gap: 9.34% | MA50 gap: -1.24% | MA200 gap: 112.28%
- vol_ratio(Volume/Vol20): 0.25409 | gap_open: 0.18%
- RS vs SILJ gap: 2.82% / slope_proxy: 0.124681
- RS vs GDXJ gap: -0.78% / slope_proxy: 0.032372
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
