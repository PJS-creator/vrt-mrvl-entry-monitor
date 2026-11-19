# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-19**
- 실행시간(UTC): **2026-11-19 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 10.0 bp / latest 3.43
- IG OAS 4주 변화: 5.0 bp / latest 0.92
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.89
- VIX: 24.56
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: -0.82% / slope_proxy: 0.002616
- GDXJ/GLD gap: -10.47% / slope_proxy: -0.005405

## VZLA (Vizsla Silver)
- close: 2.865 | RSI14: 36.686897 | ATR14%: 6.98%
- MA20 gap: -8.88% | MA50 gap: -16.90% | MA200 gap: -19.21%
- vol_ratio(Volume/Vol20): 0.714703 | gap_open: 6.71%
- RS vs SILJ gap: 4.89% / slope_proxy: 0.002762
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
- close: 6.945 | RSI14: 44.677402 | ATR14%: 8.03%
- MA20 gap: -3.36% | MA50 gap: -14.43% | MA200 gap: -17.04%
- vol_ratio(Volume/Vol20): 0.106891 | gap_open: 0.00%
- SilverMarginGate: SI=45.334999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.47% / slope_proxy: 0.005511
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

## HYMC (Hycroft Mining)
- close: 15.3616 | RSI14: 41.076829 | ATR14%: 9.21%
- MA20 gap: -9.07% | MA50 gap: -15.83% | MA200 gap: -45.57%
- vol_ratio(Volume/Vol20): 0.214928 | gap_open: 0.33%
- RS vs SILJ gap: 4.97% / slope_proxy: -0.045266
- RS vs GDXJ gap: 1.50% / slope_proxy: -0.015297
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
