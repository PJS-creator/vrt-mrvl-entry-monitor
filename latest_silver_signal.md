# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-21**
- 실행시간(UTC): **2026-10-22 03:01:05**

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
- SILJ/SLV gap: -3.51% / slope_proxy: 0.007227
- GDXJ/GLD gap: -4.20% / slope_proxy: 0.010843

## VZLA (Vizsla Silver)
- close: 3.36 | RSI14: 42.254116 | ATR14%: 5.19%
- MA20 gap: -4.82% | MA50 gap: -11.16% | MA200 gap: -12.47%
- vol_ratio(Volume/Vol20): 0.849666 | gap_open: 1.23%
- RS vs SILJ gap: 1.87% / slope_proxy: 0.001414
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
- close: 8.17 | RSI14: 42.625916 | ATR14%: 6.25%
- MA20 gap: -5.80% | MA50 gap: -10.25% | MA200 gap: -8.48%
- vol_ratio(Volume/Vol20): 0.585127 | gap_open: 0.85%
- SilverMarginGate: SI=56.724998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.51% / slope_proxy: 0.02289
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
- close: 17.129999 | RSI14: 38.555078 | ATR14%: 7.06%
- MA20 gap: -7.15% | MA50 gap: -20.70% | MA200 gap: -43.91%
- vol_ratio(Volume/Vol20): 0.6938 | gap_open: 1.65%
- RS vs SILJ gap: -11.09% / slope_proxy: -0.050672
- RS vs GDXJ gap: -14.80% / slope_proxy: -0.017348
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
