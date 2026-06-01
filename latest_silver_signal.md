# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-01**
- 실행시간(UTC): **2026-06-01 15:01:52**

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
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.06
- VIX: 15.32
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -0.26% / slope_proxy: -0.013616
- GDXJ/GLD gap: -2.31% / slope_proxy: -0.00626

## VZLA (Vizsla Silver)
- close: 3.9501 | RSI14: 62.650734 | ATR14%: 5.72%
- MA20 gap: 10.49% | MA50 gap: 15.62% | MA200 gap: -6.92%
- vol_ratio(Volume/Vol20): 0.814516 | gap_open: 1.29%
- RS vs SILJ gap: 17.83% / slope_proxy: 0.000963
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
- close: 7.76 | RSI14: 40.941713 | ATR14%: 7.50%
- MA20 gap: -9.51% | MA50 gap: -7.15% | MA200 gap: -6.78%
- vol_ratio(Volume/Vol20): 0.238642 | gap_open: 1.47%
- SilverMarginGate: SI=74.5 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.45% / slope_proxy: -0.010621
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
- close: 32.41 | RSI14: 41.279375 | ATR14%: 8.90%
- MA20 gap: -10.97% | MA50 gap: -11.66% | MA200 gap: 34.60%
- vol_ratio(Volume/Vol20): 0.267219 | gap_open: 3.78%
- RS vs SILJ gap: -9.35% / slope_proxy: 0.004637
- RS vs GDXJ gap: -5.65% / slope_proxy: 0.003196
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
