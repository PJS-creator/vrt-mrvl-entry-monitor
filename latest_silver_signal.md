# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-13**
- 실행시간(UTC): **2026-05-13 15:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.82
- IG OAS 4주 변화: -4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 3.0 bp / latest 1.95
- VIX: 17.99
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -4.60% / slope_proxy: 0.002816
- GDXJ/GLD gap: 4.32% / slope_proxy: -0.003507

## VZLA (Vizsla Silver)
- close: 3.84 | RSI14: 62.856288 | ATR14%: 5.46%
- MA20 gap: 10.44% | MA50 gap: 10.67% | MA200 gap: -8.99%
- vol_ratio(Volume/Vol20): 0.275008 | gap_open: 1.56%
- RS vs SILJ gap: 0.96% / slope_proxy: -0.01206
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
- close: 10.11 | RSI14: 65.23161 | ATR14%: 6.56%
- MA20 gap: 16.25% | MA50 gap: 17.10% | MA200 gap: 25.48%
- vol_ratio(Volume/Vol20): 0.262028 | gap_open: 1.97%
- SilverMarginGate: SI=88.764999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.41% / slope_proxy: -0.025706
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
- close: 44.060001 | RSI14: 59.429512 | ATR14%: 8.32%
- MA20 gap: 11.63% | MA50 gap: 15.40% | MA200 gap: 97.96%
- vol_ratio(Volume/Vol20): 0.370868 | gap_open: 1.17%
- RS vs SILJ gap: 4.62% / slope_proxy: 0.033856
- RS vs GDXJ gap: 10.30% / slope_proxy: 0.006943
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
