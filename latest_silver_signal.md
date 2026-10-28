# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-27**
- 실행시간(UTC): **2026-10-28 01:40:32**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 28.0 bp / latest 3.3
- IG OAS 4주 변화: 7.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: -24.0 bp / latest 2.66
- VIX: 18.39
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -2.24% / slope_proxy: 0.007101
- GDXJ/GLD gap: -7.33% / slope_proxy: 0.009364

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 42.811236 | ATR14%: 5.59%
- MA20 gap: -3.64% | MA50 gap: -12.72% | MA200 gap: -13.92%
- vol_ratio(Volume/Vol20): 0.847149 | gap_open: 0.98%
- RS vs SILJ gap: 3.33% / slope_proxy: 0.000808
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
- close: 7.51 | RSI14: 40.227979 | ATR14%: 6.89%
- MA20 gap: -9.35% | MA50 gap: -16.30% | MA200 gap: -15.29%
- vol_ratio(Volume/Vol20): 0.897923 | gap_open: 0.14%
- SilverMarginGate: SI=54.389999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.16% / slope_proxy: 0.020605
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
- close: 16.9 | RSI14: 42.544344 | ATR14%: 7.15%
- MA20 gap: -3.74% | MA50 gap: -18.45% | MA200 gap: -44.22%
- vol_ratio(Volume/Vol20): 1.204895 | gap_open: 0.26%
- RS vs SILJ gap: -7.01% / slope_proxy: -0.048539
- RS vs GDXJ gap: -10.28% / slope_proxy: -0.016537
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
