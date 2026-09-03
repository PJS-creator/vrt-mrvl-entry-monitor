# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-02**
- 실행시간(UTC): **2026-09-03 00:37:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.65
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.44
- VIX: 16.34
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 7.71% / slope_proxy: 0.02491
- GDXJ/GLD gap: 11.27% / slope_proxy: 0.007497

## VZLA (Vizsla Silver)
- close: 3.86 | RSI14: 54.690673 | ATR14%: 4.91%
- MA20 gap: 1.22% | MA50 gap: 11.77% | MA200 gap: -5.28%
- vol_ratio(Volume/Vol20): 1.056111 | gap_open: 3.95%
- RS vs SILJ gap: 1.00% / slope_proxy: 0.002179
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 9.2 | RSI14: 57.368947 | ATR14%: 6.08%
- MA20 gap: 1.11% | MA50 gap: 22.29% | MA200 gap: 4.91%
- vol_ratio(Volume/Vol20): 0.94825 | gap_open: 4.38%
- SilverMarginGate: SI=65.949997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.75% / slope_proxy: 0.006238
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

## HYMC (Hycroft Mining)
- close: 21.629999 | RSI14: 40.35117 | ATR14%: 8.78%
- MA20 gap: -15.91% | MA50 gap: -6.15% | MA200 gap: -27.16%
- vol_ratio(Volume/Vol20): 1.033008 | gap_open: 5.57%
- RS vs SILJ gap: -16.69% / slope_proxy: -0.103033
- RS vs GDXJ gap: -19.24% / slope_proxy: -0.029866
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
