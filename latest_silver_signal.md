# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-30**
- 실행시간(UTC): **2026-06-30 15:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 8.0 bp / latest 2.8
- IG OAS 4주 변화: 3.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 11.0 bp / latest 2.18
- VIX: 17.65
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 6.77% / slope_proxy: 0.006677
- GDXJ/GLD gap: -5.43% / slope_proxy: -0.001832

## VZLA (Vizsla Silver)
- close: 3.325 | RSI14: 45.458749 | ATR14%: 6.39%
- MA20 gap: -4.56% | MA50 gap: -5.22% | MA200 gap: -21.50%
- vol_ratio(Volume/Vol20): 0.172018 | gap_open: 0.31%
- RS vs SILJ gap: 8.69% / slope_proxy: 0.004688
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
- close: 6.5101 | RSI14: 40.564621 | ATR14%: 7.97%
- MA20 gap: -5.75% | MA50 gap: -17.34% | MA200 gap: -23.55%
- vol_ratio(Volume/Vol20): 0.127649 | gap_open: 0.46%
- SilverMarginGate: SI=60.455002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.43% / slope_proxy: -0.00918
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
- close: 23.379999 | RSI14: 37.419954 | ATR14%: 9.69%
- MA20 gap: -9.40% | MA50 gap: -28.18% | MA200 gap: -10.75%
- vol_ratio(Volume/Vol20): 0.180057 | gap_open: 0.21%
- RS vs SILJ gap: -19.98% / slope_proxy: -0.081527
- RS vs GDXJ gap: -17.13% / slope_proxy: -0.017344
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
