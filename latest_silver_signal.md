# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-05**
- 실행시간(UTC): **2026-03-05 15:01:46**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.08
- IG OAS 4주 변화: 10.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -15.0 bp / latest 1.77
- VIX: 21.15
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 5.94% / slope_proxy: -0.002848
- GDXJ/GLD gap: 0.43% / slope_proxy: 0.013786

## VZLA (Vizsla Silver)
- close: 4.11 | RSI14: 43.138977 | ATR14%: 8.12%
- MA20 gap: 1.93% | MA50 gap: -19.76% | MA200 gap: -0.81%
- vol_ratio(Volume/Vol20): 0.044493 | gap_open: 2.40%
- RS vs SILJ gap: -28.08% / slope_proxy: -0.027611
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.008 | RSI14: 41.924221 | ATR14%: 10.82%
- MA20 gap: -9.54% | MA50 gap: -12.55% | MA200 gap: 48.97%
- vol_ratio(Volume/Vol20): 0.184106 | gap_open: 2.12%
- SilverMarginGate: SI=82.540001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.00% / slope_proxy: 0.014401
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 45.654999 | RSI14: 54.180073 | ATR14%: 12.54%
- MA20 gap: 8.54% | MA50 gap: 21.21% | MA200 gap: 225.96%
- vol_ratio(Volume/Vol20): 0.149284 | gap_open: 2.17%
- RS vs SILJ gap: 28.54% / slope_proxy: 0.248389
- RS vs GDXJ gap: 29.42% / slope_proxy: 0.06543
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
