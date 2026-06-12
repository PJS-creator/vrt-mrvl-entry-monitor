# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-11**
- 실행시간(UTC): **2026-06-12 03:05:37**

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
- HY OAS 4주 변화: -2.0 bp / latest 2.8
- IG OAS 4주 변화: -1.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -1.70% / slope_proxy: -0.009157
- GDXJ/GLD gap: -6.07% / slope_proxy: -0.008283

## VZLA (Vizsla Silver)
- close: 3.47 | RSI14: 47.587674 | ATR14%: 7.07%
- MA20 gap: -3.29% | MA50 gap: -0.54% | MA200 gap: -18.38%
- vol_ratio(Volume/Vol20): 0.853395 | gap_open: 0.94%
- RS vs SILJ gap: 14.23% / slope_proxy: 0.003999
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
- close: 6.69 | RSI14: 38.281271 | ATR14%: 9.08%
- MA20 gap: -13.66% | MA50 gap: -18.67% | MA200 gap: -20.72%
- vol_ratio(Volume/Vol20): 0.77005 | gap_open: 0.50%
- SilverMarginGate: SI=67.120003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.69% / slope_proxy: -0.011164
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
- close: 25.190001 | RSI14: 33.83713 | ATR14%: 11.40%
- MA20 gap: -19.97% | MA50 gap: -29.92% | MA200 gap: 0.61%
- vol_ratio(Volume/Vol20): 1.209588 | gap_open: 0.52%
- RS vs SILJ gap: -19.04% / slope_proxy: -0.051184
- RS vs GDXJ gap: -16.94% / slope_proxy: -0.010535
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
