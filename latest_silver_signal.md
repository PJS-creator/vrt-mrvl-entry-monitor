# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-02**
- 실행시간(UTC): **2026-11-03 03:41:32**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 34.0 bp / latest 3.44
- IG OAS 4주 변화: 9.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: -32.0 bp / latest 2.6
- VIX: 19.42
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -1.24% / slope_proxy: 0.005769
- GDXJ/GLD gap: -10.19% / slope_proxy: 0.00623

## VZLA (Vizsla Silver)
- close: 3.05 | RSI14: 36.619313 | ATR14%: 6.12%
- MA20 gap: -7.10% | MA50 gap: -17.18% | MA200 gap: -18.28%
- vol_ratio(Volume/Vol20): 0.656512 | gap_open: 3.27%
- RS vs SILJ gap: 2.80% / slope_proxy: 0.000384
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
- close: 6.95 | RSI14: 36.250331 | ATR14%: 7.26%
- MA20 gap: -12.51% | MA50 gap: -20.97% | MA200 gap: -20.86%
- vol_ratio(Volume/Vol20): 1.331505 | gap_open: 3.69%
- SilverMarginGate: SI=49.915001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.83% / slope_proxy: 0.017271
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
- close: 16.33 | RSI14: 40.345561 | ATR14%: 7.47%
- MA20 gap: -4.81% | MA50 gap: -18.21% | MA200 gap: -45.49%
- vol_ratio(Volume/Vol20): 0.984448 | gap_open: 3.41%
- RS vs SILJ gap: -2.78% / slope_proxy: -0.048724
- RS vs GDXJ gap: -5.93% / slope_proxy: -0.016545
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
