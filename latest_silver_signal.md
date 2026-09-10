# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-10**
- 실행시간(UTC): **2026-09-10 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.71
- IG OAS 4주 변화: 2.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 0.0 bp / latest 2.43
- VIX: 15.72
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 8.48% / slope_proxy: 0.028287
- GDXJ/GLD gap: 11.63% / slope_proxy: 0.013397

## VZLA (Vizsla Silver)
- close: 3.9699 | RSI14: 53.778164 | ATR14%: 5.05%
- MA20 gap: 0.55% | MA50 gap: 11.41% | MA200 gap: -2.19%
- vol_ratio(Volume/Vol20): 0.24848 | gap_open: 3.91%
- RS vs SILJ gap: 0.59% / slope_proxy: 0.000164
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
- close: 9.9634 | RSI14: 58.866759 | ATR14%: 5.90%
- MA20 gap: 3.98% | MA50 gap: 25.15% | MA200 gap: 11.79%
- vol_ratio(Volume/Vol20): 0.354183 | gap_open: 4.79%
- SilverMarginGate: SI=64.875 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 15.67% / slope_proxy: 0.014045
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
- close: 21.93 | RSI14: 42.013381 | ATR14%: 8.04%
- MA20 gap: -11.27% | MA50 gap: -4.82% | MA200 gap: -27.10%
- vol_ratio(Volume/Vol20): 0.274512 | gap_open: 5.39%
- RS vs SILJ gap: -15.55% / slope_proxy: -0.089741
- RS vs GDXJ gap: -17.78% / slope_proxy: -0.027174
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
