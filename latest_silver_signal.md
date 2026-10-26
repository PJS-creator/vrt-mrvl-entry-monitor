# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-26**
- 실행시간(UTC): **2026-10-26 15:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 45.0 bp / latest 3.38
- IG OAS 4주 변화: 10.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -21.0 bp / latest 2.64
- VIX: 19.45
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.25% / slope_proxy: 0.007151
- GDXJ/GLD gap: -9.00% / slope_proxy: 0.009683

## VZLA (Vizsla Silver)
- close: 3.095 | RSI14: 34.763388 | ATR14%: 5.85%
- MA20 gap: -9.32% | MA50 gap: -17.32% | MA200 gap: -18.53%
- vol_ratio(Volume/Vol20): 0.301131 | gap_open: 0.32%
- RS vs SILJ gap: 1.73% / slope_proxy: 0.001032
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
- close: 7.0 | RSI14: 32.268903 | ATR14%: 7.33%
- MA20 gap: -16.23% | MA50 gap: -22.19% | MA200 gap: -21.17%
- vol_ratio(Volume/Vol20): 0.438303 | gap_open: 0.58%
- SilverMarginGate: SI=54.09 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.31% / slope_proxy: 0.021058
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
- close: 15.52 | RSI14: 32.553875 | ATR14%: 7.50%
- MA20 gap: -12.25% | MA50 gap: -25.79% | MA200 gap: -48.86%
- vol_ratio(Volume/Vol20): 0.239287 | gap_open: 0.06%
- RS vs SILJ gap: -11.74% / slope_proxy: -0.049293
- RS vs GDXJ gap: -15.61% / slope_proxy: -0.01675
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
