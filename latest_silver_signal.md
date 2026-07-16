# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-15**
- 실행시간(UTC): **2026-07-16 03:01:13**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.72
- IG OAS 4주 변화: 4.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.33
- VIX: 16.5
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 6.68% / slope_proxy: 0.009248
- GDXJ/GLD gap: -5.46% / slope_proxy: -0.004857

## VZLA (Vizsla Silver)
- close: 3.2 | RSI14: 46.42815 | ATR14%: 6.34%
- MA20 gap: -2.16% | MA50 gap: -7.45% | MA200 gap: -23.76%
- vol_ratio(Volume/Vol20): 0.675999 | gap_open: 0.00%
- RS vs SILJ gap: 5.25% / slope_proxy: 0.005337
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
- close: 6.35 | RSI14: 42.235487 | ATR14%: 7.25%
- MA20 gap: -5.05% | MA50 gap: -15.36% | MA200 gap: -25.28%
- vol_ratio(Volume/Vol20): 0.84819 | gap_open: 0.31%
- SilverMarginGate: SI=57.334999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.08% / slope_proxy: -0.005319
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
- close: 20.889999 | RSI14: 37.044797 | ATR14%: 9.56%
- MA20 gap: -9.07% | MA50 gap: -28.64% | MA200 gap: -22.57%
- vol_ratio(Volume/Vol20): 0.691257 | gap_open: 1.01%
- RS vs SILJ gap: -21.82% / slope_proxy: -0.108913
- RS vs GDXJ gap: -21.16% / slope_proxy: -0.02384
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
