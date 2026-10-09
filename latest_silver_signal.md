# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-09**
- 실행시간(UTC): **2026-10-09 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 45.0 bp / latest 3.15
- IG OAS 4주 변화: 2.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 46.0 bp / latest 2.92
- VIX: 15.41
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -0.65% / slope_proxy: 0.008227
- GDXJ/GLD gap: 0.04% / slope_proxy: 0.012231

## VZLA (Vizsla Silver)
- close: 3.555 | RSI14: 41.57274 | ATR14%: 5.22%
- MA20 gap: -6.35% | MA50 gap: -6.96% | MA200 gap: -9.59%
- vol_ratio(Volume/Vol20): 0.241157 | gap_open: 2.88%
- RS vs SILJ gap: -0.05% / slope_proxy: 0.002852
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
- close: 8.88 | RSI14: 49.09393 | ATR14%: 6.25%
- MA20 gap: -0.37% | MA50 gap: -1.53% | MA200 gap: -1.24%
- vol_ratio(Volume/Vol20): 0.178109 | gap_open: 3.07%
- SilverMarginGate: SI=61.029999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.96% / slope_proxy: 0.019973
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
- close: 18.969999 | RSI14: 41.568011 | ATR14%: 6.73%
- MA20 gap: -5.09% | MA50 gap: -16.38% | MA200 gap: -38.51%
- vol_ratio(Volume/Vol20): 0.165937 | gap_open: 2.53%
- RS vs SILJ gap: -10.71% / slope_proxy: -0.055704
- RS vs GDXJ gap: -12.80% / slope_proxy: -0.018642
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
