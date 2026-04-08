# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-07**
- 실행시간(UTC): **2026-04-08 03:01:13**

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
- 10Y Real Yield 4주 변화: 20.0 bp / latest 1.98
- VIX: 24.17
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 5.07% / slope_proxy: -0.000546
- GDXJ/GLD gap: -2.11% / slope_proxy: -0.00432

## VZLA (Vizsla Silver)
- close: 3.23 | RSI14: 39.337736 | ATR14%: 7.27%
- MA20 gap: -4.61% | MA50 gap: -20.26% | MA200 gap: -22.67%
- vol_ratio(Volume/Vol20): 0.9876 | gap_open: 1.21%
- RS vs SILJ gap: -19.57% / slope_proxy: -0.02747
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
- close: 7.86 | RSI14: 41.861799 | ATR14%: 10.39%
- MA20 gap: -5.74% | MA50 gap: -24.07% | MA200 gap: 6.42%
- vol_ratio(Volume/Vol20): 0.585287 | gap_open: 0.61%
- SilverMarginGate: SI=76.589996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -19.08% / slope_proxy: -0.02205
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
- close: 36.57 | RSI14: 49.859513 | ATR14%: 11.34%
- MA20 gap: 2.09% | MA50 gap: -8.04% | MA200 gap: 107.91%
- vol_ratio(Volume/Vol20): 0.492675 | gap_open: 2.64%
- RS vs SILJ gap: 1.47% / slope_proxy: 0.152045
- RS vs GDXJ gap: -0.65% / slope_proxy: 0.040064
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
