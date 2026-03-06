# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-06**
- 실행시간(UTC): **2026-03-06 15:01:28**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 3.0 bp / latest 3.0
- IG OAS 4주 변화: 6.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -14.0 bp / latest 1.8
- VIX: 23.75
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 0.26% / slope_proxy: -0.002859
- GDXJ/GLD gap: -3.54% / slope_proxy: 0.013611

## VZLA (Vizsla Silver)
- close: 3.904 | RSI14: 39.714795 | ATR14%: 8.55%
- MA20 gap: -2.66% | MA50 gap: -23.21% | MA200 gap: -5.95%
- vol_ratio(Volume/Vol20): 0.122725 | gap_open: 3.69%
- RS vs SILJ gap: -27.82% / slope_proxy: -0.028313
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
- close: 9.69 | RSI14: 40.385957 | ATR14%: 10.81%
- MA20 gap: -12.13% | MA50 gap: -15.42% | MA200 gap: 43.36%
- vol_ratio(Volume/Vol20): 0.123337 | gap_open: 3.31%
- SilverMarginGate: SI=82.945 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.68% / slope_proxy: 0.012238
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
- close: 41.650002 | RSI14: 49.376207 | ATR14%: 13.93%
- MA20 gap: -1.37% | MA50 gap: 9.85% | MA200 gap: 193.77%
- vol_ratio(Volume/Vol20): 0.185638 | gap_open: 0.80%
- RS vs SILJ gap: 21.45% / slope_proxy: 0.247246
- RS vs GDXJ gap: 21.01% / slope_proxy: 0.065061
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
