# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-28**
- 실행시간(UTC): **2026-10-28 15:01:18**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 10.0 bp / latest 3.18
- IG OAS 4주 변화: 4.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: -24.0 bp / latest 2.66
- VIX: 17.52
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -2.18% / slope_proxy: 0.006676
- GDXJ/GLD gap: -8.12% / slope_proxy: 0.008798

## VZLA (Vizsla Silver)
- close: 3.18 | RSI14: 40.366119 | ATR14%: 5.55%
- MA20 gap: -5.15% | MA50 gap: -14.69% | MA200 gap: -15.73%
- vol_ratio(Volume/Vol20): 0.096046 | gap_open: 0.92%
- RS vs SILJ gap: 2.27% / slope_proxy: 0.000569
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
- close: 7.32 | RSI14: 38.407048 | ATR14%: 6.75%
- MA20 gap: -10.83% | MA50 gap: -18.22% | MA200 gap: -17.24%
- vol_ratio(Volume/Vol20): 0.191951 | gap_open: 0.27%
- SilverMarginGate: SI=53.650002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.38% / slope_proxy: 0.019902
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
- close: 16.66 | RSI14: 41.422267 | ATR14%: 6.92%
- MA20 gap: -4.46% | MA50 gap: -19.02% | MA200 gap: -44.87%
- vol_ratio(Volume/Vol20): 0.186739 | gap_open: 0.00%
- RS vs SILJ gap: -6.62% / slope_proxy: -0.048561
- RS vs GDXJ gap: -9.92% / slope_proxy: -0.016601
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
