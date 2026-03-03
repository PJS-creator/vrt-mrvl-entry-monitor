# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-02**
- 실행시간(UTC): **2026-03-03 00:45:52**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 24.0 bp / latest 3.12
- IG OAS 4주 변화: 11.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: -18.0 bp / latest 1.72
- VIX: 19.86
- NFCI: -0.56294

### Leadership ratios
- SILJ/SLV gap: 10.53% / slope_proxy: -0.004904
- GDXJ/GLD gap: 7.98% / slope_proxy: 0.014722

## VZLA (Vizsla Silver)
- close: 4.4 | RSI14: 47.598718 | ATR14%: 7.92%
- MA20 gap: 5.34% | MA50 gap: -15.21% | MA200 gap: 6.86%
- vol_ratio(Volume/Vol20): 0.656293 | gap_open: 1.37%
- RS vs SILJ gap: -33.52% / slope_proxy: -0.025045
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

## SCZM (Santacruz Silver)
- close: 12.15 | RSI14: 53.610345 | ATR14%: 9.00%
- MA20 gap: 7.33% | MA50 gap: 7.23% | MA200 gap: 84.58%
- vol_ratio(Volume/Vol20): 0.921471 | gap_open: 0.32%
- SilverMarginGate: SI=91.139999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.29% / slope_proxy: 0.022819
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
- close: 55.740002 | RSI14: 69.706994 | ATR14%: 10.13%
- MA20 gap: 36.62% | MA50 gap: 55.94% | MA200 gap: 317.79%
- vol_ratio(Volume/Vol20): 1.299853 | gap_open: 0.54%
- RS vs SILJ gap: 45.15% / slope_proxy: 0.246621
- RS vs GDXJ gap: 48.17% / slope_proxy: 0.065118
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
