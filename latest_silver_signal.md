# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-04**
- 실행시간(UTC): **2026-03-04 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.08
- IG OAS 4주 변화: 10.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -18.0 bp / latest 1.76
- VIX: 23.57
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 8.40% / slope_proxy: -0.003733
- GDXJ/GLD gap: 2.56% / slope_proxy: 0.014111

## VZLA (Vizsla Silver)
- close: 4.085 | RSI14: 42.393225 | ATR14%: 8.46%
- MA20 gap: 0.37% | MA50 gap: -20.62% | MA200 gap: -1.21%
- vol_ratio(Volume/Vol20): 0.029928 | gap_open: 2.97%
- RS vs SILJ gap: -31.11% / slope_proxy: -0.02686
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.68 | RSI14: 45.216917 | ATR14%: 10.30%
- MA20 gap: -4.66% | MA50 gap: -6.50% | MA200 gap: 59.95%
- vol_ratio(Volume/Vol20): 0.194812 | gap_open: 0.18%
- SilverMarginGate: SI=83.855003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -14.17% / slope_proxy: 0.017604
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
- close: 47.869999 | RSI14: 57.290051 | ATR14%: 12.05%
- MA20 gap: 14.65% | MA50 gap: 29.08% | MA200 gap: 247.05%
- vol_ratio(Volume/Vol20): 0.159422 | gap_open: 3.71%
- RS vs SILJ gap: 32.80% / slope_proxy: 0.248391
- RS vs GDXJ gap: 33.91% / slope_proxy: 0.065453
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
