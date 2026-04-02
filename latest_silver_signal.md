# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-02**
- 실행시간(UTC): **2026-04-02 15:06:18**

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
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.28
- IG OAS 4주 변화: 6.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.04
- VIX: 25.25
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 5.92% / slope_proxy: -0.002641
- GDXJ/GLD gap: -2.00% / slope_proxy: -0.003344

## VZLA (Vizsla Silver)
- close: 3.314 | RSI14: 40.939103 | ATR14%: 7.43%
- MA20 gap: -4.27% | MA50 gap: -20.74% | MA200 gap: -20.70%
- vol_ratio(Volume/Vol20): 0.318245 | gap_open: 6.01%
- RS vs SILJ gap: -19.06% / slope_proxy: -0.027438
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
- close: 7.89 | RSI14: 41.338963 | ATR14%: 10.90%
- MA20 gap: -7.69% | MA50 gap: -25.81% | MA200 gap: 7.54%
- vol_ratio(Volume/Vol20): 0.376673 | gap_open: 8.86%
- SilverMarginGate: SI=72.879997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -19.22% / slope_proxy: -0.020962
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
- close: 36.439999 | RSI14: 49.537774 | ATR14%: 12.07%
- MA20 gap: 0.70% | MA50 gap: -9.51% | MA200 gap: 111.13%
- vol_ratio(Volume/Vol20): 0.370092 | gap_open: 7.36%
- RS vs SILJ gap: 2.04% / slope_proxy: 0.167592
- RS vs GDXJ gap: 0.12% / slope_proxy: 0.043947
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
