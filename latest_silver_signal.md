# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-09**
- 실행시간(UTC): **2026-09-09 15:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -5.0 bp / latest 2.67
- IG OAS 4주 변화: 2.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 3.0 bp / latest 2.43
- VIX: 15.72
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 6.31% / slope_proxy: 0.028186
- GDXJ/GLD gap: 13.69% / slope_proxy: 0.013115

## VZLA (Vizsla Silver)
- close: 4.09 | RSI14: 58.49109 | ATR14%: 4.88%
- MA20 gap: 3.82% | MA50 gap: 15.21% | MA200 gap: 0.76%
- vol_ratio(Volume/Vol20): 0.369704 | gap_open: 2.57%
- RS vs SILJ gap: 0.07% / slope_proxy: 0.000275
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 10.375 | RSI14: 65.024874 | ATR14%: 5.62%
- MA20 gap: 8.93% | MA50 gap: 31.49% | MA200 gap: 16.72%
- vol_ratio(Volume/Vol20): 0.302835 | gap_open: 1.50%
- SilverMarginGate: SI=68.735001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 16.72% / slope_proxy: 0.013051
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
- close: 22.879999 | RSI14: 45.227369 | ATR14%: 7.63%
- MA20 gap: -8.46% | MA50 gap: -0.83% | MA200 gap: -23.79%
- vol_ratio(Volume/Vol20): 0.306835 | gap_open: 1.83%
- RS vs SILJ gap: -15.37% / slope_proxy: -0.090415
- RS vs GDXJ gap: -17.47% / slope_proxy: -0.027291
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
