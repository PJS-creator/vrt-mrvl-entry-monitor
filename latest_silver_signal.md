# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-29**
- 실행시간(UTC): **2026-09-29 15:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 39.0 bp / latest 3.02
- IG OAS 4주 변화: 3.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 41.0 bp / latest 2.83
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: -0.62% / slope_proxy: 0.016988
- GDXJ/GLD gap: 3.58% / slope_proxy: 0.014352

## VZLA (Vizsla Silver)
- close: 3.805 | RSI14: 46.092794 | ATR14%: 5.28%
- MA20 gap: -4.37% | MA50 gap: 0.93% | MA200 gap: -4.88%
- vol_ratio(Volume/Vol20): 0.162978 | gap_open: 0.26%
- RS vs SILJ gap: 7.67% / slope_proxy: 0.0018
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
- close: 8.9 | RSI14: 47.927523 | ATR14%: 7.19%
- MA20 gap: -5.13% | MA50 gap: 2.87% | MA200 gap: -1.20%
- vol_ratio(Volume/Vol20): 0.144856 | gap_open: 0.55%
- SilverMarginGate: SI=61.580002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.45% / slope_proxy: 0.01972
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
- close: 19.110001 | RSI14: 38.317289 | ATR14%: 8.16%
- MA20 gap: -10.90% | MA50 gap: -16.71% | MA200 gap: -37.78%
- vol_ratio(Volume/Vol20): 0.270518 | gap_open: 0.61%
- RS vs SILJ gap: -12.39% / slope_proxy: -0.068734
- RS vs GDXJ gap: -16.34% / slope_proxy: -0.02183
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
