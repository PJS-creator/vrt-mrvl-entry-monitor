# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-22**
- 실행시간(UTC): **2026-07-22 15:01:36**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.69
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 7.0 bp / latest 2.35
- VIX: 17.05
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 5.80% / slope_proxy: 0.008515
- GDXJ/GLD gap: -1.75% / slope_proxy: -0.008468

## VZLA (Vizsla Silver)
- close: 3.45 | RSI14: 56.42208 | ATR14%: 5.58%
- MA20 gap: 8.24% | MA50 gap: 0.37% | MA200 gap: -17.24%
- vol_ratio(Volume/Vol20): 0.381911 | gap_open: 0.30%
- RS vs SILJ gap: 7.58% / slope_proxy: 0.006104
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
- close: 6.78 | RSI14: 51.930588 | ATR14%: 6.42%
- MA20 gap: 5.34% | MA50 gap: -6.90% | MA200 gap: -19.86%
- vol_ratio(Volume/Vol20): 0.292216 | gap_open: 2.29%
- SilverMarginGate: SI=60.505001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.69% / slope_proxy: -0.005859
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
- close: 21.809999 | RSI14: 45.82571 | ATR14%: 8.71%
- MA20 gap: 0.99% | MA50 gap: -20.63% | MA200 gap: -20.16%
- vol_ratio(Volume/Vol20): 0.3485 | gap_open: 1.64%
- RS vs SILJ gap: -18.42% / slope_proxy: -0.125574
- RS vs GDXJ gap: -19.06% / slope_proxy: -0.028037
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
