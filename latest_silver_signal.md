# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-29**
- 실행시간(UTC): **2026-06-30 03:01:14**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 11.0 bp / latest 2.83
- IG OAS 4주 변화: 4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 11.0 bp / latest 2.18
- VIX: 18.41
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 9.47% / slope_proxy: 0.006258
- GDXJ/GLD gap: -3.98% / slope_proxy: -0.001719

## VZLA (Vizsla Silver)
- close: 3.27 | RSI14: 43.463179 | ATR14%: 6.65%
- MA20 gap: -7.10% | MA50 gap: -6.89% | MA200 gap: -22.85%
- vol_ratio(Volume/Vol20): 0.464417 | gap_open: 0.91%
- RS vs SILJ gap: 7.66% / slope_proxy: 0.004565
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
- close: 6.51 | RSI14: 40.563107 | ATR14%: 8.30%
- MA20 gap: -6.85% | MA50 gap: -17.90% | MA200 gap: -23.56%
- vol_ratio(Volume/Vol20): 0.510439 | gap_open: 1.06%
- SilverMarginGate: SI=57.830002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.08% / slope_proxy: -0.009486
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
- close: 23.379999 | RSI14: 37.419954 | ATR14%: 10.06%
- MA20 gap: -11.03% | MA50 gap: -29.08% | MA200 gap: -10.46%
- vol_ratio(Volume/Vol20): 0.696631 | gap_open: 4.04%
- RS vs SILJ gap: -19.97% / slope_proxy: -0.078905
- RS vs GDXJ gap: -18.33% / slope_proxy: -0.016661
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
