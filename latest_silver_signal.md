# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-23**
- 실행시간(UTC): **2026-04-23 15:01:14**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -33.0 bp / latest 2.84
- IG OAS 4주 변화: -8.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -14.0 bp / latest 1.92
- VIX: 18.92
- NFCI: -0.497

### Leadership ratios
- SILJ/SLV gap: -0.39% / slope_proxy: 0.01308
- GDXJ/GLD gap: -0.96% / slope_proxy: -0.004038

## VZLA (Vizsla Silver)
- close: 3.4132 | RSI14: 47.899826 | ATR14%: 5.59%
- MA20 gap: 2.76% | MA50 gap: -5.14% | MA200 gap: -18.75%
- vol_ratio(Volume/Vol20): 0.248159 | gap_open: 2.31%
- RS vs SILJ gap: -5.76% / slope_proxy: -0.025846
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.7 | RSI14: 49.29971 | ATR14%: 8.01%
- MA20 gap: 4.05% | MA50 gap: -6.93% | MA200 gap: 12.60%
- vol_ratio(Volume/Vol20): 0.291484 | gap_open: 2.11%
- SilverMarginGate: SI=76.165001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.99% / slope_proxy: -0.029191
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
- close: 38.369999 | RSI14: 49.087466 | ATR14%: 9.58%
- MA20 gap: 1.54% | MA50 gap: -2.66% | MA200 gap: 93.70%
- vol_ratio(Volume/Vol20): 0.386563 | gap_open: 2.71%
- RS vs SILJ gap: 3.01% / slope_proxy: 0.059719
- RS vs GDXJ gap: 2.19% / slope_proxy: 0.012443
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
