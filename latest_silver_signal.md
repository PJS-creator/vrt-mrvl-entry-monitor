# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-16**
- 실행시간(UTC): **2026-06-16 15:05:51**

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
- HY OAS 4주 변화: -17.0 bp / latest 2.66
- IG OAS 4주 변화: -1.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.16
- VIX: 16.05
- NFCI: -0.506

### Leadership ratios
- SILJ/SLV gap: 5.82% / slope_proxy: -0.006519
- GDXJ/GLD gap: 2.44% / slope_proxy: -0.007314

## VZLA (Vizsla Silver)
- close: 3.6265 | RSI14: 51.50582 | ATR14%: 6.62%
- MA20 gap: 0.81% | MA50 gap: 3.37% | MA200 gap: -14.73%
- vol_ratio(Volume/Vol20): 0.268284 | gap_open: 0.00%
- RS vs SILJ gap: 6.07% / slope_proxy: 0.004357
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
- close: 7.6 | RSI14: 49.464092 | ATR14%: 7.97%
- MA20 gap: 1.25% | MA50 gap: -7.16% | MA200 gap: -10.33%
- vol_ratio(Volume/Vol20): 0.161025 | gap_open: 0.66%
- SilverMarginGate: SI=69.824997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.12% / slope_proxy: -0.011491
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
- close: 26.5 | RSI14: 39.062003 | ATR14%: 10.62%
- MA20 gap: -11.56% | MA50 gap: -25.15% | MA200 gap: 4.44%
- vol_ratio(Volume/Vol20): 0.464218 | gap_open: 0.72%
- RS vs SILJ gap: -23.16% / slope_proxy: -0.063414
- RS vs GDXJ gap: -21.66% / slope_proxy: -0.012823
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
