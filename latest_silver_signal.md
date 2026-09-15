# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-14**
- 실행시간(UTC): **2026-09-15 03:00:55**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.65
- IG OAS 4주 변화: 0.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.6
- VIX: 15.84
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 4.53% / slope_proxy: 0.027072
- GDXJ/GLD gap: 8.58% / slope_proxy: 0.013546

## VZLA (Vizsla Silver)
- close: 3.79 | RSI14: 47.110347 | ATR14%: 5.37%
- MA20 gap: -4.35% | MA50 gap: 5.65% | MA200 gap: -6.56%
- vol_ratio(Volume/Vol20): 0.764724 | gap_open: 3.02%
- RS vs SILJ gap: 1.40% / slope_proxy: 1.1e-05
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
- close: 8.97 | RSI14: 47.537134 | ATR14%: 6.96%
- MA20 gap: -6.76% | MA50 gap: 11.26% | MA200 gap: 0.21%
- vol_ratio(Volume/Vol20): 0.882849 | gap_open: 5.18%
- SilverMarginGate: SI=64.040001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.56% / slope_proxy: 0.015309
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
- close: 20.549999 | RSI14: 37.762862 | ATR14%: 8.38%
- MA20 gap: -14.70% | MA50 gap: -10.38% | MA200 gap: -31.93%
- vol_ratio(Volume/Vol20): 0.944534 | gap_open: 4.91%
- RS vs SILJ gap: -15.63% / slope_proxy: -0.087352
- RS vs GDXJ gap: -18.93% / slope_proxy: -0.026908
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
