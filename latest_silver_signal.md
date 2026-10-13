# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-13**
- 실행시간(UTC): **2026-10-13 15:01:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 46.0 bp / latest 3.11
- IG OAS 4주 변화: 3.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 32.0 bp / latest 2.87
- VIX: 15.21
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.37% / slope_proxy: 0.007779
- GDXJ/GLD gap: -2.40% / slope_proxy: 0.0128

## VZLA (Vizsla Silver)
- close: 3.415 | RSI14: 36.9964 | ATR14%: 5.20%
- MA20 gap: -9.28% | MA50 gap: -10.87% | MA200 gap: -12.65%
- vol_ratio(Volume/Vol20): 0.09753 | gap_open: 1.14%
- RS vs SILJ gap: -0.40% / slope_proxy: 0.002705
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
- close: 8.61 | RSI14: 45.908419 | ATR14%: 6.21%
- MA20 gap: -3.47% | MA50 gap: -5.48% | MA200 gap: -4.16%
- vol_ratio(Volume/Vol20): 0.212682 | gap_open: 0.11%
- SilverMarginGate: SI=59.77 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.58% / slope_proxy: 0.021248
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
- close: 17.652 | RSI14: 36.598691 | ATR14%: 6.97%
- MA20 gap: -10.54% | MA50 gap: -21.91% | MA200 gap: -42.63%
- vol_ratio(Volume/Vol20): 0.144915 | gap_open: 0.11%
- RS vs SILJ gap: -13.40% / slope_proxy: -0.052754
- RS vs GDXJ gap: -16.22% / slope_proxy: -0.017911
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
