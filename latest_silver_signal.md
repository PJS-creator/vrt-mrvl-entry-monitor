# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-16**
- 실행시간(UTC): **2026-10-16 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 53.0 bp / latest 3.23
- IG OAS 4주 변화: 6.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.84
- VIX: 16.46
- NFCI: -0.499

### Leadership ratios
- SILJ/SLV gap: -0.17% / slope_proxy: 0.007174
- GDXJ/GLD gap: -2.16% / slope_proxy: 0.012016

## VZLA (Vizsla Silver)
- close: 3.3401 | RSI14: 38.716429 | ATR14%: 5.40%
- MA20 gap: -8.84% | MA50 gap: -12.48% | MA200 gap: -13.76%
- vol_ratio(Volume/Vol20): 0.152109 | gap_open: 0.60%
- RS vs SILJ gap: -1.81% / slope_proxy: 0.002251
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
- close: 8.612 | RSI14: 47.758928 | ATR14%: 6.29%
- MA20 gap: -2.35% | MA50 gap: -5.79% | MA200 gap: -3.77%
- vol_ratio(Volume/Vol20): 0.21566 | gap_open: 0.36%
- SilverMarginGate: SI=57.834999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.15% / slope_proxy: 0.022161
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
- close: 17.73 | RSI14: 40.585671 | ATR14%: 7.18%
- MA20 gap: -7.44% | MA50 gap: -20.21% | MA200 gap: -42.19%
- vol_ratio(Volume/Vol20): 0.277934 | gap_open: 1.03%
- RS vs SILJ gap: -11.54% / slope_proxy: -0.051652
- RS vs GDXJ gap: -15.53% / slope_proxy: -0.017747
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
