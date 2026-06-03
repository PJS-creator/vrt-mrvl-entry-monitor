# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-03**
- 실행시간(UTC): **2026-06-03 15:05:22**

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
- SILJ/SLV gap: 2.54% / slope_proxy: -0.012116
- GDXJ/GLD gap: -1.74% / slope_proxy: -0.006299

## VZLA (Vizsla Silver)
- close: 3.96 | RSI14: 59.91198 | ATR14%: 5.75%
- MA20 gap: 8.34% | MA50 gap: 14.51% | MA200 gap: -6.84%
- vol_ratio(Volume/Vol20): 0.274047 | gap_open: 2.18%
- RS vs SILJ gap: 15.14% / slope_proxy: 0.002299
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
- close: 7.79 | RSI14: 41.383929 | ATR14%: 7.48%
- MA20 gap: -9.60% | MA50 gap: -7.18% | MA200 gap: -6.91%
- vol_ratio(Volume/Vol20): 0.280705 | gap_open: 1.56%
- SilverMarginGate: SI=74.154999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.76% / slope_proxy: -0.009406
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
- close: 33.035 | RSI14: 43.105383 | ATR14%: 8.63%
- MA20 gap: -8.73% | MA50 gap: -10.21% | MA200 gap: 35.51%
- vol_ratio(Volume/Vol20): 0.236893 | gap_open: 2.51%
- RS vs SILJ gap: -9.35% / slope_proxy: -0.003617
- RS vs GDXJ gap: -4.13% / slope_proxy: 0.001811
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
