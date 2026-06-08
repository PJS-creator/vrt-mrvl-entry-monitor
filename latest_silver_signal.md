# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-08**
- 실행시간(UTC): **2026-06-08 15:05:17**

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
- HY OAS 4주 변화: -5.0 bp / latest 2.76
- IG OAS 4주 변화: -5.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.45% / slope_proxy: -0.011286
- GDXJ/GLD gap: -7.57% / slope_proxy: -0.007053

## VZLA (Vizsla Silver)
- close: 3.488 | RSI14: 46.433328 | ATR14%: 6.90%
- MA20 gap: -4.75% | MA50 gap: 0.19% | MA200 gap: -18.00%
- vol_ratio(Volume/Vol20): 0.200569 | gap_open: 2.98%
- RS vs SILJ gap: 14.62% / slope_proxy: 0.003102
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
- close: 6.425 | RSI14: 30.957995 | ATR14%: 9.48%
- MA20 gap: -22.51% | MA50 gap: -22.86% | MA200 gap: -23.63%
- vol_ratio(Volume/Vol20): 0.543705 | gap_open: 2.19%
- SilverMarginGate: SI=68.345001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.80% / slope_proxy: -0.009449
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
- close: 26.440001 | RSI14: 31.489997 | ATR14%: 10.97%
- MA20 gap: -23.27% | MA50 gap: -27.48% | MA200 gap: 6.90%
- vol_ratio(Volume/Vol20): 0.531022 | gap_open: 2.04%
- RS vs SILJ gap: -16.78% / slope_proxy: -0.024256
- RS vs GDXJ gap: -15.03% / slope_proxy: -0.003098
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
