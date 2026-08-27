# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-27**
- 실행시간(UTC): **2026-08-27 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -20.0 bp / latest 2.67
- IG OAS 4주 변화: -1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -9.0 bp / latest 2.32
- VIX: 15.21
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 10.90% / slope_proxy: 0.023397
- GDXJ/GLD gap: 16.22% / slope_proxy: 0.004451

## VZLA (Vizsla Silver)
- close: 4.08 | RSI14: 66.28342 | ATR14%: 4.50%
- MA20 gap: 9.27% | MA50 gap: 18.74% | MA200 gap: 0.06%
- vol_ratio(Volume/Vol20): 0.482144 | gap_open: 0.75%
- RS vs SILJ gap: -2.78% / slope_proxy: 0.002809
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
- close: 9.86 | RSI14: 69.703266 | ATR14%: 5.31%
- MA20 gap: 13.25% | MA50 gap: 33.39% | MA200 gap: 13.18%
- vol_ratio(Volume/Vol20): 0.188381 | gap_open: 0.21%
- SilverMarginGate: SI=69.464996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.72% / slope_proxy: 0.004327
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
- close: 26.24 | RSI14: 54.42599 | ATR14%: 7.09%
- MA20 gap: 3.23% | MA50 gap: 13.06% | MA200 gap: -10.99%
- vol_ratio(Volume/Vol20): 0.235187 | gap_open: 0.75%
- RS vs SILJ gap: -9.11% / slope_proxy: -0.106737
- RS vs GDXJ gap: -12.75% / slope_proxy: -0.030528
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
