# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-09**
- 실행시간(UTC): **2026-06-09 15:05:46**

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
- HY OAS 4주 변화: -4.0 bp / latest 2.75
- IG OAS 4주 변화: -3.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -1.08% / slope_proxy: -0.010606
- GDXJ/GLD gap: -8.31% / slope_proxy: -0.007519

## VZLA (Vizsla Silver)
- close: 3.345 | RSI14: 42.925654 | ATR14%: 7.20%
- MA20 gap: -8.11% | MA50 gap: -4.00% | MA200 gap: -21.35%
- vol_ratio(Volume/Vol20): 0.329232 | gap_open: 0.58%
- RS vs SILJ gap: 11.79% / slope_proxy: 0.003375
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
- close: 6.2 | RSI14: 29.250828 | ATR14%: 9.75%
- MA20 gap: -23.70% | MA50 gap: -25.27% | MA200 gap: -26.39%
- vol_ratio(Volume/Vol20): 0.331441 | gap_open: 0.16%
- SilverMarginGate: SI=65.714996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -12.96% / slope_proxy: -0.009948
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
- close: 25.280001 | RSI14: 29.779733 | ATR14%: 11.29%
- MA20 gap: -24.60% | MA50 gap: -30.36% | MA200 gap: 1.77%
- vol_ratio(Volume/Vol20): 0.347999 | gap_open: 2.05%
- RS vs SILJ gap: -18.66% / slope_proxy: -0.03246
- RS vs GDXJ gap: -17.15% / slope_proxy: -0.005344
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
