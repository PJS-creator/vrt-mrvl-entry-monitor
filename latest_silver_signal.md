# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-10**
- 실행시간(UTC): **2026-06-11 03:04:23**

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
- HY OAS 4주 변화: -4.0 bp / latest 2.78
- IG OAS 4주 변화: -2.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -3.47% / slope_proxy: -0.009935
- GDXJ/GLD gap: -9.45% / slope_proxy: -0.007975

## VZLA (Vizsla Silver)
- close: 3.2 | RSI14: 39.747096 | ATR14%: 7.55%
- MA20 gap: -11.28% | MA50 gap: -8.19% | MA200 gap: -24.73%
- vol_ratio(Volume/Vol20): 0.837127 | gap_open: 3.30%
- RS vs SILJ gap: 13.42% / slope_proxy: 0.003685
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
- close: 6.03 | RSI14: 28.150731 | ATR14%: 9.94%
- MA20 gap: -23.81% | MA50 gap: -27.03% | MA200 gap: -28.47%
- vol_ratio(Volume/Vol20): 0.765826 | gap_open: 3.11%
- SilverMarginGate: SI=63.349998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -9.80% / slope_proxy: -0.010566
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
- close: 22.98 | RSI14: 26.729371 | ATR14%: 12.54%
- MA20 gap: -29.07% | MA50 gap: -36.42% | MA200 gap: -7.82%
- vol_ratio(Volume/Vol20): 1.170869 | gap_open: 3.42%
- RS vs SILJ gap: -21.05% / slope_proxy: -0.041994
- RS vs GDXJ gap: -19.31% / slope_proxy: -0.007965
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
