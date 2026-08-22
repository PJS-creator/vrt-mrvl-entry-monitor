# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-21**
- 실행시간(UTC): **2026-08-22 22:55:31**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.75
- IG OAS 4주 변화: 3.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -8.0 bp / latest 2.35
- VIX: 16.01
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 7.41% / slope_proxy: 0.020483
- GDXJ/GLD gap: 15.00% / slope_proxy: 0.001335

## VZLA (Vizsla Silver)
- close: 3.96 | RSI14: 64.080169 | ATR14%: 4.71%
- MA20 gap: 10.80% | MA50 gap: 16.37% | MA200 gap: -2.80%
- vol_ratio(Volume/Vol20): 2.171241 | gap_open: 3.36%
- RS vs SILJ gap: -2.84% / slope_proxy: 0.004125
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

## SCZM (Santacruz Silver)
- close: 9.675 | RSI14: 70.575673 | ATR14%: 5.74%
- MA20 gap: 20.07% | MA50 gap: 34.39% | MA200 gap: 12.26%
- vol_ratio(Volume/Vol20): 1.422385 | gap_open: 5.12%
- SilverMarginGate: SI=69.466003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.10% / slope_proxy: 0.001645
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
- close: 27.07 | RSI14: 57.575152 | ATR14%: 7.18%
- MA20 gap: 11.71% | MA50 gap: 16.45% | MA200 gap: -7.01%
- vol_ratio(Volume/Vol20): 1.520446 | gap_open: 4.82%
- RS vs SILJ gap: -5.24% / slope_proxy: -0.116911
- RS vs GDXJ gap: -11.20% / slope_proxy: -0.031847
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
