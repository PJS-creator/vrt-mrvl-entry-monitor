# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-30**
- 실행시간(UTC): **2026-10-01 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 43.0 bp / latest 3.08
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 47.0 bp / latest 2.91
- VIX: 16.04
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: 0.26% / slope_proxy: 0.016124
- GDXJ/GLD gap: 2.79% / slope_proxy: 0.014092

## VZLA (Vizsla Silver)
- close: 3.79 | RSI14: 45.636075 | ATR14%: 5.25%
- MA20 gap: -4.70% | MA50 gap: 0.24% | MA200 gap: -5.07%
- vol_ratio(Volume/Vol20): 0.917025 | gap_open: 0.52%
- RS vs SILJ gap: 7.44% / slope_proxy: 0.002063
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
- close: 8.83 | RSI14: 47.225303 | ATR14%: 7.16%
- MA20 gap: -5.73% | MA50 gap: 1.52% | MA200 gap: -1.90%
- vol_ratio(Volume/Vol20): 0.456118 | gap_open: 0.84%
- SilverMarginGate: SI=61.165001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.56% / slope_proxy: 0.019856
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
- close: 19.040001 | RSI14: 38.03758 | ATR14%: 8.12%
- MA20 gap: -10.74% | MA50 gap: -16.91% | MA200 gap: -38.08%
- vol_ratio(Volume/Vol20): 1.124749 | gap_open: 1.29%
- RS vs SILJ gap: -12.08% / slope_proxy: -0.06663
- RS vs GDXJ gap: -15.52% / slope_proxy: -0.021252
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
