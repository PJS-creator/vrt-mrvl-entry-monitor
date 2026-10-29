# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-29**
- 실행시간(UTC): **2026-10-29 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 2.0 bp / latest 3.14
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: -27.0 bp / latest 2.64
- VIX: 16.91
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -0.38% / slope_proxy: 0.006424
- GDXJ/GLD gap: -8.84% / slope_proxy: 0.008095

## VZLA (Vizsla Silver)
- close: 3.245 | RSI14: 42.293927 | ATR14%: 5.36%
- MA20 gap: -2.59% | MA50 gap: -12.68% | MA200 gap: -13.72%
- vol_ratio(Volume/Vol20): 0.219382 | gap_open: 3.07%
- RS vs SILJ gap: 4.24% / slope_proxy: 0.000383
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
- close: 7.2 | RSI14: 37.141041 | ATR14%: 6.86%
- MA20 gap: -11.58% | MA50 gap: -19.17% | MA200 gap: -18.42%
- vol_ratio(Volume/Vol20): 0.147267 | gap_open: 3.47%
- SilverMarginGate: SI=52.68 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.11% / slope_proxy: 0.019026
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
- close: 17.42 | RSI14: 45.740267 | ATR14%: 6.74%
- MA20 gap: 0.11% | MA50 gap: -14.52% | MA200 gap: -42.20%
- vol_ratio(Volume/Vol20): 0.297502 | gap_open: 3.33%
- RS vs SILJ gap: -2.10% / slope_proxy: -0.048368
- RS vs GDXJ gap: -4.22% / slope_proxy: -0.016565
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
