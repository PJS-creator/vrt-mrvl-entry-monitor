# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-24**
- 실행시간(UTC): **2026-04-24 15:01:11**

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
- 10Y Real Yield 4주 변화: -10.0 bp / latest 1.92
- VIX: 19.31
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.57% / slope_proxy: 0.014119
- GDXJ/GLD gap: -1.63% / slope_proxy: -0.004076

## VZLA (Vizsla Silver)
- close: 3.375 | RSI14: 47.071023 | ATR14%: 5.82%
- MA20 gap: 1.30% | MA50 gap: -5.88% | MA200 gap: -19.70%
- vol_ratio(Volume/Vol20): 0.193905 | gap_open: 1.21%
- RS vs SILJ gap: -5.49% / slope_proxy: -0.025617
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
- close: 8.66 | RSI14: 48.980966 | ATR14%: 7.96%
- MA20 gap: 2.80% | MA50 gap: -6.75% | MA200 gap: 11.69%
- vol_ratio(Volume/Vol20): 0.290081 | gap_open: 1.63%
- SilverMarginGate: SI=75.910004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.46% / slope_proxy: -0.02943
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
- close: 38.310001 | RSI14: 49.074842 | ATR14%: 9.52%
- MA20 gap: 0.50% | MA50 gap: -2.91% | MA200 gap: 91.74%
- vol_ratio(Volume/Vol20): 0.282035 | gap_open: 1.48%
- RS vs SILJ gap: 3.40% / slope_proxy: 0.052715
- RS vs GDXJ gap: 3.17% / slope_proxy: 0.010429
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
