# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-20**
- 실행시간(UTC): **2026-10-21 00:53:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 63.0 bp / latest 3.29
- IG OAS 4주 변화: 10.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 18.0 bp / latest 2.8
- VIX: 18.44
- NFCI: -0.499

### Leadership ratios
- SILJ/SLV gap: -2.05% / slope_proxy: 0.00728
- GDXJ/GLD gap: -4.28% / slope_proxy: 0.011612

## VZLA (Vizsla Silver)
- close: 3.2 | RSI14: 34.619418 | ATR14%: 5.53%
- MA20 gap: -11.50% | MA50 gap: -15.87% | MA200 gap: -17.13%
- vol_ratio(Volume/Vol20): 0.66485 | gap_open: 1.23%
- RS vs SILJ gap: -3.03% / slope_proxy: 0.001877
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
- close: 8.39 | RSI14: 45.167817 | ATR14%: 6.24%
- MA20 gap: -4.37% | MA50 gap: -8.16% | MA200 gap: -6.17%
- vol_ratio(Volume/Vol20): 0.697181 | gap_open: 0.48%
- SilverMarginGate: SI=58.084999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.07% / slope_proxy: 0.022512
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
- close: 16.860001 | RSI14: 36.67847 | ATR14%: 7.35%
- MA20 gap: -11.00% | MA50 gap: -23.42% | MA200 gap: -44.96%
- vol_ratio(Volume/Vol20): 0.918199 | gap_open: 0.12%
- RS vs SILJ gap: -13.08% / slope_proxy: -0.051547
- RS vs GDXJ gap: -16.77% / slope_proxy: -0.017702
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
