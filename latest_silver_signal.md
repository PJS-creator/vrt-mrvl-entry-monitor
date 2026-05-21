# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-21**
- 실행시간(UTC): **2026-05-21 15:01:17**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.86
- IG OAS 4주 변화: -4.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.18
- VIX: 17.44
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -4.80% / slope_proxy: -0.005743
- GDXJ/GLD gap: -5.70% / slope_proxy: -0.004289

## VZLA (Vizsla Silver)
- close: 3.32 | RSI14: 44.366757 | ATR14%: 6.35%
- MA20 gap: -4.67% | MA50 gap: -2.18% | MA200 gap: -21.54%
- vol_ratio(Volume/Vol20): 0.105984 | gap_open: 2.36%
- RS vs SILJ gap: 2.90% / slope_proxy: -0.004707
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
- close: 8.02 | RSI14: 42.594111 | ATR14%: 8.30%
- MA20 gap: -6.73% | MA50 gap: -4.96% | MA200 gap: -2.27%
- vol_ratio(Volume/Vol20): 0.440132 | gap_open: 2.39%
- SilverMarginGate: SI=75.290001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.83% / slope_proxy: -0.01756
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
- close: 32.619999 | RSI14: 40.292521 | ATR14%: 10.55%
- MA20 gap: -13.30% | MA50 gap: -12.46% | MA200 gap: 40.60%
- vol_ratio(Volume/Vol20): 0.336457 | gap_open: 1.34%
- RS vs SILJ gap: -7.79% / slope_proxy: 0.027449
- RS vs GDXJ gap: -5.15% / slope_proxy: 0.007787
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
