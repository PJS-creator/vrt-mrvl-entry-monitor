# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-29**
- 실행시간(UTC): **2026-06-29 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 11.0 bp / latest 2.83
- IG OAS 4주 변화: 4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.19
- VIX: 18.41
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 8.90% / slope_proxy: 0.006214
- GDXJ/GLD gap: -4.84% / slope_proxy: -0.00176

## VZLA (Vizsla Silver)
- close: 3.1968 | RSI14: 41.582911 | ATR14%: 6.80%
- MA20 gap: -9.09% | MA50 gap: -8.94% | MA200 gap: -24.57%
- vol_ratio(Volume/Vol20): 0.150515 | gap_open: 0.91%
- RS vs SILJ gap: 6.39% / slope_proxy: 0.00454
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

## SCZM (Santacruz Silver)
- close: 6.46 | RSI14: 40.087274 | ATR14%: 8.36%
- MA20 gap: -7.54% | MA50 gap: -18.52% | MA200 gap: -24.15%
- vol_ratio(Volume/Vol20): 0.226662 | gap_open: 1.06%
- SilverMarginGate: SI=58.365002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.82% / slope_proxy: -0.009475
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 22.620001 | RSI14: 35.941693 | ATR14%: 10.40%
- MA20 gap: -13.80% | MA50 gap: -31.36% | MA200 gap: -13.35%
- vol_ratio(Volume/Vol20): 0.236701 | gap_open: 4.04%
- RS vs SILJ gap: -21.73% / slope_proxy: -0.079241
- RS vs GDXJ gap: -20.39% / slope_proxy: -0.016761
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
