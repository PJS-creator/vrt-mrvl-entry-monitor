# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-12**
- 실행시간(UTC): **2026-03-12 15:07:25**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.06
- IG OAS 4주 변화: 7.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -9.0 bp / latest 1.78
- VIX: 24.93
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -2.36% / slope_proxy: -0.003658
- GDXJ/GLD gap: -5.76% / slope_proxy: 0.011386

## VZLA (Vizsla Silver)
- close: 3.915 | RSI14: 40.40867 | ATR14%: 7.90%
- MA20 gap: -1.86% | MA50 gap: -20.93% | MA200 gap: -6.30%
- vol_ratio(Volume/Vol20): 0.161519 | gap_open: 0.98%
- RS vs SILJ gap: -23.64% / slope_proxy: -0.028664
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
- close: 9.9918 | RSI14: 42.715406 | ATR14%: 9.96%
- MA20 gap: -7.36% | MA50 gap: -12.88% | MA200 gap: 44.16%
- vol_ratio(Volume/Vol20): 0.340474 | gap_open: 0.00%
- SilverMarginGate: SI=85.699997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.12% / slope_proxy: 0.001545
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
- close: 40.195 | RSI14: 47.763308 | ATR14%: 13.74%
- MA20 gap: -6.95% | MA50 gap: 2.49% | MA200 gap: 168.93%
- vol_ratio(Volume/Vol20): 0.194128 | gap_open: 0.40%
- RS vs SILJ gap: 14.02% / slope_proxy: 0.250629
- RS vs GDXJ gap: 13.75% / slope_proxy: 0.065802
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
