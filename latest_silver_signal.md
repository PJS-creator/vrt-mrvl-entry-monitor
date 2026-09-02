# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-02**
- 실행시간(UTC): **2026-09-02 15:01:09**

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
- 10Y Real Yield 4주 변화: 1.0 bp / latest 2.44
- VIX: 16.34
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 9.68% / slope_proxy: 0.026416
- GDXJ/GLD gap: 14.05% / slope_proxy: 0.008671

## VZLA (Vizsla Silver)
- close: 4.085 | RSI14: 60.527672 | ATR14%: 4.87%
- MA20 gap: 5.60% | MA50 gap: 17.46% | MA200 gap: 0.40%
- vol_ratio(Volume/Vol20): 0.254717 | gap_open: 2.85%
- RS vs SILJ gap: 2.74% / slope_proxy: 0.001552
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
- close: 10.0 | RSI14: 65.138829 | ATR14%: 5.84%
- MA20 gap: 8.69% | MA50 gap: 31.74% | MA200 gap: 13.74%
- vol_ratio(Volume/Vol20): 0.558877 | gap_open: 1.96%
- SilverMarginGate: SI=65.754997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 17.83% / slope_proxy: 0.008647
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
- close: 22.950001 | RSI14: 45.156746 | ATR14%: 8.43%
- MA20 gap: -10.52% | MA50 gap: -0.41% | MA200 gap: -22.90%
- vol_ratio(Volume/Vol20): 0.523009 | gap_open: 2.84%
- RS vs SILJ gap: -14.19% / slope_proxy: -0.099452
- RS vs GDXJ gap: -17.14% / slope_proxy: -0.029814
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
