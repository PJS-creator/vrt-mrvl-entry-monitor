# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-04**
- 실행시간(UTC): **2026-06-05 03:05:11**

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
- HY OAS 4주 변화: 0.0 bp / latest 2.75
- IG OAS 4주 변화: -4.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 0.28% / slope_proxy: -0.011996
- GDXJ/GLD gap: -2.92% / slope_proxy: -0.006537

## VZLA (Vizsla Silver)
- close: 3.84 | RSI14: 55.916893 | ATR14%: 5.93%
- MA20 gap: 4.66% | MA50 gap: 10.65% | MA200 gap: -9.69%
- vol_ratio(Volume/Vol20): 0.782261 | gap_open: 2.07%
- RS vs SILJ gap: 13.56% / slope_proxy: 0.002606
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 7.59 | RSI14: 40.192757 | ATR14%: 7.69%
- MA20 gap: -11.16% | MA50 gap: -9.42% | MA200 gap: -9.48%
- vol_ratio(Volume/Vol20): 0.687925 | gap_open: 4.03%
- SilverMarginGate: SI=72.845001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.16% / slope_proxy: -0.009201
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
- close: 30.32 | RSI14: 37.69566 | ATR14%: 9.63%
- MA20 gap: -15.02% | MA50 gap: -17.42% | MA200 gap: 23.73%
- vol_ratio(Volume/Vol20): 1.14172 | gap_open: 2.15%
- RS vs SILJ gap: -14.94% / slope_proxy: -0.010484
- RS vs GDXJ gap: -11.16% / slope_proxy: 0.000212
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
