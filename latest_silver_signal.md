# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-15**
- 실행시간(UTC): **2026-05-15 15:01:33**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.76
- IG OAS 4주 변화: -5.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.99
- VIX: 17.26
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -2.63% / slope_proxy: 0.000242
- GDXJ/GLD gap: -2.19% / slope_proxy: -0.003437

## VZLA (Vizsla Silver)
- close: 3.485 | RSI14: 48.601168 | ATR14%: 6.39%
- MA20 gap: -0.22% | MA50 gap: 1.01% | MA200 gap: -17.51%
- vol_ratio(Volume/Vol20): 0.265443 | gap_open: 5.59%
- RS vs SILJ gap: 2.98% / slope_proxy: -0.009595
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
- close: 8.835 | RSI14: 49.875181 | ATR14%: 8.04%
- MA20 gap: 1.47% | MA50 gap: 2.78% | MA200 gap: 8.88%
- vol_ratio(Volume/Vol20): 0.449856 | gap_open: 9.38%
- SilverMarginGate: SI=76.695 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 2.60% / slope_proxy: -0.023271
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
- close: 36.360001 | RSI14: 45.319704 | ATR14%: 10.39%
- MA20 gap: -6.74% | MA50 gap: -4.09% | MA200 gap: 60.89%
- vol_ratio(Volume/Vol20): 0.445419 | gap_open: 6.76%
- RS vs SILJ gap: -2.84% / slope_proxy: 0.028311
- RS vs GDXJ gap: -0.34% / slope_proxy: 0.006467
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
