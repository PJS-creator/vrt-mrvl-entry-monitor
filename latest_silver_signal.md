# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-15**
- 실행시간(UTC): **2026-04-15 15:01:25**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -38.0 bp / latest 2.84
- IG OAS 4주 변화: -11.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 5.0 bp / latest 1.92
- VIX: 18.36
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.08% / slope_proxy: 0.007587
- GDXJ/GLD gap: 1.87% / slope_proxy: -0.004501

## VZLA (Vizsla Silver)
- close: 3.455 | RSI14: 49.084953 | ATR14%: 6.05%
- MA20 gap: 6.55% | MA50 gap: -7.39% | MA200 gap: -17.48%
- vol_ratio(Volume/Vol20): 0.376137 | gap_open: 0.29%
- RS vs SILJ gap: -13.29% / slope_proxy: -0.027509
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 9.125 | RSI14: 54.133479 | ATR14%: 8.26%
- MA20 gap: 14.02% | MA50 gap: -5.76% | MA200 gap: 20.77%
- vol_ratio(Volume/Vol20): 0.400401 | gap_open: 0.44%
- SilverMarginGate: SI=80.214996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.62% / slope_proxy: -0.023819
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 41.48 | RSI14: 57.796665 | ATR14%: 9.34%
- MA20 gap: 17.24% | MA50 gap: 6.36% | MA200 gap: 122.13%
- vol_ratio(Volume/Vol20): 0.17667 | gap_open: 0.96%
- RS vs SILJ gap: 7.11% / slope_proxy: 0.098099
- RS vs GDXJ gap: 4.37% / slope_proxy: 0.024694
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
