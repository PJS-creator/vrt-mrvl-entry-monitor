# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-10**
- 실행시간(UTC): **2026-03-10 15:01:17**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 35.0 bp / latest 3.19
- IG OAS 4주 변화: 9.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.8
- VIX: 25.5
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 0.33% / slope_proxy: -0.002729
- GDXJ/GLD gap: -0.60% / slope_proxy: 0.012995

## VZLA (Vizsla Silver)
- close: 4.215 | RSI14: 46.704306 | ATR14%: 7.73%
- MA20 gap: 5.59% | MA50 gap: -16.05% | MA200 gap: 1.17%
- vol_ratio(Volume/Vol20): 0.148324 | gap_open: 2.26%
- RS vs SILJ gap: -25.22% / slope_proxy: -0.029159
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 10.85 | RSI14: 48.030494 | ATR14%: 9.66%
- MA20 gap: -0.83% | MA50 gap: -5.62% | MA200 gap: 58.43%
- vol_ratio(Volume/Vol20): 0.243582 | gap_open: 4.75%
- SilverMarginGate: SI=89.519997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.47% / slope_proxy: 0.006915
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 43.884998 | RSI14: 52.372009 | ATR14%: 13.17%
- MA20 gap: 2.92% | MA50 gap: 13.97% | MA200 gap: 201.45%
- vol_ratio(Volume/Vol20): 0.380362 | gap_open: 3.10%
- RS vs SILJ gap: 17.92% / slope_proxy: 0.246389
- RS vs GDXJ gap: 18.74% / slope_proxy: 0.064723
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
