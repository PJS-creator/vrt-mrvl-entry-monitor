# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-12**
- 실행시간(UTC): **2026-05-12 15:02:44**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -16.0 bp / latest 2.79
- IG OAS 4주 변화: -4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: -2.0 bp / latest 1.93
- VIX: 18.38
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -3.82% / slope_proxy: 0.004238
- GDXJ/GLD gap: 3.03% / slope_proxy: -0.003879

## VZLA (Vizsla Silver)
- close: 3.665 | RSI14: 57.333958 | ATR14%: 5.55%
- MA20 gap: 6.33% | MA50 gap: 5.62% | MA200 gap: -13.05%
- vol_ratio(Volume/Vol20): 0.28099 | gap_open: 2.41%
- RS vs SILJ gap: -0.41% / slope_proxy: -0.013358
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
- close: 9.312 | RSI14: 58.406522 | ATR14%: 6.83%
- MA20 gap: 8.40% | MA50 gap: 7.82% | MA200 gap: 16.10%
- vol_ratio(Volume/Vol20): 0.368386 | gap_open: 2.12%
- SilverMarginGate: SI=85.309998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.42% / slope_proxy: -0.027432
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
- close: 42.18 | RSI14: 56.627855 | ATR14%: 8.47%
- MA20 gap: 7.79% | MA50 gap: 10.39% | MA200 gap: 91.39%
- vol_ratio(Volume/Vol20): 0.351466 | gap_open: 3.80%
- RS vs SILJ gap: 3.90% / slope_proxy: 0.032827
- RS vs GDXJ gap: 7.80% / slope_proxy: 0.005959
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
