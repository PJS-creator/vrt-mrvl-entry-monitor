# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-26**
- 실행시간(UTC): **2026-03-27 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.17
- IG OAS 4주 변화: 7.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 25.0 bp / latest 2.02
- VIX: 25.33
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.28% / slope_proxy: -0.005233
- GDXJ/GLD gap: -9.49% / slope_proxy: 0.000696

## VZLA (Vizsla Silver)
- close: 3.06 | RSI14: 31.795467 | ATR14%: 8.84%
- MA20 gap: -17.36% | MA50 gap: -31.55% | MA200 gap: -26.88%
- vol_ratio(Volume/Vol20): 0.790454 | gap_open: 4.63%
- RS vs SILJ gap: -18.89% / slope_proxy: -0.0273
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.3 | RSI14: 33.429112 | ATR14%: 12.26%
- MA20 gap: -21.99% | MA50 gap: -33.72% | MA200 gap: 1.27%
- vol_ratio(Volume/Vol20): 0.586822 | gap_open: 3.60%
- SilverMarginGate: SI=68.845001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.18% / slope_proxy: -0.017042
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 31.18 | RSI14: 40.217753 | ATR14%: 14.71%
- MA20 gap: -21.74% | MA50 gap: -23.17% | MA200 gap: 88.98%
- vol_ratio(Volume/Vol20): 0.475516 | gap_open: 5.83%
- RS vs SILJ gap: 1.76% / slope_proxy: 0.215594
- RS vs GDXJ gap: 0.94% / slope_proxy: 0.056646
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
