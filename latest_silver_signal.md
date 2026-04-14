# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-13**
- 실행시간(UTC): **2026-04-14 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -34.0 bp / latest 2.94
- IG OAS 4주 변화: -11.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 3.0 bp / latest 1.95
- VIX: 19.23
- NFCI: -0.433

### Leadership ratios
- SILJ/SLV gap: 4.08% / slope_proxy: 0.005304
- GDXJ/GLD gap: 2.02% / slope_proxy: -0.00457

## VZLA (Vizsla Silver)
- close: 3.31 | RSI14: 43.235775 | ATR14%: 6.56%
- MA20 gap: 1.61% | MA50 gap: -12.77% | MA200 gap: -20.84%
- vol_ratio(Volume/Vol20): 0.856958 | gap_open: 1.54%
- RS vs SILJ gap: -16.96% / slope_proxy: -0.027524
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.61 | RSI14: 49.587979 | ATR14%: 9.06%
- MA20 gap: 7.99% | MA50 gap: -12.05% | MA200 gap: 14.91%
- vol_ratio(Volume/Vol20): 0.704672 | gap_open: 1.00%
- SilverMarginGate: SI=76.739998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -12.65% / slope_proxy: -0.023173
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
- close: 39.560001 | RSI14: 54.82209 | ATR14%: 10.27%
- MA20 gap: 12.38% | MA50 gap: 1.99% | MA200 gap: 116.30%
- vol_ratio(Volume/Vol20): 0.476893 | gap_open: 0.83%
- RS vs SILJ gap: 4.91% / slope_proxy: 0.115359
- RS vs GDXJ gap: 1.40% / slope_proxy: 0.029714
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
