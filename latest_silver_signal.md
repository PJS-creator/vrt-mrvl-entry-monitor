# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-08**
- 실행시간(UTC): **2026-07-09 03:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.67
- IG OAS 4주 변화: 1.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.3
- VIX: 16.13
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 3.24% / slope_proxy: 0.008035
- GDXJ/GLD gap: -7.89% / slope_proxy: -0.002152

## VZLA (Vizsla Silver)
- close: 2.96 | RSI14: 35.489503 | ATR14%: 7.19%
- MA20 gap: -11.56% | MA50 gap: -15.11% | MA200 gap: -29.85%
- vol_ratio(Volume/Vol20): 1.340748 | gap_open: 1.29%
- RS vs SILJ gap: 1.13% / slope_proxy: 0.005075
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
- close: 6.24 | RSI14: 38.546767 | ATR14%: 8.04%
- MA20 gap: -7.36% | MA50 gap: -18.49% | MA200 gap: -26.72%
- vol_ratio(Volume/Vol20): 1.050556 | gap_open: 2.20%
- SilverMarginGate: SI=58.415001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.94% / slope_proxy: -0.005935
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
- close: 20.790001 | RSI14: 32.086408 | ATR14%: 10.38%
- MA20 gap: -13.33% | MA50 gap: -32.52% | MA200 gap: -21.87%
- vol_ratio(Volume/Vol20): 0.689078 | gap_open: 3.22%
- RS vs SILJ gap: -22.84% / slope_proxy: -0.094918
- RS vs GDXJ gap: -23.04% / slope_proxy: -0.020771
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
