# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-25**
- 실행시간(UTC): **2026-08-25 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -12.0 bp / latest 2.69
- IG OAS 4주 변화: 0.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -3.0 bp / latest 2.4
- VIX: 15.85
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 9.63% / slope_proxy: 0.021831
- GDXJ/GLD gap: 15.08% / slope_proxy: 0.002732

## VZLA (Vizsla Silver)
- close: 3.985 | RSI14: 64.221797 | ATR14%: 4.64%
- MA20 gap: 9.35% | MA50 gap: 16.52% | MA200 gap: -2.22%
- vol_ratio(Volume/Vol20): 0.19187 | gap_open: 1.02%
- RS vs SILJ gap: -2.97% / slope_proxy: 0.003559
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
- close: 9.64 | RSI14: 69.305088 | ATR14%: 5.47%
- MA20 gap: 15.04% | MA50 gap: 31.87% | MA200 gap: 11.25%
- vol_ratio(Volume/Vol20): 0.101324 | gap_open: 1.88%
- SilverMarginGate: SI=68.099998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.30% / slope_proxy: 0.003087
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
- close: 25.870001 | RSI14: 53.535569 | ATR14%: 7.39%
- MA20 gap: 4.38% | MA50 gap: 11.23% | MA200 gap: -11.69%
- vol_ratio(Volume/Vol20): 0.250305 | gap_open: 3.24%
- RS vs SILJ gap: -9.23% / slope_proxy: -0.11291
- RS vs GDXJ gap: -14.79% / slope_proxy: -0.031503
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
