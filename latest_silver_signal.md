# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-11**
- 실행시간(UTC): **2026-09-11 15:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.46
- VIX: 17.84
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 7.20% / slope_proxy: 0.02789
- GDXJ/GLD gap: 11.45% / slope_proxy: 0.013575

## VZLA (Vizsla Silver)
- close: 3.995 | RSI14: 54.684923 | ATR14%: 4.89%
- MA20 gap: 0.83% | MA50 gap: 11.63% | MA200 gap: -1.57%
- vol_ratio(Volume/Vol20): 0.175479 | gap_open: 1.75%
- RS vs SILJ gap: 1.88% / slope_proxy: 0.000107
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
- close: 9.76 | RSI14: 56.260614 | ATR14%: 6.09%
- MA20 gap: 1.45% | MA50 gap: 21.71% | MA200 gap: 9.24%
- vol_ratio(Volume/Vol20): 0.240381 | gap_open: 2.17%
- SilverMarginGate: SI=65.375 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.86% / slope_proxy: 0.014657
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
- close: 21.540001 | RSI14: 41.061919 | ATR14%: 7.99%
- MA20 gap: -11.85% | MA50 gap: -6.35% | MA200 gap: -28.53%
- vol_ratio(Volume/Vol20): 0.34353 | gap_open: 2.81%
- RS vs SILJ gap: -16.09% / slope_proxy: -0.088565
- RS vs GDXJ gap: -19.17% / slope_proxy: -0.027029
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
