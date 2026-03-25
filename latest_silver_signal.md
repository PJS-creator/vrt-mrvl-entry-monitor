# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-24**
- 실행시간(UTC): **2026-03-25 03:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 24.0 bp / latest 3.19
- IG OAS 4주 변화: 8.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.01
- VIX: 26.15
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: 1.40% / slope_proxy: -0.006475
- GDXJ/GLD gap: -7.21% / slope_proxy: 0.002863

## VZLA (Vizsla Silver)
- close: 3.13 | RSI14: 31.092333 | ATR14%: 9.02%
- MA20 gap: -17.51% | MA50 gap: -31.64% | MA200 gap: -25.28%
- vol_ratio(Volume/Vol20): 0.591533 | gap_open: 2.26%
- RS vs SILJ gap: -22.23% / slope_proxy: -0.027456
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
- close: 7.91 | RSI14: 36.224454 | ATR14%: 11.55%
- MA20 gap: -19.44% | MA50 gap: -29.12% | MA200 gap: 10.44%
- vol_ratio(Volume/Vol20): 0.605228 | gap_open: 1.19%
- SilverMarginGate: SI=73.959999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.97% / slope_proxy: -0.012427
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
- close: 33.220001 | RSI14: 42.162058 | ATR14%: 14.30%
- MA20 gap: -19.92% | MA50 gap: -18.19% | MA200 gap: 104.88%
- vol_ratio(Volume/Vol20): 0.504803 | gap_open: 2.77%
- RS vs SILJ gap: 4.73% / slope_proxy: 0.231618
- RS vs GDXJ gap: 4.88% / slope_proxy: 0.060879
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
