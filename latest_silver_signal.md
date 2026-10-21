# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-21**
- 실행시간(UTC): **2026-10-21 15:01:12**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DFII10 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
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
- SILJ/SLV gap: -3.38% / slope_proxy: 0.007238
- GDXJ/GLD gap: -4.96% / slope_proxy: 0.010805

## VZLA (Vizsla Silver)
- close: 3.305 | RSI14: 39.769897 | ATR14%: 5.17%
- MA20 gap: -6.30% | MA50 gap: -12.59% | MA200 gap: -13.90%
- vol_ratio(Volume/Vol20): 0.168672 | gap_open: 1.23%
- RS vs SILJ gap: 0.80% / slope_proxy: 0.00139
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
- close: 8.18 | RSI14: 42.740457 | ATR14%: 6.13%
- MA20 gap: -5.69% | MA50 gap: -10.15% | MA200 gap: -8.37%
- vol_ratio(Volume/Vol20): 0.221338 | gap_open: 0.85%
- SilverMarginGate: SI=57.709999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.23% / slope_proxy: 0.022928
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
- close: 17.07 | RSI14: 38.137729 | ATR14%: 7.03%
- MA20 gap: -7.46% | MA50 gap: -20.97% | MA200 gap: -44.10%
- vol_ratio(Volume/Vol20): 0.162878 | gap_open: 1.65%
- RS vs SILJ gap: -10.89% / slope_proxy: -0.050647
- RS vs GDXJ gap: -14.30% / slope_proxy: -0.017333
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
