# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-12**
- 실행시간(UTC): **2026-05-13 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -16.0 bp / latest 2.79
- IG OAS 4주 변화: -4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 3.0 bp / latest 1.95
- VIX: 18.38
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -3.40% / slope_proxy: 0.00427
- GDXJ/GLD gap: 4.63% / slope_proxy: -0.003801

## VZLA (Vizsla Silver)
- close: 3.85 | RSI14: 63.313849 | ATR14%: 5.57%
- MA20 gap: 11.40% | MA50 gap: 10.83% | MA200 gap: -8.68%
- vol_ratio(Volume/Vol20): 0.923153 | gap_open: 2.41%
- RS vs SILJ gap: 1.13% / slope_proxy: -0.013329
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
- close: 10.15 | RSI14: 65.795193 | ATR14%: 6.72%
- MA20 gap: 17.59% | MA50 gap: 17.30% | MA200 gap: 26.48%
- vol_ratio(Volume/Vol20): 1.236259 | gap_open: 2.12%
- SilverMarginGate: SI=87.120003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.85% / slope_proxy: -0.027179
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

## HYMC (Hycroft Mining)
- close: 45.16 | RSI14: 61.922139 | ATR14%: 8.33%
- MA20 gap: 14.96% | MA50 gap: 18.01% | MA200 gap: 104.77%
- vol_ratio(Volume/Vol20): 1.0548 | gap_open: 3.80%
- RS vs SILJ gap: 7.50% / slope_proxy: 0.033577
- RS vs GDXJ gap: 12.45% / slope_proxy: 0.006202
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
