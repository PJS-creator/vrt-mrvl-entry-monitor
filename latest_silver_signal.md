# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-20**
- 실행시간(UTC): **2026-05-20 15:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -4.0 bp / latest 2.83
- IG OAS 4주 변화: -6.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 22.0 bp / latest 2.13
- VIX: 18.06
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -5.56% / slope_proxy: -0.003858
- GDXJ/GLD gap: -5.01% / slope_proxy: -0.00401

## VZLA (Vizsla Silver)
- close: 3.375 | RSI14: 45.979915 | ATR14%: 6.39%
- MA20 gap: -3.04% | MA50 gap: -1.00% | MA200 gap: -20.23%
- vol_ratio(Volume/Vol20): 0.265192 | gap_open: 1.84%
- RS vs SILJ gap: 3.91% / slope_proxy: -0.005973
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
- close: 8.14 | RSI14: 43.434532 | ATR14%: 8.45%
- MA20 gap: -5.53% | MA50 gap: -3.97% | MA200 gap: -0.55%
- vol_ratio(Volume/Vol20): 0.461909 | gap_open: 3.28%
- SilverMarginGate: SI=76.375 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.42% / slope_proxy: -0.019177
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
- close: 33.665001 | RSI14: 41.676284 | ATR14%: 10.55%
- MA20 gap: -11.09% | MA50 gap: -10.12% | MA200 gap: 46.02%
- vol_ratio(Volume/Vol20): 0.346658 | gap_open: 3.30%
- RS vs SILJ gap: -5.81% / slope_proxy: 0.026788
- RS vs GDXJ gap: -3.84% / slope_proxy: 0.007307
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
