# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-16**
- 실행시간(UTC): **2026-11-17 04:45:47**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 3.23
- IG OAS 4주 변화: 4.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: 17.0 bp / latest 2.91
- VIX: 19.3
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 1.18% / slope_proxy: 0.004115
- GDXJ/GLD gap: -8.81% / slope_proxy: -0.001891

## VZLA (Vizsla Silver)
- close: 2.93 | RSI14: 37.866374 | ATR14%: 6.66%
- MA20 gap: -8.27% | MA50 gap: -16.64% | MA200 gap: -18.11%
- vol_ratio(Volume/Vol20): 2.446905 | gap_open: 2.12%
- RS vs SILJ gap: 2.11% / slope_proxy: 0.001968
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

## SCZM (Santacruz Silver)
- close: 6.42 | RSI14: 36.753319 | ATR14%: 8.12%
- MA20 gap: -12.13% | MA50 gap: -22.60% | MA200 gap: -24.01%
- vol_ratio(Volume/Vol20): 1.424428 | gap_open: 2.05%
- SilverMarginGate: SI=47.334999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.46% / slope_proxy: 0.006458
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
- close: 15.3 | RSI14: 40.159797 | ATR14%: 10.11%
- MA20 gap: -10.37% | MA50 gap: -18.04% | MA200 gap: -46.45%
- vol_ratio(Volume/Vol20): 1.601439 | gap_open: 3.27%
- RS vs SILJ gap: -1.52% / slope_proxy: -0.0495
- RS vs GDXJ gap: -5.84% / slope_proxy: -0.016526
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
