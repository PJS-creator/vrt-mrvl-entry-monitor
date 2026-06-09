# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-08**
- 실행시간(UTC): **2026-06-09 03:05:22**

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
- SILJ/SLV gap: -2.93% / slope_proxy: -0.011321
- GDXJ/GLD gap: -8.43% / slope_proxy: -0.007094

## VZLA (Vizsla Silver)
- close: 3.44 | RSI14: 45.138032 | ATR14%: 7.08%
- MA20 gap: -6.00% | MA50 gap: -1.16% | MA200 gap: -19.13%
- vol_ratio(Volume/Vol20): 0.887865 | gap_open: 2.98%
- RS vs SILJ gap: 14.02% / slope_proxy: 0.00309
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
- close: 6.34 | RSI14: 30.192678 | ATR14%: 9.62%
- MA20 gap: -23.49% | MA50 gap: -23.86% | MA200 gap: -24.64%
- vol_ratio(Volume/Vol20): 1.014336 | gap_open: 2.19%
- SilverMarginGate: SI=67.915001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -12.22% / slope_proxy: -0.009468
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
- close: 26.33 | RSI14: 31.315172 | ATR14%: 11.01%
- MA20 gap: -23.57% | MA50 gap: -27.78% | MA200 gap: 6.46%
- vol_ratio(Volume/Vol20): 1.008509 | gap_open: 2.04%
- RS vs SILJ gap: -16.42% / slope_proxy: -0.024184
- RS vs GDXJ gap: -14.58% / slope_proxy: -0.003075
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
