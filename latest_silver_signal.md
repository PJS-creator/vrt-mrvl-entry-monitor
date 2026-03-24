# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-23**
- 실행시간(UTC): **2026-03-24 03:00:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 38.0 bp / latest 3.24
- IG OAS 4주 변화: 10.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.01
- VIX: 26.78
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: 0.61% / slope_proxy: -0.0067
- GDXJ/GLD gap: -7.07% / slope_proxy: 0.004021

## VZLA (Vizsla Silver)
- close: 3.1 | RSI14: 30.069406 | ATR14%: 9.38%
- MA20 gap: -19.12% | MA50 gap: -33.03% | MA200 gap: -26.02%
- vol_ratio(Volume/Vol20): 1.161385 | gap_open: 1.33%
- RS vs SILJ gap: -22.53% / slope_proxy: -0.027568
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
- close: 7.59 | RSI14: 33.080636 | ATR14%: 12.31%
- MA20 gap: -24.31% | MA50 gap: -32.30% | MA200 gap: 6.35%
- vol_ratio(Volume/Vol20): 1.139147 | gap_open: 1.96%
- SilverMarginGate: SI=67.635002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.41% / slope_proxy: -0.010324
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
- close: 32.169998 | RSI14: 40.497542 | ATR14%: 15.16%
- MA20 gap: -23.71% | MA50 gap: -20.54% | MA200 gap: 100.20%
- vol_ratio(Volume/Vol20): 0.877223 | gap_open: 1.70%
- RS vs SILJ gap: 3.50% / slope_proxy: 0.239704
- RS vs GDXJ gap: 1.89% / slope_proxy: 0.062953
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
