# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-09**
- 실행시간(UTC): **2026-03-09 15:01:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 26.0 bp / latest 3.13
- IG OAS 4주 변화: 8.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -7.0 bp / latest 1.82
- VIX: 29.49
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: -2.64% / slope_proxy: -0.002992
- GDXJ/GLD gap: -4.70% / slope_proxy: 0.013271

## VZLA (Vizsla Silver)
- close: 3.825 | RSI14: 38.330001 | ATR14%: 8.72%
- MA20 gap: -3.82% | MA50 gap: -24.21% | MA200 gap: -8.00%
- vol_ratio(Volume/Vol20): 0.162263 | gap_open: 3.00%
- RS vs SILJ gap: -26.69% / slope_proxy: -0.028911
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 9.72 | RSI14: 40.547008 | ATR14%: 10.76%
- MA20 gap: -11.44% | MA50 gap: -15.24% | MA200 gap: 42.92%
- vol_ratio(Volume/Vol20): 0.513277 | gap_open: 4.39%
- SilverMarginGate: SI=84.754997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -12.91% / slope_proxy: 0.009961
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
- close: 37.560001 | RSI14: 44.818894 | ATR14%: 15.17%
- MA20 gap: -11.07% | MA50 gap: -1.33% | MA200 gap: 161.97%
- vol_ratio(Volume/Vol20): 0.26776 | gap_open: 2.69%
- RS vs SILJ gap: 11.45% / slope_proxy: 0.245432
- RS vs GDXJ gap: 10.17% / slope_proxy: 0.064453
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
