# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-23**
- 실행시간(UTC): **2026-03-23 15:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 38.0 bp / latest 3.24
- IG OAS 4주 변화: 10.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.88
- VIX: 26.78
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: 0.32% / slope_proxy: -0.006721
- GDXJ/GLD gap: -7.17% / slope_proxy: 0.004016

## VZLA (Vizsla Silver)
- close: 3.175 | RSI14: 32.399013 | ATR14%: 9.15%
- MA20 gap: -17.25% | MA50 gap: -31.44% | MA200 gap: -24.24%
- vol_ratio(Volume/Vol20): 0.458199 | gap_open: 1.33%
- RS vs SILJ gap: -21.95% / slope_proxy: -0.027554
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
- close: 7.74 | RSI14: 34.486331 | ATR14%: 12.01%
- MA20 gap: -22.87% | MA50 gap: -30.98% | MA200 gap: 8.45%
- vol_ratio(Volume/Vol20): 0.595917 | gap_open: 1.96%
- SilverMarginGate: SI=70.050003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.15% / slope_proxy: -0.01031
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
- close: 32.259998 | RSI14: 40.633525 | ATR14%: 15.05%
- MA20 gap: -23.51% | MA50 gap: -20.32% | MA200 gap: 100.75%
- vol_ratio(Volume/Vol20): 0.41163 | gap_open: 1.70%
- RS vs SILJ gap: 2.12% / slope_proxy: 0.23944
- RS vs GDXJ gap: 0.57% / slope_proxy: 0.062889
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
