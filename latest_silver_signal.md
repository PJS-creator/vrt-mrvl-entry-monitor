# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-12**
- 실행시간(UTC): **2026-06-12 15:06:01**

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
- HY OAS 4주 변화: -2.0 bp / latest 2.8
- IG OAS 4주 변화: -1.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: 1.23% / slope_proxy: -0.008134
- GDXJ/GLD gap: -3.56% / slope_proxy: -0.008192

## VZLA (Vizsla Silver)
- close: 3.57 | RSI14: 50.173793 | ATR14%: 6.60%
- MA20 gap: -0.24% | MA50 gap: 2.19% | MA200 gap: -16.03%
- vol_ratio(Volume/Vol20): 0.2808 | gap_open: 1.44%
- RS vs SILJ gap: 14.05% / slope_proxy: 0.004249
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
- close: 6.5853 | RSI14: 37.380847 | ATR14%: 9.10%
- MA20 gap: -13.26% | MA50 gap: -19.64% | MA200 gap: -22.04%
- vol_ratio(Volume/Vol20): 0.498082 | gap_open: 2.39%
- SilverMarginGate: SI=67.099998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.52% / slope_proxy: -0.011705
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
- close: 25.58 | RSI14: 35.034807 | ATR14%: 10.72%
- MA20 gap: -16.92% | MA50 gap: -28.46% | MA200 gap: 1.73%
- vol_ratio(Volume/Vol20): 0.380776 | gap_open: 0.79%
- RS vs SILJ gap: -19.69% / slope_proxy: -0.055727
- RS vs GDXJ gap: -17.55% / slope_proxy: -0.01178
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
