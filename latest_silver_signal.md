# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-05**
- 실행시간(UTC): **2026-06-06 03:04:45**

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
- HY OAS 4주 변화: -5.0 bp / latest 2.74
- IG OAS 4주 변화: -5.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -2.87% / slope_proxy: -0.011591
- GDXJ/GLD gap: -9.26% / slope_proxy: -0.006856

## VZLA (Vizsla Silver)
- close: 3.36 | RSI14: 42.834143 | ATR14%: 7.38%
- MA20 gap: -8.33% | MA50 gap: -3.25% | MA200 gap: -21.00%
- vol_ratio(Volume/Vol20): 1.495125 | gap_open: 3.65%
- RS vs SILJ gap: 11.52% / slope_proxy: 0.002883
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
- close: 6.4 | RSI14: 30.584585 | ATR14%: 9.86%
- MA20 gap: -24.00% | MA50 gap: -23.32% | MA200 gap: -23.81%
- vol_ratio(Volume/Vol20): 1.959519 | gap_open: 3.56%
- SilverMarginGate: SI=67.995003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.75% / slope_proxy: -0.009318
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
- close: 26.43 | RSI14: 31.458615 | ATR14%: 11.38%
- MA20 gap: -24.61% | MA50 gap: -27.70% | MA200 gap: 7.35%
- vol_ratio(Volume/Vol20): 1.534465 | gap_open: 5.67%
- RS vs SILJ gap: -16.41% / slope_proxy: -0.017645
- RS vs GDXJ gap: -13.60% / slope_proxy: -0.001463
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
