# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-15**
- 실행시간(UTC): **2026-06-16 03:05:59**

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
- HY OAS 4주 변화: -9.0 bp / latest 2.71
- IG OAS 4주 변화: -1.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.16
- VIX: 16.05
- NFCI: -0.506

### Leadership ratios
- SILJ/SLV gap: 3.91% / slope_proxy: -0.006662
- GDXJ/GLD gap: 1.08% / slope_proxy: -0.007378

## VZLA (Vizsla Silver)
- close: 3.65 | RSI14: 52.170709 | ATR14%: 6.79%
- MA20 gap: 1.76% | MA50 gap: 4.23% | MA200 gap: -14.17%
- vol_ratio(Volume/Vol20): 1.002904 | gap_open: 7.80%
- RS vs SILJ gap: 8.29% / slope_proxy: 0.004346
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
- close: 7.55 | RSI14: 48.905954 | ATR14%: 8.25%
- MA20 gap: -0.06% | MA50 gap: -7.90% | MA200 gap: -10.78%
- vol_ratio(Volume/Vol20): 0.923727 | gap_open: 9.60%
- SilverMarginGate: SI=69.574997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.59% / slope_proxy: -0.011652
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
- close: 27.84 | RSI14: 41.595139 | ATR14%: 10.20%
- MA20 gap: -8.36% | MA50 gap: -21.78% | MA200 gap: 10.20%
- vol_ratio(Volume/Vol20): 1.387253 | gap_open: 11.30%
- RS vs SILJ gap: -18.50% / slope_proxy: -0.058702
- RS vs GDXJ gap: -16.57% / slope_proxy: -0.012567
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
