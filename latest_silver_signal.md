# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-28**
- 실행시간(UTC): **2026-05-29 03:05:59**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (404 Client Error: Not Found for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.71
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 18.0 bp / latest 2.1
- VIX: 16.29
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 0.33% / slope_proxy: -0.012512
- GDXJ/GLD gap: -1.17% / slope_proxy: -0.006107

## VZLA (Vizsla Silver)
- close: 3.78 | RSI14: 58.384738 | ATR14%: 5.97%
- MA20 gap: 7.22% | MA50 gap: 11.46% | MA200 gap: -10.82%
- vol_ratio(Volume/Vol20): 1.168343 | gap_open: 1.38%
- RS vs SILJ gap: 10.46% / slope_proxy: -0.000651
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
- close: 8.12 | RSI14: 44.857927 | ATR14%: 7.46%
- MA20 gap: -5.37% | MA50 gap: -2.72% | MA200 gap: -1.99%
- vol_ratio(Volume/Vol20): 1.032575 | gap_open: 0.26%
- SilverMarginGate: SI=76.074997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.74% / slope_proxy: -0.013233
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
- close: 33.169998 | RSI14: 42.771267 | ATR14%: 9.21%
- MA20 gap: -10.09% | MA50 gap: -9.71% | MA200 gap: 39.44%
- vol_ratio(Volume/Vol20): 0.654949 | gap_open: 1.81%
- RS vs SILJ gap: -9.89% / slope_proxy: 0.012464
- RS vs GDXJ gap: -5.92% / slope_proxy: 0.004742
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
