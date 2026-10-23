# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-23**
- 실행시간(UTC): **2026-10-23 15:01:09**

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
- 10Y Real Yield 4주 변화: 0.0 bp / latest 2.76
- VIX: 19.03
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.79% / slope_proxy: 0.007124
- GDXJ/GLD gap: -9.41% / slope_proxy: 0.009917

## VZLA (Vizsla Silver)
- close: 3.015 | RSI14: 32.76794 | ATR14%: 6.15%
- MA20 gap: -12.50% | MA50 gap: -19.71% | MA200 gap: -20.89%
- vol_ratio(Volume/Vol20): 0.663026 | gap_open: 0.63%
- RS vs SILJ gap: 0.19% / slope_proxy: 0.001169
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
- close: 6.94 | RSI14: 31.361164 | ATR14%: 7.75%
- MA20 gap: -17.93% | MA50 gap: -23.17% | MA200 gap: -21.97%
- vol_ratio(Volume/Vol20): 0.377303 | gap_open: 0.56%
- SilverMarginGate: SI=54.0 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.98% / slope_proxy: 0.021808
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
- close: 15.555 | RSI14: 32.327853 | ATR14%: 7.74%
- MA20 gap: -13.09% | MA50 gap: -26.44% | MA200 gap: -48.84%
- vol_ratio(Volume/Vol20): 0.342288 | gap_open: 0.89%
- RS vs SILJ gap: -10.93% / slope_proxy: -0.04965
- RS vs GDXJ gap: -14.86% / slope_proxy: -0.016855
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
