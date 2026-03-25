# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-25**
- 실행시간(UTC): **2026-03-25 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 22.0 bp / latest 3.19
- IG OAS 4주 변화: 6.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.01
- VIX: 26.95
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.30% / slope_proxy: -0.00567
- GDXJ/GLD gap: -6.39% / slope_proxy: 0.001837

## VZLA (Vizsla Silver)
- close: 3.255 | RSI14: 35.336634 | ATR14%: 8.49%
- MA20 gap: -13.45% | MA50 gap: -28.09% | MA200 gap: -22.27%
- vol_ratio(Volume/Vol20): 0.156698 | gap_open: 5.43%
- RS vs SILJ gap: -21.33% / slope_proxy: -0.027465
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.085 | RSI14: 37.941494 | ATR14%: 11.13%
- MA20 gap: -15.84% | MA50 gap: -27.12% | MA200 gap: 12.48%
- vol_ratio(Volume/Vol20): 0.297507 | gap_open: 7.46%
- SilverMarginGate: SI=73.440002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.92% / slope_proxy: -0.014805
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 36.130001 | RSI14: 46.618904 | ATR14%: 12.95%
- MA20 gap: -11.58% | MA50 gap: -11.16% | MA200 gap: 120.66%
- vol_ratio(Volume/Vol20): 0.290713 | gap_open: 9.45%
- RS vs SILJ gap: 9.03% / slope_proxy: 0.224167
- RS vs GDXJ gap: 8.40% / slope_proxy: 0.058917
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
