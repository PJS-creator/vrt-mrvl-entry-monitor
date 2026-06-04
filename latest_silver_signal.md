# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-04**
- 실행시간(UTC): **2026-06-04 15:05:36**

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
- HY OAS 4주 변화: -6.0 bp / latest 2.71
- IG OAS 4주 변화: -5.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 1.02% / slope_proxy: -0.011941
- GDXJ/GLD gap: -2.94% / slope_proxy: -0.006538

## VZLA (Vizsla Silver)
- close: 3.895 | RSI14: 57.4755 | ATR14%: 5.80%
- MA20 gap: 6.08% | MA50 gap: 12.20% | MA200 gap: -8.41%
- vol_ratio(Volume/Vol20): 0.41419 | gap_open: 2.07%
- RS vs SILJ gap: 15.06% / slope_proxy: 0.002635
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
- close: 7.57 | RSI14: 39.898095 | ATR14%: 7.71%
- MA20 gap: -11.38% | MA50 gap: -9.66% | MA200 gap: -9.72%
- vol_ratio(Volume/Vol20): 0.300327 | gap_open: 4.03%
- SilverMarginGate: SI=73.610001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.48% / slope_proxy: -0.009216
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
- close: 30.3629 | RSI14: 37.772349 | ATR14%: 9.62%
- MA20 gap: -14.90% | MA50 gap: -17.30% | MA200 gap: 23.90%
- vol_ratio(Volume/Vol20): 0.472895 | gap_open: 2.15%
- RS vs SILJ gap: -14.89% / slope_proxy: -0.010474
- RS vs GDXJ gap: -10.78% / slope_proxy: 0.000232
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
