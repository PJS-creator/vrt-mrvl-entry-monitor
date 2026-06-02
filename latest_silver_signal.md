# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-01**
- 실행시간(UTC): **2026-06-02 03:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.74
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 15.32
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 2.27% / slope_proxy: -0.013427
- GDXJ/GLD gap: -0.53% / slope_proxy: -0.006175

## VZLA (Vizsla Silver)
- close: 4.05 | RSI14: 64.859113 | ATR14%: 5.81%
- MA20 gap: 13.13% | MA50 gap: 18.48% | MA200 gap: -4.58%
- vol_ratio(Volume/Vol20): 1.615957 | gap_open: 1.29%
- RS vs SILJ gap: 17.05% / slope_proxy: 0.000948
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
- close: 8.14 | RSI14: 45.152256 | ATR14%: 7.30%
- MA20 gap: -5.29% | MA50 gap: -2.69% | MA200 gap: -2.24%
- vol_ratio(Volume/Vol20): 0.773437 | gap_open: 1.47%
- SilverMarginGate: SI=75.245003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.95% / slope_proxy: -0.01055
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
- close: 32.84 | RSI14: 42.120106 | ATR14%: 9.01%
- MA20 gap: -9.84% | MA50 gap: -10.51% | MA200 gap: 36.37%
- vol_ratio(Volume/Vol20): 0.739017 | gap_open: 3.78%
- RS vs SILJ gap: -11.00% / slope_proxy: 0.0043
- RS vs GDXJ gap: -6.59% / slope_proxy: 0.003148
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
