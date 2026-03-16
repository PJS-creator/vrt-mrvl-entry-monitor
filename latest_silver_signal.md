# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-16**
- 실행시간(UTC): **2026-03-16 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.28
- IG OAS 4주 변화: 14.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.89
- VIX: 27.19
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -1.34% / slope_proxy: -0.004424
- GDXJ/GLD gap: -7.28% / slope_proxy: 0.009957

## VZLA (Vizsla Silver)
- close: 3.6679 | RSI14: 37.116755 | ATR14%: 8.21%
- MA20 gap: -7.77% | MA50 gap: -24.74% | MA200 gap: -12.37%
- vol_ratio(Volume/Vol20): 0.124845 | gap_open: 0.00%
- RS vs SILJ gap: -23.95% / slope_proxy: -0.028159
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
- close: 9.12 | RSI14: 37.829516 | ATR14%: 10.41%
- MA20 gap: -14.84% | MA50 gap: -20.25% | MA200 gap: 30.23%
- vol_ratio(Volume/Vol20): 1.074393 | gap_open: 3.54%
- SilverMarginGate: SI=80.514999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.82% / slope_proxy: -0.00201
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
- close: 39.952499 | RSI14: 47.896647 | ATR14%: 13.15%
- MA20 gap: -8.49% | MA50 gap: 0.31% | MA200 gap: 161.04%
- vol_ratio(Volume/Vol20): 0.288242 | gap_open: 2.87%
- RS vs SILJ gap: 15.80% / slope_proxy: 0.255281
- RS vs GDXJ gap: 15.35% / slope_proxy: 0.067035
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
