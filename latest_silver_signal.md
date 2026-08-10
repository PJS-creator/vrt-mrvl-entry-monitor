# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-10**
- 실행시간(UTC): **2026-08-10 15:01:30**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.71
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.43
- VIX: 14.9
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 9.09% / slope_proxy: 0.012103
- GDXJ/GLD gap: 9.30% / slope_proxy: -0.006555

## VZLA (Vizsla Silver)
- close: 3.8699 | RSI14: 66.595666 | ATR14%: 5.09%
- MA20 gap: 16.67% | MA50 gap: 14.39% | MA200 gap: -5.34%
- vol_ratio(Volume/Vol20): 0.370671 | gap_open: 0.27%
- RS vs SILJ gap: 3.64% / slope_proxy: 0.006105
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
- close: 8.75 | RSI14: 72.691361 | ATR14%: 5.77%
- MA20 gap: 28.66% | MA50 gap: 27.67% | MA200 gap: 3.35%
- vol_ratio(Volume/Vol20): 0.618351 | gap_open: 1.19%
- SilverMarginGate: SI=64.894997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.75% / slope_proxy: -0.004335
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
- close: 26.75 | RSI14: 64.247215 | ATR14%: 6.89%
- MA20 gap: 25.59% | MA50 gap: 12.94% | MA200 gap: -5.30%
- vol_ratio(Volume/Vol20): 0.401348 | gap_open: 0.94%
- RS vs SILJ gap: -3.06% / slope_proxy: -0.144557
- RS vs GDXJ gap: -5.49% / slope_proxy: -0.036218
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
