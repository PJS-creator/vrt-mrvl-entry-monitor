# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-02**
- 실행시간(UTC): **2026-06-02 15:01:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.72
- IG OAS 4주 변화: -7.0 bp / latest 0.73
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 2.56% / slope_proxy: -0.012991
- GDXJ/GLD gap: -0.93% / slope_proxy: -0.006305

## VZLA (Vizsla Silver)
- close: 4.115 | RSI14: 66.257099 | ATR14%: 5.52%
- MA20 gap: 13.74% | MA50 gap: 19.60% | MA200 gap: -3.13%
- vol_ratio(Volume/Vol20): 0.335558 | gap_open: 2.22%
- RS vs SILJ gap: 16.84% / slope_proxy: 0.001595
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.27 | RSI14: 47.154535 | ATR14%: 6.99%
- MA20 gap: -3.99% | MA50 gap: -1.40% | MA200 gap: -0.93%
- vol_ratio(Volume/Vol20): 0.211193 | gap_open: 1.35%
- SilverMarginGate: SI=76.074997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.75% / slope_proxy: -0.009936
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
- close: 34.047501 | RSI14: 45.47823 | ATR14%: 8.43%
- MA20 gap: -6.27% | MA50 gap: -7.42% | MA200 gap: 40.50%
- vol_ratio(Volume/Vol20): 0.266399 | gap_open: 1.63%
- RS vs SILJ gap: -9.09% / slope_proxy: 0.001092
- RS vs GDXJ gap: -3.26% / slope_proxy: 0.002653
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
