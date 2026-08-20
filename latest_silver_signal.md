# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-20**
- 실행시간(UTC): **2026-08-20 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.73
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.41
- VIX: 14.89
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 9.16% / slope_proxy: 0.019778
- GDXJ/GLD gap: 14.68% / slope_proxy: 0.00049

## VZLA (Vizsla Silver)
- close: 3.955 | RSI14: 64.168678 | ATR14%: 4.72%
- MA20 gap: 11.56% | MA50 gap: 16.69% | MA200 gap: -2.95%
- vol_ratio(Volume/Vol20): 0.273738 | gap_open: 1.54%
- RS vs SILJ gap: -2.83% / slope_proxy: 0.004415
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

## SCZM (Santacruz Silver)
- close: 9.93 | RSI14: 73.573685 | ATR14%: 5.40%
- MA20 gap: 25.74% | MA50 gap: 39.62% | MA200 gap: 15.61%
- vol_ratio(Volume/Vol20): 0.570788 | gap_open: 0.94%
- SilverMarginGate: SI=68.010002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 17.37% / slope_proxy: 0.000766
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
- close: 27.5 | RSI14: 59.784001 | ATR14%: 6.88%
- MA20 gap: 14.79% | MA50 gap: 18.58% | MA200 gap: -5.25%
- vol_ratio(Volume/Vol20): 0.358094 | gap_open: 2.33%
- RS vs SILJ gap: -4.09% / slope_proxy: -0.118983
- RS vs GDXJ gap: -7.94% / slope_proxy: -0.031983
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
