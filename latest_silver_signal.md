# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-16**
- 실행시간(UTC): **2026-04-17 03:01:49**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.85
- IG OAS 4주 변화: -11.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 4.0 bp / latest 1.9
- VIX: 18.17
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 0.02% / slope_proxy: 0.008578
- GDXJ/GLD gap: 1.40% / slope_proxy: -0.004511

## VZLA (Vizsla Silver)
- close: 3.43 | RSI14: 48.22525 | ATR14%: 5.88%
- MA20 gap: 5.72% | MA50 gap: -7.14% | MA200 gap: -18.12%
- vol_ratio(Volume/Vol20): 1.214015 | gap_open: 0.88%
- RS vs SILJ gap: -11.88% / slope_proxy: -0.027561
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

## SCZM (Santacruz Silver)
- close: 9.03 | RSI14: 53.197743 | ATR14%: 8.17%
- MA20 gap: 12.19% | MA50 gap: -5.96% | MA200 gap: 19.06%
- vol_ratio(Volume/Vol20): 0.6087 | gap_open: 0.91%
- SilverMarginGate: SI=78.565002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.03% / slope_proxy: -0.024372
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
- close: 40.720001 | RSI14: 56.036826 | ATR14%: 9.21%
- MA20 gap: 14.56% | MA50 gap: 4.54% | MA200 gap: 115.96%
- vol_ratio(Volume/Vol20): 0.462824 | gap_open: 2.50%
- RS vs SILJ gap: 6.43% / slope_proxy: 0.08774
- RS vs GDXJ gap: 3.59% / slope_proxy: 0.02171
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
