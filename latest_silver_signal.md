# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-27**
- 실행시간(UTC): **2026-05-27 16:42:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -13.0 bp / latest 2.72
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 27.0 bp / latest 2.16
- VIX: 17.01
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -1.11% / slope_proxy: -0.011748
- GDXJ/GLD gap: -1.20% / slope_proxy: -0.005975

## VZLA (Vizsla Silver)
- close: 3.7 | RSI14: 56.750442 | ATR14%: 5.83%
- MA20 gap: 5.40% | MA50 gap: 9.18% | MA200 gap: -12.67%
- vol_ratio(Volume/Vol20): 0.672084 | gap_open: 2.15%
- RS vs SILJ gap: 10.83% / slope_proxy: -0.001508
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
- close: 7.92 | RSI14: 41.486002 | ATR14%: 7.53%
- MA20 gap: -7.56% | MA50 gap: -5.26% | MA200 gap: -4.17%
- vol_ratio(Volume/Vol20): 0.56025 | gap_open: 3.60%
- SilverMarginGate: SI=75.07 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.15% / slope_proxy: -0.014057
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
- close: 32.580299 | RSI14: 40.792315 | ATR14%: 9.41%
- MA20 gap: -11.88% | MA50 gap: -11.69% | MA200 gap: 37.80%
- vol_ratio(Volume/Vol20): 0.361818 | gap_open: 3.64%
- RS vs SILJ gap: -9.75% / slope_proxy: 0.018256
- RS vs GDXJ gap: -7.07% / slope_proxy: 0.00598
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
