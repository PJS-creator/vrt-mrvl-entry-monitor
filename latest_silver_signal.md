# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-23**
- 실행시간(UTC): **2026-10-25 03:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 60.0 bp / latest 3.4
- IG OAS 4주 변화: 10.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: -21.0 bp / latest 2.64
- VIX: 19.03
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.91% / slope_proxy: 0.007114
- GDXJ/GLD gap: -9.48% / slope_proxy: 0.009913

## VZLA (Vizsla Silver)
- close: 3.09 | RSI14: 34.513834 | ATR14%: 6.00%
- MA20 gap: -10.42% | MA50 gap: -17.75% | MA200 gap: -18.93%
- vol_ratio(Volume/Vol20): 1.75812 | gap_open: 0.63%
- RS vs SILJ gap: 2.86% / slope_proxy: 0.001228
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
- close: 6.95 | RSI14: 31.433038 | ATR14%: 7.76%
- MA20 gap: -17.82% | MA50 gap: -23.06% | MA200 gap: -21.86%
- vol_ratio(Volume/Vol20): 1.094708 | gap_open: 0.56%
- SilverMarginGate: SI=53.710999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.64% / slope_proxy: 0.021826
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
- close: 15.44 | RSI14: 31.926394 | ATR14%: 7.80%
- MA20 gap: -13.70% | MA50 gap: -26.98% | MA200 gap: -49.22%
- vol_ratio(Volume/Vol20): 0.855872 | gap_open: 1.65%
- RS vs SILJ gap: -11.39% / slope_proxy: -0.049709
- RS vs GDXJ gap: -15.41% / slope_proxy: -0.016873
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
