# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-22**
- 실행시간(UTC): **2026-06-23 03:00:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.66
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 3.0 bp / latest 2.21
- VIX: 16.78
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 5.71% / slope_proxy: -0.001398
- GDXJ/GLD gap: -1.46% / slope_proxy: -0.004064

## VZLA (Vizsla Silver)
- close: 3.52 | RSI14: 48.252454 | ATR14%: 6.51%
- MA20 gap: -3.07% | MA50 gap: -0.19% | MA200 gap: -17.18%
- vol_ratio(Volume/Vol20): 0.708655 | gap_open: 0.85%
- RS vs SILJ gap: 9.25% / slope_proxy: 0.004507
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
- close: 7.06 | RSI14: 44.115466 | ATR14%: 8.64%
- MA20 gap: -4.21% | MA50 gap: -13.36% | MA200 gap: -16.98%
- vol_ratio(Volume/Vol20): 0.804215 | gap_open: 2.10%
- SilverMarginGate: SI=63.610001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.56% / slope_proxy: -0.010449
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
- close: 25.049999 | RSI14: 36.834134 | ATR14%: 10.26%
- MA20 gap: -12.94% | MA50 gap: -27.78% | MA200 gap: -2.46%
- vol_ratio(Volume/Vol20): 0.598318 | gap_open: 3.52%
- RS vs SILJ gap: -21.51% / slope_proxy: -0.074173
- RS vs GDXJ gap: -19.77% / slope_proxy: -0.016192
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
