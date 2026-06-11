# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-11**
- 실행시간(UTC): **2026-06-11 15:05:51**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (502 Server Error: Bad Gateway for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI), using cached values if available.

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
- SILJ/SLV gap: -2.27% / slope_proxy: -0.0092
- GDXJ/GLD gap: -7.73% / slope_proxy: -0.008362

## VZLA (Vizsla Silver)
- close: 3.205 | RSI14: 39.913547 | ATR14%: 7.20%
- MA20 gap: -10.34% | MA50 gap: -7.99% | MA200 gap: -24.59%
- vol_ratio(Volume/Vol20): 0.185863 | gap_open: 0.94%
- RS vs SILJ gap: 11.88% / slope_proxy: 0.003953
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
- close: 6.16 | RSI14: 30.400912 | ATR14%: 9.38%
- MA20 gap: -20.22% | MA50 gap: -25.02% | MA200 gap: -26.98%
- vol_ratio(Volume/Vol20): 0.156418 | gap_open: 0.50%
- SilverMarginGate: SI=64.135002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.90% / slope_proxy: -0.011266
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
- close: 23.299999 | RSI14: 27.851653 | ATR14%: 11.84%
- MA20 gap: -25.75% | MA50 gap: -35.11% | MA200 gap: -6.90%
- vol_ratio(Volume/Vol20): 0.284408 | gap_open: 0.52%
- RS vs SILJ gap: -20.60% / slope_proxy: -0.051496
- RS vs GDXJ gap: -19.15% / slope_proxy: -0.010647
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
