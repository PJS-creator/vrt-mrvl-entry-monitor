# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-01**
- 실행시간(UTC): **2026-04-02 03:07:13**

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
- SILJ/SLV gap: 2.90% / slope_proxy: -0.003757
- GDXJ/GLD gap: -1.79% / slope_proxy: -0.002792

## VZLA (Vizsla Silver)
- close: 3.33 | RSI14: 41.330638 | ATR14%: 7.43%
- MA20 gap: -4.84% | MA50 gap: -21.39% | MA200 gap: -20.34%
- vol_ratio(Volume/Vol20): 1.021581 | gap_open: 3.03%
- RS vs SILJ gap: -20.27% / slope_proxy: -0.027351
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
- close: 8.13 | RSI14: 42.901997 | ATR14%: 10.71%
- MA20 gap: -6.03% | MA50 gap: -24.19% | MA200 gap: 11.19%
- vol_ratio(Volume/Vol20): 1.140248 | gap_open: 3.62%
- SilverMarginGate: SI=72.415001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.90% / slope_proxy: -0.020222
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
- close: 35.049999 | RSI14: 47.417991 | ATR14%: 12.35%
- MA20 gap: -3.75% | MA50 gap: -13.10% | MA200 gap: 105.05%
- vol_ratio(Volume/Vol20): 0.607047 | gap_open: 3.41%
- RS vs SILJ gap: -2.41% / slope_proxy: 0.175695
- RS vs GDXJ gap: -5.55% / slope_proxy: 0.046068
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
