# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-03**
- 실행시간(UTC): **2026-06-04 03:05:34**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
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
- SILJ/SLV gap: 1.04% / slope_proxy: -0.012228
- GDXJ/GLD gap: -3.11% / slope_proxy: -0.006364

## VZLA (Vizsla Silver)
- close: 3.86 | RSI14: 56.585573 | ATR14%: 6.07%
- MA20 gap: 5.75% | MA50 gap: 11.68% | MA200 gap: -9.18%
- vol_ratio(Volume/Vol20): 0.700813 | gap_open: 2.18%
- RS vs SILJ gap: 14.83% / slope_proxy: 0.002293
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
- close: 7.45 | RSI14: 38.067284 | ATR14%: 8.13%
- MA20 gap: -13.38% | MA50 gap: -11.16% | MA200 gap: -10.95%
- vol_ratio(Volume/Vol20): 1.394319 | gap_open: 1.56%
- SilverMarginGate: SI=73.910004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.74% / slope_proxy: -0.009499
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
- close: 32.150002 | RSI14: 41.269956 | ATR14%: 8.87%
- MA20 gap: -11.07% | MA50 gap: -12.57% | MA200 gap: 31.91%
- vol_ratio(Volume/Vol20): 0.591219 | gap_open: 2.51%
- RS vs SILJ gap: -9.74% / slope_proxy: -0.003697
- RS vs GDXJ gap: -5.20% / slope_proxy: 0.001756
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
