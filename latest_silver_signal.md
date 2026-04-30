# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-30**
- 실행시간(UTC): **2026-04-30 15:01:20**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.82
- IG OAS 4주 변화: -6.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.92
- VIX: 18.81
- NFCI: -0.518

### Leadership ratios
- SILJ/SLV gap: -2.65% / slope_proxy: 0.014644
- GDXJ/GLD gap: -4.29% / slope_proxy: -0.003873

## VZLA (Vizsla Silver)
- close: 3.455 | RSI14: 50.329186 | ATR14%: 5.67%
- MA20 gap: 2.38% | MA50 gap: -3.06% | MA200 gap: -17.89%
- vol_ratio(Volume/Vol20): 0.200341 | gap_open: 3.24%
- RS vs SILJ gap: 4.42% / slope_proxy: -0.022511
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
- close: 7.885 | RSI14: 42.254626 | ATR14%: 8.08%
- MA20 gap: -6.25% | MA50 gap: -13.87% | MA200 gap: 0.61%
- vol_ratio(Volume/Vol20): 0.242071 | gap_open: 2.85%
- SilverMarginGate: SI=73.684998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.12% / slope_proxy: -0.031395
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
- close: 36.064999 | RSI14: 45.762236 | ATR14%: 9.40%
- MA20 gap: -6.62% | MA50 gap: -8.64% | MA200 gap: 74.88%
- vol_ratio(Volume/Vol20): 0.204034 | gap_open: 5.99%
- RS vs SILJ gap: 2.43% / slope_proxy: 0.03727
- RS vs GDXJ gap: 2.33% / slope_proxy: 0.005751
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
