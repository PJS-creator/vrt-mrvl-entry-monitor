# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-21**
- 실행시간(UTC): **2026-04-22 03:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -32.0 bp / latest 2.87
- IG OAS 4주 변화: -7.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -10.0 bp / latest 1.91
- VIX: 18.87
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.58% / slope_proxy: 0.011399
- GDXJ/GLD gap: -1.40% / slope_proxy: -0.003891

## VZLA (Vizsla Silver)
- close: 3.33 | RSI14: 44.231856 | ATR14%: 6.02%
- MA20 gap: 1.02% | MA50 gap: -8.12% | MA200 gap: -20.65%
- vol_ratio(Volume/Vol20): 1.251794 | gap_open: 1.14%
- RS vs SILJ gap: -8.37% / slope_proxy: -0.026656
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
- close: 8.49 | RSI14: 47.213938 | ATR14%: 8.56%
- MA20 gap: 2.62% | MA50 gap: -10.25% | MA200 gap: 10.68%
- vol_ratio(Volume/Vol20): 1.043203 | gap_open: 1.10%
- SilverMarginGate: SI=77.775002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.27% / slope_proxy: -0.027456
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
- close: 39.41 | RSI14: 51.262961 | ATR14%: 9.83%
- MA20 gap: 5.86% | MA50 gap: 0.15% | MA200 gap: 102.66%
- vol_ratio(Volume/Vol20): 1.484716 | gap_open: 1.30%
- RS vs SILJ gap: 7.03% / slope_proxy: 0.07421
- RS vs GDXJ gap: 5.85% / slope_proxy: 0.017034
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
