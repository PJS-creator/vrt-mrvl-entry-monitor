# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-03**
- 실행시간(UTC): **2026-03-03 16:12:24**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 22.0 bp / latest 3.03
- IG OAS 4주 변화: 11.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: -18.0 bp / latest 1.72
- VIX: 21.44
- NFCI: -0.56294

### Leadership ratios
- SILJ/SLV gap: 7.84% / slope_proxy: -0.004186
- GDXJ/GLD gap: 3.15% / slope_proxy: 0.014369

## VZLA (Vizsla Silver)
- close: 4.0 | RSI14: 40.787996 | ATR14%: 9.00%
- MA20 gap: -3.03% | MA50 gap: -22.56% | MA200 gap: -3.06%
- vol_ratio(Volume/Vol20): 0.241604 | gap_open: 7.73%
- RS vs SILJ gap: -32.21% / slope_proxy: -0.026007
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
- close: 11.06 | RSI14: 47.241321 | ATR14%: 10.34%
- MA20 gap: -2.14% | MA50 gap: -2.78% | MA200 gap: 66.80%
- vol_ratio(Volume/Vol20): 0.47987 | gap_open: 9.46%
- SilverMarginGate: SI=82.855003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -10.03% / slope_proxy: 0.020188
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
- close: 48.100101 | RSI14: 57.65229 | ATR14%: 12.45%
- MA20 gap: 16.06% | MA50 gap: 32.04% | MA200 gap: 254.53%
- vol_ratio(Volume/Vol20): 0.660337 | gap_open: 10.66%
- RS vs SILJ gap: 37.19% / slope_proxy: 0.249048
- RS vs GDXJ gap: 37.45% / slope_proxy: 0.065699
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
