# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-07**
- 실행시간(UTC): **2026-05-08 03:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -19.0 bp / latest 2.75
- IG OAS 4주 변화: -5.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: -2.0 bp / latest 1.94
- VIX: 17.39
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -4.66% / slope_proxy: 0.009284
- GDXJ/GLD gap: -1.05% / slope_proxy: -0.004026

## VZLA (Vizsla Silver)
- close: 3.43 | RSI14: 50.182683 | ATR14%: 6.15%
- MA20 gap: 0.88% | MA50 gap: -2.30% | MA200 gap: -18.53%
- vol_ratio(Volume/Vol20): 1.007935 | gap_open: 3.18%
- RS vs SILJ gap: -0.31% / slope_proxy: -0.017192
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
- close: 8.83 | RSI14: 54.180391 | ATR14%: 7.52%
- MA20 gap: 4.09% | MA50 gap: 0.11% | MA200 gap: 11.18%
- vol_ratio(Volume/Vol20): 1.270169 | gap_open: 4.12%
- SilverMarginGate: SI=80.290001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 0.53% / slope_proxy: -0.029881
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
- close: 38.880001 | RSI14: 51.789727 | ATR14%: 8.81%
- MA20 gap: 0.07% | MA50 gap: 0.10% | MA200 gap: 81.06%
- vol_ratio(Volume/Vol20): 1.289009 | gap_open: 5.18%
- RS vs SILJ gap: 3.45% / slope_proxy: 0.030815
- RS vs GDXJ gap: 3.93% / slope_proxy: 0.004245
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
