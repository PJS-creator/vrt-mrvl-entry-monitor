# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-12**
- 실행시간(UTC): **2026-06-13 03:04:17**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 2.0 bp / latest 2.78
- IG OAS 4주 변화: -1.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.16
- VIX: 16.05
- NFCI: -0.506

### Leadership ratios
- SILJ/SLV gap: 0.63% / slope_proxy: -0.008179
- GDXJ/GLD gap: -3.22% / slope_proxy: -0.008176

## VZLA (Vizsla Silver)
- close: 3.59 | RSI14: 50.660692 | ATR14%: 6.66%
- MA20 gap: 0.29% | MA50 gap: 2.75% | MA200 gap: -15.56%
- vol_ratio(Volume/Vol20): 0.873243 | gap_open: 1.44%
- RS vs SILJ gap: 14.20% / slope_proxy: 0.004252
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
- close: 6.98 | RSI14: 42.141527 | ATR14%: 8.64%
- MA20 gap: -8.30% | MA50 gap: -14.91% | MA200 gap: -17.39%
- vol_ratio(Volume/Vol20): 1.344469 | gap_open: 2.39%
- SilverMarginGate: SI=68.120003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.63% / slope_proxy: -0.01148
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
- close: 25.76 | RSI14: 35.573079 | ATR14%: 10.76%
- MA20 gap: -16.36% | MA50 gap: -27.96% | MA200 gap: 2.45%
- vol_ratio(Volume/Vol20): 0.976547 | gap_open: 0.79%
- RS vs SILJ gap: -19.47% / slope_proxy: -0.055683
- RS vs GDXJ gap: -17.36% / slope_proxy: -0.011771
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
