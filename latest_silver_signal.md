# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-02**
- 실행시간(UTC): **2026-06-03 03:05:30**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.72
- IG OAS 4주 변화: -7.0 bp / latest 0.73
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 3.85% / slope_proxy: -0.012894
- GDXJ/GLD gap: 0.23% / slope_proxy: -0.00625

## VZLA (Vizsla Silver)
- close: 4.13 | RSI14: 66.564068 | ATR14%: 5.56%
- MA20 gap: 14.14% | MA50 gap: 20.02% | MA200 gap: -2.78%
- vol_ratio(Volume/Vol20): 0.78739 | gap_open: 2.22%
- RS vs SILJ gap: 16.68% / slope_proxy: 0.001592
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
- close: 8.33 | RSI14: 48.030166 | ATR14%: 7.01%
- MA20 gap: -3.33% | MA50 gap: -0.70% | MA200 gap: -0.22%
- vol_ratio(Volume/Vol20): 0.548474 | gap_open: 1.35%
- SilverMarginGate: SI=75.129997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.54% / slope_proxy: -0.009926
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
- close: 33.82 | RSI14: 44.875659 | ATR14%: 8.59%
- MA20 gap: -6.86% | MA50 gap: -8.03% | MA200 gap: 39.57%
- vol_ratio(Volume/Vol20): 0.672988 | gap_open: 1.63%
- RS vs SILJ gap: -10.13% / slope_proxy: 0.000879
- RS vs GDXJ gap: -4.69% / slope_proxy: 0.002579
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
