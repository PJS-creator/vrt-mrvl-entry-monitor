# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-14**
- 실행시간(UTC): **2026-10-14 15:01:41**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 40.0 bp / latest 3.11
- IG OAS 4주 변화: 3.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 31.0 bp / latest 2.91
- VIX: 15.27
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.11% / slope_proxy: 0.007583
- GDXJ/GLD gap: -5.17% / slope_proxy: 0.012761

## VZLA (Vizsla Silver)
- close: 3.205 | RSI14: 31.414542 | ATR14%: 5.70%
- MA20 gap: -14.24% | MA50 gap: -16.24% | MA200 gap: -17.73%
- vol_ratio(Volume/Vol20): 0.313182 | gap_open: 3.57%
- RS vs SILJ gap: -1.28% / slope_proxy: 0.002601
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
- close: 7.935 | RSI14: 39.346833 | ATR14%: 6.93%
- MA20 gap: -10.78% | MA50 gap: -13.00% | MA200 gap: -11.51%
- vol_ratio(Volume/Vol20): 0.637876 | gap_open: 5.08%
- SilverMarginGate: SI=56.314999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.32% / slope_proxy: 0.021528
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
- close: 16.76 | RSI14: 33.434877 | ATR14%: 7.42%
- MA20 gap: -14.33% | MA50 gap: -25.48% | MA200 gap: -45.46%
- vol_ratio(Volume/Vol20): 0.389289 | gap_open: 3.27%
- RS vs SILJ gap: -12.92% / slope_proxy: -0.051932
- RS vs GDXJ gap: -16.34% / slope_proxy: -0.017735
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
