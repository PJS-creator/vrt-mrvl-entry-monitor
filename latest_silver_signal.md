# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-24**
- 실행시간(UTC): **2026-04-26 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.86
- IG OAS 4주 변화: -8.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -16.0 bp / latest 1.92
- VIX: 19.31
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.64% / slope_proxy: 0.014115
- GDXJ/GLD gap: -0.84% / slope_proxy: -0.004037

## VZLA (Vizsla Silver)
- close: 3.35 | RSI14: 46.080078 | ATR14%: 5.87%
- MA20 gap: 0.59% | MA50 gap: -6.57% | MA200 gap: -20.29%
- vol_ratio(Volume/Vol20): 0.565505 | gap_open: 1.21%
- RS vs SILJ gap: -6.32% / slope_proxy: -0.025634
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.49 | RSI14: 47.309521 | ATR14%: 8.14%
- MA20 gap: 0.88% | MA50 gap: -8.54% | MA200 gap: 9.51%
- vol_ratio(Volume/Vol20): 0.63151 | gap_open: 1.63%
- SilverMarginGate: SI=76.383003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.42% / slope_proxy: -0.029529
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
- close: 38.040001 | RSI14: 48.552426 | ATR14%: 9.71%
- MA20 gap: -0.17% | MA50 gap: -3.58% | MA200 gap: 90.40%
- vol_ratio(Volume/Vol20): 0.606351 | gap_open: 1.48%
- RS vs SILJ gap: 2.54% / slope_proxy: 0.052539
- RS vs GDXJ gap: 1.79% / slope_proxy: 0.010358
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
