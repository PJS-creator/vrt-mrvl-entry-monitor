# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-17**
- 실행시간(UTC): **2026-06-17 15:01:06**

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
- 10Y Real Yield 4주 변화: 2.0 bp / latest 2.15
- VIX: 16.41
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 7.81% / slope_proxy: -0.005032
- GDXJ/GLD gap: 4.77% / slope_proxy: -0.005392

## VZLA (Vizsla Silver)
- close: 3.765 | RSI14: 55.012614 | ATR14%: 6.47%
- MA20 gap: 4.46% | MA50 gap: 7.23% | MA200 gap: -11.48%
- vol_ratio(Volume/Vol20): 0.301841 | gap_open: 1.37%
- RS vs SILJ gap: 7.05% / slope_proxy: 0.004377
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 8.08 | RSI14: 54.260701 | ATR14%: 7.80%
- MA20 gap: 7.30% | MA50 gap: -1.41% | MA200 gap: -4.70%
- vol_ratio(Volume/Vol20): 0.161171 | gap_open: 3.84%
- SilverMarginGate: SI=70.510002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.97% / slope_proxy: -0.011346
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
- close: 26.700001 | RSI14: 39.420316 | ATR14%: 10.35%
- MA20 gap: -10.92% | MA50 gap: -24.59% | MA200 gap: 5.22%
- vol_ratio(Volume/Vol20): 0.186581 | gap_open: 6.25%
- RS vs SILJ gap: -24.71% / slope_proxy: -0.063719
- RS vs GDXJ gap: -23.24% / slope_proxy: -0.013743
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
