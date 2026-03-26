# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-25**
- 실행시간(UTC): **2026-03-26 03:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 22.0 bp / latest 3.19
- IG OAS 4주 변화: 6.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.06
- VIX: 26.95
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.10% / slope_proxy: -0.005684
- GDXJ/GLD gap: -6.94% / slope_proxy: 0.001809

## VZLA (Vizsla Silver)
- close: 3.24 | RSI14: 34.855126 | ATR14%: 8.53%
- MA20 gap: -13.83% | MA50 gap: -28.42% | MA200 gap: -22.63%
- vol_ratio(Volume/Vol20): 0.833242 | gap_open: 5.43%
- RS vs SILJ gap: -20.55% / slope_proxy: -0.027446
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
- close: 8.05 | RSI14: 37.605524 | ATR14%: 11.18%
- MA20 gap: -16.19% | MA50 gap: -27.43% | MA200 gap: 12.00%
- vol_ratio(Volume/Vol20): 0.674575 | gap_open: 7.46%
- SilverMarginGate: SI=71.595001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.06% / slope_proxy: -0.014757
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

## HYMC (Hycroft Mining)
- close: 34.470001 | RSI14: 44.164534 | ATR14%: 13.58%
- MA20 gap: -15.47% | MA50 gap: -15.17% | MA200 gap: 110.63%
- vol_ratio(Volume/Vol20): 0.678891 | gap_open: 9.45%
- RS vs SILJ gap: 5.61% / slope_proxy: 0.223504
- RS vs GDXJ gap: 4.87% / slope_proxy: 0.058743
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
