# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-25**
- 실행시간(UTC): **2026-06-25 15:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.71
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.29
- VIX: 18.63
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 9.88% / slope_proxy: 0.003558
- GDXJ/GLD gap: -4.42% / slope_proxy: -0.001862

## VZLA (Vizsla Silver)
- close: 3.165 | RSI14: 39.639893 | ATR14%: 7.11%
- MA20 gap: -11.52% | MA50 gap: -10.05% | MA200 gap: -25.40%
- vol_ratio(Volume/Vol20): 0.188374 | gap_open: 1.93%
- RS vs SILJ gap: 5.30% / slope_proxy: 0.004434
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
- close: 6.55 | RSI14: 40.639954 | ATR14%: 8.70%
- MA20 gap: -8.42% | MA50 gap: -18.39% | MA200 gap: -23.07%
- vol_ratio(Volume/Vol20): 0.167784 | gap_open: 2.37%
- SilverMarginGate: SI=57.845001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.24% / slope_proxy: -0.009636
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
- close: 22.35 | RSI14: 33.29951 | ATR14%: 10.74%
- MA20 gap: -18.00% | MA50 gap: -33.59% | MA200 gap: -13.82%
- vol_ratio(Volume/Vol20): 0.217888 | gap_open: 3.00%
- RS vs SILJ gap: -23.64% / slope_proxy: -0.078309
- RS vs GDXJ gap: -22.06% / slope_proxy: -0.016807
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
