# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-21**
- 실행시간(UTC): **2026-05-22 03:00:50**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -4.0 bp / latest 2.8
- IG OAS 4주 변화: -4.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.13
- VIX: 17.44
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -5.50% / slope_proxy: -0.005797
- GDXJ/GLD gap: -5.28% / slope_proxy: -0.004269

## VZLA (Vizsla Silver)
- close: 3.38 | RSI14: 46.179147 | ATR14%: 6.35%
- MA20 gap: -3.03% | MA50 gap: -0.45% | MA200 gap: -20.13%
- vol_ratio(Volume/Vol20): 0.55507 | gap_open: 2.36%
- RS vs SILJ gap: 3.22% / slope_proxy: -0.004701
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
- close: 8.18 | RSI14: 44.028389 | ATR14%: 8.14%
- MA20 gap: -4.96% | MA50 gap: -3.10% | MA200 gap: -0.33%
- vol_ratio(Volume/Vol20): 1.307821 | gap_open: 2.39%
- SilverMarginGate: SI=76.589996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.35% / slope_proxy: -0.017537
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
- close: 33.290001 | RSI14: 41.285188 | ATR14%: 10.37%
- MA20 gap: -11.60% | MA50 gap: -10.70% | MA200 gap: 43.46%
- vol_ratio(Volume/Vol20): 0.962224 | gap_open: 1.34%
- RS vs SILJ gap: -7.29% / slope_proxy: 0.027553
- RS vs GDXJ gap: -4.43% / slope_proxy: 0.007825
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
