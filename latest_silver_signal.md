# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-07**
- 실행시간(UTC): **2026-10-08 02:15:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 36.0 bp / latest 3.03
- IG OAS 4주 변화: 2.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 48.0 bp / latest 2.91
- VIX: 15.01
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.55% / slope_proxy: 0.00967
- GDXJ/GLD gap: -1.23% / slope_proxy: 0.01194

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 35.007594 | ATR14%: 5.76%
- MA20 gap: -11.02% | MA50 gap: -10.18% | MA200 gap: -13.48%
- vol_ratio(Volume/Vol20): 1.184851 | gap_open: 3.40%
- RS vs SILJ gap: 0.12% / slope_proxy: 0.002974
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
- close: 8.45 | RSI14: 43.302815 | ATR14%: 6.87%
- MA20 gap: -6.24% | MA50 gap: -5.40% | MA200 gap: -6.04%
- vol_ratio(Volume/Vol20): 1.38079 | gap_open: 4.46%
- SilverMarginGate: SI=60.654999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.75% / slope_proxy: 0.01941
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

## HYMC (Hycroft Mining)
- close: 17.959999 | RSI14: 34.962618 | ATR14%: 7.59%
- MA20 gap: -11.34% | MA50 gap: -20.97% | MA200 gap: -41.82%
- vol_ratio(Volume/Vol20): 0.980943 | gap_open: 5.32%
- RS vs SILJ gap: -12.46% / slope_proxy: -0.05952
- RS vs GDXJ gap: -14.95% / slope_proxy: -0.019577
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
