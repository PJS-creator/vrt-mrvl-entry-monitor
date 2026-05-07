# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-06**
- 실행시간(UTC): **2026-05-07 03:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.77
- IG OAS 4주 변화: -7.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 0.0 bp / latest 1.96
- VIX: 17.38
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -2.29% / slope_proxy: 0.010603
- GDXJ/GLD gap: -0.69% / slope_proxy: -0.003958

## VZLA (Vizsla Silver)
- close: 3.46 | RSI14: 51.314031 | ATR14%: 5.92%
- MA20 gap: 2.00% | MA50 gap: -1.72% | MA200 gap: -17.81%
- vol_ratio(Volume/Vol20): 0.856952 | gap_open: 6.04%
- RS vs SILJ gap: -0.08% / slope_proxy: -0.018358
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.74 | RSI14: 53.275803 | ATR14%: 7.37%
- MA20 gap: 3.46% | MA50 gap: -1.69% | MA200 gap: 10.37%
- vol_ratio(Volume/Vol20): 1.292882 | gap_open: 4.50%
- SilverMarginGate: SI=78.415001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.27% / slope_proxy: -0.030699
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## HYMC (Hycroft Mining)
- close: 39.759998 | RSI14: 53.542679 | ATR14%: 8.40%
- MA20 gap: 2.32% | MA50 gap: 1.85% | MA200 gap: 86.67%
- vol_ratio(Volume/Vol20): 1.025239 | gap_open: 6.70%
- RS vs SILJ gap: 5.53% / slope_proxy: 0.031207
- RS vs GDXJ gap: 6.28% / slope_proxy: 0.004157
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
