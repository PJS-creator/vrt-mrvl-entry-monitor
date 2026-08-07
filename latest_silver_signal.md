# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-07**
- 실행시간(UTC): **2026-08-07 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.75
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.41
- VIX: 15.15
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 8.55% / slope_proxy: 0.011281
- GDXJ/GLD gap: 8.66% / slope_proxy: -0.007075

## VZLA (Vizsla Silver)
- close: 3.66 | RSI14: 61.772049 | ATR14%: 5.35%
- MA20 gap: 11.91% | MA50 gap: 8.30% | MA200 gap: -10.49%
- vol_ratio(Volume/Vol20): 0.756806 | gap_open: 5.38%
- RS vs SILJ gap: 0.95% / slope_proxy: 0.006027
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
- close: 8.33 | RSI14: 69.55672 | ATR14%: 5.98%
- MA20 gap: 24.75% | MA50 gap: 21.79% | MA200 gap: -1.43%
- vol_ratio(Volume/Vol20): 0.509434 | gap_open: 6.21%
- SilverMarginGate: SI=63.895 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.27% / slope_proxy: -0.004698
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
- close: 25.629999 | RSI14: 61.600035 | ATR14%: 7.33%
- MA20 gap: 22.41% | MA50 gap: 7.71% | MA200 gap: -8.94%
- vol_ratio(Volume/Vol20): 0.658233 | gap_open: 11.05%
- RS vs SILJ gap: -5.18% / slope_proxy: -0.146044
- RS vs GDXJ gap: -9.64% / slope_proxy: -0.036106
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
