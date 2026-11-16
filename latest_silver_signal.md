# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-16**
- 실행시간(UTC): **2026-11-16 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 3.2
- IG OAS 4주 변화: 5.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.86
- VIX: 19.3
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 4.07% / slope_proxy: 0.004364
- GDXJ/GLD gap: -7.12% / slope_proxy: -0.001806

## VZLA (Vizsla Silver)
- close: 3.025 | RSI14: 40.368465 | ATR14%: 6.33%
- MA20 gap: -5.43% | MA50 gap: -13.98% | MA200 gap: -15.47%
- vol_ratio(Volume/Vol20): 0.32306 | gap_open: 2.12%
- RS vs SILJ gap: 2.27% / slope_proxy: 0.001971
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 6.505 | RSI14: 37.427467 | ATR14%: 8.01%
- MA20 gap: -11.02% | MA50 gap: -21.59% | MA200 gap: -23.01%
- vol_ratio(Volume/Vol20): 0.401988 | gap_open: 3.37%
- SilverMarginGate: SI=47.27 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.04% / slope_proxy: 0.006374
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 16.139999 | RSI14: 43.181984 | ATR14%: 9.52%
- MA20 gap: -5.69% | MA50 gap: -13.62% | MA200 gap: -43.52%
- vol_ratio(Volume/Vol20): 0.216157 | gap_open: 3.14%
- RS vs SILJ gap: 0.75% / slope_proxy: -0.049226
- RS vs GDXJ gap: -3.21% / slope_proxy: -0.01645
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
