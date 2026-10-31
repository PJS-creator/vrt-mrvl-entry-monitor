# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-30**
- 실행시간(UTC): **2026-10-31 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 2.0 bp / latest 3.26
- IG OAS 4주 변화: 3.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: -25.0 bp / latest 2.63
- VIX: 17.2
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -0.40% / slope_proxy: 0.006224
- GDXJ/GLD gap: -10.90% / slope_proxy: 0.007255

## VZLA (Vizsla Silver)
- close: 3.06 | RSI14: 36.901679 | ATR14%: 6.16%
- MA20 gap: -7.44% | MA50 gap: -17.32% | MA200 gap: -18.33%
- vol_ratio(Volume/Vol20): 1.195479 | gap_open: 4.26%
- RS vs SILJ gap: 4.54% / slope_proxy: 0.000398
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

## SCZM (Santacruz Silver)
- close: 6.77 | RSI14: 33.290763 | ATR14%: 7.45%
- MA20 gap: -15.83% | MA50 gap: -23.49% | MA200 gap: -23.11%
- vol_ratio(Volume/Vol20): 1.170471 | gap_open: 5.80%
- SilverMarginGate: SI=49.134998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.06% / slope_proxy: 0.018214
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
- close: 16.42 | RSI14: 40.774677 | ATR14%: 7.38%
- MA20 gap: -4.97% | MA50 gap: -18.64% | MA200 gap: -45.36%
- vol_ratio(Volume/Vol20): 1.169454 | gap_open: 7.01%
- RS vs SILJ gap: -1.42% / slope_proxy: -0.047946
- RS vs GDXJ gap: -3.75% / slope_proxy: -0.016412
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
