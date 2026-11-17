# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-17**
- 실행시간(UTC): **2026-11-17 15:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 3.23
- IG OAS 4주 변화: 4.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: 17.0 bp / latest 2.91
- VIX: 22.91
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 2.33% / slope_proxy: 0.003961
- GDXJ/GLD gap: -6.86% / slope_proxy: -0.002874

## VZLA (Vizsla Silver)
- close: 3.065 | RSI14: 43.249395 | ATR14%: 6.28%
- MA20 gap: -3.74% | MA50 gap: -12.29% | MA200 gap: -14.10%
- vol_ratio(Volume/Vol20): 0.296453 | gap_open: 1.19%
- RS vs SILJ gap: 3.74% / slope_proxy: 0.002275
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
- close: 7.47 | RSI14: 48.978895 | ATR14%: 7.64%
- MA20 gap: 2.79% | MA50 gap: -9.40% | MA200 gap: -11.37%
- vol_ratio(Volume/Vol20): 0.679591 | gap_open: 7.17%
- SilverMarginGate: SI=47.759998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.84% / slope_proxy: 0.00582
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
- close: 16.059999 | RSI14: 43.682422 | ATR14%: 9.37%
- MA20 gap: -5.68% | MA50 gap: -13.33% | MA200 gap: -43.60%
- vol_ratio(Volume/Vol20): 0.194285 | gap_open: 0.72%
- RS vs SILJ gap: 0.79% / slope_proxy: -0.048453
- RS vs GDXJ gap: -2.93% / slope_proxy: -0.016169
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
