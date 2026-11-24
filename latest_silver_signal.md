# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-24**
- 실행시간(UTC): **2026-11-24 06:22:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 38.0 bp / latest 3.76
- IG OAS 4주 변화: 7.0 bp / latest 0.98
- 10Y Real Yield 4주 변화: 11.0 bp / latest 2.77
- VIX: 35.89
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: -0.39% / slope_proxy: 0.001183
- GDXJ/GLD gap: -10.53% / slope_proxy: -0.007933

## VZLA (Vizsla Silver)
- close: 2.74 | RSI14: 39.267028 | ATR14%: 8.14%
- MA20 gap: -11.40% | MA50 gap: -19.29% | MA200 gap: -22.32%
- vol_ratio(Volume/Vol20): 1.064275 | gap_open: 11.93%
- RS vs SILJ gap: 5.06% / slope_proxy: 0.003073
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 6.86 | RSI14: 45.687292 | ATR14%: 8.95%
- MA20 gap: -3.67% | MA50 gap: -14.22% | MA200 gap: -17.62%
- vol_ratio(Volume/Vol20): 1.736022 | gap_open: 13.72%
- SilverMarginGate: SI=42.145 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.04% / slope_proxy: 0.005787
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 13.11 | RSI14: 35.258574 | ATR14%: 12.03%
- MA20 gap: -20.83% | MA50 gap: -26.75% | MA200 gap: -53.18%
- vol_ratio(Volume/Vol20): 1.150641 | gap_open: 16.93%
- RS vs SILJ gap: -5.39% / slope_proxy: -0.0443
- RS vs GDXJ gap: -10.12% / slope_proxy: -0.015043
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **False**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Breakout/Retest)=FALSE
