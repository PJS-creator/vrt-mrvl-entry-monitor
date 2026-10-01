# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-01**
- 실행시간(UTC): **2026-10-01 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 46.0 bp / latest 3.12
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 47.0 bp / latest 2.91
- VIX: 16.34
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: -1.02% / slope_proxy: 0.014849
- GDXJ/GLD gap: 1.48% / slope_proxy: 0.013736

## VZLA (Vizsla Silver)
- close: 3.745 | RSI14: 44.158566 | ATR14%: 5.11%
- MA20 gap: -5.35% | MA50 gap: -1.12% | MA200 gap: -6.03%
- vol_ratio(Volume/Vol20): 0.350984 | gap_open: 0.00%
- RS vs SILJ gap: 6.61% / slope_proxy: 0.00234
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
- close: 8.67 | RSI14: 45.694451 | ATR14%: 7.01%
- MA20 gap: -6.69% | MA50 gap: -0.76% | MA200 gap: -3.60%
- vol_ratio(Volume/Vol20): 0.182434 | gap_open: 0.34%
- SilverMarginGate: SI=61.290001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.83% / slope_proxy: 0.019586
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
- close: 19.065001 | RSI14: 38.173669 | ATR14%: 7.69%
- MA20 gap: -9.75% | MA50 gap: -16.61% | MA200 gap: -38.05%
- vol_ratio(Volume/Vol20): 0.112659 | gap_open: 0.26%
- RS vs SILJ gap: -11.12% / slope_proxy: -0.064633
- RS vs GDXJ gap: -14.22% / slope_proxy: -0.020762
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
