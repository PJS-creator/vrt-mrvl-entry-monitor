# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-22**
- 실행시간(UTC): **2026-06-22 15:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -17.0 bp / latest 2.63
- IG OAS 4주 변화: -1.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.23
- VIX: 16.78
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 4.59% / slope_proxy: -0.001483
- GDXJ/GLD gap: -1.71% / slope_proxy: -0.004076

## VZLA (Vizsla Silver)
- close: 3.545 | RSI14: 48.998344 | ATR14%: 6.45%
- MA20 gap: -2.42% | MA50 gap: 0.51% | MA200 gap: -16.59%
- vol_ratio(Volume/Vol20): 0.179833 | gap_open: 0.85%
- RS vs SILJ gap: 9.71% / slope_proxy: 0.004516
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
- close: 7.025 | RSI14: 43.794832 | ATR14%: 8.64%
- MA20 gap: -4.67% | MA50 gap: -13.79% | MA200 gap: -17.39%
- vol_ratio(Volume/Vol20): 0.480615 | gap_open: 2.10%
- SilverMarginGate: SI=66.169998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.29% / slope_proxy: -0.010483
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
- close: 25.225 | RSI14: 37.162729 | ATR14%: 10.16%
- MA20 gap: -12.36% | MA50 gap: -27.29% | MA200 gap: -1.78%
- vol_ratio(Volume/Vol20): 0.186489 | gap_open: 3.52%
- RS vs SILJ gap: -21.19% / slope_proxy: -0.07411
- RS vs GDXJ gap: -19.16% / slope_proxy: -0.016162
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
