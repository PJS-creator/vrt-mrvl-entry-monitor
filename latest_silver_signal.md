# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-05**
- 실행시간(UTC): **2026-06-05 15:05:16**

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
- HY OAS 4주 변화: -5.0 bp / latest 2.74
- IG OAS 4주 변화: -5.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -1.22% / slope_proxy: -0.011468
- GDXJ/GLD gap: -7.53% / slope_proxy: -0.006774

## VZLA (Vizsla Silver)
- close: 3.545 | RSI14: 47.079548 | ATR14%: 6.76%
- MA20 gap: -3.53% | MA50 gap: 1.97% | MA200 gap: -16.66%
- vol_ratio(Volume/Vol20): 0.676802 | gap_open: 3.65%
- RS vs SILJ gap: 13.51% / slope_proxy: 0.002921
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
- close: 6.77 | RSI14: 33.040383 | ATR14%: 8.91%
- MA20 gap: -19.79% | MA50 gap: -18.96% | MA200 gap: -19.42%
- vol_ratio(Volume/Vol20): 0.742969 | gap_open: 3.56%
- SilverMarginGate: SI=69.330002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -9.94% / slope_proxy: -0.009234
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
- close: 27.51 | RSI14: 32.973306 | ATR14%: 10.79%
- MA20 gap: -21.65% | MA50 gap: -24.79% | MA200 gap: 11.72%
- vol_ratio(Volume/Vol20): 0.598151 | gap_open: 5.67%
- RS vs SILJ gap: -16.04% / slope_proxy: -0.01757
- RS vs GDXJ gap: -12.82% / slope_proxy: -0.001423
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
