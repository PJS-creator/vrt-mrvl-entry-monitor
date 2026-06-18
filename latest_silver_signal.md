# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-17**
- 실행시간(UTC): **2026-06-18 03:00:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -15.0 bp / latest 2.71
- IG OAS 4주 변화: -1.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: -4.0 bp / latest 2.14
- VIX: 16.41
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 6.58% / slope_proxy: -0.004057
- GDXJ/GLD gap: 0.95% / slope_proxy: -0.005574

## VZLA (Vizsla Silver)
- close: 3.58 | RSI14: 50.014444 | ATR14%: 6.79%
- MA20 gap: -1.01% | MA50 gap: 1.80% | MA200 gap: -15.82%
- vol_ratio(Volume/Vol20): 1.026396 | gap_open: 0.27%
- RS vs SILJ gap: 7.79% / slope_proxy: 0.004426
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
- close: 7.49 | RSI14: 48.206636 | ATR14%: 8.48%
- MA20 gap: 0.03% | MA50 gap: -8.50% | MA200 gap: -11.77%
- vol_ratio(Volume/Vol20): 0.752799 | gap_open: 1.63%
- SilverMarginGate: SI=68.945 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.53% / slope_proxy: -0.010886
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
- close: 25.57 | RSI14: 37.352661 | ATR14%: 10.89%
- MA20 gap: -13.58% | MA50 gap: -27.33% | MA200 gap: 0.35%
- vol_ratio(Volume/Vol20): 1.2069 | gap_open: 1.77%
- RS vs SILJ gap: -23.22% / slope_proxy: -0.068644
- RS vs GDXJ gap: -21.42% / slope_proxy: -0.014903
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
