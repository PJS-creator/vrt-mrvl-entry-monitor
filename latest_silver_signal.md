# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-02**
- 실행시간(UTC): **2026-04-04 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 17.0 bp / latest 3.17
- IG OAS 4주 변화: 4.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: 15.0 bp / latest 1.97
- VIX: 24.54
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 5.67% / slope_proxy: -0.00266
- GDXJ/GLD gap: -2.25% / slope_proxy: -0.003356

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 39.670747 | ATR14%: 7.55%
- MA20 gap: -5.75% | MA50 gap: -22.01% | MA200 gap: -21.99%
- vol_ratio(Volume/Vol20): 1.009887 | gap_open: 6.01%
- RS vs SILJ gap: -20.58% / slope_proxy: -0.027472
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
- close: 7.83 | RSI14: 40.96584 | ATR14%: 10.99%
- MA20 gap: -8.36% | MA50 gap: -26.37% | MA200 gap: 6.73%
- vol_ratio(Volume/Vol20): 0.984015 | gap_open: 7.44%
- SilverMarginGate: SI=72.735001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -20.05% / slope_proxy: -0.021007
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
- close: 36.009998 | RSI14: 48.900502 | ATR14%: 12.21%
- MA20 gap: -0.43% | MA50 gap: -10.56% | MA200 gap: 108.66%
- vol_ratio(Volume/Vol20): 0.678884 | gap_open: 7.36%
- RS vs SILJ gap: 0.58% / slope_proxy: 0.167303
- RS vs GDXJ gap: -0.87% / slope_proxy: 0.043897
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
