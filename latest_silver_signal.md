# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-16**
- 실행시간(UTC): **2026-10-17 00:45:51**

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
- 10Y Real Yield 4주 변화: 17.0 bp / latest 2.78
- VIX: 16.46
- NFCI: -0.499

### Leadership ratios
- SILJ/SLV gap: -1.86% / slope_proxy: 0.007121
- GDXJ/GLD gap: -3.69% / slope_proxy: 0.012331

## VZLA (Vizsla Silver)
- close: 3.32 | RSI14: 37.802048 | ATR14%: 5.59%
- MA20 gap: -10.29% | MA50 gap: -13.09% | MA200 gap: -14.53%
- vol_ratio(Volume/Vol20): 0.920635 | gap_open: 1.89%
- RS vs SILJ gap: -0.33% / slope_proxy: 0.002472
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
- close: 8.32 | RSI14: 44.23148 | ATR14%: 6.65%
- MA20 gap: -6.15% | MA50 gap: -8.86% | MA200 gap: -7.12%
- vol_ratio(Volume/Vol20): 1.065426 | gap_open: 0.63%
- SilverMarginGate: SI=57.134998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.19% / slope_proxy: 0.021937
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
- close: 17.42 | RSI14: 38.779017 | ATR14%: 7.44%
- MA20 gap: -9.92% | MA50 gap: -22.03% | MA200 gap: -43.25%
- vol_ratio(Volume/Vol20): 1.299685 | gap_open: 1.93%
- RS vs SILJ gap: -11.49% / slope_proxy: -0.051892
- RS vs GDXJ gap: -15.77% / slope_proxy: -0.017791
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
