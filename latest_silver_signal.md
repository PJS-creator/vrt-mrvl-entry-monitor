# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-02**
- 실행시간(UTC): **2026-03-02 18:47:38**

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
- 10Y Real Yield 4주 변화: -15.0 bp / latest 1.74
- VIX: 19.86
- NFCI: -0.56294

### Leadership ratios
- SILJ/SLV gap: 10.10% / slope_proxy: -0.004936
- GDXJ/GLD gap: 6.56% / slope_proxy: 0.014651

## VZLA (Vizsla Silver)
- close: 4.31 | RSI14: 45.933206 | ATR14%: 8.08%
- MA20 gap: 3.30% | MA50 gap: -16.91% | MA200 gap: 4.69%
- vol_ratio(Volume/Vol20): 0.458875 | gap_open: 1.37%
- RS vs SILJ gap: -33.54% / slope_proxy: -0.025045
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 11.9921 | RSI14: 52.65543 | ATR14%: 9.12%
- MA20 gap: 6.01% | MA50 gap: 5.87% | MA200 gap: 82.20%
- vol_ratio(Volume/Vol20): 0.690239 | gap_open: 0.32%
- SilverMarginGate: SI=88.315002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.64% / slope_proxy: 0.022857
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
- close: 52.9575 | RSI14: 67.401862 | ATR14%: 10.63%
- MA20 gap: 30.25% | MA50 gap: 48.38% | MA200 gap: 297.35%
- vol_ratio(Volume/Vol20): 0.929328 | gap_open: 0.54%
- RS vs SILJ gap: 40.86% / slope_proxy: 0.245917
- RS vs GDXJ gap: 43.48% / slope_proxy: 0.064923
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
