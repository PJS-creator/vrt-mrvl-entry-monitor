# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-06**
- 실행시간(UTC): **2026-03-08 15:00:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 3.0 bp / latest 3.0
- IG OAS 4주 변화: 6.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -7.0 bp / latest 1.82
- VIX: 23.75
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 1.20% / slope_proxy: -0.002788
- GDXJ/GLD gap: -2.46% / slope_proxy: 0.013665

## VZLA (Vizsla Silver)
- close: 4.0 | RSI14: 41.262588 | ATR14%: 8.40%
- MA20 gap: -0.39% | MA50 gap: -21.35% | MA200 gap: -3.64%
- vol_ratio(Volume/Vol20): 0.831519 | gap_open: 3.69%
- RS vs SILJ gap: -26.58% / slope_proxy: -0.02828
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 10.03 | RSI14: 42.163706 | ATR14%: 10.72%
- MA20 gap: -9.19% | MA50 gap: -12.50% | MA200 gap: 48.35%
- vol_ratio(Volume/Vol20): 0.81074 | gap_open: 1.91%
- SilverMarginGate: SI=84.310997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.37% / slope_proxy: 0.012371
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
- close: 38.790001 | RSI14: 46.162813 | ATR14%: 15.44%
- MA20 gap: -7.83% | MA50 gap: 2.46% | MA200 gap: 173.87%
- vol_ratio(Volume/Vol20): 0.900302 | gap_open: 1.29%
- RS vs SILJ gap: 12.49% / slope_proxy: 0.2457
- RS vs GDXJ gap: 11.14% / slope_proxy: 0.064631
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
