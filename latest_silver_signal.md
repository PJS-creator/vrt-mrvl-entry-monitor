# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-15**
- 실행시간(UTC): **2026-06-15 15:05:57**

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
- HY OAS 4주 변화: -9.0 bp / latest 2.71
- IG OAS 4주 변화: -1.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.16
- VIX: 16.05
- NFCI: -0.506

### Leadership ratios
- SILJ/SLV gap: 3.93% / slope_proxy: -0.006661
- GDXJ/GLD gap: 1.34% / slope_proxy: -0.007366

## VZLA (Vizsla Silver)
- close: 3.735 | RSI14: 54.158247 | ATR14%: 6.63%
- MA20 gap: 4.00% | MA50 gap: 6.61% | MA200 gap: -12.17%
- vol_ratio(Volume/Vol20): 0.414609 | gap_open: 7.80%
- RS vs SILJ gap: 9.91% / slope_proxy: 0.004378
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 7.65 | RSI14: 49.932885 | ATR14%: 8.14%
- MA20 gap: 1.20% | MA50 gap: -6.70% | MA200 gap: -9.61%
- vol_ratio(Volume/Vol20): 0.472819 | gap_open: 9.60%
- SilverMarginGate: SI=70.910004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.10% / slope_proxy: -0.011629
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
- close: 28.639999 | RSI14: 43.621953 | ATR14%: 9.87%
- MA20 gap: -5.85% | MA50 gap: -19.57% | MA200 gap: 13.35%
- vol_ratio(Volume/Vol20): 0.54405 | gap_open: 11.30%
- RS vs SILJ gap: -16.84% / slope_proxy: -0.058373
- RS vs GDXJ gap: -15.11% / slope_proxy: -0.012493
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
