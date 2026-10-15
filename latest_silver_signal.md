# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-14**
- 실행시간(UTC): **2026-10-15 00:49:47**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 40.0 bp / latest 3.16
- IG OAS 4주 변화: 3.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.88
- VIX: 15.27
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.21% / slope_proxy: 0.007793
- GDXJ/GLD gap: -6.20% / slope_proxy: 0.012709

## VZLA (Vizsla Silver)
- close: 3.36 | RSI14: 35.43594 | ATR14%: 5.46%
- MA20 gap: -10.67% | MA50 gap: -12.28% | MA200 gap: -14.05%
- vol_ratio(Volume/Vol20): 0.539247 | gap_open: 1.14%
- RS vs SILJ gap: -1.70% / slope_proxy: 0.002676
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
- close: 8.47 | RSI14: 44.459049 | ATR14%: 6.42%
- MA20 gap: -4.96% | MA50 gap: -6.99% | MA200 gap: -5.71%
- vol_ratio(Volume/Vol20): 0.901083 | gap_open: 0.11%
- SilverMarginGate: SI=56.23 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.15% / slope_proxy: 0.021175
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
- close: 17.57 | RSI14: 36.30351 | ATR14%: 7.14%
- MA20 gap: -10.94% | MA50 gap: -22.27% | MA200 gap: -42.90%
- vol_ratio(Volume/Vol20): 0.829211 | gap_open: 0.11%
- RS vs SILJ gap: -13.55% / slope_proxy: -0.052774
- RS vs GDXJ gap: -16.67% / slope_proxy: -0.017926
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
