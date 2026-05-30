# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-30 15:04:30**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (504 Server Error: Gateway Time-out for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10), using cached values if available.
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
- HY OAS 4주 변화: -11.0 bp / latest 2.72
- IG OAS 4주 변화: -8.0 bp / latest 0.73
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.06
- VIX: 15.74
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 2.59% / slope_proxy: -0.013075
- GDXJ/GLD gap: 1.70% / slope_proxy: -0.006186

## VZLA (Vizsla Silver)
- close: 3.88 | RSI14: 60.927756 | ATR14%: 5.74%
- MA20 gap: 9.28% | MA50 gap: 14.06% | MA200 gap: -8.52%
- vol_ratio(Volume/Vol20): 0.871978 | gap_open: 0.26%
- RS vs SILJ gap: 10.88% / slope_proxy: 0.000205
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
- close: 8.15 | RSI14: 45.274778 | ATR14%: 7.30%
- MA20 gap: -5.18% | MA50 gap: -2.43% | MA200 gap: -1.87%
- vol_ratio(Volume/Vol20): 0.940641 | gap_open: 0.00%
- SilverMarginGate: SI=75.615997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.24% / slope_proxy: -0.011761
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
- close: 33.049999 | RSI14: 42.543264 | ATR14%: 9.05%
- MA20 gap: -9.99% | MA50 gap: -9.88% | MA200 gap: 38.08%
- vol_ratio(Volume/Vol20): 0.746063 | gap_open: 0.69%
- RS vs SILJ gap: -11.76% / slope_proxy: 0.008588
- RS vs GDXJ gap: -9.48% / slope_proxy: 0.00396
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
