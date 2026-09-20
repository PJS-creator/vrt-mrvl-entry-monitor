# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-18**
- 실행시간(UTC): **2026-09-20 15:00:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -5.0 bp / latest 2.7
- IG OAS 4주 변화: -4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.61
- VIX: 15.44
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 1.47% / slope_proxy: 0.023726
- GDXJ/GLD gap: 8.52% / slope_proxy: 0.014113

## VZLA (Vizsla Silver)
- close: 4.08 | RSI14: 57.123544 | ATR14%: 5.22%
- MA20 gap: 2.24% | MA50 gap: 11.83% | MA200 gap: 1.04%
- vol_ratio(Volume/Vol20): 0.825458 | gap_open: 0.25%
- RS vs SILJ gap: 5.91% / slope_proxy: -3.4e-05
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 9.53 | RSI14: 54.128305 | ATR14%: 6.75%
- MA20 gap: -0.42% | MA50 gap: 15.54% | MA200 gap: 6.01%
- vol_ratio(Volume/Vol20): 1.708997 | gap_open: 3.92%
- SilverMarginGate: SI=67.149002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.01% / slope_proxy: 0.016872
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 21.4 | RSI14: 43.483322 | ATR14%: 7.65%
- MA20 gap: -7.15% | MA50 gap: -6.34% | MA200 gap: -29.58%
- vol_ratio(Volume/Vol20): 2.896018 | gap_open: 2.84%
- RS vs SILJ gap: -13.22% / slope_proxy: -0.081947
- RS vs GDXJ gap: -16.35% / slope_proxy: -0.02568
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
