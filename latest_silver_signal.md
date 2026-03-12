# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-11**
- 실행시간(UTC): **2026-03-12 03:07:10**

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
- SILJ/SLV gap: -0.07% / slope_proxy: -0.003108
- GDXJ/GLD gap: -3.74% / slope_proxy: 0.012294

## VZLA (Vizsla Silver)
- close: 4.09 | RSI14: 43.917896 | ATR14%: 7.79%
- MA20 gap: 2.57% | MA50 gap: -17.92% | MA200 gap: -1.98%
- vol_ratio(Volume/Vol20): 0.342698 | gap_open: 2.17%
- RS vs SILJ gap: -23.69% / slope_proxy: -0.029039
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.17 | RSI14: 43.780416 | ATR14%: 10.24%
- MA20 gap: -6.41% | MA50 gap: -11.36% | MA200 gap: 47.61%
- vol_ratio(Volume/Vol20): 1.385753 | gap_open: 0.75%
- SilverMarginGate: SI=84.900002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -12.12% / slope_proxy: 0.004187
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
- close: 42.57 | RSI14: 50.594047 | ATR14%: 13.47%
- MA20 gap: -0.97% | MA50 gap: 9.50% | MA200 gap: 188.40%
- vol_ratio(Volume/Vol20): 0.545868 | gap_open: 4.26%
- RS vs SILJ gap: 17.74% / slope_proxy: 0.248962
- RS vs GDXJ gap: 18.05% / slope_proxy: 0.065352
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
