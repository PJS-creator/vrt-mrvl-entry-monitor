# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-27**
- 실행시간(UTC): **2026-05-28 03:00:55**

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
- 10Y Real Yield 4주 변화: 18.0 bp / latest 2.1
- VIX: 17.01
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -1.93% / slope_proxy: -0.011809
- GDXJ/GLD gap: -2.24% / slope_proxy: -0.006024

## VZLA (Vizsla Silver)
- close: 3.62 | RSI14: 53.929865 | ATR14%: 5.95%
- MA20 gap: 3.24% | MA50 gap: 6.87% | MA200 gap: -14.55%
- vol_ratio(Volume/Vol20): 1.012944 | gap_open: 2.15%
- RS vs SILJ gap: 9.64% / slope_proxy: -0.001531
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 7.79 | RSI14: 40.205651 | ATR14%: 7.66%
- MA20 gap: -9.01% | MA50 gap: -6.79% | MA200 gap: -5.74%
- vol_ratio(Volume/Vol20): 0.997355 | gap_open: 3.60%
- SilverMarginGate: SI=73.370003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.69% / slope_proxy: -0.014082
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
- close: 31.98 | RSI14: 39.800365 | ATR14%: 9.58%
- MA20 gap: -13.43% | MA50 gap: -13.29% | MA200 gap: 35.28%
- vol_ratio(Volume/Vol20): 0.659474 | gap_open: 3.64%
- RS vs SILJ gap: -10.43% / slope_proxy: 0.018115
- RS vs GDXJ gap: -7.74% / slope_proxy: 0.005946
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
