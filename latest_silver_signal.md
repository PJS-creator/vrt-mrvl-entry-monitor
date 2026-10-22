# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-21**
- 실행시간(UTC): **2026-10-22 00:52:25**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DFII10 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED VIXCLS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED NFCI failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 63.0 bp / latest 3.29
- IG OAS 4주 변화: 10.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 18.0 bp / latest 2.8
- VIX: 17.31
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -3.72% / slope_proxy: 0.007162
- GDXJ/GLD gap: -4.34% / slope_proxy: 0.011109

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 37.572561 | ATR14%: 5.48%
- MA20 gap: -8.53% | MA50 gap: -14.02% | MA200 gap: -15.32%
- vol_ratio(Volume/Vol20): 0.738171 | gap_open: 0.62%
- RS vs SILJ gap: -0.61% / slope_proxy: 0.001592
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

## SCZM (Santacruz Silver)
- close: 8.25 | RSI14: 43.559783 | ATR14%: 6.39%
- MA20 gap: -5.26% | MA50 gap: -9.55% | MA200 gap: -7.67%
- vol_ratio(Volume/Vol20): 0.827207 | gap_open: 2.03%
- SilverMarginGate: SI=57.435001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.43% / slope_proxy: 0.022825
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

## HYMC (Hycroft Mining)
- close: 16.950001 | RSI14: 37.285788 | ATR14%: 7.41%
- MA20 gap: -9.15% | MA50 gap: -22.28% | MA200 gap: -44.60%
- vol_ratio(Volume/Vol20): 1.177955 | gap_open: 2.14%
- RS vs SILJ gap: -11.85% / slope_proxy: -0.051061
- RS vs GDXJ gap: -15.55% / slope_proxy: -0.017532
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
