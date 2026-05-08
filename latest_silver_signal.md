# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-08**
- 실행시간(UTC): **2026-05-08 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.79
- IG OAS 4주 변화: -4.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -2.0 bp / latest 1.94
- VIX: 17.08
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -4.36% / slope_proxy: 0.00806
- GDXJ/GLD gap: 0.83% / slope_proxy: -0.00417

## VZLA (Vizsla Silver)
- close: 3.525 | RSI14: 53.666408 | ATR14%: 5.88%
- MA20 gap: 3.26% | MA50 gap: 0.80% | MA200 gap: -16.29%
- vol_ratio(Volume/Vol20): 0.293367 | gap_open: 1.75%
- RS vs SILJ gap: 0.29% / slope_proxy: -0.015851
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
- close: 9.06 | RSI14: 56.498244 | ATR14%: 7.16%
- MA20 gap: 6.13% | MA50 gap: 3.47% | MA200 gap: 13.72%
- vol_ratio(Volume/Vol20): 0.402245 | gap_open: 1.93%
- SilverMarginGate: SI=81.220001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.25% / slope_proxy: -0.02901
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
- close: 38.689999 | RSI14: 51.398452 | ATR14%: 8.80%
- MA20 gap: -0.57% | MA50 gap: 0.18% | MA200 gap: 78.73%
- vol_ratio(Volume/Vol20): 0.398341 | gap_open: 1.93%
- RS vs SILJ gap: 0.51% / slope_proxy: 0.031904
- RS vs GDXJ gap: 0.95% / slope_proxy: 0.004779
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
