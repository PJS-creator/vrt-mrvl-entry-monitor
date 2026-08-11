# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-11**
- 실행시간(UTC): **2026-08-11 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.7
- IG OAS 4주 변화: 0.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.4
- VIX: 15.46
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 9.89% / slope_proxy: 0.01281
- GDXJ/GLD gap: 9.49% / slope_proxy: -0.006034

## VZLA (Vizsla Silver)
- close: 3.825 | RSI14: 64.458153 | ATR14%: 4.93%
- MA20 gap: 14.22% | MA50 gap: 13.10% | MA200 gap: -6.41%
- vol_ratio(Volume/Vol20): 0.197089 | gap_open: 0.77%
- RS vs SILJ gap: 0.79% / slope_proxy: 0.005999
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
- close: 9.025 | RSI14: 74.456174 | ATR14%: 5.62%
- MA20 gap: 30.07% | MA50 gap: 31.26% | MA200 gap: 6.38%
- vol_ratio(Volume/Vol20): 0.242724 | gap_open: 0.22%
- SilverMarginGate: SI=65.209999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.52% / slope_proxy: -0.003705
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
- close: 27.25 | RSI14: 65.288255 | ATR14%: 6.60%
- MA20 gap: 26.19% | MA50 gap: 15.56% | MA200 gap: -3.88%
- vol_ratio(Volume/Vol20): 0.191154 | gap_open: 0.29%
- RS vs SILJ gap: -2.20% / slope_proxy: -0.142276
- RS vs GDXJ gap: -4.51% / slope_proxy: -0.036051
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
