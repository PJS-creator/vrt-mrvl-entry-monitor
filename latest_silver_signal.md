# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-25**
- 실행시간(UTC): **2026-09-26 03:00:55**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 17.0 bp / latest 2.8
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 51.0 bp / latest 2.85
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 0.95% / slope_proxy: 0.019055
- GDXJ/GLD gap: 6.36% / slope_proxy: 0.014779

## VZLA (Vizsla Silver)
- close: 3.95 | RSI14: 50.674754 | ATR14%: 5.29%
- MA20 gap: -1.25% | MA50 gap: 5.56% | MA200 gap: -1.60%
- vol_ratio(Volume/Vol20): 0.708035 | gap_open: 0.76%
- RS vs SILJ gap: 5.17% / slope_proxy: 0.001224
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 9.48 | RSI14: 53.267699 | ATR14%: 6.69%
- MA20 gap: 0.54% | MA50 gap: 11.11% | MA200 gap: 5.20%
- vol_ratio(Volume/Vol20): 0.669999 | gap_open: 1.01%
- SilverMarginGate: SI=64.709999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.23% / slope_proxy: 0.018797
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 21.48 | RSI14: 46.219943 | ATR14%: 7.47%
- MA20 gap: -1.80% | MA50 gap: -6.31% | MA200 gap: -29.89%
- vol_ratio(Volume/Vol20): 0.826179 | gap_open: 0.05%
- RS vs SILJ gap: -8.38% / slope_proxy: -0.072994
- RS vs GDXJ gap: -11.58% / slope_proxy: -0.023083
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
