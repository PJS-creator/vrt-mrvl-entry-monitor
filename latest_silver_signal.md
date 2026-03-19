# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-19**
- 실행시간(UTC): **2026-03-19 15:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 34.0 bp / latest 3.2
- IG OAS 4주 변화: 13.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: 4.0 bp / latest 1.83
- VIX: 25.09
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -2.15% / slope_proxy: -0.006101
- GDXJ/GLD gap: -12.79% / slope_proxy: 0.006766

## VZLA (Vizsla Silver)
- close: 3.145 | RSI14: 28.626347 | ATR14%: 9.50%
- MA20 gap: -19.63% | MA50 gap: -33.56% | MA200 gap: -24.97%
- vol_ratio(Volume/Vol20): 0.691789 | gap_open: 8.63%
- RS vs SILJ gap: -22.10% / slope_proxy: -0.027553
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.33 | RSI14: 29.339486 | ATR14%: 12.78%
- MA20 gap: -29.88% | MA50 gap: -35.21% | MA200 gap: 3.39%
- vol_ratio(Volume/Vol20): 0.545018 | gap_open: 9.59%
- SilverMarginGate: SI=70.25 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -18.78% / slope_proxy: -0.006391
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 30.565001 | RSI14: 37.631438 | ATR14%: 16.77%
- MA20 gap: -29.18% | MA50 gap: -24.22% | MA200 gap: 93.58%
- vol_ratio(Volume/Vol20): 0.800377 | gap_open: 8.47%
- RS vs SILJ gap: 0.18% / slope_proxy: 0.253463
- RS vs GDXJ gap: -0.79% / slope_proxy: 0.066523
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
