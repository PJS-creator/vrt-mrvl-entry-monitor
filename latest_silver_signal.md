# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-07**
- 실행시간(UTC): **2026-04-07 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -14.0 bp / latest 3.05
- IG OAS 4주 변화: 0.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: 19.0 bp / latest 1.99
- VIX: 24.17
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 6.49% / slope_proxy: -0.00044
- GDXJ/GLD gap: -2.77% / slope_proxy: -0.004352

## VZLA (Vizsla Silver)
- close: 3.1701 | RSI14: 37.926684 | ATR14%: 7.36%
- MA20 gap: -6.29% | MA50 gap: -21.71% | MA200 gap: -24.10%
- vol_ratio(Volume/Vol20): 0.281167 | gap_open: 1.21%
- RS vs SILJ gap: -19.67% / slope_proxy: -0.027472
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

## SCZM (Santacruz Silver)
- close: 7.67 | RSI14: 40.639822 | ATR14%: 10.65%
- MA20 gap: -7.91% | MA50 gap: -25.88% | MA200 gap: 3.86%
- vol_ratio(Volume/Vol20): 0.185449 | gap_open: 0.61%
- SilverMarginGate: SI=71.095001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -19.63% / slope_proxy: -0.02208
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
- close: 35.1782 | RSI14: 47.555473 | ATR14%: 11.61%
- MA20 gap: -1.61% | MA50 gap: -11.47% | MA200 gap: 100.08%
- vol_ratio(Volume/Vol20): 0.195585 | gap_open: 2.64%
- RS vs SILJ gap: -0.64% / slope_proxy: 0.151625
- RS vs GDXJ gap: -2.33% / slope_proxy: 0.039979
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
