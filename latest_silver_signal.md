# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-27**
- 실행시간(UTC): **2026-11-28 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 51.0 bp / latest 3.77
- IG OAS 4주 변화: 10.0 bp / latest 0.99
- 10Y Real Yield 4주 변화: 6.0 bp / latest 2.73
- VIX: 26.8
- NFCI: -0.444

### Leadership ratios
- SILJ/SLV gap: 8.44% / slope_proxy: 0.0009
- GDXJ/GLD gap: -2.06% / slope_proxy: -0.010298

## VZLA (Vizsla Silver)
- close: 3.1 | RSI14: 50.690581 | ATR14%: 7.51%
- MA20 gap: 2.16% | MA50 gap: -7.15% | MA200 gap: -11.69%
- vol_ratio(Volume/Vol20): 0.452868 | gap_open: 4.55%
- RS vs SILJ gap: 7.20% / slope_proxy: 0.003486
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
- close: 8.38 | RSI14: 58.811821 | ATR14%: 7.88%
- MA20 gap: 17.27% | MA50 gap: 5.61% | MA200 gap: 1.38%
- vol_ratio(Volume/Vol20): 0.710565 | gap_open: 7.99%
- SilverMarginGate: SI=43.167 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 21.67% / slope_proxy: 0.007652
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
- close: 15.77 | RSI14: 48.756172 | ATR14%: 10.23%
- MA20 gap: -2.03% | MA50 gap: -9.89% | MA200 gap: -42.98%
- vol_ratio(Volume/Vol20): 0.633371 | gap_open: 8.09%
- RS vs SILJ gap: 3.41% / slope_proxy: -0.038812
- RS vs GDXJ gap: -0.26% / slope_proxy: -0.013628
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
